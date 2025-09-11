
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

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ResponseReasoningItemParam", "Summary"]


class Summary(TypedDict, total=False):
    text: Required[str]
    """
    A short summary of the reasoning used by the model when generating the response.
    """

    type: Required[Literal["summary_text"]]
    """The type of the object. Always `summary_text`."""


class ResponseReasoningItemParam(TypedDict, total=False):

    summary: Required[Iterable[Summary]]
    """Reasoning text contents."""

    type: Required[Literal["reasoning"]]
    """The type of the object. Always `reasoning`."""
