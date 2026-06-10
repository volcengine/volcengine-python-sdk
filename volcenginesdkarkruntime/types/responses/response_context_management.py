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

__all__ = ["ResponseContextManagement", "AppliedContextManagementEdit"]


class AppliedContextManagementEdit(BaseModel):
    type: Literal["clear_thinking", "clear_tool_uses"]
    """The applied context edit strategy type."""

    cleared_thinking_turns: Optional[int] = None
    """The number of thinking turns cleared by the strategy."""

    cleared_tool_uses: Optional[int] = None
    """The number of tool uses cleared by the strategy."""


class ResponseContextManagement(BaseModel):
    applied_edits: List[AppliedContextManagementEdit]
    """Context edit strategies applied during response creation."""
