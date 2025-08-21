
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
from .response_output_item import ResponseOutputItem

__all__ = ["ResponseOutputItemDoneEvent"]


class ResponseOutputItemDoneEvent(BaseModel):
    item: ResponseOutputItem
    """The output item that was marked done."""

    output_index: int
    """The index of the output item that was marked done."""

    type: Literal["response.output_item.done"]
    """The type of the event. Always `response.output_item.done`."""
