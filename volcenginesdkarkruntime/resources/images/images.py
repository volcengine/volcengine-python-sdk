from __future__ import annotations

import httpx

from ..._base_client import make_request_options
from ..._utils._utils import apikey_required, async_apikey_required
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...types.images import ImagesResponse
from ..._types import Body, Query, Headers


class Images(SyncAPIResource):
    @apikey_required
    def generate(
        self,
        *,
        model: str,
        prompt: str,
        image: str | None = None,
        response_format: str | None = None,
        size: str | None = None,
        seed: int | None = None,
        guidance_scale: float | None = None,
        watermark: bool | None = None,
        optimize_prompt: bool | None = None,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None = None,
    ) -> ImagesResponse:
        resp = self._post(
            "/images/generations",
            body={
                "model": model,
                "prompt": prompt,
                "image": image,
                "response_format": response_format,
                "size": size,
                "seed": seed,
                "guidance_scale": guidance_scale,
                "watermark": watermark,
                "optimize_prompt": optimize_prompt,
            },
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=ImagesResponse,
        )

        return resp


class AsyncImages(AsyncAPIResource):
    @async_apikey_required
    async def generate(
        self,
        *,
        model: str,
        prompt: str,
        image: str | None = None,
        response_format: str | None = None,
        size: str | None = None,
        seed: int | None = None,
        guidance_scale: float | None = None,
        watermark: bool | None = None,
        optimize_prompt: bool | None = None,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None = None,
    ) -> ImagesResponse:
        return await self._post(
            "/images/generations",
            body={
                "model": model,
                "prompt": prompt,
                "image": image,
                "response_format": response_format,
                "size": size,
                "seed": seed,
                "guidance_scale": guidance_scale,
                "watermark": watermark,
                "optimize_prompt": optimize_prompt,
            },
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=ImagesResponse,
        )
