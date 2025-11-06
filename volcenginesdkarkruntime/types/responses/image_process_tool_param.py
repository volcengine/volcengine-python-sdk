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

from .image_process_grounding_options_param import ImageProcessGroundingOptionsParam
from .image_process_point_options_param import ImageProcessPointOptionsParam
from .image_process_rotate_options_param import ImageProcessRotateOptionsParam
from .image_process_zoom_options_param import ImageProcessZoomOptionsParam

__all__ = ["ImageProcessToolParam"]


class ImageProcessToolParam(TypedDict, total=False):
    type: Required[Literal["image_process"]]
    """The type of the image process. Always `image_process`."""

    point: Optional[ImageProcessPointOptionsParam]
    """Whether enable point tool."""

    grounding: Optional[ImageProcessGroundingOptionsParam]
    """Whether enable grounding tool."""

    zoom: Optional[ImageProcessZoomOptionsParam]
    """Whether enable zoom tool."""

    rotate: Optional[ImageProcessRotateOptionsParam]
    """Whether enable rotate tool."""
