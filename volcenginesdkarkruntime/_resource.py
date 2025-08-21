
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

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._client import Ark, AsyncArk


class SyncAPIResource:
    _client: "Ark"

    def __init__(self, client: "Ark") -> None:
        self._client = client
        self._post = client.post
        self._get = client.get
        self._delete = client.delete
        self._post_without_retry = client.post_without_retry
        self._get_api_list = client.get_api_list


class AsyncAPIResource:
    _client: "AsyncArk"

    def __init__(self, client: "AsyncArk") -> None:
        self._client = client
        self._post = client.post
        self._get = client.get
        self._delete = client.delete
        self._post_without_retry = client.post_without_retry
        self._get_api_list = client.get_api_list
