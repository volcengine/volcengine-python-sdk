# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations
import httpx

from typing import Iterable, Optional

from ..._types import Body, Query, Headers
from .completions import Completions, AsyncCompletions
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._utils._utils import with_sts_token, async_with_sts_token
from ..._base_client import (
    make_request_options,
)
from ...types.context import CreateContextResponse, CloneContextResponse
from ...types.context.context_create_params import TTLTypes, TruncationStrategy, to_optional_ttl
from ...types.chat import ChatCompletionMessageParam

__all__ = ["Context", "AsyncContext"]


class Context(SyncAPIResource):
    @cached_property
    def completions(self) -> Completions:
        return Completions(self._client)

    @with_sts_token
    def create(
            self,
            *,
            model: str,
            messages: Iterable[ChatCompletionMessageParam],
            ttl: Optional[TTLTypes] | None = None,
            truncation_strategy: Optional[TruncationStrategy] | None = None,
            extra_headers: Headers | None = None,
            extra_query: Query | None = None,
            extra_body: Body | None = None,
            timeout: float | httpx.Timeout | None = None,
    ) -> CreateContextResponse:
        ttl = to_optional_ttl(ttl)
        return self._post(
            "/context/create",
            body={
                "model": model,
                "messages": messages,
                "ttl": ttl,
                "truncation_strategy": truncation_strategy,
            },
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=CreateContextResponse,
        )

    def clone(
            self,
            *,
            context_id: str,
            extra_headers: Headers | None = None,
            extra_query: Query | None = None,
            extra_body: Body | None = None,
            timeout: float | httpx.Timeout | None = None,
    ) -> CloneContextResponse:
        return self._post(
            "/context/clone",
            body={
                "context_id": context_id,
            },
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=CloneContextResponse,
        )


class AsyncContext(AsyncAPIResource):
    @cached_property
    def completions(self) -> AsyncCompletions:
        return AsyncCompletions(self._client)

    @async_with_sts_token
    async def create(
            self,
            *,
            model: str,
            messages: Iterable[ChatCompletionMessageParam],
            ttl: Optional[TTLTypes] | None = None,
            truncation_strategy: Optional[TruncationStrategy] | None = None,
            extra_headers: Headers | None = None,
            extra_query: Query | None = None,
            extra_body: Body | None = None,
            timeout: float | httpx.Timeout | None = None,
    ) -> CreateContextResponse:
        ttl = to_optional_ttl(ttl)
        return await self._post(
            "/context/create",
            body={
                "model": model,
                "messages": messages,
                "ttl": ttl,
                "truncation_strategy": truncation_strategy,
            },
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=CreateContextResponse,
        )
