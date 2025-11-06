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

from typing_extensions import Literal

from ..._models import BaseModel
from .image_process_grounding_options import ImageProcessGroundingOptions
from .image_process_point_options import ImageProcessPointOptions
from .image_process_rotate_options import ImageProcessRotateOptions
from .image_process_zoom_options import ImageProcessZoomOptions

__all__ = ["ImageProcessTool"]


class ImageProcessTool(BaseModel):
    type: Literal["image_process"]
    """The type of the image process. Always `image_process`."""

    point: Optional[ImageProcessPointOptions] = None
    """Whether enable point tool."""

    grounding: Optional[ImageProcessGroundingOptions] = None
    """Whether enable grounding tool."""

    zoom: Optional[ImageProcessZoomOptions] = None
    """Whether enable zoom tool."""

    rotate: Optional[ImageProcessRotateOptions] = None
    """Whether enable rotate tool."""
