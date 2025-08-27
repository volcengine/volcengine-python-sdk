
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

from typing_extensions import Literal, Required, Optional, List

from ..._models import BaseModel

__all__ = [
    "WebSearchTool",
    "UserLocation",
]


class UserLocation(BaseModel):
    type: Literal["approximate"]
    """The type of the user location. Always `approximate`."""
    city: Optional[str]
    """The city of the user location."""
    country: Optional[str]
    """The country of the user location."""
    region: Optional[str]
    """The region of the user location."""
    timezone: Optional[float]
    """The timezone of the user location."""


class WebSearchTool(BaseModel):

    type: Literal["web_search"]
    """The type of the web search. Always `web_search`."""

    limit: Optional[int]
    """The maximum number of results to return. Defaults to 3."""

    sources: Optional[List[Literal["toutiao", "douyin", "moji", "search_engine"]]]
    """The source type of web search."""

    user_location: Optional[UserLocation]
    """The user location."""

