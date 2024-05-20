from __future__ import annotations

import logging
import os
import threading
import time
from collections import defaultdict

from httpx import Timeout, URL, Client, AsyncClient
from typing import Dict, Tuple

from volcenginesdkcore.rest import ApiException
from ._exceptions import ArkAPIError

import volcenginesdkark

from . import resources
from ._base_client import SyncAPIClient, AsyncAPIClient
from ._constants import (
    DEFAULT_MAX_RETRIES,
    BASE_URL,
    _DEFAULT_ADVISORY_REFRESH_TIMEOUT,
    _DEFAULT_MANDATORY_REFRESH_TIMEOUT,
    _DEFAULT_STS_TIMEOUT,
    DEFAULT_TIMEOUT
)
from ._streaming import Stream

__all__ = ["Ark", "AsyncArk"]


class Ark(SyncAPIClient):
    chat: resources.Chat

    def __init__(
        self,
        *,
        base_url: str | URL = BASE_URL,
        ak: str | None = None,
        sk: str | None = None,
        timeout: float | Timeout | None = DEFAULT_TIMEOUT,
        max_retries: int = DEFAULT_MAX_RETRIES,
        http_client: Client | None = None,
    ) -> None:
        """init ark client, this client is thread unsafe. If need to use in multi thread, init a new `Ark` client in
        each thread

            Args:
                ak: access key id
                sk: secret access key
                timeout: timeout of client. default httpx.Timeout(timeout=60.0, connect=60.0)
                max_retries: times of retry when request failed. default 1
                http_client: specify customized http_client
            Returns:
                ark client
        """

        if ak is None:
            ak = os.environ.get("VOLC_ACCESSKEY")
        if sk is None:
            sk = os.environ.get("VOLC_SECRETKEY")
        self.ak = ak
        self.sk = sk

        super().__init__(
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_query=None,
        )

        self._default_stream_cls = Stream
        self._sts_token_manager: StsTokenManager | None = None

        self.chat = resources.Chat(self)

    def _get_endpoint_sts_token(self, endpoint_id: str):
        if self._sts_token_manager is None:
            if self.ak is None or self.sk is None:
                raise ArkAPIError("must set ak and sk before get endpoint token.")
            self._sts_token_manager = StsTokenManager(self.ak, self.sk)
        return self._sts_token_manager.get(endpoint_id)


class AsyncArk(AsyncAPIClient):
    chat: resources.AsyncChat

    def __init__(
        self,
        *,
        ak: str | None = None,
        sk: str | None = None,
        base_url: str | URL = BASE_URL,
        timeout: float | Timeout | None = DEFAULT_TIMEOUT,
        max_retries: int = DEFAULT_MAX_RETRIES,
        http_client: AsyncClient | None = None,
    ) -> None:
        """init async ark client, this client is thread unsafe

            Args:
                ak: access key id
                sk: secret access key
                timeout: timeout of client. default httpx.Timeout(timeout=60.0, connect=60.0)
                max_retries: times of retry when request failed. default 1
                http_client: specify customized http_client
            Returns:
                async ark client
        """

        if ak is None:
            ak = os.environ.get("VOLC_ACCESSKEY")
        if sk is None:
            sk = os.environ.get("VOLC_SECRETKEY")
        self.ak = ak
        self.sk = sk

        super().__init__(
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_query=None,
        )

        self._default_stream_cls = Stream
        self._sts_token_manager: StsTokenManager | None = None

        self.chat = resources.AsyncChat(self)

    def _get_endpoint_sts_token(self, endpoint_id: str):
        if self._sts_token_manager is None:
            if self.ak is None or self.sk is None:
                raise ArkAPIError("must set ak and sk before get endpoint token.")
            self._sts_token_manager = StsTokenManager(self.ak, self.sk)
        return self._sts_token_manager.get(endpoint_id)


class StsTokenManager(object):

    # The time at which we'll attempt to refresh, but not
    # block if someone else is refreshing.
    _advisory_refresh_timeout: int = _DEFAULT_ADVISORY_REFRESH_TIMEOUT
    # The time at which all threads will block waiting for
    # refreshed credentials.
    _mandatory_refresh_timeout: int = _DEFAULT_MANDATORY_REFRESH_TIMEOUT

    def __init__(self, ak: str, sk: str):
        self._endpoint_sts_tokens: Dict[str, Tuple[str, int]] = defaultdict(lambda: ("", 0))
        self._refresh_lock = threading.Lock()

        import volcenginesdkcore

        configuration = volcenginesdkcore.Configuration()
        configuration.ak = ak
        configuration.sk = sk
        configuration.region = "cn-beijing"

        volcenginesdkcore.Configuration.set_default(configuration)
        self.api_instance = volcenginesdkark.ARKApi()

    def _need_refresh(self, ep: str, refresh_in: int | None = None) -> bool:
        if refresh_in is None:
            refresh_in = self._advisory_refresh_timeout

        return self._endpoint_sts_tokens[ep][1] - time.time() < refresh_in

    def _protected_refresh(self, ep: str, ttl: int = _DEFAULT_STS_TIMEOUT, is_mandatory: bool = False):
        if ttl < _DEFAULT_ADVISORY_REFRESH_TIMEOUT * 2:
            raise ArkAPIError("ttl should not be under {} seconds.".format(_DEFAULT_ADVISORY_REFRESH_TIMEOUT * 2))

        try:
            api_key, expired_time = self._load_api_key(
                ep, ttl
            )
            self._endpoint_sts_tokens[ep] = (api_key, expired_time)
        except ApiException as e:
            if is_mandatory:
                raise ArkAPIError("load api key cause error: e={}".format(e))
            else:
                logging.error("load api key cause error: e={}".format(e))

    def _refresh(self, ep: str):
        if not self._need_refresh(ep, self._advisory_refresh_timeout):
            return

        if self._refresh_lock.acquire(False):
            if not self._need_refresh(ep, self._advisory_refresh_timeout):
                return

            try:
                is_mandatory_refresh = self._need_refresh(
                    ep, self._mandatory_refresh_timeout
                )

                self._protected_refresh(ep, is_mandatory=is_mandatory_refresh)
                return
            finally:
                self._refresh_lock.release()
        elif self._need_refresh(ep, self._mandatory_refresh_timeout):
            with self._refresh_lock:
                if not self._need_refresh(ep, self._mandatory_refresh_timeout):
                    return

                self._protected_refresh(ep, is_mandatory=True)

    def get(self, ep: str) -> str:
        self._refresh(ep)
        return self._endpoint_sts_tokens[ep][0]

    def _load_api_key(self, ep: str, duration_seconds: int) -> Tuple[str, int]:
        get_api_key_request = volcenginesdkark.GetApiKeyRequest(
            duration_seconds=duration_seconds,
            resource_type="endpoint",
            resource_ids=[ep],
        )
        resp: volcenginesdkark.GetApiKeyResponse = self.api_instance.get_api_key(
            get_api_key_request
        )

        return resp.api_key, resp.expired_time