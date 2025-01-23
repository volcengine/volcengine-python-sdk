from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional

import httpx
from typing_extensions import Literal

from ..._types import Body, Query, Headers
from ..._utils._utils import with_sts_token, async_with_sts_token
from ..._base_client import make_request_options
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._compat import cached_property

from ..._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._streaming import Stream, AsyncStream
from ...types.context import ContextChatCompletion, ContextChatCompletionChunk
from ...types.chat import (
    ChatCompletionMessageParam,
    completion_create_params,
    ChatCompletionStreamOptionsParam,
    ChatCompletionToolParam,
    ChatCompletionToolChoiceOptionParam,
)

__all__ = ["Completions", "AsyncCompletions"]


class Completions(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CompletionsWithRawResponse:
        return CompletionsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CompletionsWithStreamingResponse:
        return CompletionsWithStreamingResponse(self)

    @with_sts_token
    def create(
        self,
        *,
        context_id: str,
        messages: Iterable[ChatCompletionMessageParam],
        model: str,
        frequency_penalty: Optional[float] | None = None,
        function_call: completion_create_params.FunctionCall | None = None,
        logit_bias: Optional[Dict[str, int]] | None = None,
        logprobs: Optional[bool] | None = None,
        max_tokens: Optional[int] | None = None,
        presence_penalty: Optional[float] | None = None,
        stop: Union[Optional[str], List[str]] | None = None,
        stream: Optional[Literal[False]] | Literal[True] | None = None,
        stream_options: Optional[ChatCompletionStreamOptionsParam] | None = None,
        temperature: Optional[float] | None = None,
        tools: Iterable[ChatCompletionToolParam] | None = None,
        top_logprobs: Optional[int] | None = None,
        top_p: Optional[float] | None = None,
        repetition_penalty: Optional[float] | None = None,
        n: Optional[int] | None = None,
        tool_choice: ChatCompletionToolChoiceOptionParam | None = None,
        response_format: completion_create_params.ResponseFormat | None = None,
        user: str | None = None,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None = None,
    ) -> ContextChatCompletion | Stream[ContextChatCompletionChunk]:
        return self._post(
            "/context/chat/completions",
            body={
                "context_id": context_id,
                "messages": messages,
                "model": model,
                "frequency_penalty": frequency_penalty,
                "function_call": function_call,
                "logit_bias": logit_bias,
                "logprobs": logprobs,
                "max_tokens": max_tokens,
                "presence_penalty": presence_penalty,
                "stop": stop,
                "stream": stream,
                "stream_options": stream_options,
                "temperature": temperature,
                "tools": tools,
                "top_logprobs": top_logprobs,
                "top_p": top_p,
                "user": user,
                "repetition_penalty": repetition_penalty,
                "n": n,
                "tool_choice": tool_choice,
                "response_format": response_format,
            },
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=ContextChatCompletion,
            stream=stream or False,
            stream_cls=Stream[ContextChatCompletionChunk],
        )


class AsyncCompletions(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCompletionsWithRawResponse:
        return AsyncCompletionsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCompletionsWithStreamingResponse:
        return AsyncCompletionsWithStreamingResponse(self)

    @async_with_sts_token
    async def create(
        self,
        *,
        context_id: str,
        messages: Iterable[ChatCompletionMessageParam],
        model: str,
        frequency_penalty: Optional[float] | None = None,
        function_call: completion_create_params.FunctionCall | None = None,
        logit_bias: Optional[Dict[str, int]] | None = None,
        logprobs: Optional[bool] | None = None,
        max_tokens: Optional[int] | None = None,
        presence_penalty: Optional[float] | None = None,
        stop: Union[Optional[str], List[str]] | None = None,
        stream: Optional[Literal[False]] | Literal[True] | None = None,
        stream_options: Optional[ChatCompletionStreamOptionsParam] | None = None,
        temperature: Optional[float] | None = None,
        tools: Iterable[ChatCompletionToolParam] | None = None,
        top_logprobs: Optional[int] | None = None,
        top_p: Optional[float] | None = None,
        user: str | None = None,
        repetition_penalty: Optional[float] | None = None,
        n: Optional[int] | None = None,
        tool_choice: ChatCompletionToolChoiceOptionParam | None = None,
        response_format: completion_create_params.ResponseFormat | None = None,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None = None,
    ) -> ContextChatCompletion | AsyncStream[ContextChatCompletionChunk]:
        return await self._post(
            "/context/chat/completions",
            body={
                "context_id": context_id,
                "messages": messages,
                "model": model,
                "frequency_penalty": frequency_penalty,
                "function_call": function_call,
                "logit_bias": logit_bias,
                "logprobs": logprobs,
                "max_tokens": max_tokens,
                "presence_penalty": presence_penalty,
                "stop": stop,
                "stream": stream,
                "stream_options": stream_options,
                "temperature": temperature,
                "tools": tools,
                "top_logprobs": top_logprobs,
                "top_p": top_p,
                "user": user,
                "repetition_penalty": repetition_penalty,
                "n": n,
                "tool_choice": tool_choice,
                "response_format": response_format,
            },
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=ContextChatCompletion,
            stream=stream or False,
            stream_cls=AsyncStream[ContextChatCompletionChunk],
        )


class CompletionsWithRawResponse:
    def __init__(self, completions: Completions) -> None:
        self._completions = completions

        self.create = to_raw_response_wrapper(
            completions.create,
        )


class AsyncCompletionsWithRawResponse:
    def __init__(self, completions: AsyncCompletions) -> None:
        self._completions = completions

        self.create = async_to_raw_response_wrapper(
            completions.create,
        )


class CompletionsWithStreamingResponse:
    def __init__(self, completions: Completions) -> None:
        self._completions = completions

        self.create = to_streamed_response_wrapper(
            completions.create,
        )


class AsyncCompletionsWithStreamingResponse:
    def __init__(self, completions: AsyncCompletions) -> None:
        self._completions = completions

        self.create = async_to_streamed_response_wrapper(
            completions.create,
        )
