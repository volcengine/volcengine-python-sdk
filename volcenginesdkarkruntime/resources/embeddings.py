from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal

import httpx

from .._types import Body, Query, Headers
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from .._base_client import (
    make_request_options,
)
from .._utils._utils import with_sts_token, async_with_sts_token
from ..types.create_embedding_response import CreateEmbeddingResponse

__all__ = ["Embeddings", "AsyncEmbeddings"]


class Embeddings(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EmbeddingsWithRawResponse:
        return EmbeddingsWithRawResponse(self)

    @with_sts_token
    def create(
        self,
        *,
        input: Union[str, List[str]],
        model: str,
        encoding_format: Literal["float", "base64"] = "float",
        user: str | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None = None,
    ) -> CreateEmbeddingResponse:
        return self._post(
            "/embeddings",
            body={
                "input": input,
                "model": model,
                "user": user,
                "encoding_format": encoding_format,
            },
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=CreateEmbeddingResponse,
        )


class AsyncEmbeddings(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEmbeddingsWithRawResponse:
        return AsyncEmbeddingsWithRawResponse(self)

    @async_with_sts_token
    async def create(
        self,
        *,
        input: Union[str, List[str]],
        model: str,
        encoding_format: Literal["float", "base64"] = "float",
        user: str | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None = None,
    ) -> CreateEmbeddingResponse:
        return await self._post(
            "/embeddings",
            body={
                "input": input,
                "model": model,
                "user": user,
                "encoding_format": encoding_format,
            },
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=CreateEmbeddingResponse,
        )


class EmbeddingsWithRawResponse:
    def __init__(self, embeddings: Embeddings) -> None:
        self._embeddings = embeddings

        self.create = to_raw_response_wrapper(
            embeddings.create,
        )


class AsyncEmbeddingsWithRawResponse:
    def __init__(self, embeddings: AsyncEmbeddings) -> None:
        self._embeddings = embeddings

        self.create = async_to_raw_response_wrapper(
            embeddings.create,
        )
