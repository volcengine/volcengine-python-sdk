
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

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel
from .response_output_message import ResponseOutputMessage
from .response_input_message_item import ResponseInputMessageItem
from .response_function_tool_call_item import ResponseFunctionToolCallItem
from .response_function_tool_call_output_item import ResponseFunctionToolCallOutputItem


__all__ = [
    "ResponseItem",
]

ResponseItem: TypeAlias = Annotated[
    Union[
        ResponseInputMessageItem,
        ResponseOutputMessage,
        ResponseFunctionToolCallItem,
        ResponseFunctionToolCallOutputItem,
    ],
    PropertyInfo(discriminator="type"),
]
