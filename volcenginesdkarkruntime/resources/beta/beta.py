from __future__ import annotations

from ..._compat import cached_property
from .chat.chat import Chat, AsyncChat
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["Beta", "AsyncBeta"]


class Beta(SyncAPIResource):
    @cached_property
    def chat(self) -> Chat:
        return Chat(self._client)

    @cached_property
    def with_raw_response(self) -> BetaWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.
        """
        return BetaWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BetaWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.
        """
        return BetaWithStreamingResponse(self)


class AsyncBeta(AsyncAPIResource):
    @cached_property
    def chat(self) -> AsyncChat:
        return AsyncChat(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBetaWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.
        """
        return AsyncBetaWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBetaWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.
        """
        return AsyncBetaWithStreamingResponse(self)


class BetaWithRawResponse:
    def __init__(self, beta: Beta) -> None:
        self._beta = beta


class AsyncBetaWithRawResponse:
    def __init__(self, beta: AsyncBeta) -> None:
        self._beta = beta


class BetaWithStreamingResponse:
    def __init__(self, beta: Beta) -> None:
        self._beta = beta


class AsyncBetaWithStreamingResponse:
    def __init__(self, beta: AsyncBeta) -> None:
        self._beta = beta
