
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

from .chat_completion_tool_message_param import ChatCompletionToolMessageParam
from .chat_completion_user_message_param import ChatCompletionUserMessageParam
from .chat_completion_system_message_param import ChatCompletionSystemMessageParam
from .chat_completion_function_message_param import ChatCompletionFunctionMessageParam
from .chat_completion_assistant_message_param import ChatCompletionAssistantMessageParam

__all__ = ["ChatCompletionMessageParam"]

ChatCompletionMessageParam = Union[
    ChatCompletionSystemMessageParam,
    ChatCompletionUserMessageParam,
    ChatCompletionAssistantMessageParam,
    ChatCompletionToolMessageParam,
    ChatCompletionFunctionMessageParam,
]
