
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

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["TruncationStrategy"]


class TruncationStrategy(BaseModel):
    type: Literal["last_history_tokens"]
    """The truncation strategy to use for the context. The default is last_history_tokens."""
    last_history_tokens: Optional[int] = None
    """The number of most recent tokens from the context when constructing the chat completion."""
