from typing import List, Optional

from ..._models import BaseModel
from typing_extensions import Literal

__all__ = ["CreateContextResponse", "TruncationStrategy"]


class TruncationStrategy(BaseModel):
    type: Literal["last_history_tokens"]
    """The truncation strategy to use for the context. The default is last_history_tokens."""
    last_history_tokens: Optional[int] = None
    """The number of most recent tokens from the context when constructing the chat completion."""


class CreateContextResponse(BaseModel):
    id: str
    """A unique identifier for the context."""
    model: str
    """The endpoint used for the context."""
    ttl: int
    """The time to live (TTL) for the context in seconds."""
    truncation_strategy: TruncationStrategy
    """
    Controls for how a context will be truncated prior to the run. 
    Use this to control the context window for the chat completion.
    """
