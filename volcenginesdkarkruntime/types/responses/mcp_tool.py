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

from typing import Optional, Dict, Union, List
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel


__all__ = [
    "Mcp",
    "McpAllowedTools",
    "McpAllowedToolsMcpAllowedToolsFilter",
    "McpRequireApproval",
    "McpRequireApprovalMcpToolApprovalFilter",
    "McpRequireApprovalMcpToolApprovalFilterAlways",
    "McpRequireApprovalMcpToolApprovalFilterNever",
]


class McpAllowedToolsMcpAllowedToolsFilter(BaseModel):
    tool_names: Optional[List[str]] = None
    """List of allowed tool names."""


class McpRequireApprovalMcpToolApprovalFilterAlways(BaseModel):
    tool_names: Optional[List[str]] = None
    """List of tools that require approval."""


class McpRequireApprovalMcpToolApprovalFilterNever(BaseModel):
    tool_names: Optional[List[str]] = None
    """List of tools that do not require approval."""


class McpRequireApprovalMcpToolApprovalFilter(BaseModel):
    always: Optional[McpRequireApprovalMcpToolApprovalFilterAlways] = None
    """A list of tools that always require approval."""

    never: Optional[McpRequireApprovalMcpToolApprovalFilterNever] = None
    """A list of tools that never require approval."""


McpAllowedTools: TypeAlias = Union[
    List[str], McpAllowedToolsMcpAllowedToolsFilter, None
]

McpRequireApproval: TypeAlias = Union[
    McpRequireApprovalMcpToolApprovalFilter, Literal["always", "never"], None
]


class Mcp(BaseModel):
    server_label: str
    """A label for this MCP server, used to identify it in tool calls."""

    server_url: str
    """The URL for the MCP server."""

    type: Literal["mcp"]
    """The type of the MCP tool. Always `mcp`."""

    allowed_tools: Optional[McpAllowedTools] = None
    """List of allowed tool names or a filter object."""

    headers: Optional[Dict[str, str]] = None
    """Optional HTTP headers to send to the MCP server.

    Use for authentication or other purposes.
    """

    require_approval: Optional[McpRequireApproval] = None
    """Specify which of the MCP server's tools require approval."""

    server_description: Optional[str] = None
    """Optional description of the MCP server, used to provide more context."""
