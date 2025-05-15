from __future__ import annotations

from typing import (
    Dict,
    List,
    Union,
    Iterable,
    Optional,
    Callable,
    Iterator,
    AsyncIterator,
)

import httpx
import warnings
from typing_extensions import Literal

from ..._types import Body, Query, Headers
from ..._utils._utils import with_sts_token, async_with_sts_token
from ..._utils._key_agreement import aes_gcm_decrypt_base64_string
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
    ChatCompletionToolChoiceOptionParam,
)
from ..._constants import ARK_E2E_ENCRYPTION_HEADER

__all__ = ["Completions", "AsyncCompletions"]


def _process_messages(
    messages: Iterable[ChatCompletionMessageParam], f: Callable[[str], str]
):
    for message in messages:
        if message.get("content", None) is not None:
            current_content = message.get("content")
            if isinstance(current_content, str):
                message["content"] = f(current_content)
            elif isinstance(current_content, Iterable):
                for part in current_content:
                    if part.get("type", None) == "text":
                        part["text"] = f(part["text"])
                    elif part.get("type", None) == "image_url":
                        if part["image_url"]["url"].startswith("data:"):
                            part["image_url"]["url"] = f(part["image_url"]["url"])
                        else:
                            warnings.warn(
                                "encryption is not supported for image url, "
                                "please use base64 image if you want encryption"
                            )
                    else:
                        raise TypeError(
                            "encryption is not supported for content type {}".format(
                                type(part)
                            )
                        )
            else:
                raise TypeError(
                    "encryption is not supported for content type {}".format(
                        type(message.get("content"))
                    )
                )


class Completions(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CompletionsWithRawResponse:
        return CompletionsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CompletionsWithStreamingResponse:
        return CompletionsWithStreamingResponse(self)

    def _encrypt(
        self,
        model: str,
        messages: Iterable[ChatCompletionMessageParam],
        extra_headers: Headers,
    ) -> tuple[bytes, bytes]:
        client = self._client._get_endpoint_certificate(model)
        _crypto_key, _crypto_nonce, session_token = client.generate_ecies_key_pair()
        extra_headers["X-Session-Token"] = session_token
        _process_messages(
            messages,
            lambda x: client.encrypt_string_with_key(_crypto_key, _crypto_nonce, x),
        )
        return _crypto_key, _crypto_nonce

    def _decrypt_chunk(
        self, key: bytes, nonce: bytes, resp: Stream[ChatCompletionChunk]
    ) -> Iterator[ChatCompletionChunk]:
        for chunk in resp:
            if chunk.choices is not None:
                for index, choice in enumerate(chunk.choices):
                    if choice.delta is not None and choice.delta.content is not None:
                        choice.delta.content = aes_gcm_decrypt_base64_string(
                            key, nonce, choice.delta.content
                        )
                    chunk.choices[index] = choice
            yield chunk

    def _decrypt(
        self,
        key: bytes,
        nonce: bytes,
        resp: ChatCompletion | Stream[ChatCompletionChunk],
    ) -> ChatCompletion | Stream[ChatCompletionChunk]:
        if isinstance(resp, ChatCompletion):
            if resp.choices is not None:
                for index, choice in enumerate(resp.choices):
                    if (
                        choice.message is not None
                        and choice.message.content is not None
                    ):
                        choice.message.content = aes_gcm_decrypt_base64_string(
                            key, nonce, choice.message.content
                        )
                    resp.choices[index] = choice
            return resp
        else:
            return Stream._make_stream_from_iterator(
                self._decrypt_chunk(key, nonce, resp)
            )

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
        parallel_tool_calls: Optional[bool] | None = None,
        service_tier: Optional[Literal["auto", "default"]] | None = None,
        tool_choice: ChatCompletionToolChoiceOptionParam | None = None,
        response_format: completion_create_params.ResponseFormat | None = None,
        thinking: completion_create_params.Thinking | None = None,
        user: str | None = None,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None = None,
    ) -> ChatCompletion | Stream[ChatCompletionChunk]:
        is_encrypt = False
        if (
            extra_headers is not None
            and extra_headers.get(ARK_E2E_ENCRYPTION_HEADER, None) == "true"
        ):
            is_encrypt = True
            e2e_key, e2e_nonce = self._encrypt(model, messages, extra_headers)

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
                "parallel_tool_calls": parallel_tool_calls,
                "service_tier": service_tier,
                "tool_choice": tool_choice,
                "response_format": response_format,
                "thinking": thinking,
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
            resp = self._decrypt(e2e_key, e2e_nonce, resp)
        return resp


class AsyncCompletions(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCompletionsWithRawResponse:
        return AsyncCompletionsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCompletionsWithStreamingResponse:
        return AsyncCompletionsWithStreamingResponse(self)

    def _encrypt(
        self,
        model: str,
        messages: Iterable[ChatCompletionMessageParam],
        extra_headers: Headers,
    ) -> tuple[bytes, bytes]:
        client = self._client._get_endpoint_certificate(model)
        _crypto_key, _crypto_nonce, session_token = client.generate_ecies_key_pair()
        extra_headers["X-Session-Token"] = session_token
        _process_messages(
            messages,
            lambda x: client.encrypt_string_with_key(_crypto_key, _crypto_nonce, x),
        )
        return _crypto_key, _crypto_nonce

    async def _decrypt_chunk(
        self, key: bytes, nonce: bytes, resp: AsyncStream[ChatCompletionChunk]
    ) -> AsyncIterator[ChatCompletionChunk]:
        async for chunk in resp:
            if chunk.choices is not None:
                for index, choice in enumerate(chunk.choices):
                    if choice.delta is not None and choice.delta.content is not None:
                        choice.delta.content = aes_gcm_decrypt_base64_string(
                            key, nonce, choice.delta.content
                        )
                    chunk.choices[index] = choice
            yield chunk

    async def _decrypt(
        self,
        key: bytes,
        nonce: bytes,
        resp: ChatCompletion | AsyncStream[ChatCompletionChunk],
    ) -> ChatCompletion | AsyncStream[ChatCompletionChunk]:
        if isinstance(resp, ChatCompletion):
            if resp.choices is not None:
                for index, choice in enumerate(resp.choices):
                    if (
                        choice.message is not None
                        and choice.message.content is not None
                    ):
                        choice.message.content = aes_gcm_decrypt_base64_string(
                            key, nonce, choice.message.content
                        )
                    resp.choices[index] = choice
            return resp
        else:
            return AsyncStream._make_stream_from_iterator(
                self._decrypt_chunk(key, nonce, resp)
            )

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
        parallel_tool_calls: Optional[bool] | None = None,
        service_tier: Optional[Literal["auto", "default"]] | None = None,
        tool_choice: ChatCompletionToolChoiceOptionParam | None = None,
        response_format: completion_create_params.ResponseFormat | None = None,
        thinking: completion_create_params.Thinking | None = None,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None = None,
    ) -> ChatCompletion | AsyncStream[ChatCompletionChunk]:
        is_encrypt = False
        if (
            extra_headers is not None
            and extra_headers.get(ARK_E2E_ENCRYPTION_HEADER, None) == "true"
        ):
            is_encrypt = True
            e2e_key, e2e_nonce = self._encrypt(model, messages, extra_headers)

        resp = await self._post(
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
                "parallel_tool_calls": parallel_tool_calls,
                "service_tier": service_tier,
                "tool_choice": tool_choice,
                "response_format": response_format,
                "thinking": thinking,
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

        if is_encrypt:
            resp = await self._decrypt(e2e_key, e2e_nonce, resp)
        return resp


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
