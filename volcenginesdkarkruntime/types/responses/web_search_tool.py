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

from typing_extensions import Literal, Optional, List

from ..._models import BaseModel

from .user_location import UserLocation

__all__ = [
    "WebSearchTool",
]


class WebSearchTool(BaseModel):

    type: Literal["web_search"]
    """The type of the web search. Always `web_search`."""

    limit: Optional[int]
    """The maximum number of results to return. Defaults to 3."""

    sources: Optional[List[Literal["toutiao", "douyin", "moji", "search_engine"]]]
    """The source type of web search."""

    user_location: Optional[UserLocation]
    """The user location."""
