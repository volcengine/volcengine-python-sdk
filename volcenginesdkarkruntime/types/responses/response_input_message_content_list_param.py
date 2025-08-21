
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

from typing import List, Union
from typing_extensions import TypeAlias

from .response_input_text_param import ResponseInputTextParam
from .response_input_image_param import ResponseInputImageParam
from .response_input_video_param import ResponseInputVideoParam

__all__ = ["ResponseInputMessageContentListParam", "ResponseInputContentParam"]

ResponseInputContentParam: TypeAlias = Union[ResponseInputTextParam, ResponseInputImageParam, ResponseInputVideoParam]

ResponseInputMessageContentListParam: TypeAlias = List[ResponseInputContentParam]
