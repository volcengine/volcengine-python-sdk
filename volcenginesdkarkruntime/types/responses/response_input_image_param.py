
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

from .response_input_image_pixel_limit_param import ResponseInputImagePixelLimit


__all__ = ["ResponseInputImageParam"]


class ResponseInputImageParam(TypedDict, total=False):
    detail: Required[Literal["low", "high", "auto"]]
    """The detail level of the image to be sent to the model.

    One of `high`, `low`, or `auto`. Defaults to `auto`.
    """

    type: Required[Literal["input_image"]]
    """The type of the input item. Always `input_image`."""

    image_url: Optional[str]
    """The URL of the image to be sent to the model.

    A fully qualified URL or base64 encoded image in a data URL.
    """
    image_pixel_limit: Optional[ResponseInputImagePixelLimit]
    """
    If the image size is not within this range, it will be proportionally scaled up or down to fit within the range.
    """
