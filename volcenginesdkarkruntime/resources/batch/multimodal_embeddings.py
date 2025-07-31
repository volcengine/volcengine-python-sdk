from __future__ import annotations

from typing import List

import httpx
from typing_extensions import Literal

from ..._base_client import make_request_options
from ..._compat import cached_property
from ..._resource import AsyncAPIResource, SyncAPIResource
from ..._types import Body, Headers, Query
from ..._utils._utils import async_with_sts_token, with_sts_token
from ...types.multimodal_embedding import (
    EmbeddingInputParam,
    MultimodalEmbeddingResponse,
)
from ..multimodal_embeddings import (
    AsyncMultimodalEmbeddingsWithRawResponse,
    MultimodalEmbeddingsWithRawResponse,
)
from ._utils import async_with_batch_retry, get_request_last_time, with_batch_retry

__all__ = ["MultimodalEmbeddings", "AsyncMultimodalEmbeddings"]


class MultimodalEmbeddings(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MultimodalEmbeddingsWithRawResponse:
        return MultimodalEmbeddingsWithRawResponse(self)

    @with_sts_token
    def create(
        self,
        *,
        input: List[EmbeddingInputParam],
        model: str,
        encoding_format: Literal["float", "base64"] = "float",
        dimensions: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None = None,
    ) -> MultimodalEmbeddingResponse:
        deadline = get_request_last_time(self._client, timeout)
        breaker = self._client.get_model_breaker(model)

        return with_batch_retry(
            deadline,
            breaker,
            self._post_without_retry,
            "/batch/embeddings/multimodal",
            body={
                "input": input,
                "model": model,
                "encoding_format": encoding_format,
                "dimensions": dimensions,
            },
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=MultimodalEmbeddingResponse,
        )


class AsyncMultimodalEmbeddings(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMultimodalEmbeddingsWithRawResponse:
        return AsyncMultimodalEmbeddingsWithRawResponse(self)

    @async_with_sts_token
    async def create(
        self,
        *,
        input: List[EmbeddingInputParam],
        model: str,
        encoding_format: Literal["float", "base64"] = "float",
        dimensions: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None = None,
    ) -> MultimodalEmbeddingResponse:
        deadline = get_request_last_time(self._client, timeout)
        breaker = await self._client.get_model_breaker(model)

        return await async_with_batch_retry(
            deadline,
            breaker,
            self._post_without_retry,
            "/batch/embeddings/multimodal",
            body={
                "input": input,
                "model": model,
                "encoding_format": encoding_format,
                "dimensions": dimensions,
            },
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=MultimodalEmbeddingResponse,
        )
