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

try:
    from urllib.request import urlopen, Request
    from urllib.error import URLError, HTTPError
except ImportError:
    from urllib2 import urlopen, Request, URLError, HTTPError

logger = logging.getLogger(__name__)

# TODO: Replace placeholders once ECS IMDS endpoint and protocol are confirmed.
_IMDS_ENDPOINT = "http://100.96.0.96"  # TODO: confirm actual endpoint
_IMDS_CREDENTIALS_PATH = "/volcstack/latest/iam/security_credentials/{role_name}"  # TODO

# TODO: IMDSv2 token support (if applicable)
_IMDS_TOKEN_PATH = "/volcstack/latest/api/token"  # TODO
_IMDS_TOKEN_TTL_HEADER = "X-volcengine-ecs-metadata-token-ttl-seconds"  # TODO
_IMDS_TOKEN_HEADER = "X-volcengine-ecs-metadata-token"  # TODO

# TODO: Response field names (confirm with ECS team)
_FIELD_AK = "AccessKeyId"  # TODO: could be AccessKeyID
_FIELD_SK = "SecretAccessKey"
_FIELD_TOKEN = "SessionToken"
_FIELD_EXPIRATION = "ExpiredTime"


class EcsRoleCredentialProvider(Provider):
    """Obtains temporary credentials from the ECS Instance Metadata Service (IMDS).

    The provider queries IMDS for IAM role credentials, caches them, and
    refreshes automatically before expiration.

    roleName priority: constructor param > VOLCENGINE_ECS_METADATA env.
    Disabled when VOLCENGINE_ECS_METADATA_DISABLED=true.
    """

    PROVIDER_NAME = "EcsRoleCredentialProvider"

    def __init__(self, role_name=None, connect_timeout=1, read_timeout=1,
                 max_retries=3, retry_interval=1, expired_buffer_seconds=300):
        self._role_name = role_name
        self._connect_timeout = connect_timeout
        self._read_timeout = read_timeout
        self._max_retries = max_retries
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
        disabled = os.environ.get("VOLCENGINE_ECS_METADATA_DISABLED", "").lower()
        if disabled == "true":
            raise RuntimeError(
                "{}: IMDS is disabled via VOLCENGINE_ECS_METADATA_DISABLED=true.".format(
                    self.PROVIDER_NAME
                )
            )
        self.refresh()
        return self._credentials

    def _resolve_role_name(self):
        if self._role_name:
            return self._role_name

        env_role = os.environ.get("VOLCENGINE_ECS_METADATA", "").strip()
        if env_role:
            return env_role

        raise RuntimeError(
            "{}: role name is not set. "
            "Please set VOLCENGINE_ECS_METADATA or pass role_name explicitly.".format(
                self.PROVIDER_NAME
            )
        )

    def _refresh_credentials(self):
        role_name = self._resolve_role_name()
        url = _IMDS_ENDPOINT + _IMDS_CREDENTIALS_PATH.format(role_name=role_name)
        body = self._do_request(url)

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

    def _do_request(self, url):
        timeout = self._connect_timeout + self._read_timeout
        last_error = None

        for attempt in range(self._max_retries):
            try:
                req = Request(url)
                resp = urlopen(req, timeout=timeout)
                return resp.read().decode('utf-8')
            except (URLError, HTTPError, IOError, OSError) as e:
                last_error = e
                if attempt < self._max_retries - 1:
                    time.sleep(self._retry_interval)

        raise RuntimeError(
            "{}: failed to connect to IMDS at '{}' after {} retries: {}".format(
                self.PROVIDER_NAME, url, self._max_retries, last_error
            )
        )
