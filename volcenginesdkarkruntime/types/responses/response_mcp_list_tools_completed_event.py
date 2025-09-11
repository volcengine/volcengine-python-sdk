
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

__all__ = ["ResponseMcpListToolsCompletedEvent"]


class ResponseMcpListToolsCompletedEvent(BaseModel):
    item_id: str
    """The ID of the MCP tool call item that produced this output."""

    output_index: int
    """The index of the output item that was processed."""

    sequence_number: int
    """The sequence number of this event."""

    type: Literal["response.mcp_list_tools.completed"]
    """The type of the event. Always 'response.mcp_list_tools.completed'."""
