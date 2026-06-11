"""
数据接收方接口.
"""

__all__ = ["Server"]

import base64
import hashlib
import json
import os
import random
import time
import uuid
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from threading import Lock

import requests
from typing_extensions import TYPE_CHECKING, Dict, Optional, Tuple, Union

if TYPE_CHECKING:
    from _typeshed import GenericPath
else:
    GenericPath = str

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey

from bytedance.tks.client import TKSClient, TKSConfig, utc8_timestamp
from . import error
from .config import ServerConfig
from .crypto import FileMode, PublicKey, ResponseKey, ServerSessionKey
from .log import LogConfig, logger
from .ra import (
    RaRequest,
    RaResponse,
    RaResponseMetadata,
    RaResponsePod,
    RaResponsePods,
    attest_client,
    validata_ra_request,
)
from .service import EpsClient, RasClient
from .utils import RepeatTimer, request_bytedance_gateway, weak_repeat_timer


@dataclass(eq=False)
class Server:
    """
    数据接收方接口.

    本类的所有方法是线程安全的.
    """

    config: ServerConfig

    ras_client: RasClient = field(init=False, repr=False)

    eps_client: EpsClient = field(init=False, repr=False)

    refresh_timer: Optional[RepeatTimer] = field(init=False, default=None)

    session_key: Optional[ServerSessionKey] = field(init=False, default=None)

    old_session_key: Optional[ServerSessionKey] = field(init=False, default=None)

    session_key_lock: Lock = field(init=False, default_factory=Lock)
    """
    线程安全: 修改 session_key 应该加锁.
    """

    root_key_info: Dict[str, PublicKey] = field(init=False, default_factory=dict)

    def __post_init__(self):
        try:
            # 处理环境变量
            # need_evidence = os.environ.get("NEED_EVIDENCE")
            # if need_evidence != None:
            #     if str(need_evidence).lower() == "false":
            #         self.config.need_evidence = False
            #
            # attest_gpu = os.environ.get("ATTEST_GPU")
            # if attest_gpu != None:
            #     if str(attest_gpu).lower() == "false":
            #         self.config.attest_gpu = False
            self._init_log()

            self.ras_client = RasClient(self.config)
            self.eps_client = EpsClient(self.config)

            if self.config.root_key_config:
                self._root_key_parse()

            if self.config.refresh_interval is not None:
                refresh_interval = self.config.refresh_interval

                # 避免多实例集中访问TKS，所以这里加了一个随机数
                refresh_interval = refresh_interval + random.randint(1, 60)
                logger.info(
                    f"start auto update key, refresh_interval={refresh_interval}"
                )

                self.refresh_timer = timer = weak_repeat_timer(
                    refresh_interval, self._auto_update
                )
                timer.start()

            self._auto_update()
        except Exception as e:
            logger.critical(f"__post_init__ failed, e={e}")

    def _auto_update(self):
        """
        :return:
        """
        try:
            self._auto_load_key()
        except Exception as e:
            logger.critical(f"load tks key failed, e={e}")

        try:
            if self.config.client_ra_config is not None:
                if not self.attest_client():
                    logger.error("attest client failed, Please check your config !")

        except Exception as e:
            logger.critical(f"attest client failed, e={e}")

    def _auto_load_key(self):
        try:
            logger.info("start load_key")
            if self.config.key_file:
                if not self.load_file_key():
                    logger.error("load key from local key file failed, Please check your config !")
            elif self.config.key_type == "tks":
                if not self.load_tks_key():
                    logger.error("load key from tks failed, Please check your config !")
            elif self.config.key_type == "random":
                if not self.generate_key():
                    logger.error("generate key failed !")
            else:
                logger.critical("key config error, Both TKS keyid or key file is empty")

        except Exception as e:
            logger.critical(f"load key failed, e={e}")

    def _add_key(self, private_pem: Union[str, bytes], tks_version: Optional[int]):
        """
        添加密钥对.
        """
        # 判断是否需要更新密钥
        if isinstance(private_pem, str):
            new_md5 = hashlib.md5(private_pem.encode()).hexdigest()
        else:
            new_md5 = hashlib.md5(private_pem).hexdigest()

        if self.session_key:
            old_md5 = self.session_key.pem_md5
        else:
            old_md5 = ""

        if old_md5 != new_md5:
            expire_at = datetime.now(timezone.utc) + timedelta(
                seconds=self.config.valid_time
            )
            session_key = ServerSessionKey.load(
                private_pem, expire_at, tks_version, new_md5
            )
            with self.session_key_lock:
                self.old_session_key = self.session_key
                self.session_key = session_key

    def _pcc_login(self) -> Dict[str, str]:
        """
        访问pcc_controller模块，获取cookie
        :return:
        """

        if self.config.pcc_login_url is None:
            raise error.ConfigError("pcc_login_url", "PCC login url is missing")
        if self.config.pcc_password is None:
            raise error.ConfigError("pcc parameter", "PCC parameter is missing")

        ts = str(utc8_timestamp())
        req_body = {
            "Username": self.config.pcc_app_id,
            "Password": hashlib.md5(
                self.config.pcc_password.encode() + ts.encode()
            ).hexdigest(),
        }

        response = requests.post(
            self.config.pcc_login_url, headers={"TimeStamp": ts}, json=req_body
        )
        cookies = response.cookies
        jeddak_pcc_session = cookies.get("jeddak_pcc_session")
        assert jeddak_pcc_session is not None
        cookies = {"jeddak_pcc_session": jeddak_pcc_session}
        return cookies

    def _get_pairkey_from_pem(self, private_key: bytes) -> Optional[Dict[str, str]]:
        """
        从私钥pem中产生公私钥对 for peixuan
        :param private_key:
        :return:
        """
        private_key_pem = serialization.load_pem_private_key(private_key, password=None)
        if not isinstance(private_key_pem, RSAPrivateKey):
            logger.error("not RSAPrivateKey")
            return None

        pub_key = private_key_pem.public_key()
        pub_key_str = pub_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo,
        ).decode("utf-8")

        ret = dict()
        ret["pub_key"] = pub_key_str
        ret["pri_key"] = private_key.decode()

        return ret

    def _get_tks_info_from_pcc(self, service_id: str, app_id: str):
        try:
            if not service_id:
                return None

            top_conf = json.loads(self.config.bytedance_top_info)
            top_conf["action"] = "ListJscKey"

            url = top_conf.get("url", "open.volcengineapi.com")
            body = {"ServiceId": service_id, "AccountId": app_id}
            response = request_bytedance_gateway(url, body, {}, top_conf)
            if not response or response.status_code != 200:
                logger.error("get tks info from pcc_controller failed")
                return None

            ra_res = json.loads(response.text).get("Result")
            if not ra_res:
                logger.error(f"get key info from pcc_controller error: ServiceId={service_id}")
                return None

            key_list = json.loads(response.text).get("Result").get("KeyList")
            if len(key_list) == 1:
                ring_id = key_list[0].get("RingID")
                key_id = key_list[0].get("KeyID")
                return ring_id, key_id
            else:
                logger.error(f"get key info from pcc_controller error: key_list={key_list}")
                return None

        except Exception as e:
            logger.critical("_get_tks_info_from_pcc exception={}".format(e))
            return None

    def load_tks_key(self) -> bool:
        """
        从 TKS 获取或更新密钥对.
        """
        logger.info("start load TKS key")

        app_id, ring_id, key_id = (
            self.config.tks_app_id,
            self.config.tks_ring_id,
            self.config.tks_key_id,
        )

        pcc_conf = None
        top_conf = None
        if self.config.bytedance_pcc_info:
            pcc_conf = json.loads(self.config.bytedance_pcc_info)
        elif self.config.bytedance_top_info:
            top_conf = json.loads(self.config.bytedance_top_info)

        enable_tls = True
        if enable_tls_env := os.environ.get("enable_tls"):
            enable_tls = enable_tls_env.lower() == "true"
        elif enable_tls_env := os.environ.get("ENABLE_TLS"):
            enable_tls = enable_tls_env.lower() == "true"

        cfg = TKSConfig(
            addr=self.config.tks_url,
            enable_tls=enable_tls,
            pcc_config=pcc_conf,
            top_config=top_conf,
        )

        tks_client = TKSClient(app_id, cfg)

        need_evidence_conf = self.config.need_evidence
        need_evidence = self.config.need_evidence
        need_evidence_env = os.environ.get("NEED_EVIDENCE")
        if need_evidence_env:
            need_evidence = not (need_evidence_env.lower() == "false")
        logger.info(
            f"need_evidence: conf={need_evidence_conf}, env={need_evidence_env}, use={need_evidence}"
        )

        attest_gpu_conf = self.config.attest_gpu
        attest_gpu = attest_gpu_conf
        attest_gpu_env = os.environ.get("ATTEST_GPU")
        if attest_gpu_env:
            attest_gpu = not (attest_gpu_env.lower() == "false")
        logger.info(
            f"attest_gpu: conf={attest_gpu_conf}, env={attest_gpu_env}, use={attest_gpu}"
        )

        max_try_count = 3
        for _ in range(max_try_count):
            try:
                service_id = self.config.service_id
                if not service_id:
                    service_id = os.getenv("JPCC_JCK_SERVICE_ID")

                key_info = self._get_tks_info_from_pcc(service_id, self.config.tks_app_id)
                if key_info:
                    ring_id = key_info[0]
                    key_id = key_info[1]

                if self.config.pcc_login_url:
                    cookies = self._pcc_login()
                    private_key = tks_client.get_key(
                        ring_id=ring_id,
                        key_id=key_id,
                        need_evidence=need_evidence,
                        attest_gpu=attest_gpu,
                        cookies=cookies,
                    )
                else:
                    private_key = tks_client.get_key(
                        ring_id=ring_id,
                        key_id=key_id,
                        need_evidence=need_evidence,
                        attest_gpu=attest_gpu,
                        policy_id=self.config.tks_policy_id,
                        tks_url=self.config.tks_url,
                        tks_uid=self.config.tks_app_id,
                        tks_service_name=self.config.tks_service_name,
                    )

                pair_key_info = self._get_pairkey_from_pem(private_key)
                logger.info("get key from TKS success")
                if pair_key_info:
                    logger.debug(f"TKS public key={pair_key_info.get('pub_key')}")

                self._add_key(private_key, None)

                return True
            except Exception as e:
                logger.critical(f"load_tks_key exception={e}")
                logger.critical("load_tks_key failed, try again ....")
                time.sleep(5)

        return False

    def load_file_key(self, path: Optional[GenericPath] = None):
        """
        从文件读取 RSA 密钥.

        Args:
            path: 密钥文件路径. 默认为配置中的 `key_file`.
        """

        path = path or self.config.key_file
        if path is None:
            raise error.ParamError("path", "Key file is not specified")

        with open(path) as f:
            self.load_key(f.read())

        return True

    def load_key(self, private_key: Union[str, bytes]):
        """
        导入 RSA 密钥.

        Args:
            private_key: PEM 格式的 RSA 私钥.
        """
        self._add_key(private_key, tks_version=None)

    def generate_key(self):
        """
        随机生成密钥对.
        """
        expire_at = datetime.now(timezone.utc) + timedelta(
            seconds=self.config.valid_time
        )

        session_key = ServerSessionKey.generate(expire_at)
        # 修改时加锁
        with self.session_key_lock:
            self.old_session_key = self.session_key
            self.session_key = session_key

        return True

    def remove_expired_keys(self):
        """
        删除已过期的密钥对.
        """
        # 修改时加锁
        with self.session_key_lock:
            if self.session_key is not None and self.session_key.is_expired():
                self.session_key = None

            if self.old_session_key is not None and self.old_session_key.is_expired():
                self.old_session_key = None

    def _get_public_key(self) -> str:
        """
        获取已保存的最新的公钥.

        Raises:
            KeyMissingError: 没有可用的密钥. 应通过 `load_tks_key`, `load_key`, 或
                `generate_key` 添加密钥.
        """
        with self.session_key_lock:
            current_key = self.session_key

        if not current_key:
            raise error.KeyMissingError() from None

        return current_key.get_public_key()

    def handle_ra_request(self, request: RaRequest) -> RaResponse:
        """
        处理来自数据发送方的远程证明请求.
        应当在调用本函数前, 验证请求中 `token` 身份令牌的有效性.

        Returns:
            远程证明响应. 可作为 JSON 响应给数据发送方.
        Raises:
            NetworkError: 访问证明生成服务 (EPS) 或远程证明服务 (RAS) 时出现问题.
            KeyMissingError: 没有可用的密钥. 应通过 `load_tks_key`, `load_key`, 或
                `generate_key` 添加密钥.
        """
        validata_ra_request(request)

        # quote = self.eps_client.get_quote(request["nonce"])
        # token = self.ras_client.get_attestation_evaluation("TDX", quote)

        res_meta_data = RaResponseMetadata(Code=0, Message="success")
        res_result: RaResponsePods = {
            "pod_1": RaResponsePod(
                evidence="evidence",
                token="token",
                key_info={"pub_key_info": self._get_public_key()},
            ),
        }

        return RaResponse(ResponseMetadata=res_meta_data, ResponseResult=res_result)

    def decrypt(
            self,
            message: Union[str, bytes],
            app_info: Optional[str] = None,
            sign: Optional[str] = None,
    ) -> bytes:
        """
        解密二进制数据.

        Raises:
            DecryptionError: 加密消息不合法, 或者加密使用的密钥不在当前可用的密钥中.
            KeyMissingError: 没有可用的密钥. 应通过 `load_tks_key`, `load_key`, 或
                `generate_key` 添加密钥.
        """
        if app_info and sign:
            if not self.verify_sign(app_info, message, sign):
                raise error.SignatureError("verify sign failed")

        plaintext, _ = self.decrypt_with_response(message)
        return plaintext

    def decrypt_with_response(
            self,
            message: Union[str, bytes],
            app_info: Optional[str] = None,
            sign: Optional[str] = None,
    ) -> Tuple[bytes, ResponseKey]:
        """
        解密二进制数据, 并获取用于加密响应的密钥.

        Raises:
            DecryptionError: 加密消息不合法, 或者加密使用的密钥不在当前可用的密钥中.
            KeyMissingError: 没有可用的密钥. 应通过 `load_tks_key`, `load_key`, 或
                `generate_key` 添加密钥.
        """
        last_error: Optional[Exception] = None

        if app_info and sign:
            if not self.verify_sign(app_info, message, sign):
                raise error.SignatureError("verify sign failed")

        with self.session_key_lock:
            current_key = self.session_key
            old_key = self.old_session_key

        for key in [current_key, old_key]:
            if key is None:
                continue
            try:
                response_key = key.decrypt(message)
                return response_key
            except Exception as e:
                last_error = e
                continue

        if last_error:
            # 尝试更新一下密钥，因为上面的失败可能是本地密钥版本晚于客户端的密钥版本，等TKS支持密钥版本后可用密钥版本号来比较
            self._auto_load_key()
            if self.session_key is not None:
                try:
                    response_key = self.session_key.decrypt(message)
                    return response_key
                except Exception as e:
                    last_error = e

        raise last_error or error.KeyMissingError()

    def decrypt_file(
            self,
            metadata: Union[str, bytes],
            source_path: GenericPath,
            dest_path: GenericPath,
            mode: FileMode,
            app_info: Optional[str] = None,
            sign: Optional[str] = None,
    ) -> ResponseKey:
        """
        解密文件数据.

        Returns:
            用于加密响应的密钥.
        """
        if mode not in ["b", "t"]:
            raise error.ParamError("mode", "Mode should be 'b' or 't'")

        if app_info and sign:
            # Use metadata as the signed message to avoid empty msg causing verify_sign to fail.
            if not self.verify_sign(app_info, metadata, sign):
                raise error.SignatureError("verify sign failed")

        with self.session_key_lock:
            current_key = self.session_key
            old_key = self.old_session_key

        last_error: Optional[Exception] = None
        for key in [current_key, old_key]:
            if key is None:
                continue
            try:
                with open(source_path, f"r{mode}") as source, open(
                        dest_path, f"w{mode}"
                ) as dest:
                    response_key = key.decrypt_stream(metadata, source, dest, mode)
                    return response_key
            except Exception as e:
                last_error = e
                continue

        if last_error:
            # 尝试更新一下密钥，因为上面的失败可能是本地密钥版本晚于客户端的密钥版本，等TKS支持密钥版本后可用密钥版本号来比较
            self._auto_load_key()
            if self.session_key is not None:
                try:
                    with open(source_path, f"r{mode}") as source, open(
                            dest_path, f"w{mode}"
                    ) as dest:
                        response_key = self.session_key.decrypt_stream(
                            metadata, source, dest, mode
                        )
                        return response_key
                except Exception as e:
                    last_error = e

        raise last_error or error.KeyMissingError()

    def attest_client(self) -> bool:
        """
        对客户端进行远程证明, 判断客户端是否可信.

        Returns:
            True 为可信, False 为不可信.
        """
        client_ra_config = self.config.client_ra_config
        if not client_ra_config:
            return True

        client_ra_config = json.loads(client_ra_config)
        if not client_ra_config.get("open"):
            return True

        logger.info("start attest client")
        nonce = ''.join(str(uuid.uuid4()).split('-'))[-16:]
        max_try_count = 3
        for _ in range(max_try_count):
            ret = attest_client(client_ra_config, self.config.bytedance_top_info, nonce)
            if ret:
                logger.info("attest client success")
                return True
            else:
                logger.info("attest client failed, try again...")

        return False

    def _root_key_parse(self):
        """
        [{
            "app_info": "lenovo_xiao_tian",
            "pub_key": "******"
        }]
        :return:
        """
        try:
            root_key_config = self.config.root_key_config
            if not root_key_config:
                return

            if isinstance(root_key_config, str):
                root_key_config = json.loads(root_key_config)

            for tmp_info in root_key_config:
                app_info = tmp_info.get("app_info")
                pub_key = tmp_info.get("pub_key")
                if pub_key:
                    with open(pub_key) as f:
                        public_pem = f.read()
                    self.root_key_info[app_info] = PublicKey.from_public_pem(public_pem)
                else:
                    # 从pcc_controller中读取
                    public_pem = self._get_app_key_from_pcc(app_info)
                    if public_pem:
                        self.root_key_info[app_info] = PublicKey.from_public_pem(
                            public_pem
                        )
                    else:
                        logger.error("get app pubkey from pcc_controller failed")

            logger.info("root_key_parse success")
        except Exception as e:
            logger.critical("root_key_parse exception={}".format(e))
            raise error.ConfigError("RootKey conf", "RootPubKey conf error")

    def verify_sign(
            self, app_info: str, msg: Union[str, bytes], sign: Union[str, bytes]
    ) -> bool:
        """
        签名验证
        :param app_info: app_id+app_name
        :param msg:
        :param sign:
        :return:
        """
        try:
            if not app_info or not msg or not sign:
                logger.info(f"verify_sign error, app_info={app_info}, sign={sign}")
                raise error.SignatureError("RSA signing failed") from None

            if app_info not in self.root_key_info:
                logger.info(
                    f"verify_sign error, can not find app_info in root key conf, app_info={app_info}"
                )
                raise error.SignatureError(
                    f"can not find app_info={app_info}"
                ) from None

            if isinstance(sign, str):
                sign = base64.b64decode(sign.encode())

            return self.root_key_info[app_info].verify(sign, msg)

        except Exception as e:
            logger.critical("verify_sign exception={}".format(e))
            raise error.SignatureError("can not find app_info") from e

    def _get_app_key_from_pcc(self, app_info):
        try:
            if not app_info:
                return None

            top_conf = json.loads(self.config.bytedance_top_info)
            top_conf["action"] = "ListJscAppInfo"

            url = top_conf.get("top_url", "open.volcengineapi.com")
            body = {"PageSize": -1}
            headers = {}
            response = request_bytedance_gateway(url, body, headers, top_conf)
            if not response or response.status_code != 200:
                logger.error("get app key from pcc_controller failed")
                return None

            ra_res = json.loads(response.text).get("Result")
            if not ra_res:
                logger.error(
                    f"get app key from pcc_controller error: app_info={app_info}"
                )
                return None

            app_list = json.loads(response.text).get("Result").get("AppList")
            for app in app_list:
                if app_info == app.get("AppInfo"):
                    return app.get("AppKey")

            return None
        except Exception as e:
            logger.critical("get_app_key_from_pcc exception={}".format(e))
            return None

    def _init_log(self):
        config = LogConfig()

        log_config = dict()
        if self.config.log_config:
            log_config = json.loads(self.config.log_config)

        if config_dir := log_config.get("dir"):
            config.dir = config_dir

        if config_filename := log_config.get("filename"):
            config.filename = config_filename
        # else:
        #     config.filename = "server.log"

        if config_rotation := log_config.get("rotation"):
            config.rotation = config_rotation

        if config_retention := log_config.get("retention"):
            config.retention = config_retention

        if config_level := log_config.get("level"):
            config.level = config_level

        logger.init_log_config(config)
