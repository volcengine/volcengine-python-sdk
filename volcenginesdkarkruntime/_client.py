
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

from __future__ import annotations

import asyncio
import logging
import os
import threading
import time
from collections import defaultdict

from httpx import Timeout, URL, Client, AsyncClient
from typing import Dict, Tuple, Optional

from volcenginesdkcore.rest import ApiException
from ._exceptions import ArkAPIError
from ._models import BaseModel
import volcenginesdkark

from . import resources
from .resources.beta import beta
from .resources.batch import batch
from ._base_client import SyncAPIClient, AsyncAPIClient
from ._constants import (
    DEFAULT_MAX_RETRIES,
    BASE_URL,
    _DEFAULT_ADVISORY_REFRESH_TIMEOUT,
    _DEFAULT_MANDATORY_REFRESH_TIMEOUT,
    _DEFAULT_STS_TIMEOUT,
    _DEFAULT_RESOURCE_TYPE,
    DEFAULT_TIMEOUT,
)
from ._streaming import Stream

from ._utils._key_agreement import key_agreement_client
from ._utils._model_breaker import ModelBreaker

__all__ = ["Ark", "AsyncArk"]


class Ark(SyncAPIClient):
    beta: beta.Beta
    chat: resources.Chat
    bot_chat: resources.BotChat
    embeddings: resources.Embeddings
    tokenization: resources.Tokenization
    context: resources.Context
    multimodal_embeddings: resources.MultimodalEmbeddings
    content_generation: resources.ContentGeneration
    images: resources.Images
    batch_chat: resources.BatchChat
    responses: resources.Responses
    input_items: resources.InputItems
    """ `batch_chat` is deprecated, use `batch.chat` instead """
    batch: batch.Batch
    model_breaker_map: dict[str, ModelBreaker]
    model_breaker_lock: threading.Lock

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
        self._base_url = base_url
        self.ak = ak
        self.sk = sk
        self.api_key = api_key
        self.region = region

        assert (api_key is not None) or (ak is not None and sk is not None), (
            "you need to support api_key or ak&sk"
        )

        super().__init__(
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_query=None,
        )

        self._default_stream_cls = Stream
        self._sts_token_manager: StsTokenManager | None = None
        self._certificate_manager: E2ECertificateManager | None = None

        self.beta = beta.Beta(self)
        self.chat = resources.Chat(self)
        self.bot_chat = resources.BotChat(self)
        self.embeddings = resources.Embeddings(self)
        self.tokenization = resources.Tokenization(self)
        self.context = resources.Context(self)
        self.multimodal_embeddings = resources.MultimodalEmbeddings(self)
        self.content_generation = resources.ContentGeneration(self)
        self.images = resources.Images(self)
        self.batch_chat = resources.BatchChat(self)
        self.responses = resources.Responses(self)
        self.input_items = resources.InputItems(self)
        self.batch = batch.Batch(self)
        self.model_breaker_map = defaultdict(ModelBreaker)
        self.model_breaker_lock = threading.Lock()
        # self.classification = resources.Classification(self)

    def _get_endpoint_sts_token(self, endpoint_id: str):
        if self._sts_token_manager is None:
            if self.ak is None or self.sk is None:
                raise ArkAPIError("must set ak and sk before get endpoint token.")
            self._sts_token_manager = StsTokenManager(self.ak, self.sk, self.region)
        return self._sts_token_manager.get(endpoint_id)

    def _get_endpoint_certificate(self, endpoint_id: str) -> key_agreement_client:
        if self._certificate_manager is None:
            cert_path = os.environ.get("E2E_CERTIFICATE_PATH")
            if (
                (self.ak is None or self.sk is None)
                and cert_path is None
                and self.api_key is None
            ):
                raise ArkAPIError(
                    "must set (api_key) or (ak and sk) \
                                  or (E2E_CERTIFICATE_PATH) before get endpoint token."
                )
            self._certificate_manager = E2ECertificateManager(
                self.ak, self.sk, self.region, self._base_url, self.api_key
            )
        return self._certificate_manager.get(endpoint_id)

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

    def get_model_breaker(self, model_name: str) -> ModelBreaker:
        with self.model_breaker_lock:
            return self.model_breaker_map[model_name]


class AsyncArk(AsyncAPIClient):
    beta: beta.AsyncBeta
    chat: resources.AsyncChat
    bot_chat: resources.AsyncBotChat
    embeddings: resources.AsyncEmbeddings
    tokenization: resources.AsyncTokenization
    context: resources.AsyncContext
    multimodal_embeddings: resources.AsyncMultimodalEmbeddings
    content_generation: resources.AsyncContentGeneration
    images: resources.AsyncImages
    batch_chat: resources.AsyncBatchChat
    responses: resources.AsyncResponses
    input_items: resources.AsyncInputItems
    """ `batch_chat` is deprecated, use `batch.chat` instead """
    batch: batch.AsyncBatch
    model_breaker_map: dict[str, ModelBreaker]
    model_breaker_lock: asyncio.Lock

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
        self._base_url = base_url
        self.ak = ak
        self.sk = sk
        self.api_key = api_key
        self.region = region

        assert (api_key is not None) or (ak is not None and sk is not None), (
            "you need to support api_key or ak&sk"
        )

        super().__init__(
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_query=None,
        )

        self._default_stream_cls = Stream
        self._sts_token_manager: StsTokenManager | None = None
        self._certificate_manager: E2ECertificateManager | None = None

        self.beta = beta.AsyncBeta(self)
        self.chat = resources.AsyncChat(self)
        self.bot_chat = resources.AsyncBotChat(self)
        self.embeddings = resources.AsyncEmbeddings(self)
        self.tokenization = resources.AsyncTokenization(self)
        self.context = resources.AsyncContext(self)
        self.multimodal_embeddings = resources.AsyncMultimodalEmbeddings(self)
        self.content_generation = resources.AsyncContentGeneration(self)
        self.images = resources.AsyncImages(self)
        self.batch_chat = resources.AsyncBatchChat(self)
        self.responses = resources.AsyncResponses(self)
        self.input_items = resources.AsyncInputItems(self)
        self.batch = batch.AsyncBatch(self)
        self.model_breaker_map = defaultdict(ModelBreaker)
        self.model_breaker_lock = asyncio.Lock()
        # self.classification = resources.AsyncClassification(self)

    def _get_endpoint_sts_token(self, endpoint_id: str):
        if self._sts_token_manager is None:
            if self.ak is None or self.sk is None:
                raise ArkAPIError("must set ak and sk before get endpoint token.")
            self._sts_token_manager = StsTokenManager(self.ak, self.sk, self.region)
        return self._sts_token_manager.get(endpoint_id)

    def _get_bot_sts_token(self, bot_id: str):
        if self._sts_token_manager is None:
            if self.ak is None or self.sk is None:
                raise ArkAPIError("must set ak and sk before get endpoint token.")
            self._sts_token_manager = StsTokenManager(self.ak, self.sk, self.region)
        return self._sts_token_manager.get(bot_id, resource_type="bot")

    def _get_endpoint_certificate(self, endpoint_id: str) -> key_agreement_client:
        if self._certificate_manager is None:
            cert_path = os.environ.get("E2E_CERTIFICATE_PATH")
            if (
                (self.ak is None or self.sk is None)
                and cert_path is None
                and self.api_key is None
            ):
                raise ArkAPIError(
                    "must set (api_key) or (ak and sk) \
                                  or (E2E_CERTIFICATE_PATH) before get endpoint token."
                )
            self._certificate_manager = E2ECertificateManager(
                self.ak, self.sk, self.region, self._base_url, self.api_key
            )
        return self._certificate_manager.get(endpoint_id)

    @property
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    async def get_model_breaker(self, model_name: str) -> ModelBreaker:
        async with self.model_breaker_lock:
            return self.model_breaker_map[model_name]


class StsTokenManager(object):
    # The time at which we'll attempt to refresh, but not
    # block if someone else is refreshing.
    _advisory_refresh_timeout: int = _DEFAULT_ADVISORY_REFRESH_TIMEOUT
    # The time at which all threads will block waiting for
    # refreshed credentials.
    _mandatory_refresh_timeout: int = _DEFAULT_MANDATORY_REFRESH_TIMEOUT

    def __init__(self, ak: str, sk: str, region: str):
        self._endpoint_sts_tokens: Dict[str, Tuple[str, int]] = defaultdict(
            lambda: ("", 0)
        )
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

    def _protected_refresh(
        self,
        ep: str,
        ttl: int = _DEFAULT_STS_TIMEOUT,
        is_mandatory: bool = False,
        resource_type: str = _DEFAULT_RESOURCE_TYPE,
    ):
        if ttl < self._advisory_refresh_timeout * 2:
            raise ArkAPIError(
                "ttl should not be under {} seconds.".format(
                    self._advisory_refresh_timeout * 2
                )
            )

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

                self._protected_refresh(
                    ep, is_mandatory=is_mandatory_refresh, resource_type=resource_type
                )
                return
            finally:
                self._refresh_lock.release()
        elif self._need_refresh(ep, self._mandatory_refresh_timeout):
            with self._refresh_lock:
                if not self._need_refresh(ep, self._mandatory_refresh_timeout):
                    return

                self._protected_refresh(
                    ep, is_mandatory=True, resource_type=resource_type
                )

    def get(self, ep: str, resource_type: str = _DEFAULT_RESOURCE_TYPE) -> str:
        self._refresh(ep, resource_type=resource_type)
        return self._endpoint_sts_tokens[ep][0]

    def _load_api_key(
        self,
        ep: str,
        duration_seconds: int,
        resource_type: str = _DEFAULT_RESOURCE_TYPE,
    ) -> Tuple[str, int]:
        get_api_key_request = volcenginesdkark.GetApiKeyRequest(
            duration_seconds=duration_seconds,
            resource_type=resource_type,
            resource_ids=[ep],
        )
        resp: volcenginesdkark.GetApiKeyResponse = self.api_instance.get_api_key(
            get_api_key_request
        )

        return resp.api_key, resp.expired_time


class CertificateResponse(BaseModel):
    error: Optional[Dict[str, str]] = None
    """The error information."""

    Certificate: str
    """The certificate content."""


class E2ECertificateManager(object):
    def __init__(
        self,
        ak: str,
        sk: str,
        region: str,
        base_url: str | URL = BASE_URL,
        api_key: str | None = None,
    ):
        self._certificate_manager: Dict[str, key_agreement_client] = {}

        # local cache prepare
        self._init_local_cert_cache()

        # api instance prepare
        import volcenginesdkcore

        configuration = volcenginesdkcore.Configuration()
        configuration.ak = ak
        configuration.sk = sk
        configuration.region = region
        configuration.schema = "https"
        volcenginesdkcore.Configuration.set_default(configuration)
        self.api_instance = volcenginesdkark.ARKApi()

        # global cert path prepare
        self.cert_path = os.environ.get("E2E_CERTIFICATE_PATH")

        # ark client prepare
        self._ark_client_enabled = True
        if api_key is None:
            self._ark_client_enabled = False
        else:
            self.client = Ark(
                base_url=base_url,
                api_key=api_key,
            )
        self._e2e_uri = "/e2e/get/certificate"
        self._x_session_token = {"X-Session-Token": self._e2e_uri}

    def _load_cert_by_cert_path(self) -> str:
        with open(self.cert_path, "r") as f:
            cert_pem = f.read()
        return cert_pem

    def _load_cert_by_ak_sk(self, ep: str) -> str:
        get_endpoint_certificate_request = (
            volcenginesdkark.GetEndpointCertificateRequest(id=ep)
        )
        try:
            resp: volcenginesdkark.GetEndpointCertificateResponse = (
                self.api_instance.get_endpoint_certificate(
                    get_endpoint_certificate_request
                )
            )
        except ApiException as e:
            raise ArkAPIError(
                "Getting model vendor encryption certificate failed: %s\n" % e
            )

        return resp.pca_instance_certificate

    def _sync_load_cert_by_auth(self, ep: str) -> str:
        try:  # try to make request with session header (used for header statistic)
            resp = self.client.post(
                self._e2e_uri,
                options={"headers": self._x_session_token},
                body={"model": ep},
                cast_to=CertificateResponse,
            )
        except Exception as e:
            raise ArkAPIError("Getting Certificate failed: %s\n" % e)
        if resp.error is not None:
            raise ArkAPIError("Getting Certificate failed: %s\n" % resp.error)
        return resp.Certificate

    def _save_cert_to_file(self, ep: str, cert_pem: str):
        cert_file_path = os.path.join(self._cert_storage_path, f"{ep}.pem")
        with open(cert_file_path, "w") as f:
            f.write(cert_pem)

    def _load_cert_locally(self, ep: str) -> str | None:
        cert_file_path = os.path.join(self._cert_storage_path, f"{ep}.pem")
        if os.path.exists(cert_file_path):
            last_modified_time = os.path.getmtime(cert_file_path)
            current_time = time.time()
            time_difference = current_time - last_modified_time
            if time_difference <= self._cert_expiration_seconds:
                with open(cert_file_path, "r") as f:
                    return f.read()
            else:
                os.remove(cert_file_path)
        return None

    def _init_local_cert_cache(self):
        self._cert_storage_path = "/tmp/ark/certificates"
        self._cert_expiration_seconds = 14 * 24 * 60 * 60  # 14 days

        if not os.path.exists(self._cert_storage_path):
            try:
                os.makedirs(self._cert_storage_path)
            except FileExistsError:
                pass
            except Exception as e:
                raise ArkAPIError(
                    "failed to create certificate directory %s: %s\n" % (self._cert_storage_path, e)
                )

    def get(self, ep: str) -> key_agreement_client:
        if ep not in self._certificate_manager:
            cert_pem = self._load_cert_locally(ep)
            if cert_pem is None:
                if self.cert_path is not None:
                    cert_pem = self._load_cert_by_cert_path()
                elif self._ark_client_enabled:
                    cert_pem = self._sync_load_cert_by_auth(ep)
                else:
                    cert_pem = self._load_cert_by_ak_sk(ep)
                self._save_cert_to_file(ep, cert_pem)
            self._certificate_manager[ep] = key_agreement_client(
                certificate_pem_string=cert_pem
            )
        return self._certificate_manager[ep]
