
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

from typing import List, Union

import httpx

from .._types import Body, Query, Headers
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from .._base_client import (
    make_request_options,
)
from .._utils._utils import with_sts_token, async_with_sts_token
from ..types.create_tokenization_response import CreateTokenizationResponse

__all__ = ["Tokenization", "AsyncTokenization"]


class Tokenization(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TokenizationWithRawResponse:
        return TokenizationWithRawResponse(self)

    @with_sts_token
    def create(
        self,
        *,
        text: Union[str, List[str]],
        model: str,
        user: str | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None = None,
    ) -> CreateTokenizationResponse:
        return self._post(
            "/tokenization",
            body={
                "text": text,
                "model": model,
                "user": user,
            },
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=CreateTokenizationResponse,
        )


class AsyncTokenization(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTokenizationWithRawResponse:
        return AsyncTokenizationWithRawResponse(self)

    @async_with_sts_token
    async def create(
        self,
        *,
        text: Union[str, List[str]],
        model: str,
        user: str | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None = None,
    ) -> CreateTokenizationResponse:
        return await self._post(
            "/tokenization",
            body={
                "text": text,
                "model": model,
                "user": user,
            },
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=CreateTokenizationResponse,
        )


class TokenizationWithRawResponse:
    def __init__(self, tokenization: Tokenization) -> None:
        self._tokenization = tokenization

        self.create = to_raw_response_wrapper(
            tokenization.create,
        )


class AsyncTokenizationWithRawResponse:
    def __init__(self, tokenization: AsyncTokenization) -> None:
        self._tokenization = tokenization

        self.create = async_to_raw_response_wrapper(
            tokenization.create,
        )
