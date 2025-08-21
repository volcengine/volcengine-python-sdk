
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

__all__ = ["ResponseWebSearchItem"]


class ResponseWebSearchAction(BaseModel):
    query: str
    """The query of the web search action."""
    type: Literal["search"]
    """The type of the action. Always `search`."""


class ResponseWebSearchItem(BaseModel):
    id: str
    """The unique identifier of the web search item."""

    action: Optional[ResponseWebSearchAction] = None
    """The action of the web search item."""

    type: Literal["web_search_call"]
    """The type of the object. Always `web_search_call`."""

    status: Optional[Literal["in_progress", "completed", "incomplete"]] = None
    """The status of the item.

    One of `in_progress`, `completed`, or `incomplete`. Populated when items are
    returned via API.
    """
