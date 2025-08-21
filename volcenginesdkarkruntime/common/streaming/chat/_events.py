
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

from typing import List, Union, Generic, Optional
from typing_extensions import Literal

from ._types import ParsedChatCompletionSnapshot
from ...._models import BaseModel, GenericModel
from ..._parsing import ResponseFormatT
from ....types.chat import ChatCompletionChunk, ChatCompletionTokenLogprob


class ChunkEvent(BaseModel):
    type: Literal["chunk"]

    chunk: ChatCompletionChunk

    snapshot: ParsedChatCompletionSnapshot


class ContentDeltaEvent(BaseModel):
    """This event is yielded for every chunk with `choice.delta.content` data."""

    type: Literal["content.delta"]

    delta: str

    snapshot: str

    parsed: Optional[object] = None


class ContentDoneEvent(GenericModel, Generic[ResponseFormatT]):
    type: Literal["content.done"]

    content: str

    parsed: Optional[ResponseFormatT] = None


class FunctionToolCallArgumentsDeltaEvent(BaseModel):
    type: Literal["tool_calls.function.arguments.delta"]

    name: str

    index: int

    arguments: str
    """Accumulated raw JSON string"""

    parsed_arguments: object
    """The parsed arguments so far"""

    arguments_delta: str
    """The JSON string delta"""


class FunctionToolCallArgumentsDoneEvent(BaseModel):
    type: Literal["tool_calls.function.arguments.done"]

    name: str

    index: int

    arguments: str
    """Accumulated raw JSON string"""

    parsed_arguments: object
    """The parsed arguments"""


class LogprobsContentDeltaEvent(BaseModel):
    type: Literal["logprobs.content.delta"]

    content: List[ChatCompletionTokenLogprob]

    snapshot: List[ChatCompletionTokenLogprob]


class LogprobsContentDoneEvent(BaseModel):
    type: Literal["logprobs.content.done"]

    content: List[ChatCompletionTokenLogprob]


ChatCompletionStreamEvent = Union[
    ChunkEvent,
    ContentDeltaEvent,
    ContentDoneEvent[ResponseFormatT],
    FunctionToolCallArgumentsDeltaEvent,
    FunctionToolCallArgumentsDoneEvent,
    LogprobsContentDeltaEvent,
    LogprobsContentDoneEvent,
]
