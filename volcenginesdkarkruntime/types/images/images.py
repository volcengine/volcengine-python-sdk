
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

from typing import List

from volcenginesdkarkruntime._models import BaseModel

__all__ = ["ImagesResponse"]


class Usage(BaseModel):
    generated_images: int
    """The number of images generated."""


class Image(BaseModel):
    url: str
    """The URL of the generated image, if any."""

    b64_json: str
    """The Base 64 encoded string of the generated image, if any."""


class Error(BaseModel):
    message: str
    """The reason for failed image generation"""

    code: str
    """The error code for failed image generation"""


class ImagesResponse(BaseModel):
    model: str
    """The model used to generated the images."""

    data: List[Image]
    """The generated images."""

    error: Error
    """The error body, if applicable."""

    usage: Usage
    """The usage information for the generation of images."""

    created_at: int
    """The Unix timestamp when the image was generated."""
