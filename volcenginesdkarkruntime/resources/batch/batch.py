from __future__ import annotations

from ..._compat import cached_property
from .chat.chat import Chat, AsyncChat
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["Batch", "AsyncBatch"]


class Batch(SyncAPIResource):
    @cached_property
    def chat(self) -> Chat:
        return Chat(self._client)


class AsyncBatch(AsyncAPIResource):
    @cached_property
    def chat(self) -> AsyncChat:
        return AsyncChat(self._client)
