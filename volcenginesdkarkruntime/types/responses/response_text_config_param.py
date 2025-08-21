
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

from __future__ import annotations

from typing_extensions import TypedDict

from .response_format_text_config_param import ResponseFormatTextConfigParam

__all__ = ["ResponseTextConfigParam"]


class ResponseTextConfigParam(TypedDict, total=False):
    format: ResponseFormatTextConfigParam
    """An object specifying the format that the model must output.

    The default format is `{ "type": "text" }` with no additional options.

    Setting to `{ "type": "json_object" }` enables the older JSON mode, which
    ensures the message the model generates is valid JSON. Using `json_schema` is
    preferred for models that support it.
    """
