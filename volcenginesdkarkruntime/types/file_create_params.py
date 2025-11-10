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

__all__ = ["FileCreateParams", "PreprocessConfigs"]


class FileCreateParams(TypedDict, total=False):
    file: Required[FileTypes]
    """The File object (not file name) to be uploaded."""

    purpose: Required[FilePurpose]
    """The intended purpose of the uploaded file.
    """

    expire_at: datetime.datetime
    """The expiration timestamp for the file.
    """

    preprocess_configs: Optional[PreprocessConfigs]
    """The preprocess configs of the file."""


class Video(TypedDict, total=False):
    """The video configs of the file."""

    fps: float
    """The fps of the video."""


class PreprocessConfigs(TypedDict, total=False):
    """The preprocess configs of the file."""

    video: Optional[Video]
    """The video configs of the file."""
