# Copyright (c) [2025] [OpenAI]
# Copyright (c) [2025] [ByteDance Ltd. and/or its affiliates.]
# SPDX-License-Identifier: Apache-2.0
#
# This file has been modified by [ByteDance Ltd. and/or its affiliates.] on 2025.7
#
# Original file was released under Apache License Version 2.0, with the full license text
# available at https://github.com/openai/openai-python/blob/main/LICENSE.
#
# This modified file is released under the same license.

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
