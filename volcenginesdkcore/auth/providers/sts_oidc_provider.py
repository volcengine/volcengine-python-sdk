import os
import threading
import time
import uuid
from datetime import datetime

import dateutil.parser
import dateutil.tz

from volcenginesdkcore import UniversalApi, UniversalInfo, ApiClient, Configuration
from .provider import Provider, CredentialValue


class AssumeRoleOidcCredentials:
    def __init__(self, ak, sk, session_token, current_time, expired_time):
        self.ak = ak
        self.sk = sk
        self.session_token = session_token
        self.current_time = current_time
        self.expired_time = expired_time


class StsOidcCredentialProvider(Provider):
    """Obtains temporary credentials via STS AssumeRoleWithOIDC.

    Supports two usage modes:

    1. Legacy mode (backward compatible):
       StsOidcCredentialProvider(role_name=..., account_id=..., oidc_token=...)
       In this mode, host/policy/session_name use ctor values or defaults only,
       environment variables are NOT consulted.

    2. Env-aware mode (for default chain / CLI delegate):
       StsOidcCredentialProvider(role_trn=..., oidc_token_file=...)
       or StsOidcCredentialProvider()  # all from env
       In this mode, parameters fall back to VOLCENGINE_OIDC_* env vars.

    Parameter resolution (env-aware mode):
      - role_trn: ctor > env(VOLCENGINE_OIDC_ROLE_TRN)
      - oidc_token_file: ctor > env(VOLCENGINE_OIDC_TOKEN_FILE)
      - session_name: ctor > env(VOLCENGINE_OIDC_ROLE_SESSION_NAME) > auto-generate
      - policy: ctor > env(VOLCENGINE_OIDC_ROLE_POLICY)
      - host: ctor > env(VOLCENGINE_OIDC_STS_ENDPOINT) > sts.volcengineapi.com
    """

    PROVIDER_NAME = "StsOidcCredentialProvider"

    def __init__(self, role_name=None, account_id=None, oidc_token=None,
                 duration_seconds=3600, scheme='https',
                 host=None, region='cn-beijing', timeout=30,
                 expired_buffer_seconds=60, policy=None,
                 role_trn=None, oidc_token_file=None, session_name=None):

        # Detect legacy mode: user passed oidc_token directly (old-style usage).
        # In legacy mode, we do NOT read env vars for host/policy/session_name
        # to preserve 100% backward compatibility.
        self._legacy_mode = oidc_token is not None

        # --- role_trn resolution ---
        if role_trn:
            self._role_trn = role_trn
        elif role_name and account_id:
            self._role_trn = 'trn:iam::' + account_id + ':role/' + role_name
        elif not self._legacy_mode:
            env_trn = os.environ.get("VOLCENGINE_OIDC_ROLE_TRN", "")
            self._role_trn = env_trn if env_trn else None
        else:
            self._role_trn = None

        # Keep original fields for backward compat
        self.role_name = role_name
        self.account_id = account_id

        # --- oidc_token resolution ---
        self._oidc_token = oidc_token
        if not self._legacy_mode:
            self._oidc_token_file = oidc_token_file or os.environ.get("VOLCENGINE_OIDC_TOKEN_FILE", "") or None
        else:
            self._oidc_token_file = oidc_token_file

        # --- session_name resolution ---
        if session_name:
            self._session_name = session_name
        elif not self._legacy_mode:
            self._session_name = os.environ.get("VOLCENGINE_OIDC_ROLE_SESSION_NAME", "") or None
        else:
            # Legacy mode: will use uuid.uuid4().hex at call time (original behavior)
            self._session_name = None

        # --- policy resolution ---
        if policy is not None:
            self.policy = policy
        elif not self._legacy_mode:
            self.policy = os.environ.get("VOLCENGINE_OIDC_ROLE_POLICY") or None
        else:
            self.policy = None

        # --- host resolution ---
        if host:
            self.host = host
        elif not self._legacy_mode:
            self.host = os.environ.get("VOLCENGINE_OIDC_STS_ENDPOINT", "") or "sts.volcengineapi.com"
        else:
            self.host = "sts.volcengineapi.com"

        self.timeout = timeout
        self.duration_seconds = duration_seconds
        self.region = region
        self.scheme = scheme

        if expired_buffer_seconds > 600:
            raise ValueError('expired_buffer_seconds must be less than or equal to 600')
        self.expired_buffer_seconds = expired_buffer_seconds

        self.expired_time = None
        self.credentials = None
        self._lock = threading.Lock()

    def retrieve(self):
        return self.credentials

    def is_expired(self):
        return (self.credentials is None or
                (self.expired_time and self.expired_time < time.time() + self.expired_buffer_seconds))

    def refresh(self):
        with self._lock:
            if self.is_expired():
                self._assume_role_oidc()

    def get_credentials(self):
        self.refresh()
        return self.credentials

    def _resolve_oidc_token(self):
        """Resolve the OIDC token from inline value or file."""
        if self._oidc_token:
            return self._oidc_token

        token_file = self._oidc_token_file
        if not token_file:
            raise RuntimeError(
                "{}: OIDC token not provided. Set oidc_token, oidc_token_file, "
                "or VOLCENGINE_OIDC_TOKEN_FILE environment variable.".format(self.PROVIDER_NAME)
            )

        try:
            with open(token_file, 'r') as f:
                token = f.read().strip()
        except (IOError, OSError) as e:
            raise RuntimeError(
                "{}: failed to read OIDC token file '{}': {}".format(
                    self.PROVIDER_NAME, token_file, e
                )
            )

        if not token:
            raise RuntimeError(
                "{}: OIDC token file '{}' is empty.".format(self.PROVIDER_NAME, token_file)
            )

        return token

    def _assume_role_oidc(self):
        # Validate role_trn
        if not self._role_trn:
            raise RuntimeError(
                "{}: role_trn not provided. Set role_trn (or role_name+account_id), "
                "or VOLCENGINE_OIDC_ROLE_TRN environment variable.".format(self.PROVIDER_NAME)
            )

        oidc_token = self._resolve_oidc_token()

        # Session name: legacy mode uses uuid (original behavior), env mode uses timestamp
        if self._session_name:
            session_name = self._session_name
        elif self._legacy_mode:
            session_name = uuid.uuid4().hex
        else:
            session_name = "credentials-python-" + str(int(time.time() * 1000000))

        params = {
            'DurationSeconds': self.duration_seconds,
            'RoleSessionName': session_name,
            'RoleTrn': self._role_trn,
            'OIDCToken': oidc_token,
        }
        if self.policy:
            params['Policy'] = self.policy

        configuration = type.__call__(Configuration)
        configuration.host = self.host
        configuration.region = self.region
        configuration.scheme = self.scheme
        configuration.read_timeout = self.timeout
        c = UniversalApi(ApiClient(configuration))
        info = UniversalInfo(method='POST', service='sts', version='2018-01-01',
                             action='AssumeRoleWithOIDC',
                             content_type='application/x-www-form-urlencoded')

        resp, status_code, resp_header = c.do_call_with_http_info(info=info, body=params)
        if 'Credentials' not in resp:
            raise RuntimeError(
                '{}: failed to retrieve credentials from STS: {}'.format(
                    self.PROVIDER_NAME, str(resp_header)
                )
            )
        resp_cred = resp['Credentials']

        # Parse expiration
        dt = dateutil.parser.parse(resp_cred['Expiration'])
        self.expired_time = (dt - datetime(1970, 1, 1, tzinfo=dateutil.tz.tzutc())).total_seconds()

        self.credentials = CredentialValue(
            ak=resp_cred['AccessKeyId'],
            sk=resp_cred['SecretAccessKey'],
            session_token=resp_cred['SessionToken'],
            provider_name=self.PROVIDER_NAME,
        )
