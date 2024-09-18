from typing import Optional
from ..._models import BaseModel

__all__ = ["ContextCompletionUsage"]


class ContextCompletionUsage(BaseModel):
    prompt_tokens: int = 0
    """
    prompt_tokens stands for the prompt tokens of chat completion
    """
    completion_tokens: int = 0
    """
    completion_tokens stands for the completion tokens of chat completion
    """
    total_tokens: int = 0
    """
    total_tokens stands for the total tokens of chat completion
    """
    prompt_hit_cache_count: Optional[int] = None
    """
    prompt_hit_cache_count stands for the prompt hit cache count of context chat completion
    """
    prompt_miss_cache_count: Optional[int] = None
    """
    prompt_miss_cache_count stands for the prompt miss cache count of context chat completion
    """
