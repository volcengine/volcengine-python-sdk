
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

__all__ = ["ResponseReasoningItem", "Summary"]


class Summary(BaseModel):
    text: str
    """
    A short summary of the reasoning used by the model when generating the response.
    """

    type: Literal["summary_text"]
    """The type of the object. Always `summary_text`."""


class ResponseReasoningItem(BaseModel):
    id: str
    """The unique identifier of the reasoning content."""

    summary: List[Summary]
    """Reasoning text contents."""

    type: Literal["reasoning"]
    """The type of the object. Always `reasoning`."""

    status: Optional[Literal["in_progress", "completed", "incomplete"]] = None
    """The status of the item.

    One of `in_progress`, `completed`, or `incomplete`. Populated when items are
    returned via API.
    """
