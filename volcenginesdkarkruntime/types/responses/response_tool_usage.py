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

from typing import Dict, Optional

from ..._models import BaseModel

__all__ = ["ToolUsage", "ToolUsageDetails"]


class ToolUsage(BaseModel):
    web_search: Optional[int] = None
    """The usage of web search tools."""

    mcp: Optional[int] = None
    """The usage of mcp tools."""

    knowledge_search: Optional[int] = None
    """The usage of knowledge search tools."""


class ToolUsageDetails(BaseModel):
    web_search: "Dict[str, int]"
    """The usage of web search tools."""

    mcp: "Dict[str, int]"
    """The usage of MCP tools."""

    knowledge_search: "Dict[str, int]"
    """The usage of knowledge search tools."""
