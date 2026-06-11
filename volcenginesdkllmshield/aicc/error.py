"""
安全通信错误类型.
"""

from dataclasses import dataclass, field
from enum import Enum

from typing_extensions import Literal, Optional


class ErrorKind(Enum):
    CONFIG = "config"
    PARAM = "param"

    NETWORK = "network"
    SERVICE = "service"

    ENCRYPTION = "encryption"
    DECRYPTION = "decryption"
    SIGNATURE = "signature"
    KEY_MISSING = "key_missing"
    KEY_EXPIRED = "key_expired"
    NONCE_REUSED = "nonce_reused"


class SecureChannelError(Exception):
    kind: ErrorKind


@dataclass
class ConfigError(SecureChannelError):
    kind: ErrorKind = field(init=False, repr=False, default=ErrorKind.CONFIG)

    config_object: object
    message: str

    def __str__(self) -> str:
        return f"{self.config_object}: {self.message}"


@dataclass
class ParamError(SecureChannelError):
    kind: ErrorKind = field(init=False, repr=False, default=ErrorKind.PARAM)

    param: str
    message: str

    def __str__(self) -> str:
        return f"{self.param}: {self.message}"


@dataclass
class NetworkError(SecureChannelError):
    kind: ErrorKind = field(init=False, repr=False, default=ErrorKind.NETWORK)

    service_name: Literal["EPS", "RA", "RAS", "TKS"]
    service: str
    endpoint: Optional[str]

    def _service(self) -> str:
        if self.endpoint is None:
            return f"{self.service_name} service {self.service}"
        else:
            return f"endpoint {self.endpoint} of {self.service_name} service {self.service}"

    def __str__(self) -> str:
        return f"Cannot access {self._service()}"


@dataclass
class ServiceError(NetworkError):
    kind: ErrorKind = field(init=False, repr=False, default=ErrorKind.SERVICE)

    message: str

    def __str__(self) -> str:
        return f"{self._service().capitalize()} returned error: {self.message}"


@dataclass
class EncryptionError(SecureChannelError):
    kind: ErrorKind = field(init=False, repr=False, default=ErrorKind.ENCRYPTION)

    message: str

    def __str__(self) -> str:
        return self.message


@dataclass
class DecryptionError(SecureChannelError):
    kind: ErrorKind = field(init=False, repr=False, default=ErrorKind.DECRYPTION)

    message: str

    def __str__(self) -> str:
        return self.message


@dataclass
class SignatureError(SecureChannelError):
    kind: ErrorKind = field(init=False, repr=False, default=ErrorKind.SIGNATURE)

    message: str

    def __str__(self) -> str:
        return self.message


@dataclass
class KeyMissingError(SecureChannelError):
    kind: ErrorKind = field(init=False, repr=False, default=ErrorKind.KEY_MISSING)

    def __str__(self) -> str:
        return "Can not get key, Please check your config !"


@dataclass
class KeyExpiredError(SecureChannelError):
    kind: ErrorKind = field(init=False, repr=False, default=ErrorKind.KEY_EXPIRED)

    def __str__(self) -> str:
        return "Key has expired"


@dataclass
class NonceReusedError(SecureChannelError):
    kind: ErrorKind = field(init=False, repr=False, default=ErrorKind.NONCE_REUSED)

    def __str__(self) -> str:
        return "Nonce is reused"
