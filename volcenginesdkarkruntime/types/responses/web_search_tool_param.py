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

from typing import List, Optional

from typing_extensions import Literal, Required, TypedDict

from .user_location_param import UserLocationParam

__all__ = ["WebSearchToolParam"]


class WebSearchToolParam(TypedDict, total=False):
    type: Required[Literal["web_search"]]
    """The type of the web search. Always `web_search`."""

    limit: Optional[int]
    """The maximum number of results to return. Defaults to 3."""

    user_location: Optional[UserLocationParam]
    """The user location."""

    sources: Required[List[Literal["toutiao", "douyin", "moji", "search_engine"]]]
    """The source type of web search."""

    max_keyword: Optional[int]
    """Max number of keywords to search per web search call"""
