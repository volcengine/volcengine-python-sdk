"""
证明生成服务 (Evidence Provision Service, EPS) 的客户端.
"""

__all__ = ["EpsClient", "EpsConfig"]

import logging
from dataclasses import dataclass

from typing_extensions import Any, Mapping

from .. import error
from .eps_models import Evidence, ExtendRuntimeMeasurementParams, NonceData

logger = logging.getLogger(__name__)


@dataclass
class EpsConfig:
    """访问证明生成服务所需的配置."""

    eps_url: str = "http://localhost:8006"
    """EPS 服务 Attestation Agent 的 HTTP 地址."""


def aa_request(endpoint: str, params: Mapping[str, Any], config: EpsConfig) -> str:
    """
    向 Attestation Agent 的指定端点发送 HTTP GET 请求.

    Returns:
        响应体的字符串.
    """
    import requests

    try:
        response = requests.get(config.eps_url + endpoint, params)
    except Exception as e:
        logger.exception(f"Network error: service={config.eps_url} {endpoint=}")
        raise error.NetworkError("EPS", config.eps_url, endpoint) from e

    if response.status_code != 200:
        logger.error(
            f"Service error: service={config.eps_url} {endpoint=} code={response.status_code}"
        )
        raise error.ServiceError("EPS", config.eps_url, endpoint, f"code={response.status_code}")
    if (content_type := response.headers["content-type"]) != "application/octet-stream":
        logger.error(f"Service error: service={config.eps_url} {endpoint=} {content_type=}")
        raise error.ServiceError("EPS", config.eps_url, endpoint, f"{content_type=}")

    try:
        return str(response.content, encoding="utf-8")
    except UnicodeDecodeError as e:
        logger.exception(f"Service error: service={config.eps_url} {endpoint=}")
        raise error.ServiceError("EPS", config.eps_url, endpoint, "cannot decode text") from e


@dataclass(eq=False)
class EpsClient:
    """
    证明生成服务 (Evidence Provision Service, EPS) 的客户端.

    本类的所有方法是线程安全的.
    """

    config: EpsConfig
    """访问证明生成服务所需的配置."""

    def get_token(self, token_type: str) -> str:
        """
        访问 Attestation Agent 的 `/aa/token` 端点, 获取令牌.

        Returns:
            令牌.
        """
        return aa_request("/aa/token", {"token_type": token_type}, self.config)

    def get_evidence_raw(self, nonce: str) -> str:
        """
        访问 Attestation Agent 的 `/aa/evidence` 端点, 获取证明.

        Returns:
            JSON 编码的证明. 包含 `cc_eventlog`, `quote`, `aa_eventlog` 字段.
        """
        nonce_data = NonceData(runtime_data="", nonce=nonce, user_data="")

        return aa_request("/aa/evidence", nonce_data, self.config)

    def get_evidence(self, nonce: str) -> Evidence:
        """
        访问 Attestation Agent 的 `/aa/evidence` 端点, 获取证明.

        Returns:
            证明内容, 包含 `cc_eventlog`, `quote`, `aa_eventlog` 字段.
        """
        import json

        raw = self.get_evidence_raw(nonce)

        return json.loads(raw)

    def get_eventlog(self, nonce: str) -> str:
        """
        访问 Attestation Agent 的 `/aa/eventlog` 端点, 获取事件日志.

        Returns:
            Base64 编码的事件日志. 事件日志长度较大 (~1.5MB).
        """
        nonce_data = NonceData(runtime_data="", nonce=nonce, user_data="")

        return aa_request("/aa/eventlog", nonce_data, self.config)

    def get_quote(self, nonce: str) -> str:
        """
        访问 Attestation Agent 的 `/aa/quote` 端点, 获取度量值.

        Returns:
            Base64 编码的度量值.
        """
        nonce_data = NonceData(runtime_data="", nonce=nonce, user_data="")

        return aa_request("/aa/quote", nonce_data, self.config)

    def get_extended_runtime_measurement(self, params: ExtendRuntimeMeasurementParams) -> str:
        """
        访问 Attestation Agent 的 `/aa/extend_runtime_measurement` 端点, 获取运行时度量事件日志.

        Returns:
            明文的运行时度量事件日志.
        """
        return aa_request("/aa/extend_runtime_measurement", params, self.config)
