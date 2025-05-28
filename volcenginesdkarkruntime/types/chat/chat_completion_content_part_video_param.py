from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ChatCompletionContentPartVideoParam", "VideoURL"]


class VideoURL(TypedDict, total=False):
    url: Required[str]
    """Either a URL of the video or the base64 encoded video data."""

    fps: float
    """The sampling fps of the video."""


class ChatCompletionContentPartVideoParam(TypedDict, total=False):
    video_url: Required[VideoURL]

    type: Required[Literal["video_url"]]
    """The type of the content part."""
