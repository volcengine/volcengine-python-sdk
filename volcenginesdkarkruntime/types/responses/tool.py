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

from typing import Union

from typing_extensions import Annotated, TypeAlias

from ..._utils import PropertyInfo
from .doubao_app_tool import DoubaoAppTool
from .function_tool import FunctionTool
from .image_process_tool import ImageProcessTool
from .knowledge_search_tool import KnowledgeSearchTool
from .mcp_tool import Mcp
from .web_search_tool import WebSearchTool

__all__ = ["Tool"]

Tool: TypeAlias = Annotated[
    Union[
        FunctionTool,
        WebSearchTool,
        ImageProcessTool,
        Mcp,
        KnowledgeSearchTool,
        DoubaoAppTool,
    ],
    PropertyInfo(discriminator="type"),
]
