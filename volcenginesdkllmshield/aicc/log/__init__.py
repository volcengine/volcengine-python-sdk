__all__ = [
    "DEBUG",
    "INFO",
    "WARNING",
    "ERROR",
    "CRITICAL",
    "FORMAT",
    "LogConfig",
    "debug",
    "info",
    "warning",
    "error",
    "critical",
    "init_log_config"
]

from .config import DEBUG, INFO, WARNING, ERROR, CRITICAL, FORMAT, LogConfig
from .logger import init_log_config, info, debug, warning, error, critical

_initialized = False
if not _initialized:
    config = LogConfig()
    init_log_config(config)
    _initialized = True
