import os
import logging

logger: logging.Logger = logging.getLogger("ark")
httpx_logger: logging.Logger = logging.getLogger("httpx")


def _basic_config() -> None:
    logging.basicConfig(
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


def setup_logging() -> None:
    level = logging.getLevelNamesMapping().get(os.environ.get("ARK_LOG", "").upper())
    if level is not None:
        _basic_config()
        logger.setLevel(level)
        httpx_logger.setLevel(level)
