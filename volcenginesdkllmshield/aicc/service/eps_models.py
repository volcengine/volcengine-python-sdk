"""
证明生成服务 (EPS) 定义的数据类型.
"""

from typing_extensions import NotRequired, TypedDict


class NonceData(TypedDict):
    """
    Attestation Agent 的 `/aa/evidence`, `/aa/quote`, `/aa/eventlog` 端点的请求体.
    目前 Attestation Agent 会将三个字段值直接连接.
    """

    runtime_data: str

    nonce: str

    user_data: str


class ExtendRuntimeMeasurementParams(TypedDict):
    """
    Attestation Agent 的 `/aa/extend_runtime_measurement` 端点的请求体.
    """

    domain: str

    operation: str

    context: str

    register_index: NotRequired[int]


class Evidence(TypedDict):
    """
    Attestation Agent 的 `/aa/evidence` 端点的响应体.
    """

    cc_eventlog: str
    """Base64 编码的事件日志. 事件日志长度较大 (~1.5MB)."""

    quote: str
    """Base64 编码的度量值."""

    aa_eventlog: str
    """明文的运行时度量事件日志."""
