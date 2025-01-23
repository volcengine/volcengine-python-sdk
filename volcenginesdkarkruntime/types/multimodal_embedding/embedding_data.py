from typing import List
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["MultimodalEmbedding"]


class MultimodalEmbedding(BaseModel):
    embedding: List[float]
    """The embedding vector, which is a list of floats."""

    object: Literal["embedding"]
    """The object type, which is always "embedding"."""
