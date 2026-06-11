__all__ = [
    "debug",
    "info",
    "warning",
    "error",
    "critical",
    "init_log_config"
]

import os.path
import sys
from typing import Any

from loguru import logger

from . import LogConfig, FORMAT


def init_log_config(*configs: LogConfig):
    """Initialize logging configuration with given configs."""
    logger.remove()

    log_level = "INFO"
    if os.environ.get("log_level"):
        log_level = os.environ.get("log_level")
    if os.environ.get("LOG_LEVEL"):
        log_level = os.environ.get("LOG_LEVEL")

    logger.add(sink=sys.stdout, format=FORMAT, level=log_level)

    for config in configs:
        if not config.dir:
            config.dir = "jsc_log"

        if not config.filename:
            config.filename = "jsc.log"

        os.makedirs(config.dir, exist_ok=True)
        fullpath = os.path.join(config.dir, config.filename)

        if config.rotation <= 0:
            config.rotation = 100
        rotation = f"{config.rotation} MB"

        if config.retention <= 0:
            config.retention = 7
        retention = f"{config.retention} days"

        logger.add(
            sink=fullpath,
            rotation=rotation,
            retention=retention,
            compression=config.compression,
            format=config.format,
            level=config.level
        )


def msg_proc(message: str) -> str:
    if message:
        return f"[jsc]:{message}"
    else:
        return message


def debug(message: str, *args: Any, **kwargs: Any) -> None:
    """Log debug message."""
    logger.opt(depth=1).debug(msg_proc(message), *args, **kwargs)


def info(message: str, *args: Any, **kwargs: Any) -> None:
    """Log info message."""
    logger.opt(depth=1).info(msg_proc(message), *args, **kwargs)


def warning(message: str, *args: Any, **kwargs: Any) -> None:
    """Log warning message."""
    logger.opt(depth=1).warning(msg_proc(message), *args, **kwargs)


def error(message: str, *args: Any, **kwargs: Any) -> None:
    """Log error message."""
    logger.opt(depth=1).error(msg_proc(message), *args, **kwargs)


def critical(message: str, *args: Any, **kwargs: Any) -> None:
    """Log critical message."""
    logger.opt(depth=1).critical(msg_proc(message), *args, **kwargs)
