
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
import json
import logging
import time
from random import random
from types import TracebackType
from typing import (
    Type,
    Dict,
    TypeVar,
    Any,
    Optional,
    cast,
    TYPE_CHECKING,
    Union,
    Generic,
    Iterable,
    AsyncIterator,
    Iterator,
    Generator
)
from typing_extensions import override

import anyio
import httpx
import pydantic

from pydantic import PrivateAttr
from httpx import URL, Timeout, Limits
from httpx._types import RequestFiles

from . import _exceptions  # type: ignore
from ._constants import (
    DEFAULT_MAX_RETRIES,
    DEFAULT_TIMEOUT,
    INITIAL_RETRY_DELAY,
    MAX_RETRY_DELAY,
    RAW_RESPONSE_HEADER,
    DEFAULT_CONNECTION_LIMITS,
    CLIENT_REQUEST_HEADER,
    VERSION,
)
from ._exceptions import (
    ArkAPITimeoutError,
    ArkAPIConnectionError,
    ArkAPIStatusError,
    ArkAPIResponseValidationError,
)
from ._models import construct_type, GenericModel
from ._request_options import RequestOptions, ExtraRequestOptions
from ._response import ArkAPIResponse, ArkAsyncAPIResponse
from ._streaming import SSEDecoder, SSEBytesDecoder, Stream, AsyncStream
from ._types import (
    ResponseT,
    NotGiven,
    NOT_GIVEN,
    PostParser,
    Body,
    Query,
)
from ._utils._utils import _gen_request_id, is_given, is_mapping
from ._compat import model_copy, PYDANTIC_V2

SyncPageT = TypeVar("SyncPageT", bound="BaseSyncPage[Any]")
AsyncPageT = TypeVar("AsyncPageT", bound="BaseAsyncPage[Any]")

_T = TypeVar("_T")
_StreamT = TypeVar("_StreamT", bound=Stream[Any])
_AsyncStreamT = TypeVar("_AsyncStreamT", bound=AsyncStream[Any])

log: logging.Logger = logging.getLogger(__name__)


class _DefaultHttpxClient(httpx.Client):
    def __init__(self, **kwargs: Any) -> None:
        kwargs.setdefault("timeout", DEFAULT_TIMEOUT)
        kwargs.setdefault("limits", DEFAULT_CONNECTION_LIMITS)
        kwargs.setdefault("follow_redirects", True)
        super().__init__(**kwargs)


if TYPE_CHECKING:
    DefaultHttpxClient = httpx.Client
    """An alias to `httpx.Client` that provides the same defaults that this SDK
    uses internally.

    This is useful because overriding the `http_client` with your own instance of
    `httpx.Client` will result in httpx's defaults being used, not ours.
    """
else:
    DefaultHttpxClient = _DefaultHttpxClient


class SyncHttpxClientWrapper(DefaultHttpxClient):
    def __del__(self) -> None:
        try:
            self.close()
        except Exception:
            pass


def make_request_options(
    *,
    query: Dict[str, Any] | None = None,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None = None,
    post_parser: PostParser | NotGiven = NOT_GIVEN,
) -> ExtraRequestOptions:
    options: ExtraRequestOptions = {}
    if extra_headers is not None:
        options["headers"] = extra_headers

    if extra_body is not None:
        options["extra_body"] = extra_body

    if query is not None:
        options["params"] = query

    if extra_query is not None:
        options["params"] = {**options.get("params", {}), **extra_query}

    if timeout:
        options["timeout"] = timeout

    if is_given(post_parser):
        # internal
        options["post_parser"] = post_parser  # type: ignore

    return options


_HttpxClientT = TypeVar("_HttpxClientT", bound=Union[httpx.Client, httpx.AsyncClient])


class BaseClient(Generic[_HttpxClientT]):
    _client: _HttpxClientT
    _base_url: URL
    max_retries: int
    timeout: Union[float, Timeout, None]
    _limits: Union[httpx.Limits, None]

    def __init__(
        self,
        *,
        base_url: str | URL,
        max_retries: int = DEFAULT_MAX_RETRIES,
        timeout: float | Timeout | None = DEFAULT_TIMEOUT,
        limits: Limits | None = None,
        custom_headers: Dict[str, str] | None = None,
        custom_query: Dict[str, Any] | None = None,
    ) -> None:
        self._base_url = self._enforce_trailing_slash(URL(base_url))
        self.max_retries = max_retries
        self.timeout = timeout
        self._limits = limits
        self._custom_headers = custom_headers or {}
        self._custom_query = custom_query or {}

        if max_retries is None:  # pyright: ignore[reportUnnecessaryComparison]
            raise TypeError(
                "max_retries cannot be None. If you want to disable retries, pass `0`; if you want unlimited retries, pass `math.inf` or a very high number`"
            )

    @property
    def auth_headers(self) -> dict[str, str]:
        return {}

    @property
    def user_agent(self) -> str:
        return "volc-sdk-python/" + VERSION

    def default_headers(self) -> Dict[str, str]:
        return {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "User-Agent": self.user_agent,
            CLIENT_REQUEST_HEADER: _gen_request_id(),
            **self.auth_headers,
            **self._custom_headers,
        }

    def _make_sse_decoder(self) -> SSEDecoder | SSEBytesDecoder:
        return SSEDecoder()

    def _build_headers(self, options: RequestOptions) -> httpx.Headers:
        custom_headers = options.headers or {}
        headers_dict = {**self.default_headers(), **custom_headers}
        headers = httpx.Headers(headers_dict)

        return headers

    def _prepare_url(self, url: str) -> URL:
        merge_url = URL(url)
        if merge_url.is_relative_url:
            merge_raw_path = self._base_url.raw_path + merge_url.raw_path.lstrip(b"/")
            return self._base_url.copy_with(raw_path=merge_raw_path)

        return merge_url

    def _should_stream_response_body(self, request: httpx.Request) -> bool:
        return request.headers.get(RAW_RESPONSE_HEADER) == "stream"

    def _build_request(
        self,
        options: RequestOptions,
    ) -> httpx.Request:
        if log.isEnabledFor(logging.DEBUG):
            log.debug("Request options: %s", options.model_dump(exclude_unset=True))

        body = options.body
        if options.extra_body is not None:
            if body is None:
                body = options.extra_body
            elif isinstance(body, Dict):
                body = {**body, **options.extra_body}
            else:
                raise RuntimeError(
                    f"Unexpected JSON data type, {type(body)}, cannot merge with `extra_body`"
                )

        headers = self._build_headers(options)
        params = options.params

        return self._client.build_request(  # pyright: ignore[reportUnknownMemberType]
            headers=headers,
            timeout=options.timeout if options.timeout else self.timeout,
            method=options.method,
            url=self._prepare_url(options.url),
            params=params,  # type: ignore
            json=body,
        )

    def _calculate_retry_timeout(
        self,
        remaining_retries: int,
        options: RequestOptions,
        response_headers: Optional[httpx.Headers] = None,
    ) -> float:
        max_retries = options.max_retries if options.max_retries else self.max_retries

        nb_retries = max_retries - remaining_retries

        # Apply exponential backoff, but not more than the max.
        sleep_seconds = min(INITIAL_RETRY_DELAY * pow(2.0, nb_retries), MAX_RETRY_DELAY)

        # Apply some jitter, plus-or-minus half a second.
        jitter = 1 - 0.25 * random()
        timeout = sleep_seconds * jitter
        return timeout if timeout >= 0 else 0

    def _should_retry(self, response: httpx.Response) -> bool:
        # Note: this is not a standard header
        should_retry_header = response.headers.get("x-should-retry")

        # If the server explicitly says whether or not to retry, obey.
        if should_retry_header == "true":
            log.debug("Retrying as header `x-should-retry` is set to `true`")
            return True
        if should_retry_header == "false":
            log.debug("Not retrying as header `x-should-retry` is set to `false`")
            return False

        # Retry on request timeouts.
        if response.status_code == 408:
            log.debug("Retrying due to status code %i", response.status_code)
            return True

        # Retry on lock timeouts.
        if response.status_code == 409:
            log.debug("Retrying due to status code %i", response.status_code)
            return True

        # Retry on rate limits.
        if response.status_code == 429:
            log.debug("Retrying due to status code %i", response.status_code)
            return True

        # Retry internal errors.
        if response.status_code >= 500:
            log.debug("Retrying due to status code %i", response.status_code)
            return True

        log.debug("Not retrying")
        return False

    def _make_status_error(
        self, err_msg: str, *, body: object, response: httpx.Response, request_id: str
    ) -> ArkAPIStatusError:
        data = body.get("error", body) if isinstance(body, Dict) else body
        if response.status_code == 400:
            return _exceptions.ArkBadRequestError(
                err_msg, response=response, body=data, request_id=request_id
            )

        if response.status_code == 401:
            return _exceptions.ArkAuthenticationError(
                err_msg, response=response, body=data, request_id=request_id
            )

        if response.status_code == 403:
            return _exceptions.ArkPermissionDeniedError(
                err_msg, response=response, body=data, request_id=request_id
            )

        if response.status_code == 404:
            return _exceptions.ArkNotFoundError(
                err_msg, response=response, body=data, request_id=request_id
            )

        if response.status_code == 409:
            return _exceptions.ArkConflictError(
                err_msg, response=response, body=data, request_id=request_id
            )

        if response.status_code == 422:
            return _exceptions.ArkUnprocessableEntityError(
                err_msg, response=response, body=data, request_id=request_id
            )

        if response.status_code == 429:
            return _exceptions.ArkRateLimitError(
                err_msg, response=response, body=data, request_id=request_id
            )

        if response.status_code >= 500:
            return _exceptions.ArkInternalServerError(
                err_msg, response=response, body=data, request_id=request_id
            )
        return ArkAPIStatusError(
            err_msg, response=response, body=data, request_id=request_id
        )

    def _make_status_error_from_response(
        self, response: httpx.Response, request_id: str
    ) -> ArkAPIStatusError:
        if response.is_closed and not response.is_stream_consumed:
            body = None
            err_msg = f"Error code: {response.status_code}"
        else:
            err_text = response.text.strip()
            body = err_text

            try:
                body = json.loads(err_text)
                err_msg = f"Error code: {response.status_code} - {body}"
            except Exception:
                err_msg = err_text or f"Error code: {response.status_code}"

        return self._make_status_error(
            err_msg, body=body, response=response, request_id=request_id
        )

    def _enforce_trailing_slash(self, url: URL) -> URL:
        if url.raw_path.endswith(b"/"):
            return url
        return url.copy_with(raw_path=url.raw_path + b"/")

    def _process_response_data(
        self,
        *,
        data: object,
        cast_to: type[ResponseT],
        response: httpx.Response,
    ) -> ResponseT:
        request_id = (
            response.headers.get(CLIENT_REQUEST_HEADER, "") if response else None
        )
        if data is None:
            return cast(ResponseT, None)

        if cast_to is object:
            return cast(ResponseT, data)

        try:
            return cast(ResponseT, construct_type(type_=cast_to, value=data))
        except pydantic.ValidationError as err:
            raise ArkAPIResponseValidationError(
                response=response, body=data, request_id=request_id
            ) from err

    def _remaining_retries(
        self,
        remaining_retries: Optional[int],
        options: RequestOptions,
    ) -> int:
        return (
            remaining_retries
            if remaining_retries is not None
            else options.get_max_retries(self.max_retries)
        )


class SyncAPIClient(BaseClient):
    _client: httpx.Client

    def __init__(
        self,
        *,
        base_url: str | URL,
        max_retries: int = DEFAULT_MAX_RETRIES,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        custom_headers: Dict[str, str] | None = None,
        custom_query: Dict[str, object] | None = None,
    ) -> None:
        if http_client is not None and not isinstance(http_client, httpx.Client):  # pyright: ignore[reportUnnecessaryIsInstance]
            raise TypeError(
                f"Invalid `http_client` argument; Expected an instance of `httpx.Client` but got {type(http_client)}"
            )

        super().__init__(
            base_url=base_url,
            timeout=cast(Timeout, timeout),
            max_retries=max_retries,
            custom_query=custom_query,
            custom_headers=custom_headers,
        )

        self._client = http_client or SyncHttpxClientWrapper(
            base_url=self._enforce_trailing_slash(URL(base_url)),
            timeout=cast(Timeout, timeout),
        )

    def _request(
        self,
        *,
        cast_to: Type[ResponseT],
        options: RequestOptions,
        remaining_retries: int | None,
        stream: bool,
        stream_cls: type[_StreamT] | None,
    ) -> ResponseT | _StreamT:
        retries = self._remaining_retries(remaining_retries, options)
        request = self._build_request(options)
        req_id = request.headers.get(CLIENT_REQUEST_HEADER, "")
        try:
            response = self._client.send(
                request,
                stream=stream or self._should_stream_response_body(request=request),
            )
        except httpx.TimeoutException as err:
            if retries > 0:
                return self._retry_request(
                    options,
                    cast_to,
                    retries,
                    stream=stream,
                    stream_cls=stream_cls,
                    response_headers=None,
                )

            log.debug("Raising timeout error")
            raise ArkAPITimeoutError(request=request, request_id=req_id) from err
        except Exception as err:
            log.debug("Encountered Exception", exc_info=True)

            if retries > 0:
                return self._retry_request(
                    options,
                    cast_to,
                    retries,
                    stream=stream,
                    stream_cls=stream_cls,
                    response_headers=None,
                )

            log.debug("Raising connection error")
            raise ArkAPIConnectionError(request=request, request_id=req_id) from err

        log.debug(
            'HTTP Request: %s %s "%i %s"',
            request.method,
            request.url,
            response.status_code,
            response.reason_phrase,
        )

        try:
            response.raise_for_status()
        except httpx.HTTPStatusError as err:  # thrown on 4xx and 5xx status code
            log.debug("Encountered httpx.HTTPStatusError", exc_info=True)

            if retries > 0 and self._should_retry(err.response):
                err.response.close()
                return self._retry_request(
                    options,
                    cast_to,
                    retries,
                    err.response.headers,
                    stream=stream,
                    stream_cls=stream_cls,
                )

            # If the response is streamed then we need to explicitly read the response
            # to completion before attempting to access the response text.
            if not err.response.is_closed:
                err.response.read()

            log.debug("Re-raising status error")
            raise self._make_status_error_from_response(
                err.response, request_id=req_id
            ) from None

        return self._process_response(
            cast_to=cast_to,
            response=response,
            stream=stream,
            stream_cls=stream_cls,
            options=options,
        )

    def _retry_request(
        self,
        options: RequestOptions,
        cast_to: Type[ResponseT],
        remaining_retries: int,
        response_headers: httpx.Headers | None,
        *,
        stream: bool,
        stream_cls: type[_StreamT] | None,
    ) -> ResponseT | _StreamT:
        remaining = remaining_retries - 1
        if remaining == 1:
            log.info("1 retry left")
        else:
            log.info("%i retries left", remaining)

        timeout = self._calculate_retry_timeout(remaining, options, response_headers)
        log.info("Retrying request to %s in %f seconds", options.url, timeout)

        # In a synchronous context we are blocking the entire thread. Up to the library user to run the client in a
        # different thread if necessary.
        time.sleep(timeout)

        return self._request(
            options=options,
            cast_to=cast_to,
            remaining_retries=remaining,
            stream=stream,
            stream_cls=stream_cls,
        )

    def _process_response(
        self,
        *,
        cast_to: Type[ResponseT],
        options: RequestOptions,
        response: httpx.Response,
        stream: bool,
        stream_cls: type[Stream[Any]] | type[AsyncStream[Any]] | None,
    ) -> ResponseT:
        if cast_to == httpx.Response:
            return cast(ResponseT, response)

        api_response = ArkAPIResponse(
            raw=response,
            client=self,
            cast_to=cast("type[ResponseT]", cast_to),  # pyright: ignore[reportUnnecessaryCast]
            stream=stream,
            stream_cls=stream_cls,
            options=options,
        )
        if bool(response.request.headers.get(RAW_RESPONSE_HEADER)):
            return cast(ResponseT, api_response)

        return api_response.parse()

    def post(
        self,
        path: str,
        *,
        cast_to: Type[ResponseT],
        body: Dict | None = None,
        options: ExtraRequestOptions = {},
        files: RequestFiles | None = None,
        stream: bool = False,
        stream_cls: type[_StreamT] | None = None,
    ) -> ResponseT | _StreamT:
        opts = RequestOptions.construct(  # type: ignore
            method="post",
            url=path,
            files=files,
            body=body,
            **options,
        )

        return cast(
            ResponseT, self.request(cast_to, opts, stream=stream, stream_cls=stream_cls)
        )

    def get(
        self,
        path: str,
        *,
        cast_to: Type[ResponseT],
        params: list[tuple[str, str]] | None = None,
        options: ExtraRequestOptions = {},
        stream: bool = False,
        stream_cls: type[_StreamT] | None = None,
    ) -> ResponseT | _StreamT:
        opts = RequestOptions.construct(
            method="get",
            url=path,
            params=params,
            **options,
        )

        return cast(
            ResponseT, self.request(cast_to, opts, stream=stream, stream_cls=stream_cls)
        )

    def delete(
        self,
        path: str,
        *,
        cast_to: Type[ResponseT],
        params: list[tuple[str, str]] | None = None,
        options: ExtraRequestOptions = {},
    ) -> ResponseT:
        opts = RequestOptions.construct(  # type: ignore
            method="delete",
            url=path,
            params=params,
            **options,
        )

        return cast(ResponseT, self.request(cast_to, opts))

    def post_without_retry(
        self,
        path: str,
        *,
        cast_to: Type[ResponseT],
        body: Dict | None = None,
        options: ExtraRequestOptions = {},
        files: RequestFiles | None = None,
        stream: bool = False,
        stream_cls: type[_StreamT] | None = None,
    ) -> ResponseT | _StreamT:
        opts = RequestOptions.construct(  # type: ignore
            method="post",
            url=path,
            body=body,
            files=files,
            **options,
        )

        return cast(
            ResponseT,
            self.request(
                cast_to, opts, remaining_retries=0, stream=stream, stream_cls=stream_cls
            ),
        )

    def get_api_list(
        self,
        path: str,
        *,
        model: Type[object],
        page: Type[SyncPageT],
        body: Body | None = None,
        options: ExtraRequestOptions = {},
        method: str = "get",
    ) -> AsyncPageT:
        opts = RequestOptions.construct(method=method, url=path, json_data=body, **options)
        return self._request_api_list(model, page, opts)

    def _request_api_list(
        self,
        model: Type[object],
        page: Type[SyncPageT],
        options: RequestOptions,
    ) -> AsyncPageT:
        def _parser(resp: AsyncPageT) -> SyncPageT:
            resp._set_private_attributes(
                client=self,
                model=model,
                options=options,
            )
            return resp

        options.post_parser = _parser
        return self.request(page, options, stream=False)

    def request(
        self,
        cast_to: Type[ResponseT],
        options: RequestOptions,
        remaining_retries: Optional[int] = None,
        *,
        stream: bool = False,
        stream_cls: type[_StreamT] | None = None,
    ) -> ResponseT | _StreamT:
        return self._request(
            cast_to=cast_to,
            options=options,
            stream=stream,
            stream_cls=stream_cls,
            remaining_retries=remaining_retries,
        )

    def is_closed(self) -> bool:
        return self._client.is_closed

    def close(self) -> None:
        """Close the underlying HTTPX client.

        The client will *not* be usable after this.
        """
        # If an error is thrown while constructing a client, self._client
        # may not be present
        if hasattr(self, "_client"):
            self._client.close()

    def __enter__(self: _T) -> _T:
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        self.close()


class _DefaultAsyncHttpxClient(httpx.AsyncClient):
    def __init__(self, **kwargs: Any) -> None:
        kwargs.setdefault("timeout", DEFAULT_TIMEOUT)
        kwargs.setdefault("limits", DEFAULT_CONNECTION_LIMITS)
        kwargs.setdefault("follow_redirects", True)
        super().__init__(**kwargs)


if TYPE_CHECKING:
    DefaultAsyncHttpxClient = httpx.AsyncClient
    """An alias to `httpx.AsyncClient` that provides the same defaults that this SDK
    uses internally.

    This is useful because overriding the `http_client` with your own instance of
    `httpx.AsyncClient` will result in httpx's defaults being used, not ours.
    """
else:
    DefaultAsyncHttpxClient = _DefaultAsyncHttpxClient


class AsyncHttpxClientWrapper(DefaultAsyncHttpxClient):
    def __del__(self) -> None:
        try:
            # TODO(someday): support non asyncio runtimes here
            asyncio.get_running_loop().create_task(self.aclose())
        except Exception:
            pass


class AsyncAPIClient(BaseClient):
    _client: httpx.AsyncClient

    def __init__(
        self,
        *,
        base_url: str | URL,
        max_retries: int = DEFAULT_MAX_RETRIES,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        custom_headers: Dict[str, str] | None = None,
        custom_query: Dict[str, object] | None = None,
    ) -> None:
        if http_client is not None and not isinstance(http_client, httpx.AsyncClient):  # pyright: ignore[reportUnnecessaryIsInstance]
            raise TypeError(
                f"Invalid `http_client` argument; Expected an instance of `httpx.Client` but got {type(http_client)}"
            )

        super().__init__(
            base_url=base_url,
            timeout=cast(Timeout, timeout),
            max_retries=max_retries,
            custom_query=custom_query,
            custom_headers=custom_headers,
        )

        self._client = http_client or AsyncHttpxClientWrapper(
            base_url=self._enforce_trailing_slash(URL(base_url)),
            timeout=cast(Timeout, timeout),
        )

    async def post(
        self,
        path: str,
        *,
        cast_to: Type[ResponseT],
        body: Dict | None = None,
        options: ExtraRequestOptions = {},
        files: RequestFiles | None = None,
        stream: bool = False,
        stream_cls: type[_AsyncStreamT] | None = None,
    ) -> ResponseT | _AsyncStreamT:
        opts = RequestOptions.construct(
            method="post",
            url=path,
            body=body,
            files=files,
            **options,
        )

        return await self.request(cast_to, opts, stream=stream, stream_cls=stream_cls)

    async def get(
        self,
        path: str,
        *,
        cast_to: Type[ResponseT],
        params: list[tuple[str, str]] | None = None,
        options: ExtraRequestOptions = {},
        stream: bool = False,
        stream_cls: type[_AsyncStreamT] | None = None,
    ) -> ResponseT | _AsyncStreamT:
        opts = RequestOptions.construct(
            method="get",
            url=path,
            params=params,
            **options,
        )

        return await self.request(cast_to, opts, stream=stream, stream_cls=stream_cls)

    async def delete(
        self,
        path: str,
        *,
        cast_to: Type[ResponseT],
        params: list[tuple[str, str]] | None = None,
        options: ExtraRequestOptions = {},
    ) -> ResponseT:
        opts = RequestOptions.construct(
            method="delete",
            url=path,
            params=params,
            **options,
        )

        return await self.request(cast_to, opts)

    async def post_without_retry(
        self,
        path: str,
        *,
        cast_to: Type[ResponseT],
        body: Dict | None = None,
        options: ExtraRequestOptions = {},
        files: RequestFiles | None = None,
        stream: bool = False,
        stream_cls: type[_AsyncStreamT] | None = None,
    ) -> ResponseT | _AsyncStreamT:
        opts = RequestOptions.construct(
            method="post",
            url=path,
            body=body,
            files=files,
            **options,
        )

        return await self.request(
            cast_to, opts, remaining_retries=0, stream=stream, stream_cls=stream_cls
        )

    async def get_api_list(
        self,
        path: str,
        *,
        model: Type[object],
        page: Type[AsyncPageT],
        body: Body | None = None,
        options: ExtraRequestOptions = {},
        method: str = "get",
    ) -> AsyncPageT:
        opts = RequestOptions.construct(method=method, url=path, json_data=body, **options)
        return await self._request_api_list(model, page, opts)

    async def _request_api_list(
        self,
        model: Type[object],
        page: Type[AsyncPageT],
        options: RequestOptions,
    ) -> AsyncPageT:
        def _parser(resp: AsyncPageT) -> SyncPageT:
            resp._set_private_attributes(
                client=self,
                model=model,
                options=options,
            )
            return resp

        options.post_parser = _parser

        return await self.request(page, options, stream=False)

    async def request(
        self,
        cast_to: Type[ResponseT],
        options: RequestOptions,
        remaining_retries: Optional[int] = None,
        *,
        stream: bool = False,
        stream_cls: type[_StreamT] | None = None,
    ) -> ResponseT | _StreamT:
        return await self._request(
            cast_to=cast_to,
            options=options,
            stream=stream,
            stream_cls=stream_cls,
            remaining_retries=remaining_retries,
        )

    async def _request(
        self,
        *,
        cast_to: Type[ResponseT],
        options: RequestOptions,
        remaining_retries: int | None,
        stream: bool,
        stream_cls: type[_AsyncStreamT] | None,
    ) -> ResponseT | _AsyncStreamT:
        retries = self._remaining_retries(remaining_retries, options)
        request = self._build_request(options)
        req_id = request.headers.get(CLIENT_REQUEST_HEADER, "")
        try:
            response = await self._client.send(
                request,
                stream=stream or self._should_stream_response_body(request=request),
            )
        except httpx.TimeoutException as err:
            if retries > 0:
                return await self._retry_request(
                    options,
                    cast_to,
                    retries,
                    stream=stream,
                    stream_cls=stream_cls,
                    response_headers=None,
                )

            log.debug("Raising timeout error")
            raise ArkAPITimeoutError(request=request, request_id=req_id) from err
        except Exception as err:
            log.debug("Encountered Exception", exc_info=True)

            if retries > 0:
                return await self._retry_request(
                    options,
                    cast_to,
                    retries,
                    stream=stream,
                    stream_cls=stream_cls,
                    response_headers=None,
                )

            log.debug("Raising connection error")
            raise ArkAPIConnectionError(request=request, request_id=req_id) from err

        log.debug(
            'HTTP Request: %s %s "%i %s"',
            request.method,
            request.url,
            response.status_code,
            response.reason_phrase,
        )

        try:
            response.raise_for_status()
        except httpx.HTTPStatusError as err:  # thrown on 4xx and 5xx status code
            log.debug("Encountered httpx.HTTPStatusError", exc_info=True)

            if retries > 0 and self._should_retry(err.response):
                await err.response.aclose()
                return await self._retry_request(
                    options,
                    cast_to,
                    retries,
                    err.response.headers,
                    stream=stream,
                    stream_cls=stream_cls,
                )

            # If the response is streamed then we need to explicitly read the response
            # to completion before attempting to access the response text.
            if not err.response.is_closed:
                await err.response.aread()

            log.debug("Re-raising status error")
            raise self._make_status_error_from_response(
                err.response, request_id=req_id
            ) from None

        return await self._process_response(
            cast_to=cast_to,
            response=response,
            stream=stream,
            stream_cls=stream_cls,
            options=options,
        )

    async def _retry_request(
        self,
        options: RequestOptions,
        cast_to: Type[ResponseT],
        remaining_retries: int,
        response_headers: httpx.Headers | None,
        *,
        stream: bool,
        stream_cls: type[_AsyncStreamT] | None,
    ) -> ResponseT | _AsyncStreamT:
        remaining = remaining_retries - 1
        if remaining == 1:
            log.debug("1 retry left")
        else:
            log.debug("%i retries left", remaining)

        timeout = self._calculate_retry_timeout(remaining, options, response_headers)
        log.info("Retrying request to %s in %f seconds", options.url, timeout)

        await anyio.sleep(timeout)

        return await self._request(
            options=options,
            cast_to=cast_to,
            remaining_retries=remaining,
            stream=stream,
            stream_cls=stream_cls,
        )

    async def _process_response(
        self,
        *,
        cast_to: Type[ResponseT],
        options: RequestOptions,
        response: httpx.Response,
        stream: bool,
        stream_cls: type[Stream[Any]] | type[AsyncStream[Any]] | None,
    ) -> ResponseT:
        if cast_to == httpx.Response:
            return cast(ResponseT, response)

        api_response = ArkAsyncAPIResponse(
            raw=response,
            client=self,
            cast_to=cast("type[ResponseT]", cast_to),  # pyright: ignore[reportUnnecessaryCast]
            stream=stream,
            stream_cls=stream_cls,
            options=options,
        )
        if bool(response.request.headers.get(RAW_RESPONSE_HEADER)):
            return cast(ResponseT, api_response)

        return await api_response.parse()

    def is_closed(self) -> bool:
        return self._client.is_closed

    async def close(self) -> None:
        """Close the underlying HTTPX client.

        The client will *not* be usable after this.
        """
        await self._client.aclose()

    async def __aenter__(self: _T) -> _T:
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        await self.close()


class PageInfo:
    """Stores the necessary information to build the request to retrieve the next page.

    Either `url` or `params` must be set.
    """

    url: URL | NotGiven
    params: Query | NotGiven
    json: Body | NotGiven

    def __init__(
        self,
        *,
        url: URL | NotGiven = NOT_GIVEN,
        json: Body | NotGiven = NOT_GIVEN,
        params: Query | NotGiven = NOT_GIVEN,
    ) -> None:
        self.url = url
        self.json = json
        self.params = params

    @override
    def __repr__(self) -> str:
        if self.url:
            return f"{self.__class__.__name__}(url={self.url})"
        if self.json:
            return f"{self.__class__.__name__}(json={self.json})"
        return f"{self.__class__.__name__}(params={self.params})"


class BasePage(GenericModel, Generic[_T]):
    """
    Defines the core interface for pagination.

    Type Args:
        ModelT: The pydantic model that represents an item in the response.

    Methods:
        has_next_page(): Check if there is another page available
        next_page_info(): Get the necessary information to make a request for the next page
    """

    _options: RequestOptions = PrivateAttr()
    _model: Type[_T] = PrivateAttr()

    def has_next_page(self) -> bool:
        items = self._get_page_items()
        if not items:
            return False
        return self.next_page_info() is not None

    def next_page_info(self) -> Optional[PageInfo]: ...

    def _get_page_items(self) -> Iterable[_T]:  # type: ignore[empty-body]
        ...

    def _params_from_url(self, url: URL) -> httpx.QueryParams:
        # TODO: do we have to preprocess params here?
        return httpx.QueryParams(cast(Any, self._options.params)).merge(url.params)

    def _info_to_options(self, info: PageInfo) -> RequestOptions:
        options = model_copy(self._options)
        options._strip_raw_response_header()

        if not isinstance(info.params, NotGiven):
            options.params = {**options.params, **info.params}
            return options

        if not isinstance(info.url, NotGiven):
            params = self._params_from_url(info.url)
            url = info.url.copy_with(params=params)
            options.params = dict(url.params)
            options.url = str(url)
            return options

        if not isinstance(info.json, NotGiven):
            if not is_mapping(info.json):
                raise TypeError("Pagination is only supported with mappings")

            if not options.json_data:
                options.json_data = {**info.json}
            else:
                if not is_mapping(options.json_data):
                    raise TypeError("Pagination is only supported with mappings")

                options.json_data = {**options.json_data, **info.json}
            return options

        raise ValueError("Unexpected PageInfo state")


class BaseSyncPage(BasePage[_T], Generic[_T]):
    _client: SyncAPIClient = pydantic.PrivateAttr()

    def _set_private_attributes(
        self,
        client: SyncAPIClient,
        model: Type[_T],
        options: RequestOptions,
    ) -> None:
        if PYDANTIC_V2 and getattr(self, "__pydantic_private__", None) is None:
            self.__pydantic_private__ = {}

        self._model = model
        self._client = client
        self._options = options

    # Pydantic uses a custom `__iter__` method to support casting BaseModels
    # to dictionaries. e.g. dict(model).
    # As we want to support `for item in page`, this is inherently incompatible
    # with the default pydantic behaviour. It is not possible to support both
    # use cases at once. Fortunately, this is not a big deal as all other pydantic
    # methods should continue to work as expected as there is an alternative method
    # to cast a model to a dictionary, model.dict(), which is used internally
    # by pydantic.
    def __iter__(self) -> Iterator[_T]:  # type: ignore
        for page in self.iter_pages():
            for item in page._get_page_items():
                yield item

    def iter_pages(self: SyncPageT) -> Iterator[SyncPageT]:
        page = self
        while True:
            yield page
            if page.has_next_page():
                page = page.get_next_page()
            else:
                return

    def get_next_page(self: SyncPageT) -> SyncPageT:
        info = self.next_page_info()
        if not info:
            raise RuntimeError(
                "No next page expected; please check `.has_next_page()` before calling `.get_next_page()`."
            )

        options = self._info_to_options(info)
        return self._client._request_api_list(self._model, page=self.__class__, options=options)


class AsyncPaginator(Generic[_T, AsyncPageT]):
    def __init__(
        self,
        client: AsyncAPIClient,
        options: RequestOptions,
        page_cls: Type[AsyncPageT],
        model: Type[_T],
    ) -> None:
        self._model = model
        self._client = client
        self._options = options
        self._page_cls = page_cls

    def __await__(self) -> Generator[Any, None, AsyncPageT]:
        return self._get_page().__await__()

    async def _get_page(self) -> AsyncPageT:
        def _parser(resp: AsyncPageT) -> AsyncPageT:
            resp._set_private_attributes(
                model=self._model,
                options=self._options,
                client=self._client,
            )
            return resp

        self._options.post_parser = _parser

        return await self._client.request(self._page_cls, self._options)

    async def __aiter__(self) -> AsyncIterator[_T]:
        # https://github.com/microsoft/pyright/issues/3464
        page = cast(
            AsyncPageT,
            await self,  # type: ignore
        )
        async for item in page:
            yield item


class BaseAsyncPage(BasePage[_T], Generic[_T]):
    _client: AsyncAPIClient = pydantic.PrivateAttr()

    def _set_private_attributes(
        self,
        model: Type[_T],
        client: AsyncAPIClient,
        options: RequestOptions,
    ) -> None:
        if PYDANTIC_V2 and getattr(self, "__pydantic_private__", None) is None:
            self.__pydantic_private__ = {}

        self._model = model
        self._client = client
        self._options = options

    async def __aiter__(self) -> AsyncIterator[_T]:
        async for page in self.iter_pages():
            for item in page._get_page_items():
                yield item

    async def iter_pages(self: AsyncPageT) -> AsyncIterator[AsyncPageT]:
        page = self
        while True:
            yield page
            if page.has_next_page():
                page = await page.get_next_page()
            else:
                return

    async def get_next_page(self: AsyncPageT) -> AsyncPageT:
        info = self.next_page_info()
        if not info:
            raise RuntimeError(
                "No next page expected; please check `.has_next_page()` before calling `.get_next_page()`."
            )

        options = self._info_to_options(info)
        return await self._client._request_api_list(self._model, page=self.__class__, options=options)
