from __future__ import annotations

import datetime
import functools
import inspect
import logging
from types import TracebackType
from typing import (
    Any,
    Union,
    Generic,
    TypeVar,
    Iterator,
    AsyncIterator,
    cast,
    Callable,
    Awaitable,
    TYPE_CHECKING,
)

import httpx
from typing_extensions import ParamSpec, override, get_origin

from ._constants import CLIENT_REQUEST_HEADER, RAW_RESPONSE_HEADER  # type: ignore
from ._exceptions import ArkError
from ._streaming import Stream, AsyncStream
from ._utils import extract_type_arg, is_annotated_type  # type: ignore

if TYPE_CHECKING:
    from ._base_client import BaseClient

P = ParamSpec("P")
R = TypeVar("R")
_T = TypeVar("_T")
_APIResponseT = TypeVar("_APIResponseT", bound="ArkAPIResponse[Any]")
_AsyncAPIResponseT = TypeVar("_AsyncAPIResponseT", bound="ArkAsyncAPIResponse[Any]")
_DefaultStreamT = TypeVar("_DefaultStreamT", bound=Union[Stream[Any], AsyncStream[Any]])

log: logging.Logger = logging.getLogger(__name__)


class BaseAPIResponse(Generic[R]):
    _cast_to: type[R]
    _client: BaseClient
    _parsed_by_type: dict[type[Any], Any]
    _is_sse_stream: bool
    _stream_cls: type[Stream[Any]] | type[AsyncStream[Any]] | None
    _request_id: str

    http_response: httpx.Response

    def __init__(
        self,
        *,
        raw: httpx.Response,
        cast_to: type[R],
        client: BaseClient,
        stream: bool,
        stream_cls: type[Stream[Any]] | type[AsyncStream[Any]] | None,
    ) -> None:
        self._cast_to = cast_to
        self._client = client
        self._parsed_by_type = {}
        self._is_sse_stream = stream
        self._stream_cls = stream_cls
        self.http_response = raw

    @property
    def request_id(self) -> str:
        return self.http_response.headers.get(CLIENT_REQUEST_HEADER)

    @property
    def headers(self) -> httpx.Headers:
        return self.http_response.headers

    @property
    def http_request(self) -> httpx.Request:
        return self.http_response.request

    @property
    def status_code(self) -> int:
        return self.http_response.status_code

    @property
    def url(self) -> httpx.URL:
        return self.http_response.url

    @property
    def method(self) -> str:
        return self.http_request.method

    @property
    def http_version(self) -> str:
        return self.http_response.http_version

    @property
    def elapsed(self) -> datetime.timedelta:
        return self.http_response.elapsed

    @property
    def is_closed(self) -> bool:
        return self.http_response.is_closed

    @override
    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} [{self.status_code} {self.http_response.reason_phrase}] type={self._cast_to}>"

    def _parse(self) -> R:

        if self._is_sse_stream:
            if self._stream_cls is None:
                raise MissingStreamClassError()

            return cast(
                R,
                self._stream_cls(
                    cast_to=extract_type_arg(self._stream_cls),
                    response=self.http_response,
                    client=self._client,  # type: ignore
                ),
            )

        cast_to = self._cast_to
        if is_annotated_type(cast_to):
            cast_to = extract_type_arg(cast_to, 0)

        origin = get_origin(cast_to) or cast_to

        if (
            inspect.isclass(cast_to)
            and cast_to.__name__ == "HttpxBinaryResponseContent"
        ):
            return cast(R, cast_to(response))  # type: ignore

        if origin == ArkAPIResponse:
            raise RuntimeError("Unexpected state - cast_to is `ArkAPIResponse`")

        content_type, *_ = self.http_response.headers.get("content-type", "*").split(
            ";"
        )
        if content_type != "application/json":
            if cast_to is object:
                try:
                    data = self.http_response.json()
                except Exception as exc:
                    log.debug(
                        "Could not read JSON from response data due to %s - %s",
                        type(exc),
                        exc,
                    )
                else:
                    return cast(R, data)

            return response.text  # type: ignore

        data = self.http_response.json()

        return self._client._process_response_data(
            data=data,
            cast_to=cast_to,  # type: ignore
            response=self.http_response,
        )


class ArkAPIResponse(BaseAPIResponse[R]):
    @property
    def request_id(self) -> str:
        return self.http_response.headers.get(CLIENT_REQUEST_HEADER, "")

    def parse(self) -> R:
        if not self._is_sse_stream:
            self.read()
        return self._parse()

    def read(self) -> bytes:
        try:
            return self.http_response.read()
        except httpx.StreamConsumed as exc:
            raise StreamAlreadyConsumed() from exc

    def text(self) -> str:
        self.read()
        return self.http_response.text

    def json(self) -> object:
        self.read()
        return self.http_response.json()

    def close(self) -> None:
        self.http_response.close()

    def iter_bytes(self, chunk_size: int | None = None) -> Iterator[bytes]:
        for chunk in self.http_response.iter_bytes(chunk_size):
            yield chunk

    def iter_text(self, chunk_size: int | None = None) -> Iterator[str]:
        for chunk in self.http_response.iter_text(chunk_size):
            yield chunk

    def iter_lines(self) -> Iterator[str]:
        for chunk in self.http_response.iter_lines():
            yield chunk


class ArkAsyncAPIResponse(BaseAPIResponse[R]):
    @property
    def request_id(self) -> str:
        return self.http_response.headers.get(CLIENT_REQUEST_HEADER, "")

    async def parse(self) -> R:
        if not self._is_sse_stream:
            await self.read()

        return self._parse()

    async def read(self) -> bytes:
        try:
            return await self.http_response.aread()
        except httpx.StreamConsumed as exc:
            raise StreamAlreadyConsumed() from exc

    async def text(self) -> str:
        await self.read()
        return self.http_response.text

    async def json(self) -> object:
        await self.read()
        return self.http_response.json()

    async def close(self) -> None:
        await self.http_response.aclose()

    async def iter_bytes(self, chunk_size: int | None = None) -> AsyncIterator[bytes]:
        async for chunk in self.http_response.aiter_bytes(chunk_size):
            yield chunk

    async def iter_text(self, chunk_size: int | None = None) -> AsyncIterator[str]:
        async for chunk in self.http_response.aiter_text(chunk_size):
            yield chunk

    async def iter_lines(self) -> AsyncIterator[str]:
        """Like `iter_text()` but will only yield chunks for each line"""
        async for chunk in self.http_response.aiter_lines():
            yield chunk


class MissingStreamClassError(TypeError):
    def __init__(self) -> None:
        super().__init__(
            "The `stream` argument was set to `True` but the `stream_cls` argument was not given."
        )


class StreamAlreadyConsumed(ArkError):

    def __init__(self) -> None:
        message = (
            "Attempted to read or stream some content, but the content has "
            "already been streamed. "
            "This could be due to attempting to stream the response "
            "content more than once."
            "\n\n"
            "You can fix this by manually accumulating the response content while streaming "
            "or by calling `.read()` before starting to stream."
        )
        super().__init__(message)


def to_raw_response_wrapper(func: Callable[P, R]) -> Callable[P, ArkAPIResponse[R]]:
    """Higher order function that takes one of our bound API methods and wraps it
    to support returning the raw `APIResponse` object directly.
    """

    @functools.wraps(func)
    def wrapped(*args: P.args, **kwargs: P.kwargs) -> ArkAPIResponse[R]:
        extra_headers: dict[str, str] = {
            **(cast(Any, kwargs.get("extra_headers")) or {})
        }
        extra_headers[RAW_RESPONSE_HEADER] = "raw"

        kwargs["extra_headers"] = extra_headers

        return cast(ArkAPIResponse[R], func(*args, **kwargs))

    return wrapped


def async_to_raw_response_wrapper(
    func: Callable[P, Awaitable[R]]
) -> Callable[P, Awaitable[ArkAsyncAPIResponse[R]]]:
    """Higher order function that takes one of our bound API methods and wraps it
    to support returning the raw `APIResponse` object directly.
    """

    @functools.wraps(func)
    async def wrapped(*args: P.args, **kwargs: P.kwargs) -> ArkAsyncAPIResponse[R]:
        extra_headers: dict[str, str] = {
            **(cast(Any, kwargs.get("extra_headers")) or {})
        }
        extra_headers[RAW_RESPONSE_HEADER] = "raw"

        kwargs["extra_headers"] = extra_headers

        return cast(ArkAsyncAPIResponse[R], await func(*args, **kwargs))

    return wrapped


def to_streamed_response_wrapper(
    func: Callable[P, R]
) -> Callable[P, ResponseContextManager[ArkAPIResponse[R]]]:
    """Higher order function that takes one of our bound API methods and wraps it
    to support streaming and returning the raw `APIResponse` object directly.
    """

    @functools.wraps(func)
    def wrapped(
        *args: P.args, **kwargs: P.kwargs
    ) -> ResponseContextManager[ArkAPIResponse[R]]:
        extra_headers: dict[str, str] = {
            **(cast(Any, kwargs.get("extra_headers")) or {})
        }
        extra_headers[RAW_RESPONSE_HEADER] = "stream"

        kwargs["extra_headers"] = extra_headers

        make_request = functools.partial(func, *args, **kwargs)

        return ResponseContextManager(
            cast(Callable[[], ArkAPIResponse[R]], make_request)
        )

    return wrapped


def async_to_streamed_response_wrapper(
    func: Callable[P, Awaitable[R]],
) -> Callable[P, AsyncResponseContextManager[ArkAsyncAPIResponse[R]]]:
    """Higher order function that takes one of our bound API methods and wraps it
    to support streaming and returning the raw `APIResponse` object directly.
    """

    @functools.wraps(func)
    def wrapped(
        *args: P.args, **kwargs: P.kwargs
    ) -> AsyncResponseContextManager[ArkAsyncAPIResponse[R]]:
        extra_headers: dict[str, str] = {
            **(cast(Any, kwargs.get("extra_headers")) or {})
        }
        extra_headers[RAW_RESPONSE_HEADER] = "stream"

        kwargs["extra_headers"] = extra_headers

        make_request = func(*args, **kwargs)

        return AsyncResponseContextManager(
            cast(Awaitable[ArkAsyncAPIResponse[R]], make_request)
        )

    return wrapped


class ResponseContextManager(Generic[_APIResponseT]):
    """Context manager for ensuring that a request is not made
    until it is entered and that the response will always be closed
    when the context manager exits
    """

    def __init__(self, request_func: Callable[[], _APIResponseT]) -> None:
        self._request_func = request_func
        self.__response: _APIResponseT | None = None

    def __enter__(self) -> _APIResponseT:
        self.__response = self._request_func()
        return self.__response

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        if self.__response is not None:
            self.__response.close()


class AsyncResponseContextManager(Generic[_AsyncAPIResponseT]):
    """Context manager for ensuring that a request is not made
    until it is entered and that the response will always be closed
    when the context manager exits
    """

    def __init__(self, api_request: Awaitable[_AsyncAPIResponseT]) -> None:
        self._api_request = api_request
        self.__response: _AsyncAPIResponseT | None = None

    async def __aenter__(self) -> _AsyncAPIResponseT:
        self.__response = await self._api_request
        return self.__response

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        if self.__response is not None:
            await self.__response.close()
