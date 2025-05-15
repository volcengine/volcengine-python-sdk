from __future__ import annotations

from typing import Union

from typing_extensions import Literal, TypedDict

__all__ = [
    "CreateTaskContentTextParam",
    "CreateTaskContentImageDataParam",
    "CreateTaskContentImageParam",
    "CreateTaskContentParam",
]


class CreateTaskContentTextParam(TypedDict):
    type: Literal["text"]
    text: str
    """Text prompt describing the video generation job."""


class CreateTaskContentImageDataParam(TypedDict):
    url: str
    """URL of the image to be used for content generation."""


class CreateTaskContentImageParam(TypedDict):
    type: Literal["image_url"]
    image_url: CreateTaskContentImageDataParam
    role: str
    """Image data object containing image URL."""


CreateTaskContentParam = Union[CreateTaskContentTextParam, CreateTaskContentImageParam]
