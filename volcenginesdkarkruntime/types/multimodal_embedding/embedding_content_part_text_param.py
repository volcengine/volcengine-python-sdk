from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["MultimodalEmbeddingContentPartTextParam"]


class MultimodalEmbeddingContentPartTextParam(TypedDict, total=False):
    text: Required[str]
    """The text content."""

    type: Required[Literal["text"]]
    """The type of the content part."""
