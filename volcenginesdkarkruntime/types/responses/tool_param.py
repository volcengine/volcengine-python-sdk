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

from __future__ import annotations

from typing import Union

from typing_extensions import TypeAlias

from .doubao_app_tool_param import DoubaoAppToolParam
from .function_tool_param import FunctionToolParam
from .image_process_tool_param import ImageProcessToolParam
from .knowledge_search_tool_param import KnowledgeSearchToolParam
from .mcp_tool_param import Mcp
from .web_search_tool_param import WebSearchToolParam

__all__ = ["ToolParam"]

ToolParam: TypeAlias = Union[
    FunctionToolParam,
    WebSearchToolParam,
    ImageProcessToolParam,
    Mcp,
    KnowledgeSearchToolParam,
    DoubaoAppToolParam,
]
