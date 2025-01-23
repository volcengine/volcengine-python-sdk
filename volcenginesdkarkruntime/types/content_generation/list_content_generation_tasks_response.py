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
