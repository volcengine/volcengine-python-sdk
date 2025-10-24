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

from __future__ import annotations

from typing import Any, Dict, Optional

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["KnowledgeSearchTool"]


class KnowledgeSearchTool(BaseModel):
    type: Literal["knowledge_search"]
    """The type of the knowledge search. Always `knowledge_search`."""

    knowledge_resource_id: str
    """The knowledge base id"""

    description: Optional[str] = None
    """Description of the content of the knowledge base"""

    limit: Optional[int] = None
    """The maximum number of results to return. Defaults to 3."""

    dense_weight: Optional[float] = None
    """Knowledge search dense_weight"""

    doc_filter: Optional[Dict[str, Any]] = None
    """Knowledge search filter"""

    ranking_options: Optional[Dict[str, Any]] = None
    """Knowledge search ranking options"""

    max_keyword: Optional[int] = None
    """Max number of keywords to search per knowledge search call"""
