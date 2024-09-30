from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional, Callable

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
from ...types.chat import (
    ChatCompletion,
    ChatCompletionChunk,
    ChatCompletionMessageParam,
    completion_create_params,
    ChatCompletionStreamOptionsParam,
    ChatCompletionToolParam,
    ChatCompletionToolChoiceOptionParam
)

__all__ = ["Completions", "AsyncCompletions"]


class Completions(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CompletionsWithRawResponse:
        return CompletionsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CompletionsWithStreamingResponse:
        return CompletionsWithStreamingResponse(self)

    def _process_messages(self, messages: Iterable[ChatCompletionMessageParam],
                          f: Callable[[str], str]):
        for message in messages:
            if message.get("content", None) is not None:
                if isinstance(message.get("content"), str):
                    message["content"] = f(message.get("content"))
                elif isinstance(message.get("content"), Iterable):
                    content = message.get("content")
                    for i, c in enumerate(content):
                        if not isinstance(c, Dict):
                            raise TypeError("content type {} is not supported end-to-end encryption".
                                            format(type(c)))
                        for key in c.keys():
                            if key == 'type':
                                continue
                            if isinstance(c[key], str):
                                content[i][key] = f(c[key])
                            if isinstance(c[key], Dict):
                                for k in c[key].keys():
                                    if isinstance(c[key][k], str):
                                        content[i][key][k] = f(c[key][k])
                    message["content"] = content
                else:
                    raise TypeError("content type {} is not supported end-to-end encryption".
                                    format(type(message.get('content'))))

    def _encrypt(self, model: str, messages: Iterable[ChatCompletionMessageParam], extra_headers: Headers):
        client = self._client._get_endpoint_certificate(model)
        self._ka_client = client
        self._crypto_key, self._crypto_nonce, session_token = client.generate_ecies_key_pair()
        extra_headers['X-Session-Token'] = session_token
        self._process_messages(messages, lambda x: client.encrypt_string_with_key(self._crypto_key,
                                                                                  self._crypto_nonce,
                                                                                  x))

    def _decrypt(self, completion: ChatCompletion | Stream[ChatCompletionChunk]):
        if isinstance(completion, ChatCompletion):
            if completion.choices is not None:
                choice = completion.choices[0]
                if choice.message.content is not None:
                    if isinstance(choice.message.content, str):
                        choice.message.content = self._ka_client.decrypt_string_with_key(self._crypto_key,
                                                                                         self._crypto_nonce,
                                                                                         choice.message.content)
                    else:
                        raise TypeError("content type {} is not supported end-to-end encryption".
                                        format(type(choice.message.content)))
                completion.choices[0] = choice
        elif isinstance(completion, Stream):
            for chunk in completion:
                if chunk.choices:
                    choice = chunk.choices[0]
                    if choice.delta.content is not None:
                        if isinstance(choice.delta.content, str):
                            choice.delta.content = self._ka_client.decrypt_string_with_key(self._crypto_key,
                                                                                             self._crypto_nonce,
                                                                                             choice.delta.content)
                        else:
                            raise TypeError("content type {} is not supported end-to-end encryption".
                                            format(type(choice.delta.content)))
                    chunk.choices[0] = choice

    @with_sts_token
    def create(
        self,
        *,
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
        is_encrypt: bool | None = None,
    ) -> ChatCompletion | Stream[ChatCompletionChunk]:
        if is_encrypt:
            if extra_headers is None:
                extra_headers = dict()
            self._encrypt(model, messages, extra_headers)

        resp = self._post(
            "/chat/completions",
            body={
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
            cast_to=ChatCompletion,
            stream=stream or False,
            stream_cls=Stream[ChatCompletionChunk],
        )

        if is_encrypt:
            self._decrypt(resp)
        return resp


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
    ) -> ChatCompletion | AsyncStream[ChatCompletionChunk]:
        return await self._post(
            "/chat/completions",
            body={
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
            cast_to=ChatCompletion,
            stream=stream or False,
            stream_cls=AsyncStream[ChatCompletionChunk],
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
