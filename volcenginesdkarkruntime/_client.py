from __future__ import annotations

import os
from typing import Dict

import httpx
from httpx import Timeout, URL

from . import resources, _exceptions
from ._base_client import SyncAPIClient, AsyncAPIClient
from ._constants import DEFAULT_MAX_RETRIES, BASE_URL
from ._exceptions import ArkError, ArkAPIStatusError
from ._streaming import Stream

__all__ = ["Ark", "AsyncArk"]


class Ark(SyncAPIClient):
    chat: resources.Chat

    def __init__(
        self,
        *,
        base_url: str | URL = BASE_URL,
        api_key: str | None = None,
        timeout: float | Timeout | None = None,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_query: Dict[str, object] | None = None,
        http_client: httpx.Client | None = None,
    ) -> None:
        if api_key is None:
            api_key = os.environ.get("ARK_API_KEY")
        self.api_key = api_key

        super().__init__(
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_query=default_query,
        )

        self._default_stream_cls = Stream

        self.chat = resources.Chat(self)

    @property
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}


class AsyncArk(AsyncAPIClient):
    chat: resources.AsyncChat

    def __init__(
        self,
        *,
        base_url: str | URL = BASE_URL,
        api_key: str | None = None,
        timeout: float | Timeout | None = None,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_query: Dict[str, object] | None = None,
        http_client: httpx.Client | None = None,
    ) -> None:
        if api_key is None:
            api_key = os.environ.get("ARK_API_KEY")
        self.api_key = api_key

        super().__init__(
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_query=default_query,
        )

        self._default_stream_cls = Stream

        self.chat = resources.AsyncChat(self)


    @property
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}
