
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

import datetime
from typing import Union, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["TruncationStrategy", "TTLTypes", "to_optional_ttl"]


class TruncationStrategy(TypedDict, total=False):
    type: Required[Literal["last_history_tokens", "rolling_tokens"]]
    """The truncation strategy to use for the context. The default is last_history_tokens."""
    last_history_tokens: Optional[int]
    """The number of most recent tokens from the context when constructing the chat completion."""
    rolling_tokens: Optional[bool]
    """If true, the context will not rolling when reach the max tokens limit."""


TTLTypes = Union[int, datetime.timedelta]


def to_optional_ttl(ttl: TTLTypes | None) -> int | None:
    if ttl is None:
        return None
    elif isinstance(ttl, datetime.timedelta):
        return int(ttl.total_seconds())
    elif isinstance(ttl, int):
        return ttl
    else:
        raise TypeError(
            f"Could not convert input to `ttl` \n'  type: {type(ttl)}\n",
            ttl,
        )
