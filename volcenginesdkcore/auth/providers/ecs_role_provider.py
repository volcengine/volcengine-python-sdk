# coding=utf-8
import json
import logging
import os
import threading
import time
from datetime import datetime

import dateutil.parser
import dateutil.tz

from .provider import Provider, CredentialValue

logger = logging.getLogger(__name__)

# ECS IMDSv2 endpoint and protocol
_IMDS_ENDPOINT = "http://100.96.0.96"
_IMDS_CREDENTIALS_PATH = "/volcstack/latest/iam/security_credentials/{role_name}"  # POST
_IMDS_ROLE_NAME_PATH = "/volcstack/latest/iam/security_credentials?type=user"  # GET
_IMDS_TOKEN_PATH = "/latest/api/token"  # GET

# ECS IMDSv2 headers
_IMDS_TOKEN_TTL_HEADER = "X-volc-ecs-metadata-token-ttl-seconds"
_IMDS_TOKEN_HEADER = "X-volc-ecs-metadata-token"
_IMDS_TOKEN_TTL_SECONDS = "21600"  # 6 hours

# ECS IMDSv2 response field names
_FIELD_AK = "AccessKeyId"
_FIELD_SK = "SecretAccessKey"
_FIELD_TOKEN = "SessionToken"
_FIELD_EXPIRATION = "ExpiredTime"


class EcsRoleCredentialProvider(Provider):
    """Obtains temporary credentials from the ECS Instance Metadata Service (IMDSv2).

    Flow:
      1. GET token from IMDSv2 (every time, no cache)
      2. Resolve roleName: param > env > auto-detect from IMDS
      3. POST to get STS credentials with token header

    roleName priority: constructor param > VOLCENGINE_ECS_METADATA env > auto-detect from IMDS.
    Disabled when VOLCENGINE_ECS_METADATA_DISABLED=true.
    """

    PROVIDER_NAME = "EcsRoleCredentialProvider"

    def __init__(self, role_name=None, connect_timeout=1, read_timeout=1,
                 max_retries=3, retry_interval=1, expired_buffer_seconds=300):
        if os.environ.get("VOLCENGINE_ECS_METADATA_DISABLED", "").lower() == "true":
            raise ValueError(
                "{}: IMDS credentials are disabled via "
                "VOLCENGINE_ECS_METADATA_DISABLED=true.".format(self.PROVIDER_NAME)
            )

        self._role_name = role_name
        self._connect_timeout = connect_timeout
        self._read_timeout = read_timeout
        self._max_retries = max(max_retries, 1)
        self._retry_interval = retry_interval
        self._expired_buffer_seconds = expired_buffer_seconds

        self._credentials = None
        self._expired_time = None
        self._lock = threading.Lock()

    def retrieve(self):
        return self._credentials

    def is_expired(self):
        return (self._credentials is None or
                (self._expired_time is not None
                 and self._expired_time < time.time() + self._expired_buffer_seconds))

    def refresh(self):
        with self._lock:
            if self.is_expired():
                self._refresh_credentials()

    def get_credentials(self):
        self.refresh()
        return self._credentials

    # --- IMDSv2 token ---

    def _get_imdsv2_token(self):
        """GET a fresh IMDSv2 token. Not cached — fetched every time."""
        url = _IMDS_ENDPOINT + _IMDS_TOKEN_PATH
        headers = {_IMDS_TOKEN_TTL_HEADER: _IMDS_TOKEN_TTL_SECONDS}
        body = self._do_request(url, method="GET", extra_headers=headers)
        token = body.strip()
        if not token:
            raise RuntimeError(
                "{}: IMDSv2 token endpoint returned empty response.".format(
                    self.PROVIDER_NAME
                )
            )
        return token

    # --- roleName resolution ---

    def _resolve_role_name(self, imds_token):
        """Resolve roleName: param > env > auto-detect from IMDS (every time).

        Not cached — roles can be dynamically unbound/rebound on the instance,
        and IMDS is a local call (~1-5ms) so the cost is negligible.
        This matches AWS and Alibaba Cloud SDK behavior.
        """
        if self._role_name:
            return self._role_name

        env_role = os.environ.get("VOLCENGINE_ECS_METADATA", "").strip()
        if env_role:
            return env_role

        return self._auto_detect_role_name(imds_token)

    def _auto_detect_role_name(self, imds_token):
        """GET role list from IMDS, extract first role name."""
        url = _IMDS_ENDPOINT + _IMDS_ROLE_NAME_PATH
        headers = {_IMDS_TOKEN_HEADER: imds_token}
        body = self._do_request(url, method="GET", extra_headers=headers)

        try:
            roles = json.loads(body)
        except ValueError:
            # Fallback: try splitting by newlines (plain text response)
            roles = [r.strip() for r in body.strip().split('\n') if r.strip()]

        # roles should be a list of strings
        if isinstance(roles, list):
            roles = [r.strip() if isinstance(r, str) else str(r) for r in roles if r]
        else:
            raise RuntimeError(
                "{}: unexpected role list response format: {}".format(
                    self.PROVIDER_NAME, type(roles).__name__
                )
            )

        if not roles:
            raise RuntimeError(
                "{}: no IAM roles found via IMDS.".format(self.PROVIDER_NAME)
            )

        if len(roles) > 1:
            logger.warning(
                "%s: multiple IAM roles found via IMDS: %s. Using the first one '%s'. "
                "Set VOLCENGINE_ECS_METADATA or pass role_name explicitly to avoid ambiguity.",
                self.PROVIDER_NAME, roles, roles[0],
            )

        return roles[0]

    # --- Credential refresh ---

    def _refresh_credentials(self):
        # Step 1: Get IMDSv2 token (fresh every time)
        imds_token = self._get_imdsv2_token()

        # Step 2: Resolve role name
        role_name = self._resolve_role_name(imds_token)

        # Step 3: POST to get credentials
        url = _IMDS_ENDPOINT + _IMDS_CREDENTIALS_PATH.format(role_name=role_name)
        headers = {_IMDS_TOKEN_HEADER: imds_token}
        body = self._do_request(url, method="POST", extra_headers=headers)

        try:
            data = json.loads(body)
        except ValueError as e:
            raise RuntimeError(
                "{}: failed to parse IMDS response: {}".format(self.PROVIDER_NAME, e)
            )

        ak = data.get(_FIELD_AK)
        sk = data.get(_FIELD_SK)
        token = data.get(_FIELD_TOKEN)
        expiration_str = data.get(_FIELD_EXPIRATION)

        if not ak or not sk:
            raise RuntimeError(
                "{}: IMDS response missing required credential fields.".format(
                    self.PROVIDER_NAME
                )
            )

        if expiration_str:
            dt = dateutil.parser.parse(expiration_str)
            self._expired_time = (
                dt - datetime(1970, 1, 1, tzinfo=dateutil.tz.tzutc())
            ).total_seconds()
        else:
            self._expired_time = None

        self._credentials = CredentialValue(
            ak=ak,
            sk=sk,
            session_token=token,
            provider_name=self.PROVIDER_NAME,
        )

    # --- HTTP helper ---

    def _do_request(self, url, method="GET", extra_headers=None):
        """Perform an HTTP request with retries."""
        # Late imports to avoid circular deps (auth.providers is imported
        # indirectly by volcenginesdkcore/__init__.py).
        from volcenginesdkcore import ApiClient, Configuration
        timeout = self._connect_timeout + self._read_timeout
        return ApiClient(Configuration())._do_http_request(
            url=url,
            method=method,
            headers=extra_headers,
            timeout=timeout,
            max_retries=self._max_retries,
            retry_interval=self._retry_interval,
            request_name="IMDS request",
            provider_name=self.PROVIDER_NAME,
        )
