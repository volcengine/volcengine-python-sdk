
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

from typing import Optional

from .chat_completion_message_tool_call import Function, ChatCompletionMessageToolCall

__all__ = ["ParsedFunctionToolCall", "ParsedFunction"]

# we need to disable this check because we're overriding properties
# with subclasses of their types which is technically unsound as
# properties can be mutated.
# pyright: reportIncompatibleVariableOverride=false


class ParsedFunction(Function):
    parsed_arguments: Optional[object] = None
    """
    The arguments to call the function with.
    """


class ParsedFunctionToolCall(ChatCompletionMessageToolCall):
    function: ParsedFunction
    """The function that the model called."""
