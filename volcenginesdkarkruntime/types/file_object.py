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

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["FileObject"]


class Error(BaseModel):
    code: str
    """The error code."""

    message: str
    """The error message."""

    param: Optional[str] = None
    """The parameter that was invalid, if any."""

    type: Optional[str] = None
    """The error type."""


class FileObject(BaseModel):
    id: str
    """The file identifier, which can be referenced in the API endpoints."""

    bytes: int
    """The size of the file, in bytes."""

    created_at: int
    """The Unix timestamp (in seconds) for when the file was created."""

    expire_at: int
    """The Unix timestamp (in seconds) for when the file will expire."""

    filename: str
    """The name of the file."""

    object: Literal["file"]
    """The object type, which is always `file`."""

    purpose: Literal["user_data",]
    """The intended purpose of the file.
    """

    status: Literal["processing", "active", "failed"]
    """The current status of the file, which can be either `processing`, `active`, or
    `failed`.
    """

    error: Optional[Error] = None
    """The error information, if status=`failed`."""

    mime_type: Optional[str] = None
    """The MIME type of the file."""

    preprocess_configs: Optional[dict] = None
    """The preprocess configs of the file."""
