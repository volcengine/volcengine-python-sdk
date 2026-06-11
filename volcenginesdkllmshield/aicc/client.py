"""
数据发送方接口.
"""

__all__ = ["Client"]

import base64
import json
import time
from dataclasses import dataclass, field
from typing import Any

from typing_extensions import TYPE_CHECKING, Dict, Optional, Tuple, Union

if TYPE_CHECKING:
    from _typeshed import GenericPath
else:
    GenericPath = str

from . import error
from .config import ClientConfig
from .consts import ClientConst
from .crypto import ClientSessionKey, FileMode, PrivateKey, ResponseKey
from .log import LogConfig, logger
from .ra import attest_server, generate_nonce
from .utils import RepeatTimer, weak_repeat_timer


@dataclass(eq=False)
class Client:
    """
    数据发送方接口.

    本类的所有方法是线程安全的.
    """

    config: ClientConfig

    session_key: Optional[ClientSessionKey] = field(init=False, default=None)

    attest_timer: Optional[RepeatTimer] = field(init=False, default=None)

    root_key_info: Dict[str, PrivateKey] = field(init=False, default_factory=dict)

    last_ra_time: float = 0.0

    def __post_init__(self):
        try:
            self._init_log()

            if self.config.root_key_config:
                self._root_key_parse()

            # if self.config.attest_interval is not None:
            #     # 初始化客户端时，以当前时间作为最近活跃时间
            #     self.last_active_time = time.time()
            #     # 内置最小定时间隔配置，避免因用户的不当配置造成的高负荷
            #     self.attest_timer = timer = weak_repeat_timer(
            #         max(self.config.attest_interval, ClientConst.MIN_ATTEST_INTERVAL),
            #         self._attest_server_no_raise,
            #     )
            #     timer.start()

            self._attest_server_no_raise()
        except Exception as e:
            logger.critical(f"__post_init__ failed, e={e}")

    def _attest_server_no_raise(self):
        logger.info("attest_server active")
        try:
            if not self.attest_server(None):
                logger.error("ra attest failed, Please check your config !")
            else:
                self.last_ra_time = time.time()
                logger.info("attest_server success")
        except Exception as e:
            logger.critical(f"Failed to attest server, {e}")

    def attest_server(self, token: Optional[str] = None) -> bool:
        """
        对数据接收方进行远程证明.
        """
        if self.config.pub_key_path:
            with open(self.config.pub_key_path) as f:
                public_pem = f.read()
            logger.debug(f"read pub key success, pub_key={public_pem}")
            self.session_key = ClientSessionKey.load(public_pem)
            return True
        else:
            max_try_count = 3
            count = 0

            nonce = generate_nonce()
            while count < max_try_count:
                count += 1
                ret, pub_key = attest_server(token, self.config, nonce)
                if ret:
                    logger.info("ra attest success")
                    if pub_key:
                        logger.debug(f"get pub key success, pub_key={pub_key}")
                        self.session_key = ClientSessionKey.load(pub_key)
                        return True
                else:
                    if pub_key and not self.config.attest_must:
                        logger.warning(f"ra attest failed, but get pub key success, pub_key={pub_key}")
                        self.session_key = ClientSessionKey.load(pub_key)
                        return True
                    else:
                        time.sleep(2)
                        logger.info("ra attest failed, try again...")

            return False

    def _get_key(self) -> ClientSessionKey:
        # 线程安全: 将 session_key 字段保存为本地变量, 避免访问两次
        key = self.session_key
        if key is None:
            raise error.KeyMissingError()
        return key

    def encrypt(self, plaintext: Union[str, bytes]) -> str:
        """
        加密字符串或二进制数据.

        Returns:
            信封加密数据.

        Raises:
            KeyMissingError: 没有可用的密钥. 应通过 `attest_server` 验证数据接收方, 并获取密钥.
        """
        message, _ = self.encrypt_with_response(plaintext)
        return message

    def encrypt_with_response(
            self, plaintext: Union[str, bytes]
    ) -> Tuple[str, ResponseKey]:
        """
        加密字符串或二进制数据, 并获取用于解密响应的密钥.

        Returns:
            信封加密数据, 及用于解密响应的密钥.

        Raises:
            KeyMissingError: 没有可用的密钥. 应通过 `attest_server` 验证数据接收方, 并获取密钥.
        """
        try:
            if (
                self.config.attest_interval is not None
                and time.time() - self.last_ra_time > self.config.attest_interval
            ):
                self._attest_server_no_raise()

            message, response_key = self._get_key().encrypt_with_response(plaintext)
            return message.serialize(), response_key
        except error.KeyMissingError as e:
            raise e
        except Exception as e:
            raise error.EncryptionError(
                "Encrypt failed, Please check your config"
            ) from e

    def encrypt_file(
            self,
            source_path: GenericPath,
            dest_path: GenericPath,
            mode: FileMode,
    ) -> str:
        """
        加密文件数据.

        Returns:
            信封加密元数据. 可伴随加密文件发送给数据接收方.
        """
        metadata, _ = self.encrypt_file_with_response(source_path, dest_path, mode)
        return metadata

    def encrypt_file_with_response(
            self,
            source_path: GenericPath,
            dest_path: GenericPath,
            mode: FileMode,
    ) -> Tuple[str, ResponseKey]:
        """
        加密文件数据, 并获取用于解密响应的密钥.

        Returns:
            信封加密元数据, 及用于解密响应的密钥. 其中元数据可伴随加密文件发送给数据接收方.
        """
        if (
                self.config.attest_interval is not None
                and time.time() - self.last_ra_time > self.config.attest_interval
        ):
            self._attest_server_no_raise()

        if mode not in ["b", "t"]:
            raise error.ParamError("mode", "Mode should be 'b' or 't'")

        try:
            key = self._get_key()
            with open(source_path, f"r{mode}") as source, open(
                    dest_path, f"w{mode}"
            ) as dest:
                metadata, response_key = key.encrypt_stream_with_response(
                    source, dest, mode
                )

            return metadata.serialize(), response_key
        except error.KeyMissingError as e:
            raise e
        except Exception as e:
            raise error.EncryptionError(
                "Encrypt file failed, Please check your config"
            ) from e

    def _root_key_parse(self):
        try:
            root_key_config = self.config.root_key_config
            if not root_key_config:
                return

            if isinstance(root_key_config, str):
                root_key_config = json.loads(root_key_config)

            for app_info, pri_key_path in root_key_config.items():
                with open(pri_key_path) as f:
                    private_pem = f.read()
                self.root_key_info[app_info] = PrivateKey.from_private_pem(private_pem)

            logger.info("root_key_parse success")
        except Exception as e:
            logger.critical("root_key_parse exception={}".format(e))
            raise error.ConfigError("RootKey conf", "RootPriKey conf error")

    def gen_sign(self, app_info: str, msg: Union[str, bytes]) -> str:
        """
        生成签名
        :param app_info: app_id+app_name
        :param msg: app_id+app_name
        :return:
        """
        try:
            if not app_info or not msg:
                logger.error("gen_sign error, app_info is NULL")
                raise error.SignatureError("RSA signing failed") from None

            if app_info not in self.root_key_info:
                logger.info(
                    f"gen_sign error, can not find app_info in root key conf, app_info={app_info}"
                )
                raise error.SignatureError(
                    f"can not find app_info={app_info}"
                ) from None

            return base64.b64encode(self.root_key_info[app_info].sign(msg)).decode()

        except Exception as e:
            logger.critical("gen_sign exception={}".format(e))
            raise error.SignatureError("can not find app_info") from e

    # def dynamic_update_interval(self):
    #     """
    #     动态更新定时逻辑的时间间隔。对不活跃的客户端，增大其定时逻辑的时间间隔
    #     """
    #     try:
    #         # 对于非定时RA的客户端，不做动态更新
    #         if self.config.attest_interval is None or self.attest_timer is None:
    #             return
    #
    #         # 如果超过一定时间没有活跃，就增大定时逻辑的时间间隔
    #         if time.time() - self.last_active_time > ClientConst.INACTIVE_THRESHOLD:
    #             self.attest_timer.interval = max(
    #                 self.config.attest_interval, ClientConst.INACTIVE_ATTEST_INTERVAL
    #             )
    #         else:
    #             # 如果活跃时间在阈值内，就恢复初始的时间间隔
    #             self.attest_timer.interval = max(
    #                 self.config.attest_interval, ClientConst.MIN_ATTEST_INTERVAL
    #             )
    #     except Exception as e:
    #         logger.error("dynamic_update_interval exception={}".format(e))

    def _init_log(self):
        config = LogConfig()

        log_config: Dict[str, Any] = {}
        if self.config.log_config:
            log_config = json.loads(self.config.log_config)

        if dir := log_config.get("dir"):
            config.dir = dir

        if filename := log_config.get("filename"):
            config.filename = filename
        # else:
        #     config.filename = "client.log"

        if rotation := log_config.get("rotation"):
            config.rotation = rotation

        if retention := log_config.get("retention"):
            config.retention = retention

        if level := log_config.get("level"):
            config.level = level

        logger.init_log_config(config)
