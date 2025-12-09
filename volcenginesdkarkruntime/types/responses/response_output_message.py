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

from typing import List, Optional

from typing_extensions import Literal

from ..._models import BaseModel
from .content import Content

__all__ = ["ResponseOutputMessage"]


class ResponseOutputMessage(BaseModel):
    type: Literal["message"]
    """The type of the output message. Always `message`."""

    role: Literal["assistant"]
    """The role of the output message. Always `assistant`."""

    content: List[Content]
    """The content of the output message."""

    status: Literal["in_progress", "completed", "incomplete", "searching", "failed"]
    """The status of the message input. One of `in_progress`, `completed`, or `incomplete`. Populated when input items are returned via API."""

    id: str
    """The unique ID of the output message."""

    partial: Optional[bool] = None
