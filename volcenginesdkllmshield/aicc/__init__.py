__all__ = [
    "Client",
    "ClientConfig",
    "FileMode",
    "RaRequest",
    "RaResponse",
    "ResponseKey",
    "Server",
    "ServerConfig",
    "TksAppOptions",
    "__version__",
]

__version__ = "0.1.7.78"

from .client import Client
from .config import ClientConfig, ServerConfig
from .crypto import FileMode, ResponseKey
from .ra import RaRequest, RaResponse
# from .server import Server
from .service import TksAppOptions


def __getattr__(name: str) -> object:
    if name == "Server":
        from .server import Server
        return Server
    raise AttributeError(f"module {__name__} has no attribute {name}")
