# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from functools import cache

from .completions import Completions, AsyncCompletions
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["Chat", "AsyncChat"]


class Chat(SyncAPIResource):
    @property
    @cache
    def completions(self) -> Completions:
        return Completions(self._client)


class AsyncChat(AsyncAPIResource):
    @property
    @cache
    def completions(self) -> AsyncCompletions:
        return AsyncCompletions(self._client)
