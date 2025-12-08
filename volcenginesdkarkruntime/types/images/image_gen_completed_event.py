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


from volcenginesdkarkruntime._models import BaseModel

__all__ = ["ImageGenCompletedEvent"]


class Usage(BaseModel):
    generated_images: int
    """The number of images generated."""
    output_tokens: int
    """The number of output tokens."""
    total_tokens: int
    """The total number of tokens."""


class Error(BaseModel):
    message: str
    """The reason for failed image generation"""

    code: str
    """The error code for failed image generation"""


class ImageGenCompletedEvent(BaseModel):
    type: str
    """The type of image generating event."""

    model: str
    """The model used to generated the images."""

    error: Error
    """The error body, if applicable."""

    usage: Usage
    """The usage information for the generation of images."""

    created_at: int
    """The Unix timestamp when the image was generated."""
