from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from ..chat.chat_completion_chunk import Choice
from ..completion_usage import CompletionUsage

__all__ = [
    "ContextChatCompletionChunk",
]


class ContextChatCompletionChunk(BaseModel):
    id: str
    """A unique identifier for the chat completion. Each chunk has the same ID."""

    choices: List[Choice]
    """A list of chat completion choices.

    Can be more than one if `n` is greater than 1.
    """

    created: int
    """The Unix timestamp (in seconds) of when the chat completion was created.

    Each chunk has the same timestamp.
    """

    model: str
    """The model to generate the completion."""

    object: Literal["chat.completion.chunk"]
    """The object type, which is always `chat.completion.chunk`."""

    usage: Optional[CompletionUsage] = None
    """
    An optional field that will only be present when you set
    `stream_options: {"include_usage": true}` in your request. When present, it
    contains a null value except for the last chunk which contains the token usage
    statistics for the entire request.
    """
