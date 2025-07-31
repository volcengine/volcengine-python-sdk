from __future__ import annotations

from ..._compat import cached_property
from ..._resource import AsyncAPIResource, SyncAPIResource
from .chat.chat import AsyncChat, Chat
from .embeddings import AsyncEmbeddings, Embeddings

__all__ = ["Batch", "AsyncBatch"]


class Batch(SyncAPIResource):
    @cached_property
    def chat(self) -> Chat:
        return Chat(self._client)

    @cached_property
    def embeddings(self) -> Embeddings:
        return Embeddings(self._client)


class AsyncBatch(AsyncAPIResource):
    @cached_property
    def chat(self) -> AsyncChat:
        return AsyncChat(self._client)

    @cached_property
    def embeddings(self) -> AsyncEmbeddings:
        return AsyncEmbeddings(self._client)
