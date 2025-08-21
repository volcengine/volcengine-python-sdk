
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

from pydantic import BaseModel
from typing import Optional

__all__ = ["MultimodalEmbeddingUsage", "PromptTokensDetails"]


class PromptTokensDetails(BaseModel):
    text_tokens: int
    """Number of tokens in the text."""
    image_tokens: int
    """Number of tokens in the image."""


class MultimodalEmbeddingUsage(BaseModel):
    prompt_tokens: int
    """Number of tokens in the prompt."""

    total_tokens: int
    """Total number of tokens used in the request (prompt + completion)."""

    prompt_tokens_details: Optional[PromptTokensDetails] = None
    """Prompt tokens details."""
