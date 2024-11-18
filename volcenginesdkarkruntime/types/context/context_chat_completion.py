from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from ..chat.chat_completion import Choice
from ..completion_usage import CompletionUsage

__all__ = [
    "ContextChatCompletion",
]


class ContextChatCompletion(BaseModel):
    id: str
    """A unique identifier for the chat completion."""

    choices: List[Choice]
    """A list of chat completion choices.

    Can be more than one if `n` is greater than 1.
    """

    created: int
    """The Unix timestamp (in seconds) of when the chat completion was created."""

    model: str
    """The model used for the chat completion."""

    object: Literal["chat.completion"]
    """The object type, which is always `chat.completion`."""

    usage: Optional[CompletionUsage] = None
    """Usage statistics for the completion request."""
