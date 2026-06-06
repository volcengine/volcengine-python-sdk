"""
远程证明服务 (Remote Attestation Service, RAS) 的客户端.
"""

__all__ = ["RasClient", "RasConfig"]

import base64
import json
import logging
from dataclasses import dataclass

from typing_extensions import Any

from .. import error

# try:
#     import grpc
#
#     from .ras_models import attestation_pb2, attestation_pb2_grpc
# except ModuleNotFoundError:
#     grpc = None
#     attestation_pb2_grpc = None


logger = logging.getLogger(__name__)

KNOWN_TEE = ["SEV", "SGX", "SNP", "TDX", "Sample", "AzSnpVtpm", "CSV", "CCA", "AzTdxVtpm"]


@dataclass
class RasConfig:
    """访问远程证明服务所需的配置."""

    ras_address: str = "localhost:50004"
    """远程证明服务的 GRPC 地址."""


def encode_base64_no_pad(data: Any) -> str:
    return base64.urlsafe_b64encode(json.dumps(data).encode("utf-8")).decode("utf-8").rstrip("=")


@dataclass(eq=False)
class RasClient:
    """
    远程证明服务 (Remote Attestation Service, RAS) 的客户端.

    本类的所有方法是线程安全的.
    """

    config: RasConfig
    """访问远程证明服务所需的配置."""

    def get_attestation_evaluation(self, tee: str, quote: str) -> str:
        """
        访问远程证明服务的 AttestationRequest 端点来验证度量值.

        Args:
            tee: 所属 TEE 环境类型.
            quote: Base64 编码的度量值. 参考 `EpsClient#get_quote()`.
        Returns:
            Base64 编码的验证令牌.
        """
        pass

        # if grpc is None or attestation_pb2_grpc is None:
        #     raise error.ConfigError(self, "RAS depends on grpcio which is not installed")
        #
        # # An early sanity check.
        # if tee not in KNOWN_TEE:
        #     raise error.ParamError("tee", f"Unknown TEE type '{tee}'")
        #
        # encoded_evidence = encode_base64_no_pad({"quote": quote})
        # request = attestation_pb2.AttestationRequest(  # pyright: ignore
        #     tee=tee, evidence=encoded_evidence, policy_ids=[]
        # )
        #
        # try:
        #     channel = grpc.insecure_channel(self.config.ras_address)
        #     client = attestation_pb2_grpc.AttestationServiceStub(channel)
        #
        #     response = client.AttestationEvaluate(request)
        # except Exception as e:
        #     logger.exception(
        #         f"Network error service={self.config.ras_address} endpoint=AttestationEvaluate"
        #     )
        #     raise error.NetworkError("RAS", self.config.ras_address, "AttestationEvaluate") from e
        #
        # return response.attestation_token
