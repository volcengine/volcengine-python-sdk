
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

from typing import List
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
from ..types.multimodal_embedding import EmbeddingInputParam
from ..types.multimodal_embedding import (
    MultimodalEmbeddingResponse,
    SparseEmbeddingInput,
)

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
        sparse_embedding: SparseEmbeddingInput | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None = None,
    ) -> MultimodalEmbeddingResponse:
        return self._post(
            "/embeddings/multimodal",
            body={
                "input": input,
                "model": model,
                "encoding_format": encoding_format,
                "dimensions": dimensions,
                "sparse_embedding": sparse_embedding,
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
        sparse_embedding: SparseEmbeddingInput | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None = None,
    ) -> MultimodalEmbeddingResponse:
        return await self._post(
            "/embeddings/multimodal",
            body={
                "input": input,
                "model": model,
                "encoding_format": encoding_format,
                "dimensions": dimensions,
                "sparse_embedding": sparse_embedding,
            },
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=MultimodalEmbeddingResponse,
        )


class MultimodalEmbeddingsWithRawResponse:
    def __init__(self, embeddings: MultimodalEmbeddings) -> None:
        self._embeddings = embeddings

        self.create = to_raw_response_wrapper(
            embeddings.create,
        )


class AsyncMultimodalEmbeddingsWithRawResponse:
    def __init__(self, embeddings: AsyncMultimodalEmbeddings) -> None:
        self._embeddings = embeddings

        self.create = async_to_raw_response_wrapper(
            embeddings.create,
        )
