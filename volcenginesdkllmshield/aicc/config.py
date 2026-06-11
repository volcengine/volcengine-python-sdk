"""
安全通信配置.
"""

import json
import os
from dataclasses import dataclass
from datetime import timedelta

from typing_extensions import TYPE_CHECKING, Optional, Self

if TYPE_CHECKING:
    from _typeshed import GenericPath
else:
    GenericPath = str

from .ra import RaConfig
from .service import EpsConfig, RasConfig, TksConfig


@dataclass
class ClientConfig(RaConfig):
    """
    安全通信数据发送方配置.
    """

    attest_interval: Optional[float] = 3600
    """
    自动对数据接收方进行远程证明的时间间隔 (秒).
    为空表示不自动进行远程证明 (默认).
    """

    root_key_config: Optional[str] = None
    """
    root_key的配置，json格式的字符串.
    """

    log_config: Optional[str] = None

    pub_key_path: Optional[str] = None

    @classmethod
    def from_file(cls, path: GenericPath) -> Self:
        """从文件读取配置对象."""

        with open(path) as f:
            return cls.from_dict(json.load(f))

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        """从 dict 对象创建配置对象."""

        obj.pop("$schema", None)

        return cls(**obj)

    @classmethod
    def from_env(cls, env_key: str) -> Self:
        """从环境变量读取配置对象."""

        config = os.getenv(env_key, "{}")
        return cls.from_dict(json.loads(config))


@dataclass
class ServerConfig(EpsConfig, RasConfig, TksConfig):
    """
    安全通信数据接收方配置.
    """

    tks_app_id: Optional[str] = None
    """
    TKS app id.
    """

    tks_ring_id: Optional[str] = None
    """
    TKS 密钥环 id.
    为空表示不访问 TKS 获取密钥 (默认).
    """

    tks_key_id: Optional[str] = None
    """
    TKS 密钥 id.
    为空表示不访问 TKS 获取密钥 (默认).
    """

    key_file: Optional[GenericPath] = None
    """
    密钥文件路径.
    为空表示不从文件读取密钥 (默认).
    """

    refresh_interval: Optional[float] = None
    """
    自动从 TKS 或者文件获取密钥的时间间隔 (秒).
    为空表示不自动获取 (默认).
    """

    valid_time: float = timedelta(minutes=30).total_seconds()
    """【未启用】密钥的有效期 (秒). 默认为 30 分钟. """

    client_ra_url: Optional[str] = None
    """
    客户端 RA 接口地址.
    为空表示不需要对客户端做 RA (默认).
    """

    pcc_login_url: Optional[str] = None
    pcc_app_id: Optional[str] = None
    pcc_password: Optional[str] = None
    """
    pcc_controller模块的登录信息.
    为空表示不需要做.
    """

    bytedance_pcc_info: str = ""
    """访问bytedance pcc_controller 网关的信息."""

    bytedance_top_info: str = ""
    """访问bytedance TOP网关的信息."""

    root_key_config: Optional[str] = None
    """
    root_key的配置，json格式的字符串.
    """

    client_ra_config: Optional[str] = None
    """
    客户端RA的配置，json格式的字符串.
    """

    log_config: Optional[str] = None

    need_evidence: bool = True

    attest_gpu: bool = True

    key_type: str = "tks"

    service_id: str = ""

    tks_policy_id: str = ""

    tks_url: str = ""

    tks_service_name: str = ""

    @classmethod
    def from_file(cls, path: GenericPath) -> Self:
        """从文件读取配置对象."""

        with open(path) as f:
            return cls.from_dict(json.load(f))

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        """从 dict 对象创建配置对象."""

        obj.pop("$schema", None)

        return cls(**obj)

    @classmethod
    def from_env(cls, env_key: str) -> Self:
        """从env中读取配置对象."""

        conf_value = os.getenv(env_key, "{}")
        if isinstance(conf_value, str):
            conf_value = json.loads(conf_value)
        return cls.from_dict(conf_value)
