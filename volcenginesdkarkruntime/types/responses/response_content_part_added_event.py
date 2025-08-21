
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

from typing import Union
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel
from .response_output_text import ResponseOutputText

__all__ = ["ResponseContentPartAddedEvent", "Part"]

Part: TypeAlias = Annotated[Union[ResponseOutputText], PropertyInfo(discriminator="type")]


class ResponseContentPartAddedEvent(BaseModel):
    content_index: int
    """The index of the content part that was added."""

    item_id: str
    """The ID of the output item that the content part was added to."""

    output_index: int
    """The index of the output item that the content part was added to."""

    part: Part
    """The content part that was added."""

    type: Literal["response.content_part.added"]
    """The type of the event. Always `response.content_part.added`."""
