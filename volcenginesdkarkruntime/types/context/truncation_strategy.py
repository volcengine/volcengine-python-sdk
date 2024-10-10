from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["TruncationStrategy"]


class TruncationStrategy(BaseModel):
    type: Literal["last_history_tokens"]
    """The truncation strategy to use for the context. The default is last_history_tokens."""
    last_history_tokens: Optional[int] = None
    """The number of most recent tokens from the context when constructing the chat completion."""
