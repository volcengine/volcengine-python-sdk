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

from typing_extensions import Literal, Required, TypedDict

__all__ = ["KnowledgeSearchToolParam"]


class KnowledgeSearchToolParam(TypedDict, total=False):
    type: Required[Literal["knowledge_search"]]
    """The type of the knowledge search. Always `knowledge_search`."""

    knowledge_resource_id: Required[str]
    """The knowledge base id"""

    description: Optional[str]
    """Description of the content of the knowledge base"""

    limit: Optional[int]
    """The maximum number of results to return. Defaults to 3."""

    dense_weight: Optional[float]
    """Knowledge search dense_weight"""

    doc_filter: Optional[Dict[str, Any]]
    """Knowledge search filter"""

    ranking_options: Optional[Dict[str, Any]]
    """Knowledge search ranking options"""

    max_keyword: Optional[int]
    """Max number of keywords to search per knowledge search call"""
