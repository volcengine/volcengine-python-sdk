
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

from ..._models import BaseModel
from ..completion_usage import CompletionUsage
from .truncation_strategy import TruncationStrategy

__all__ = ["CreateContextResponse"]


class CreateContextResponse(BaseModel):
    id: str
    """A unique identifier for the context."""
    model: str
    """The endpoint used for the context."""
    mode: str
    """The mode used for the context."""
    ttl: int
    """The time to live (TTL) for the context in seconds."""
    truncation_strategy: TruncationStrategy
    """
    Controls for how a context will be truncated prior to the run. 
    Use this to control the context window for the chat completion.
    """
    usage: CompletionUsage
    """
    usage for context create.
    """
