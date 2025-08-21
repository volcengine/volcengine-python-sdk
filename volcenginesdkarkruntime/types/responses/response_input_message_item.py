
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

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .response_input_message_content_list import ResponseInputMessageContentList

__all__ = ["ResponseInputMessageItem"]


class ResponseInputMessageItem(BaseModel):
    id: str
    """The unique ID of the message input."""

    content: ResponseInputMessageContentList
    """
    A list of one or many input items to the model, containing different content
    types.
    """

    role: Literal["user", "system", "developer"]
    """The role of the message input. One of `user`, `system`, or `developer`."""

    status: Optional[Literal["in_progress", "completed", "incomplete"]] = None
    """The status of item.

    One of `in_progress`, `completed`, or `incomplete`. Populated when items are
    returned via API.
    """

    type: Optional[Literal["message"]] = None
    """The type of the message input. Always set to `message`."""
