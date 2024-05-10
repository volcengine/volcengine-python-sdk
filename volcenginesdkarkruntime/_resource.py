from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._client import Ark, AsyncArk


class SyncAPIResource:
    _client: "Ark"

    def __init__(self, client: "Ark") -> None:
        self._client = client
        self._post = client.post


class AsyncAPIResource:
    _client: "AsyncArk"

    def __init__(self, client: "AsyncArk") -> None:
        self._client = client
        self._post = client.post
