
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
from .response_output_message import ResponseOutputMessage
from .response_reasoning_item import ResponseReasoningItem
from .response_function_tool_call import ResponseFunctionToolCall
from .response_web_search_item import ResponseWebSearchItem

__all__ = ["ResponseOutputItem"]

ResponseOutputItem: TypeAlias = Annotated[
    Union[
        ResponseOutputMessage,
        ResponseFunctionToolCall,
        ResponseReasoningItem,
        ResponseWebSearchItem,
    ],
    PropertyInfo(discriminator="type"),
]
