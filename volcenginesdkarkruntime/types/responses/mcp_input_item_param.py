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

from typing_extensions import TypedDict, Required, Optional, Iterable, Literal

__all__ = [
    "McpListTools",
    "McpListToolsTool",
    "McpApprovalRequest",
    "McpApprovalResponse",
    "McpCall",
]


class McpListToolsTool(TypedDict, total=False):
    input_schema: Required[object]
    """The JSON schema describing the tool's input."""

    name: Required[str]
    """The name of the tool."""

    annotations: Optional[object]
    """Additional annotations about the tool."""

    description: Optional[str]
    """The description of the tool."""


class McpListTools(TypedDict, total=False):
    id: Required[str]
    """The unique ID of the list."""

    server_label: Required[str]
    """The label of the MCP server."""

    tools: Required[Iterable[McpListToolsTool]]
    """The tools available on the server."""

    type: Required[Literal["mcp_list_tools"]]
    """The type of the item. Always `mcp_list_tools`."""

    error: Optional[str]
    """Error message if the server could not list tools."""


class McpApprovalRequest(TypedDict, total=False):
    id: Required[str]
    """The unique ID of the approval request."""

    arguments: Required[str]
    """A JSON string of arguments for the tool."""

    name: Required[str]
    """The name of the tool to run."""

    server_label: Required[str]
    """The label of the MCP server making the request."""

    type: Required[Literal["mcp_approval_request"]]
    """The type of the item. Always `mcp_approval_request`."""


class McpApprovalResponse(TypedDict, total=False):
    approval_request_id: Required[str]
    """The ID of the approval request being answered."""

    approve: Required[bool]
    """Whether the request was approved."""

    type: Required[Literal["mcp_approval_response"]]
    """The type of the item. Always `mcp_approval_response`."""

    id: Optional[str]
    """The unique ID of the approval response"""

    reason: Optional[str]
    """Optional reason for the decision."""


class McpCall(TypedDict, total=False):
    id: Required[str]
    """The unique ID of the tool call."""

    arguments: Required[str]
    """A JSON string of the arguments passed to the tool."""

    name: Required[str]
    """The name of the tool that was run."""

    server_label: Required[str]
    """The label of the MCP server running the tool."""

    type: Required[Literal["mcp_call"]]
    """The type of the item. Always `mcp_call`."""

    error: Optional[str]
    """The error from the tool call, if any."""

    output: Optional[str]
    """The output from the tool call."""
