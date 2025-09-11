
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

from typing import Iterable, Union, List, Optional

import httpx

from volcenginesdkarkruntime._base_client import make_request_options
from volcenginesdkarkruntime._resource import SyncAPIResource, AsyncAPIResource
from volcenginesdkarkruntime.types.content_generation.create_task_content_param import (
    CreateTaskContentParam,
)
from ..._compat import cached_property
from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from ..._types import Body, Query, Headers
from ..._utils._utils import apikey_required, async_apikey_required
from ...types.content_generation.content_generation_task import ContentGenerationTask
from ...types.content_generation.content_generation_task_id import (
    ContentGenerationTaskID,
)
from ...types.content_generation.list_content_generation_tasks_response import (
    ListContentGenerationTasksResponse,
)


class Tasks(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TasksWithRawResponse:
        return TasksWithRawResponse(self)

    @apikey_required
    def create(
        self,
        *,
        model: str,
        content: Iterable[CreateTaskContentParam],
        callback_url: Optional[str] = None,
        return_last_frame: Optional[bool] = None,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None = None,
    ) -> ContentGenerationTaskID:
        resp = self._post(
            "/contents/generations/tasks",
            body={
                "model": model,
                "content": content,
                "callback_url": callback_url,
                "return_last_frame": return_last_frame,
            },
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=ContentGenerationTaskID,
        )
        return resp

    @apikey_required
    def get(
        self,
        *,
        task_id: str,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None = None,
    ) -> ContentGenerationTask:
        resp = self._get(
            path=f"/contents/generations/tasks/{task_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=ContentGenerationTask,
        )
        return resp

    @apikey_required
    def list(
        self,
        page_num: int | None = None,
        page_size: int | None = None,
        status: str | None = None,
        task_ids: Union[List[str], str] | None = None,
        model: str | None = None,
        extra_headers: Headers | None = None,
        extra_body: Body | None = None,
        extra_query: Query | None = None,
        timeout: float | httpx.Timeout | None = None,
    ) -> ListContentGenerationTasksResponse:
        query_params = []
        if page_num:
            query_params.append(("page_num", page_num))
        if page_size:
            query_params.append(("page_size", page_size))
        if status:
            query_params.append(("filter.status", status))
        if model:
            query_params.append(("filter.model", model))
        if task_ids:
            if isinstance(task_ids, str):
                task_ids = [task_ids]
            for task_id in task_ids:
                query_params.append(("filter.task_ids", task_id))

        resp = self._get(
            path="/contents/generations/tasks",
            params=query_params,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=ListContentGenerationTasksResponse,
        )
        return resp

    @apikey_required
    def delete(
        self,
        task_id: str,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None = None,
    ) -> None:
        resp = self._delete(
            path=f"/contents/generations/tasks/{task_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=ContentGenerationTask,
        )
        return resp


class AsyncTasks(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTasksWithRawResponse:
        return AsyncTasksWithRawResponse(self)

    @async_apikey_required
    async def create(
        self,
        *,
        model: str,
        content: Iterable[CreateTaskContentParam],
        callback_url: Optional[str] = None,
        return_last_frame: Optional[bool] = None,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None = None,
    ) -> ContentGenerationTaskID:
        resp = await self._post(
            "/contents/generations/tasks",
            body={
                "model": model,
                "content": content,
                "callback_url": callback_url,
                "return_last_frame": return_last_frame,
            },
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=ContentGenerationTaskID,
        )
        return resp

    @async_apikey_required
    async def get(
        self,
        *,
        task_id: str,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None = None,
    ) -> ContentGenerationTask:
        resp = await self._get(
            path=f"/contents/generations/tasks/{task_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=ContentGenerationTask,
        )
        return resp

    @async_apikey_required
    async def list(
        self,
        page_num: int | None = None,
        page_size: int | None = None,
        status: str | None = None,
        task_ids: Union[List[str], str] | None = None,
        model: str | None = None,
        extra_headers: Headers | None = None,
        extra_body: Body | None = None,
        extra_query: Query | None = None,
        timeout: float | httpx.Timeout | None = None,
    ) -> ListContentGenerationTasksResponse:
        query_params = []
        if page_num:
            query_params.append(("page_num", page_num))
        if page_size:
            query_params.append(("page_size", page_size))
        if status:
            query_params.append(("filter.status", status))
        if model:
            query_params.append(("filter.model", model))
        if task_ids:
            if isinstance(task_ids, str):
                task_ids = [task_ids]
            for task_id in task_ids:
                query_params.append(("filter.task_ids", task_id))

        resp = await self._get(
            path="/contents/generations/tasks",
            params=query_params,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=ListContentGenerationTasksResponse,
        )
        return resp

    @async_apikey_required
    async def delete(
        self,
        task_id: str,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None = None,
    ) -> None:
        resp = await self._delete(
            path=f"/contents/generations/tasks/{task_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=ContentGenerationTask,
        )
        return resp


class TasksWithRawResponse:
    def __init__(self, tasks: Tasks) -> None:
        self._tasks = tasks

        self.create = to_raw_response_wrapper(
            tasks.create,
        )


class AsyncTasksWithRawResponse:
    def __init__(self, tasks: AsyncTasks) -> None:
        self._tasks = tasks

        self.create = async_to_raw_response_wrapper(
            tasks.create,
        )
