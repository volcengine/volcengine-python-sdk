
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

from typing import Optional, List
from ..._models import BaseModel


class BotCompletionUsage(BaseModel):
    name: Optional[str] = None
    """
    name stands for endpoint called in bot
    """
    prompt_tokens: int = 0
    """
    prompt_tokens stands for the prompt tokens of different endpoints
    """
    completion_tokens: int = 0
    """
    completion_tokens stands for the completion tokens of different endpoints
    """
    total_tokens: int = 0
    """
    total_tokens stands for the total tokens of different endpoints
    """


class BotActionUsage(BaseModel):
    name: Optional[str] = None
    """
    name stands for different action source name
    """
    search_count: Optional[int] = None
    """
    search_count stands for the search count of different action source
    """


class BotUsage(BaseModel):
    model_usage: Optional[List[BotCompletionUsage]] = None
    """
    model_usage stands for the model usage of different endpoints
    """
    action_usage: Optional[List[BotActionUsage]] = None
    """
    action_usage stands for the action usage of different action source
    """
