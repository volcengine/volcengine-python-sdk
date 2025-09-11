
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

from typing import List
from typing_extensions import Literal, TypedDict

from .response_includable import ResponseIncludable

__all__ = ["InputItemListParams"]


class InputItemListParams(TypedDict, total=False):
    after: str
    """An item ID to list items after, used in pagination."""

    before: str
    """An item ID to list items before, used in pagination."""

    include: List[ResponseIncludable]
    """Additional fields to include in the response.

    See the `include` parameter for Response creation above for more information.
    """

    limit: int
    """A limit on the number of objects to be returned.

    Limit can range between 1 and 100, and the default is 20.
    """

    order: Literal["asc", "desc"]
    """The order to return the input items in. Default is `desc`.

    - `asc`: Return the input items in ascending order.
    - `desc`: Return the input items in descending order.
    """
