from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["MultimodalEmbeddingContentPartImageParam", "ImageURL"]


class ImageURL(TypedDict, total=False):
    url: Required[str]
    """Either a URL of the image or the base64 encoded image data."""


class MultimodalEmbeddingContentPartImageParam(TypedDict, total=False):
    image_url: Required[ImageURL]

    type: Required[Literal["image_url"]]
    """The type of the content part."""
