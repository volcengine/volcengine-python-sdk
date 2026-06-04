# Copyright (c) [2025] [OpenAI]
# Copyright (c) [2025] [ByteDance Ltd. and/or its affiliates.]
# SPDX-License-Identifier: Apache-2.0
#
# This file has been modified by [ByteDance Ltd. and/or its affiliates.] on 2025.7
#
# Original file was released under Apache License Version 2.0, with the full license text
# available at https://github.com/openai/openai-python/blob/main/LICENSE.
#
# This modified file is released under the same license.

from __future__ import annotations
import datetime
from typing_extensions import Required, TypedDict
from typing import Optional
from .._types import FileTypes
from .file_purpose import FilePurpose

__all__ = ["FileCreateParams", "PreprocessConfigs", "Video", "TosStorageParam"]


class TosStorageParam(TypedDict, total=False):
    """Specifies a user-owned TOS bucket destination."""

    bucket: str
    """The TOS bucket name."""

    prefix: str
    """The upload prefix under the bucket."""

    object_key: str
    """The full object path in the bucket."""


class FileCreateParams(TypedDict, total=False):
    file: FileTypes
    """The File object (not file name) to be uploaded.
    Mutually exclusive with `url`.
    """

    purpose: Required[FilePurpose]
    """The intended purpose of the uploaded file."""

    expire_at: datetime.datetime
    """The expiration timestamp for the file."""

    preprocess_configs: Optional[PreprocessConfigs]
    """The preprocess configs of the file."""

    url: str
    """An alternative file source (http/https or tos:// scheme).
    Mutually exclusive with the binary `file` field.
    """

    tos: Optional[TosStorageParam]
    """Specifies the user-owned TOS bucket destination.
    Required when `url` is provided; optional with binary file upload.
    """


class Video(TypedDict, total=False):
    """The video configs of the file."""

    fps: float
    """The fps of the video."""

    model: str
    """The model used for video preprocessing."""

    max_video_tokens: int
    """The maximum number of tokens for the video."""

    min_frame_tokens: int
    """The minimum number of tokens per frame."""

    max_frame_tokens: int
    """The maximum number of tokens per frame."""

    min_frames: int
    """The minimum number of frames to extract."""


class PreprocessConfigs(TypedDict, total=False):
    """The preprocess configs of the file."""

    video: Optional[Video]
    """The video configs of the file."""
