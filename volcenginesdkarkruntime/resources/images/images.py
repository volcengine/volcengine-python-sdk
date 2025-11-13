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

from typing import Optional
from typing_extensions import Literal, overload

import httpx

from ..._types import NOT_GIVEN, NotGiven
from ..._base_client import make_request_options
from ..._utils._utils import apikey_required, async_apikey_required
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...types.images import (
    OptimizePromptOptions,
    SequentialImageGenerationOptions,
    ImagesResponse,
)
from ...types.images.image_gen_stream_event import ImageGenStreamEvent
from ..._types import Body, Query, Headers
from ..._streaming import Stream
from ...types.images.images import OptimizePromptOptions


class Images(SyncAPIResource):
    @overload
    def generate(
        self,
        *,
        model: str,
        prompt: str,
        image: str | list[str] | None = None,
        response_format: str | None = None,
        size: str | None = None,
        seed: int | None = None,
        guidance_scale: float | None = None,
        watermark: bool | None = None,
        optimize_prompt: bool | None = None,
        optimize_prompt_options: OptimizePromptOptions | None = None,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None = None,
        sequential_image_generation: str | None = None,
        sequential_image_generation_options: SequentialImageGenerationOptions
        | None = None,
        stream: Optional[Literal[False]] | NotGiven = NOT_GIVEN,
    ) -> ImagesResponse:
        ...

        """
        ImageSequenceGeneration: 
            Controls whether the multi-image feature is enforced
            - Enum values:
                - auto: Automatic mode; the model decides whether to return multiple images and how many based on the user's prompt
                - disabled: Disables multi-image; the model generates only a single image
        """

    @overload
    def generate(
        self,
        *,
        model: str,
        prompt: str,
        image: str | list[str] | None = None,
        response_format: str | None = None,
        size: str | None = None,
        seed: int | None = None,
        guidance_scale: float | None = None,
        watermark: bool | None = None,
        optimize_prompt: bool | None = None,
        optimize_prompt_options: OptimizePromptOptions | None = None,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None = None,
        sequential_image_generation: str | None = None,
        sequential_image_generation_options: SequentialImageGenerationOptions
        | None = None,
        stream: Literal[True],
    ) -> Stream[ImageGenStreamEvent]: ...

    @overload
    def generate(
        self,
        *,
        model: str,
        prompt: str,
        image: str | list[str] | None = None,
        response_format: str | None = None,
        size: str | None = None,
        seed: int | None = None,
        guidance_scale: float | None = None,
        watermark: bool | None = None,
        optimize_prompt: bool | None = None,
        optimize_prompt_options: OptimizePromptOptions | None = None,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None = None,
        sequential_image_generation: str | None = None,
        sequential_image_generation_options: SequentialImageGenerationOptions
        | None = None,
        stream: bool,
    ) -> ImagesResponse | Stream[ImageGenStreamEvent]: ...

    @apikey_required
    def generate(
        self,
        *,
        model: str,
        prompt: str,
        image: str | list[str] | None = None,
        response_format: str | None = None,
        size: str | None = None,
        seed: int | None = None,
        guidance_scale: float | None = None,
        watermark: bool | None = None,
        optimize_prompt: bool | None = None,
        optimize_prompt_options: OptimizePromptOptions | None = None,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None = None,
        sequential_image_generation: str | None = None,
        sequential_image_generation_options: SequentialImageGenerationOptions
        | None = None,
        stream: Optional[Literal[False]] | Literal[True] | NotGiven = NOT_GIVEN,
    ) -> ImagesResponse | Stream[ImageGenStreamEvent]:
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
                "optimize_prompt_options": (
                    optimize_prompt_options.model_dump(mode="json")
                    if optimize_prompt_options is not None
                    else None
                ),
                "sequential_image_generation": sequential_image_generation,
                "sequential_image_generation_options": (
                    sequential_image_generation_options.model_dump(mode="json")
                    if sequential_image_generation_options is not None
                    else None
                ),
                "stream": stream,
            },
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=ImagesResponse,
            stream=stream or False,
            stream_cls=Stream[ImageGenStreamEvent],
        )

        return resp


class AsyncImages(AsyncAPIResource):
    @overload
    async def generate(
        self,
        *,
        model: str,
        prompt: str,
        image: str | list[str] | None = None,
        response_format: str | None = None,
        size: str | None = None,
        seed: int | None = None,
        guidance_scale: float | None = None,
        watermark: bool | None = None,
        optimize_prompt: bool | None = None,
        optimize_prompt_options: OptimizePromptOptions | None = None,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None = None,
        sequential_image_generation: str | None = None,
        sequential_image_generation_options: SequentialImageGenerationOptions
        | None = None,
        stream: Optional[Literal[False]] | NotGiven = NOT_GIVEN,
    ) -> ImagesResponse: ...

    @overload
    async def generate(
        self,
        *,
        model: str,
        prompt: str,
        image: str | list[str] | None = None,
        response_format: str | None = None,
        size: str | None = None,
        seed: int | None = None,
        guidance_scale: float | None = None,
        watermark: bool | None = None,
        optimize_prompt: bool | None = None,
        optimize_prompt_options: OptimizePromptOptions | None = None,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None = None,
        sequential_image_generation: str | None = None,
        sequential_image_generation_options: SequentialImageGenerationOptions
        | None = None,
        stream: Literal[True],
    ) -> Stream[ImageGenStreamEvent]: ...

    @overload
    async def generate(
        self,
        *,
        model: str,
        prompt: str,
        image: str | list[str] | None = None,
        response_format: str | None = None,
        size: str | None = None,
        seed: int | None = None,
        guidance_scale: float | None = None,
        watermark: bool | None = None,
        optimize_prompt: bool | None = None,
        optimize_prompt_options: OptimizePromptOptions | None = None,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None = None,
        sequential_image_generation: str | None = None,
        sequential_image_generation_options: SequentialImageGenerationOptions
        | None = None,
        stream: bool,
    ) -> ImagesResponse | Stream[ImageGenStreamEvent]: ...

    @async_apikey_required
    async def generate(
        self,
        *,
        model: str,
        prompt: str,
        image: str | list[str] | None = None,
        response_format: str | None = None,
        size: str | None = None,
        seed: int | None = None,
        guidance_scale: float | None = None,
        watermark: bool | None = None,
        optimize_prompt: bool | None = None,
        optimize_prompt_options: OptimizePromptOptions | None = None,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None = None,
        sequential_image_generation: str | None = None,
        sequential_image_generation_options: SequentialImageGenerationOptions
        | None = None,
        stream: Optional[Literal[False]] | Literal[True] | NotGiven = NOT_GIVEN,
    ) -> ImagesResponse | Stream[ImageGenStreamEvent]:
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
                "optimize_prompt_options": (
                    optimize_prompt_options.model_dump(mode="json")
                    if optimize_prompt_options is not None
                    else None
                ),
                "sequential_image_generation": sequential_image_generation,
                "sequential_image_generation_options": (
                    sequential_image_generation_options.model_dump(mode="json")
                    if sequential_image_generation_options is not None
                    else None
                ),
                "stream": stream,
            },
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=ImagesResponse,
            stream=stream or False,
            stream_cls=Stream[ImageGenStreamEvent],
        )
