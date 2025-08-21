
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

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ResponseWebSearchCallInProgressEvent"]


class ResponseWebSearchCallInProgressEvent(BaseModel):

    item_id: str
    """The ID of the item this event is associated with."""

    output_index: int
    """The index of the output item this event is associated with."""

    type: Literal["response.web_search_call.in_progress"]
    """The type of the event. Always `response.web_search_call.in_progress`."""
