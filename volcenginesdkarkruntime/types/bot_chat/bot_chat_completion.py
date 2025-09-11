
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

from typing import List, Optional, Dict
from ..chat.chat_completion import ChatCompletion
from ..bot_chat.bot_reference import Reference
from ..bot_chat.bot_usage import BotUsage

__all__ = [
    "BotChatCompletion",
]


class BotChatCompletion(ChatCompletion):
    bot_usage: Optional[BotUsage] = None
    """
    bot_usage stands for the model & plugin usage of the bot, only return when "include_usage" is set true
    """

    references: Optional[List[Reference]] = None
    """
    references stands for the reference of difference plugins
    """

    metadata: Optional[Dict[str, object]] = None
    """
    metadata stands for the additional metadata of the bot
    """
