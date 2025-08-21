
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

from .tool_choice_options import ToolChoiceOptions
from .tool_choice_function_param import ToolChoiceFunctionParam

__all__ = [
    "ToolChoice",
]

ToolChoice: TypeAlias = Union[ToolChoiceOptions, ToolChoiceFunctionParam]
