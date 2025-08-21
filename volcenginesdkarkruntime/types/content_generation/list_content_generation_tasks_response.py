
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

from .content_generation_task import ContentGenerationTask
from volcenginesdkarkruntime._models import BaseModel

__all__ = ["ListContentGenerationTasksResponse"]


class Content(BaseModel):
    video_url: str
    """URL of the generated video."""


class Usage(BaseModel):
    completion_tokens: int
    """Number of tokens used during the content generation process."""


class ListContentGenerationTasksResponse(BaseModel):
    total: int
    """Total number of filtered content generation tasks."""

    items: List[ContentGenerationTask]
    """List of content generation task items."""
