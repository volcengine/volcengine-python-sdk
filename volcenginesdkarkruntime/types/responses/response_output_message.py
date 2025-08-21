
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

from typing import List, Union
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel
from .response_output_text import ResponseOutputText

__all__ = ["ResponseOutputMessage", "Content"]

Content: TypeAlias = Annotated[Union[ResponseOutputText], PropertyInfo(discriminator="type")]


class ResponseOutputMessage(BaseModel):
    id: str
    """The unique ID of the output message."""

    content: List[Content]
    """The content of the output message."""

    role: Literal["assistant"]
    """The role of the output message. Always `assistant`."""

    status: Literal["in_progress", "completed", "incomplete"]
    """The status of the message input.

    One of `in_progress`, `completed`, or `incomplete`. Populated when input items
    are returned via API.
    """

    type: Literal["message"]
    """The type of the output message. Always `message`."""
