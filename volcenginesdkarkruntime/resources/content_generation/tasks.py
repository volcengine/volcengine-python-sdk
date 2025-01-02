from __future__ import annotations

from typing import Iterable, Union, List
import httpx

from ..._types import Body, Query, Headers
from ...types.content_generation.content_generation_task import ContentGenerationTask
from ...types.content_generation.content_generation_task_id import ContentGenerationTaskID
from volcenginesdkarkruntime._base_client import make_request_options
from volcenginesdkarkruntime._resource import SyncAPIResource
from volcenginesdkarkruntime.types.content_generation.create_task_content_param import CreateTaskContentParam
from ...types.content_generation.list_content_generation_tasks_response import ListContentGenerationTasksResponse


class Tasks(SyncAPIResource):
    def create(
            self,
            *,
            model: str,
            content: Iterable[CreateTaskContentParam],
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


    def get(
            self,
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

    def list(
            self,
            page_num: int | None = None,
            page_size: int | None = None,
            status: str | None = None,
            task_ids : Union[List[str], str] | None = None,
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

    def delete(
            self,
            task_id: str,
            extra_headers: Headers | None = None,
            extra_query: Query | None = None,
            extra_body: Body | None = None,
            timeout: float | httpx.Timeout | None = None,
    ):
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
