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
    _DEFAULT_RESOURCE_TYPE,
    DEFAULT_TIMEOUT
)
from ._streaming import Stream

from ._utils._key_agreement import key_agreement_client

__all__ = ["Ark", "AsyncArk"]


class Ark(SyncAPIClient):
    chat: resources.Chat
    bot_chat: resources.BotChat
    embeddings: resources.Embeddings
    tokenization: resources.Tokenization

    def __init__(
        self,
        *,
        base_url: str | URL = BASE_URL,
        ak: str | None = None,
        sk: str | None = None,
        api_key: str | None = None,
        region: str = "cn-beijing",
        timeout: float | Timeout | None = DEFAULT_TIMEOUT,
        max_retries: int = DEFAULT_MAX_RETRIES,
        http_client: Client | None = None,
    ) -> None:
        """init ark client, this client is thread unsafe. If need to use in multi thread, init a new `Ark` client in
        each thread

            Args:
                ak: access key id
                sk: secret access key
                api_key: api key，this api key will not be refreshed
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
        if api_key is None:
            api_key = os.environ.get("ARK_API_KEY")
        self.ak = ak
        self.sk = sk
        self.api_key = api_key
        self.region = region

        assert (api_key is not None) or (ak is not None and sk is not None), "you need to support api_key or ak&sk"

        super().__init__(
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_query=None,
        )

        self._default_stream_cls = Stream
        self._sts_token_manager: StsTokenManager | None = None
        self._certificate_manager: Dict[str, key_agreement_client] | None = None

        self.chat = resources.Chat(self)
        self.bot_chat = resources.BotChat(self)
        self.embeddings = resources.Embeddings(self)
        self.tokenization = resources.Tokenization(self)
        # self.classification = resources.Classification(self)

    def _get_endpoint_sts_token(self, endpoint_id: str):
        if self._sts_token_manager is None:
            if self.ak is None or self.sk is None:
                raise ArkAPIError("must set ak and sk before get endpoint token.")
            self._sts_token_manager = StsTokenManager(self.ak, self.sk, self.region)
        return self._sts_token_manager.get(endpoint_id)

    def _get_endpoint_certificate(self, endpoint_id: str) -> key_agreement_client:
        seed_pem = """-----BEGIN CERTIFICATE-----
MIICxjCCAm2gAwIBAgIUG8YxEzdBJnYjBEYSc1j2diJ8/uMwCgYIKoZIzj0EAwIw
gYQxITAfBgNVBAMMGE1hYVMgU0RLIFN1YiBDQSBFQ0MgUDI1NjEbMBkGA1UECgwS
Vm9sY2FubyBFbmdpbmUgQXJrMREwDwYDVQQLDAhTZWN1cml0eTELMAkGA1UEBhMC
Q04xEDAOBgNVBAgMB0JlaWppbmcxEDAOBgNVBAcMB0JlaWppbmcwHhcNMjQwMTAz
MDY1MjM4WhcNMjkwMTAzMDY1MjM4WjCBgjELMAkGA1UEBhMCQ04xEDAOBgNVBAgT
B0JlaWppbmcxEDAOBgNVBAcTB0JlaWppbmcxGzAZBgNVBAoTElZvbGNhbm8gRW5n
aW5lIEFyazERMA8GA1UECxMIU2VjdXJpdHkxHzAdBgNVBAMTFk1hYVMgQ3J5cHRv
IFNESyBPbmxpbmUwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNCAATD7RyZC51FCwuK
xYKh2ZCwIvbNDvQfosUk3gKc0B/+euemDWDAaVazuBOm8okHsSmUrsEudeksRruG
LTGu1lBxo4G8MIG5MA4GA1UdDwEB/wQEAwIDiDBYBgNVHR8EUTBPME2gS6BJhkdo
dHRwOi8vY3JsLnZvbGNjYS5jb20vdm9sYzE/c249NURCNEUwNDNFRjQ3MEY3RDBB
REU0RDIyMTNBNTU1NTEzMjEyOEM3MzA4BggrBgEFBQcBAQQsMCowKAYIKwYBBQUH
MAGGHGh0dHA6Ly9vY3NwLnZvbGNjYS5jb20vdm9sYzEwEwYDVR0lBAwwCgYIKwYB
BQUHAwEwCgYIKoZIzj0EAwIDRwAwRAIgFSel9WBkyPmpdG6YzReb7ShCVKq3scT3
9T2mfBgooPkCIHpRalKvIJX5S9oSyTf6iQiUcwzfUHd47Ew+PUV7O6aq
-----END CERTIFICATE-----"""
        if self._certificate_manager is None:
            self._certificate_manager = {}
        if endpoint_id not in self._certificate_manager:
            if self.ak is None or self.sk is None:
                raise ArkAPIError("must set ak and sk before get endpoint token.")
            self._certificate_manager[endpoint_id] = key_agreement_client(
                certificate_pem_string=seed_pem
            )
        return self._certificate_manager[endpoint_id]

    def _get_bot_sts_token(self, bot_id: str):
        if self._sts_token_manager is None:
            if self.ak is None or self.sk is None:
                raise ArkAPIError("must set ak and sk before get endpoint token.")
            self._sts_token_manager = StsTokenManager(self.ak, self.sk, self.region)
        return self._sts_token_manager.get(bot_id, resource_type="bot")

    @property
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}


class AsyncArk(AsyncAPIClient):
    chat: resources.AsyncChat
    bot_chat: resources.AsyncBotChat
    embeddings: resources.AsyncEmbeddings
    tokenization: resources.AsyncTokenization

    def __init__(
        self,
        *,
        ak: str | None = None,
        sk: str | None = None,
        api_key: str | None = None,
        base_url: str | URL = BASE_URL,
        region: str = "cn-beijing",
        timeout: float | Timeout | None = DEFAULT_TIMEOUT,
        max_retries: int = DEFAULT_MAX_RETRIES,
        http_client: AsyncClient | None = None,
    ) -> None:
        """init async ark client, this client is thread unsafe

            Args:
                ak: access key id
                sk: secret access key
                api_key: api key，this api key will not be refreshed
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
        if api_key is None:
            api_key = os.environ.get("ARK_API_KEY")
        self.ak = ak
        self.sk = sk
        self.api_key = api_key
        self.region = region

        assert (api_key is not None) or (ak is not None and sk is not None), "you need to support api_key or ak&sk"

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
        self.bot_chat = resources.AsyncBotChat(self)
        self.embeddings = resources.AsyncEmbeddings(self)
        self.tokenization = resources.AsyncTokenization(self)
        # self.classification = resources.AsyncClassification(self)

    def _get_endpoint_sts_token(self, endpoint_id: str):
        if self._sts_token_manager is None:
            if self.ak is None or self.sk is None:
                raise ArkAPIError("must set ak and sk before get endpoint token.")
            self._sts_token_manager = StsTokenManager(self.ak, self.sk, self.region)
        return self._sts_token_manager.get(endpoint_id)

    @property
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}


class StsTokenManager(object):
    # The time at which we'll attempt to refresh, but not
    # block if someone else is refreshing.
    _advisory_refresh_timeout: int = _DEFAULT_ADVISORY_REFRESH_TIMEOUT
    # The time at which all threads will block waiting for
    # refreshed credentials.
    _mandatory_refresh_timeout: int = _DEFAULT_MANDATORY_REFRESH_TIMEOUT

    def __init__(self, ak: str, sk: str, region: str):
        self._endpoint_sts_tokens: Dict[str, Tuple[str, int]] = defaultdict(lambda: ("", 0))
        self._refresh_lock = threading.Lock()

        import volcenginesdkcore

        configuration = volcenginesdkcore.Configuration()
        configuration.ak = ak
        configuration.sk = sk
        configuration.region = region
        configuration.schema = "https"

        volcenginesdkcore.Configuration.set_default(configuration)
        self.api_instance = volcenginesdkark.ARKApi()

    def _need_refresh(self, ep: str, refresh_in: int | None = None) -> bool:
        if refresh_in is None:
            refresh_in = self._advisory_refresh_timeout

        return self._endpoint_sts_tokens[ep][1] - time.time() < refresh_in

    def _protected_refresh(self, ep: str, ttl: int = _DEFAULT_STS_TIMEOUT, is_mandatory: bool = False,
                           resource_type: str = _DEFAULT_RESOURCE_TYPE):
        if ttl < self._advisory_refresh_timeout * 2:
            raise ArkAPIError("ttl should not be under {} seconds.".format(self._advisory_refresh_timeout * 2))

        try:
            api_key, expired_time = self._load_api_key(
                ep, ttl, resource_type=resource_type
            )
            self._endpoint_sts_tokens[ep] = (api_key, expired_time)
        except ApiException as e:
            if is_mandatory:
                raise ArkAPIError("load api key cause error: e={}".format(e))
            else:
                logging.error("load api key cause error: e={}".format(e))

    def _refresh(self, ep: str, resource_type: str = _DEFAULT_RESOURCE_TYPE):
        if not self._need_refresh(ep, self._advisory_refresh_timeout):
            return

        if self._refresh_lock.acquire(False):
            if not self._need_refresh(ep, self._advisory_refresh_timeout):
                return

            try:
                is_mandatory_refresh = self._need_refresh(
                    ep, self._mandatory_refresh_timeout
                )

                self._protected_refresh(ep, is_mandatory=is_mandatory_refresh, resource_type=resource_type)
                return
            finally:
                self._refresh_lock.release()
        elif self._need_refresh(ep, self._mandatory_refresh_timeout):
            with self._refresh_lock:
                if not self._need_refresh(ep, self._mandatory_refresh_timeout):
                    return

                self._protected_refresh(ep, is_mandatory=True, resource_type=resource_type)

    def get(self, ep: str, resource_type: str = _DEFAULT_RESOURCE_TYPE) -> str:
        self._refresh(ep, resource_type=resource_type)
        return self._endpoint_sts_tokens[ep][0]

    def _load_api_key(self, ep: str, duration_seconds: int,
                      resource_type: str = _DEFAULT_RESOURCE_TYPE) -> Tuple[str, int]:
        get_api_key_request = volcenginesdkark.GetApiKeyRequest(
            duration_seconds=duration_seconds,
            resource_type=resource_type,
            resource_ids=[ep],
        )
        resp: volcenginesdkark.GetApiKeyResponse = self.api_instance.get_api_key(
            get_api_key_request
        )

        return resp.api_key, resp.expired_time
