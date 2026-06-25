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

from typing import Iterable, Union

from typing_extensions import Literal, TypeAlias, TypedDict

__all__ = [
    "ResponseContextManagementParam",
    "ResponseContextManagementEditParam",
    "ResponseContextManagementKeepParam",
    "ResponseContextManagementTurnStrategyParam",
]


class ResponseContextManagementTurnStrategyParam(TypedDict, total=False):
    type: Literal["thinking_turns", "tool_uses"]
    """The strategy type used by `keep` or `trigger`."""

    value: int
    """The number of recent thinking or tool-use turns."""


ResponseContextManagementKeepParam: TypeAlias = Union[
    Literal["all"],
    ResponseContextManagementTurnStrategyParam,
]


class ResponseContextManagementEditParam(TypedDict, total=False):
    type: Literal["clear_thinking", "clear_tool_uses"]
    """The context edit strategy type."""

    keep: ResponseContextManagementKeepParam
    """How much context to retain when applying the strategy."""

    exclude_tools: Iterable[str]
    """Tool names that should not be cleared."""

    clear_tool_inputs: bool
    """Whether to clear tool call arguments."""

    trigger: ResponseContextManagementTurnStrategyParam
    """The threshold that triggers tool-use cleanup."""


class ResponseContextManagementParam(TypedDict, total=False):
    edits: Iterable[ResponseContextManagementEditParam]
    """Context edit strategies to apply during response creation."""
