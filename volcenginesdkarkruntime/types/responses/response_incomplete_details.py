
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
from typing import Optional

__all__ = ["IncompleteDetails", "ContentFilter"]


class IncompleteDetails(BaseModel):
    reason: str = ""
    """The reason why the response is incomplete."""
    content_filter: Optional[str] = None
    """The content filter details."""


class ContentFilter(BaseModel):
    type: str = ""
    """The content filter hit type."""
    details: Optional[str] = None
    """Details about why the content is filtered."""
