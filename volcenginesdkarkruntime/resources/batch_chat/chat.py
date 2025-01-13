# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .completions import Completions, AsyncCompletions
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["BatchChat", "AsyncBatchChat"]


class BatchChat(SyncAPIResource):
    @cached_property
    def completions(self) -> Completions:
        return Completions(self._client)


class AsyncBatchChat(AsyncAPIResource):
    @cached_property
    def completions(self) -> AsyncCompletions:
        return AsyncCompletions(self._client)
