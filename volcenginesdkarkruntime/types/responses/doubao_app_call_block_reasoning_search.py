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

from typing import List, Optional

from typing_extensions import Literal

from ..._models import BaseModel
from .doubao_app_search_result import DoubaoAppSearchResult

__all__ = ["DoubaoAppCallBlockReasoningSearch"]


class DoubaoAppCallBlockReasoningSearch(BaseModel):
    id: Optional[str] = None

    type: Literal["reasoning_search"]

    summary: Optional[str] = None

    queries: List[str]

    results: List[DoubaoAppSearchResult]

    status: Literal["in_progress", "completed", "incomplete", "searching", "failed"]

    parent_id: Optional[str] = None
