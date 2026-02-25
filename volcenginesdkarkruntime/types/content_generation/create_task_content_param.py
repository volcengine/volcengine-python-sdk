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


class CreateTaskContentDraftTaskParam(TypedDict):
    type: Literal["draft_task"]
    draft_task: CreateTaskContentDraftTaskDataParam
    """ID of the draft task to be used for content generation."""

class CreateTaskContentDraftTaskDataParam(TypedDict):
    id: str
    """ID of the draft task to be used for content generation."""

CreateTaskContentParam = Union[CreateTaskContentTextParam, CreateTaskContentImageParam, CreateTaskContentDraftTaskParam]
