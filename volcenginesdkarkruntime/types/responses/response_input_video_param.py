
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

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ResponseInputVideoParam"]


class ResponseInputVideoParam(TypedDict, total=False):

    type: Required[Literal["input_video"]]
    """The type of the input item. Always `input_video`."""

    video_url: Optional[str]
    """The URL of the video to be sent to the model.

    A fully qualified URL or base64 encoded video in a data URL.
    """
    fps: Optional[float]
    """
    Extract a specified number of images from the video every second.
    """
