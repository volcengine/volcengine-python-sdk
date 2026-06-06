"""
密钥管理服务 (Trusted Key Service, TKS) 的客户端.
TCA采用背调模式
"""

__all__ = ["TksClient", "TksConfig"]

from dataclasses import dataclass, field
from typing_extensions import Any, Optional, Tuple

from .eps import EpsClient
from .ras import RasClient


@dataclass
class TksConfig:
    """访问密钥管理服务所需的配置."""

    tks_url: str = "http://localhost:6789"
    """TKS 服务的 HTTP 地址."""

    tks_timezone: float = 8.0
    """TKS 服务使用的时区. 一般不需要修改."""

    tks_enable_server_auth: bool = True
    """
    是否对 TKS 服务提供的证明报告进行验证.
    默认为是.
    """

    tks_enable_bi_auth: bool = True
    """
    是否将客户端的证明报告发送给 TKS 服务.
    默认为是.
    """


@dataclass(eq=False)
class TksClient:
    """
    密钥管理服务 (Trusted Key Service, TKS) 的客户端.

    本类的所有方法是线程安全的.
    """

    config: TksConfig
    """访问密钥管理服务所需的配置."""

    ras_client: Optional[RasClient] = field(repr=False, default=None)

    eps_client: Optional[EpsClient] = field(repr=False, default=None)
