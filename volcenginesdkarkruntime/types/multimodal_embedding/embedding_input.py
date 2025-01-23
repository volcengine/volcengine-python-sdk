from __future__ import annotations

from typing import Union

from .embedding_content_part_image_param import MultimodalEmbeddingContentPartImageParam
from .embedding_content_part_text_param import (
    MultimodalEmbeddingContentPartTextParam,
)

__all__ = ["EmbeddingInputParam"]

EmbeddingInputParam = Union[
    MultimodalEmbeddingContentPartImageParam, MultimodalEmbeddingContentPartTextParam
]
