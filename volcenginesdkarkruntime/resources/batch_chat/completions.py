
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

import asyncio
import time
from datetime import timedelta, datetime
from random import random
from typing import Dict, List, Union, Iterable, Optional, Callable
from typing_extensions import Literal

import httpx
import warnings

from ..._exceptions import ArkAPITimeoutError, ArkAPIConnectionError, ArkAPIStatusError
from ..._types import Body, Query, Headers
from ..._utils import with_sts_token, async_with_sts_token, deepcopy_minimal
from ..._utils._key_agreement import aes_gcm_decrypt_base64_string
from ..._base_client import make_request_options
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._compat import cached_property

from ..._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
)
from ...types.chat import (
    ChatCompletion,
    ChatCompletionMessageParam,
    completion_create_params,
    ChatCompletionToolParam,
    ChatCompletionToolChoiceOptionParam,
)
from ..._constants import (
    ARK_E2E_ENCRYPTION_HEADER,
    INITIAL_RETRY_DELAY,
    MAX_RETRY_DELAY,
)

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


def _calculate_retry_timeout(retry_times) -> float:
    nbRetries = min(retry_times, MAX_RETRY_DELAY / INITIAL_RETRY_DELAY)
    sleep_seconds = min(INITIAL_RETRY_DELAY * pow(2, nbRetries), MAX_RETRY_DELAY)
    # Apply some jitter, plus-or-minus half a second.
    jitter = 1 - 0.25 * random()
    timeout = sleep_seconds * jitter
    return timeout if timeout >= 0 else 0


def _get_retry_after(response):
    retry_after = response.headers.get("Retry-After")
    if retry_after is not None:
        if retry_after.isdigit():
            return int(retry_after)
    return None


def _should_retry(response):
    # Retry on request timeouts.
    if response.status_code == 408:
        return True

    # Retry on lock timeouts.
    if response.status_code == 409:
        return True

    # Retry on rate limits.
    if response.status_code == 429:
        return True

    # Retry internal errors.
    if response.status_code >= 500:
        return True

    return False


class Completions(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CompletionsWithRawResponse:
        return CompletionsWithRawResponse(self)

    def _process_messages(
        self, messages: Iterable[ChatCompletionMessageParam], f: Callable[[str], str]
    ):
        for message in messages:
            if message.get("content", None) is not None:
                current_content = message.get("content")
                if isinstance(current_content, str):
                    message["content"] = f(current_content)
                elif isinstance(current_content, Iterable):
                    raise TypeError(
                        "content type {} is not supported end-to-end encryption".format(
                            type(message.get("content"))
                        )
                    )
                else:
                    raise TypeError(
                        "content type {} is not supported end-to-end encryption".format(
                            type(message.get("content"))
                        )
                    )

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

    def _decrypt(
        self, key: bytes, nonce: bytes, resp: ChatCompletion
    ) -> ChatCompletion:
        if resp.choices is not None:
            for index, choice in enumerate(resp.choices):
                if (
                    choice.message is not None and choice.finish_reason != 'content_filter'
                    and choice.message.content is not None
                ):
                    choice.message.content = aes_gcm_decrypt_base64_string(
                        key, nonce, choice.message.content
                    )
                resp.choices[index] = choice
        return resp

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
        max_completion_tokens: Optional[int] | None = None,
        user: str | None = None,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None = None,
    ) -> ChatCompletion:
        is_encrypt = False
        if (
            extra_headers is not None
            and extra_headers.get(ARK_E2E_ENCRYPTION_HEADER, None) == "true"
        ):
            is_encrypt = True
            messages = deepcopy_minimal(messages)
            e2e_key, e2e_nonce = self._encrypt(model, messages, extra_headers)
        retryTimes = 0
        last_time = self._get_request_last_time(timeout)
        model_breaker = self._client.get_model_breaker(model)
        while True:
            model_breaker.wait()
            if datetime.now() > last_time:
                raise ArkAPITimeoutError(None, None)
            try:
                resp = self._post_without_retry(
                    "/batch/chat/completions",
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
                        "max_completion_tokens": max_completion_tokens,
                    },
                    options=make_request_options(
                        extra_headers=extra_headers,
                        extra_query=extra_query,
                        extra_body=extra_body,
                        timeout=timeout,
                    ),
                    cast_to=ChatCompletion,
                )
            except (ArkAPITimeoutError, ArkAPIConnectionError):
                waitTime = _calculate_retry_timeout(retryTimes)
                if datetime.now() + timedelta(seconds=waitTime) > last_time:
                    raise ArkAPITimeoutError(None, None)
                time.sleep(waitTime)
                retryTimes = retryTimes + 1
                continue
            except ArkAPIStatusError as err:
                retry_after = _get_retry_after(err.response)
                if retry_after is not None:
                    model_breaker.reset(retry_after)
                if _should_retry(err.response):
                    continue
                else:
                    raise err
            if is_encrypt:
                resp = self._decrypt(e2e_key, e2e_nonce, resp)
            return resp

    def _get_request_last_time(self, timeout):
        if timeout is None:
            timeout = self._client.timeout
        timeoutSeconds = 0
        if isinstance(timeout, httpx.Timeout):
            timeoutSeconds = timeout.read
        elif isinstance(timeout, float):
            timeoutSeconds = timeout
        elif isinstance(self._client.timeout, int):
            timeoutSeconds = timeout
        else:
            raise TypeError(
                "timeout type {} is not supported".format(type(self._client.timeout))
            )
        return datetime.now() + timedelta(seconds=timeoutSeconds)


class AsyncCompletions(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCompletionsWithRawResponse:
        return AsyncCompletionsWithRawResponse(self)

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

    async def _decrypt(
        self, key: bytes, nonce: bytes, resp: ChatCompletion
    ) -> ChatCompletion:
        if resp.choices is not None:
            for index, choice in enumerate(resp.choices):
                if (
                    choice.message is not None and choice.finish_reason != 'content_filter'
                    and choice.message.content is not None
                ):
                    choice.message.content = aes_gcm_decrypt_base64_string(
                        key, nonce, choice.message.content
                    )
                resp.choices[index] = choice
        return resp

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
        max_completion_tokens: Optional[int] | None = None,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None = None,
    ) -> ChatCompletion:
        is_encrypt = False
        if (
            extra_headers is not None
            and extra_headers.get(ARK_E2E_ENCRYPTION_HEADER, None) == "true"
        ):
            is_encrypt = True
            messages = deepcopy_minimal(messages)
            e2e_key, e2e_nonce = self._encrypt(model, messages, extra_headers)

        retryTimes = 0
        last_time = self._get_request_last_time(timeout)
        model_breaker = await self._client.get_model_breaker(model)
        while True:
            await model_breaker.asyncwait()
            if datetime.now() > last_time:
                raise ArkAPITimeoutError(None, None)
            try:
                resp = await self._post_without_retry(
                    "/batch/chat/completions",
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
                        "max_completion_tokens": max_completion_tokens,
                    },
                    options=make_request_options(
                        extra_headers=extra_headers,
                        extra_query=extra_query,
                        extra_body=extra_body,
                        timeout=timeout,
                    ),
                    cast_to=ChatCompletion,
                )
            except (ArkAPITimeoutError, ArkAPIConnectionError):
                waitTime = _calculate_retry_timeout(retryTimes)
                if datetime.now() + timedelta(seconds=waitTime) > last_time:
                    raise ArkAPITimeoutError(None, None)
                await asyncio.sleep(waitTime)
                retryTimes = retryTimes + 1
                continue
            except ArkAPIStatusError as err:
                retry_after = _get_retry_after(err.response)
                if retry_after is not None:
                    model_breaker.reset(retry_after)
                if _should_retry(err.response):
                    continue
                else:
                    raise err
            if is_encrypt:
                resp = await self._decrypt(e2e_key, e2e_nonce, resp)
            return resp

    def _get_request_last_time(self, timeout):
        if timeout is None:
            timeout = self._client.timeout
        timeoutSeconds = 0
        if isinstance(timeout, httpx.Timeout):
            timeoutSeconds = timeout.read
        elif isinstance(timeout, float):
            timeoutSeconds = timeout
        elif isinstance(self._client.timeout, int):
            timeoutSeconds = timeout
        else:
            raise TypeError(
                "timeout type {} is not supported".format(type(self._client.timeout))
            )
        return datetime.now() + timedelta(seconds=timeoutSeconds)


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
