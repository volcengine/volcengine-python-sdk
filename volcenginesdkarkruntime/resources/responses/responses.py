
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

from typing import (
    Union,
    Iterable,
    Optional,
)

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
from ...types.responses.response_create_params import ToolChoice
from ...types.responses.response import Response
from ...types.responses.tool_param import ToolParam
from ...types.responses.response_input_param import ResponseInputParam
from ...types.responses.response_stream_event import ResponseStreamEvent
from ...types.responses.response_text_config_param import ResponseTextConfigParam
from ...types.responses.response_caching_param import ResponseCaching
from volcenginesdkarkruntime.types.shared_params.thinking import Thinking

__all__ = ["Responses", "AsyncResponses"]


def _add_beta_headers(extra_headers: Headers | None = None, tools: Iterable[ToolParam] | None = ()) -> Headers:
    if tools is None:
        return extra_headers
    for tool_param in tools:
        if tool_param.get("type", "") == "web_search":
            if extra_headers is None:
                extra_headers = {}
            extra_headers["ark-beta-web-search"] = "true"
            break
    return extra_headers


class Responses(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ResponsesWithRawResponse:
        return ResponsesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ResponsesWithStreamingResponse:
        return ResponsesWithStreamingResponse(self)

    @with_sts_token
    def create(
        self,
        *,
        input: Union[str, ResponseInputParam],
        model: str,
        instructions: Optional[str] | None = None,
        max_output_tokens: Optional[int] | None = None,
        parallel_tool_calls: Optional[bool] | None = None,
        previous_response_id: Optional[str] | None = None,
        thinking: Optional[Thinking] | None = None,
        store: Optional[bool] | None = None,
        caching: Optional[ResponseCaching] | None = None,
        stream: Optional[Literal[False]] | Literal[True] | None = None,
        temperature: Optional[float] | None = None,
        text: ResponseTextConfigParam | None = None,
        tool_choice: ToolChoice | None = None,
        tools: Iterable[ToolParam] | None = None,
        top_p: Optional[float] | None = None,
        max_tool_calls: Optional[int] | None = None,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | None = None,
    ) -> Response | Stream[ResponseStreamEvent]:
        extra_headers = _add_beta_headers(extra_headers, tools)
        resp = self._post(
            "/responses",
            body={
                "input": input,
                "model": model,
                "instructions": instructions,
                "max_output_tokens": max_output_tokens,
                "parallel_tool_calls": parallel_tool_calls,
                "previous_response_id": previous_response_id,
                "thinking": thinking,
                "store": store,
                "caching": caching,
                "stream": stream,
                "temperature": temperature,
                "text": text,
                "tool_choice": tool_choice,
                "tools": tools,
                "top_p": top_p,
                "max_tool_calls": max_tool_calls
            },
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=Response,
            stream=stream or False,
            stream_cls=Stream[ResponseStreamEvent],
        )
        return resp

    def retrieve(
        self,
        response_id: str,
        *,

        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None = None,
    ) -> Response:
        if not response_id:
            raise ValueError(f"Expected a non-empty value for `response_id` but received {response_id!r}")
        return self._get(
            f"/responses/{response_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=Response,
            stream=False,
            stream_cls=Stream[ResponseStreamEvent],
        )

    def delete(
        self,
        response_id: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None = None,
    ) -> None:
        if not response_id:
            raise ValueError(f"Expected a non-empty value for `response_id` but received {response_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/responses/{response_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=type(None),
        )


class AsyncResponses(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncResponsesWithRawResponse:
        return AsyncResponsesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncResponsesWithStreamingResponse:
        return AsyncResponsesWithStreamingResponse(self)

    @async_with_sts_token
    async def create(
        self,
        *,
        input: Union[str, ResponseInputParam],
        model: str,
        instructions: Optional[str] | None = None,
        max_output_tokens: Optional[int] | None = None,
        parallel_tool_calls: Optional[bool] | None = None,
        previous_response_id: Optional[str] | None = None,
        thinking: Optional[Thinking] | None = None,
        store: Optional[bool] | None = None,
        caching: Optional[ResponseCaching] | None = None,
        stream: Optional[Literal[False]] | Literal[True] | None = None,
        temperature: Optional[float] | None = None,
        text: ResponseTextConfigParam | None = None,
        tool_choice: ToolChoice | None = None,
        tools: Iterable[ToolParam] | None = None,
        top_p: Optional[float] | None = None,
        max_tool_calls: Optional[int] | None = None,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | None = None,
    ) -> Response | AsyncStream[ResponseStreamEvent]:
        extra_headers = _add_beta_headers(extra_headers, tools)
        resp = await self._post(
            "/responses",
            body={
                "input": input,
                "model": model,
                "instructions": instructions,
                "max_output_tokens": max_output_tokens,
                "parallel_tool_calls": parallel_tool_calls,
                "previous_response_id": previous_response_id,
                "thinking": thinking,
                "store": store,
                "caching": caching,
                "stream": stream,
                "temperature": temperature,
                "text": text,
                "tool_choice": tool_choice,
                "tools": tools,
                "top_p": top_p,
                "max_tool_calls": max_tool_calls,
            },
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=Response,
            stream=stream or False,
            stream_cls=AsyncStream[ResponseStreamEvent],
        )

        return resp

    async def retrieve(
            self,
            response_id: str,
            *,

            extra_headers: Headers | None = None,
            extra_query: Query | None = None,
            extra_body: Body | None = None,
            timeout: float | httpx.Timeout | None = None,
    ) -> Response:
        if not response_id:
            raise ValueError(f"Expected a non-empty value for `response_id` but received {response_id!r}")
        return await self._get(
            f"/responses/{response_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=Response,
            stream=False,
            stream_cls=Stream[ResponseStreamEvent],
        )

    async def delete(
            self,
            response_id: str,
            *,
            extra_headers: Headers | None = None,
            extra_query: Query | None = None,
            extra_body: Body | None = None,
            timeout: float | httpx.Timeout | None = None,
    ) -> None:
        if not response_id:
            raise ValueError(f"Expected a non-empty value for `response_id` but received {response_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/responses/{response_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=type(None),
        )


class ResponsesWithRawResponse:
    def __init__(self, responses: Responses) -> None:
        self._responses = responses

        self.create = to_raw_response_wrapper(
            responses.create,
        )


class AsyncResponsesWithRawResponse:
    def __init__(self, responses: AsyncResponses) -> None:
        self._responses = responses

        self.create = async_to_raw_response_wrapper(
            responses.create,
        )


class ResponsesWithStreamingResponse:
    def __init__(self, responses: Responses) -> None:
        self._responses = responses

        self.create = to_streamed_response_wrapper(
            responses.create,
        )


class AsyncResponsesWithStreamingResponse:
    def __init__(self, responses: AsyncResponses) -> None:
        self._responses = responses

        self.create = async_to_streamed_response_wrapper(
            responses.create,
        )
