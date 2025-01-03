from typing import List

from volcenginesdkarkruntime._models import BaseModel

__all__ = ["ListContentGenerationTasksResponse"]


class Content(BaseModel):
    video_url: str
    """URL of the generated video."""


class Usage(BaseModel):
    completion_tokens: int
    """Number of tokens used during the content generation process."""


class Item(BaseModel):
    id: str
    """Unique identifier for the content generation task."""

    model: str
    """Name or identifier of the model used for generation."""

    status: str
    """Status of the content generation task (e.g., 'succeed', 'failed')."""

    failure_reason: str
    """Description of why the task failed, if it did. Otherwise empty."""

    content: Content
    """Generated content details (e.g., video URL)."""

    usage: Usage
    """Usage statistics for the content generation task."""

    created_at: int
    """Timestamp (in Unix epoch) of when the task was created."""

    updated_at: int
    """Timestamp (in Unix epoch) of when the task was last updated."""


class ListContentGenerationTasksResponse(BaseModel):
    total: int
    """Total number of filtered content generation tasks."""

    items: List[Item]
    """List of content generation task items."""
