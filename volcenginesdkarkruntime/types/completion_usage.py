# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import BaseModel
from typing import Optional

__all__ = ["CompletionUsage", "PromptTokensDetails"]


class PromptTokensDetails(BaseModel):
    cached_tokens: int
    """Number of tokens hit cache."""


class CompletionUsage(BaseModel):
    completion_tokens: int
    """Number of tokens in the generated completion."""

    prompt_tokens: int
    """Number of tokens in the prompt."""

    total_tokens: int
    """Total number of tokens used in the request (prompt + completion)."""

    prompt_tokens_details: Optional[PromptTokensDetails] = None
    """Prompt tokens details."""
