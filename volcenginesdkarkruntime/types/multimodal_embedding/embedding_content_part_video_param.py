from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["MultimodalEmbeddingContentPartVideoParam", "VideoURL"]


class VideoURL(TypedDict, total=False):
    url: Required[str]
    """Either a URL of the video or the base64 encoded video data."""
    fps: float
    """The sampling fps of the video."""
    max_video_tokens: int
    """The maximum number of video tokens. Must be between 10240 and 204800."""

    min_frame_tokens: int
    """The minimum number of tokens per frame. Must be between 16 and 128."""

    max_frame_tokens: int
    """The maximum number of tokens per frame. Must be between 128 and 640."""

    min_frames: int
    """The minimum number of sampled frames. Must be between 5 and 16."""



class MultimodalEmbeddingContentPartVideoParam(TypedDict, total=False):
    video_url: Required[VideoURL]

    type: Required[Literal["video_url"]]
    """The type of the content part."""
