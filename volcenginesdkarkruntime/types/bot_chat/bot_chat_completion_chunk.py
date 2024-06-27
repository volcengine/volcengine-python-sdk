from typing import List, Optional, Dict

from ..chat.chat_completion_chunk import ChatCompletionChunk
from ..bot_chat.bot_reference import Reference
from ..bot_chat.bot_usage import BotUsage

__all__ = [
    "BotChatCompletionChunk",
]


class BotChatCompletionChunk(ChatCompletionChunk):
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
