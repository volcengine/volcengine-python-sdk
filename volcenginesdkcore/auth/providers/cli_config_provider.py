# coding=utf-8
import calendar
import hashlib
import json
import os
import tempfile
import threading
import time

from datetime import datetime

from .provider import Provider, CredentialValue

_DEFAULT_REGION = "cn-beijing"
_OAUTH_BASE_URL_TEMPLATE = "https://cloudidentity-oauth.{}.volces.com"
_PORTAL_BASE_URL_TEMPLATE = "https://cloudidentity-portal.{}.volces.com"
_PORTAL_ACCESS_TOKEN_HEADER = "x-bd-cloudidentity-bearer-token"
_HTTP_TIMEOUT = 30
_HTTP_MAX_RETRIES = 3
_HTTP_RETRY_INTERVAL = 1


class CLIConfigCredentialProvider(Provider):
    """Reads credentials from the Volcengine CLI config.json file.

    Default path: ~/.volcengine/config.json
    Override with env var: VOLCENGINE_CLI_CONFIG_FILE
    Profile selection:
      constructor profile_name > VOLCENGINE_PROFILE env var > "current" field in JSON > "default"

    Supports mode field in profile:
      - "AK" or "" or None (default): read access-key/secret-key/session-token
      - "StsToken": same as AK but session-token is required
      - "RamRoleArn": delegate to StsCredentialProvider
      - "OIDC": delegate to StsOidcCredentialProvider
      - "EcsRole": delegate to EcsRoleCredentialProvider
      - "sso": delegate to SsoCredentialProvider
      - Other modes: raise RuntimeError (unsupported)
    """

    PROVIDER_NAME = "CLIConfigCredentialProvider"

    def __init__(self, profile_name=None, config_path=None):
        self._profile_name = profile_name
        self._config_path = config_path
        self._delegate = None
        self._static_cred = None
        self._initialized = False
        self._init_lock = threading.Lock()
        self._resolved_config_path = None

    def _init_delegate(self):
        profile, profile_name, config = self._load_profile()
        raw_mode = profile.get("mode", "") or ""
        mode = raw_mode.lower().strip()

        if mode in ("ak", ""):
            self._static_cred = self._read_ak_mode(profile, profile_name, require_token=False)
        elif mode == "ststoken":
            self._static_cred = self._read_ak_mode(profile, profile_name, require_token=True)
        elif mode == "ramrolearn":
            self._static_cred = None
            self._delegate = self._create_ram_role_arn_delegate(profile, profile_name)
        elif mode == "oidc":
            self._static_cred = None
            self._delegate = self._create_oidc_delegate(profile, profile_name)
        elif mode == "ecsrole":
            self._static_cred = None
            self._delegate = self._create_ecs_role_delegate(profile, profile_name)
        elif mode == "sso":
            self._static_cred = None
            self._delegate = self._create_sso_delegate(profile, profile_name, config)
        else:
            raise RuntimeError(
                "{}: unsupported mode: {}".format(self.PROVIDER_NAME, mode)
            )

    def _load_profile(self):
        config_path = (
            self._config_path
            or os.environ.get("VOLCENGINE_CLI_CONFIG_FILE")
            or os.path.expanduser("~/.volcengine/config.json")
        )
        self._resolved_config_path = config_path

        if not os.path.isfile(config_path):
            raise RuntimeError(
                "{}: config file not found at '{}'.".format(self.PROVIDER_NAME, config_path)
            )

        with open(config_path, 'r') as f:
            try:
                config = json.load(f)
            except ValueError as e:
                raise RuntimeError(
                    "{}: failed to parse config file '{}': {}".format(
                        self.PROVIDER_NAME, config_path, e
                    )
                )

        profile_name = (self._profile_name
                        or os.environ.get("VOLCENGINE_PROFILE")
                        or config.get("current"))

        if not profile_name:
            profile_name = "default"

        profiles = config.get("profiles", {})
        profile = profiles.get(profile_name)

        if profile is None:
            raise RuntimeError(
                "{}: profile '{}' not found in config file.".format(
                    self.PROVIDER_NAME, profile_name
                )
            )

        return profile, profile_name, config

    def retrieve(self):
        return self.get_credentials()

    def is_expired(self):
        if not self._initialized:
            return True
        if self._delegate is not None:
            return self._delegate.is_expired()
        return False

    def refresh(self):
        if self._delegate is not None:
            return self._delegate.refresh()
        return

    def get_credentials(self):
        if not self._initialized:
            with self._init_lock:
                if not self._initialized:
                    self._init_delegate()
                    self._initialized = True
        if self._delegate is not None:
            return self._delegate.get_credentials()
        return self._static_cred

    def _read_ak_mode(self, profile, profile_name, require_token=False):
        ak = profile.get("access-key", "").strip()
        sk = profile.get("secret-key", "").strip()

        if not ak or not sk:
            raise RuntimeError(
                "{}: profile '{}' does not contain valid access-key and secret-key.".format(
                    self.PROVIDER_NAME, profile_name
                )
            )

        session_token = profile.get("session-token", "").strip() or None

        if require_token and not session_token:
            raise RuntimeError(
                "{}: profile '{}' mode is StsToken but session-token is not set.".format(
                    self.PROVIDER_NAME, profile_name
                )
            )

        return CredentialValue(
            ak=ak,
            sk=sk,
            session_token=session_token,
            provider_name=self.PROVIDER_NAME,
        )

    def _create_ram_role_arn_delegate(self, profile, profile_name):
        from .sts_provider import StsCredentialProvider

        ak = profile.get("access-key", "").strip()
        sk = profile.get("secret-key", "").strip()
        role_name = profile.get("role-name", "").strip()
        account_id = profile.get("account-id", "").strip()

        if not ak or not sk:
            raise RuntimeError(
                "{}: profile '{}' mode is RamRoleArn but access-key/secret-key is not set.".format(
                    self.PROVIDER_NAME, profile_name
                )
            )
        if not role_name:
            raise RuntimeError(
                "{}: profile '{}' mode is RamRoleArn but role-name is not set.".format(
                    self.PROVIDER_NAME, profile_name
                )
            )
        if not account_id:
            raise RuntimeError(
                "{}: profile '{}' mode is RamRoleArn but account-id is not set.".format(
                    self.PROVIDER_NAME, profile_name
                )
            )

        return StsCredentialProvider(ak=ak, sk=sk, role_name=role_name, account_id=account_id)

    def _create_oidc_delegate(self, profile, profile_name):
        from .sts_oidc_provider import StsOidcCredentialProvider

        role_trn = (profile.get("role-trn") or "").strip()
        oidc_token_file = (profile.get("oidc-token-file") or "").strip()
        policy = (profile.get("policy") or "").strip() or None

        if not role_trn:
            raise RuntimeError(
                "{}: profile '{}' mode is OIDC but role-trn is not set.".format(
                    self.PROVIDER_NAME, profile_name
                )
            )
        if not oidc_token_file:
            raise RuntimeError(
                "{}: profile '{}' mode is OIDC but oidc-token-file is not set.".format(
                    self.PROVIDER_NAME, profile_name
                )
            )

        return StsOidcCredentialProvider(
            role_trn=role_trn,
            oidc_token_file=oidc_token_file,
            policy=policy,
        )

    def _create_ecs_role_delegate(self, profile, profile_name):
        from .ecs_role_provider import EcsRoleCredentialProvider

        role_name = profile.get("role-name", "").strip()

        if not role_name:
            raise RuntimeError(
                "{}: profile '{}' mode is EcsRole but role-name is not set.".format(
                    self.PROVIDER_NAME, profile_name
                )
            )

        return EcsRoleCredentialProvider(role_name=role_name)

    def _create_sso_delegate(self, profile, profile_name, config):
        session_name = (profile.get("sso-session-name") or "").strip()
        if not session_name:
            raise RuntimeError(
                "{}: profile '{}' mode is sso but sso-session-name is not set.".format(
                    self.PROVIDER_NAME, profile_name
                )
            )

        sso_sessions = config.get("sso-session", {}) or {}
        session = sso_sessions.get(session_name)
        if session is None:
            raise RuntimeError(
                "{}: sso-session '{}' not found in config file.".format(
                    self.PROVIDER_NAME, session_name
                )
            )

        start_url = (session.get("start-url") or "").strip()
        if not start_url:
            raise RuntimeError(
                "{}: sso-session '{}' does not contain start-url.".format(
                    self.PROVIDER_NAME, session_name
                )
            )

        region = (session.get("region") or "").strip() or _DEFAULT_REGION

        account_id = (profile.get("account-id") or "").strip()
        if not account_id:
            raise RuntimeError(
                "{}: profile '{}' mode is sso but account-id is not set.".format(
                    self.PROVIDER_NAME, profile_name
                )
            )

        role_name = (profile.get("role-name") or "").strip()
        if not role_name:
            raise RuntimeError(
                "{}: profile '{}' mode is sso but role-name is not set.".format(
                    self.PROVIDER_NAME, profile_name
                )
            )

        config_path = self._resolved_config_path or (
            self._config_path
            or os.environ.get("VOLCENGINE_CLI_CONFIG_FILE")
            or os.path.expanduser("~/.volcengine/config.json")
        )
        cache_dir = os.path.join(os.path.dirname(config_path), "sso", "cache")

        return SsoCredentialProvider(
            profile=profile,
            start_url=start_url,
            session_name=session_name,
            region=region,
            account_id=account_id,
            role_name=role_name,
            cache_dir=cache_dir,
        )


def _unix_timestamp_to_epoch(ts):
    """Convert a Unix timestamp (seconds, milliseconds, microseconds, or
    nanoseconds) to seconds since epoch as a float."""
    if ts >= 1e18:
        return ts / 1e9
    elif ts >= 1e15:
        return ts / 1e6
    elif ts >= 1e12:
        return ts / 1e3
    else:
        return float(ts)


def _token_cache_filename(start_url, session_name):
    """Compute the SHA-1 cache filename, matching the Go SDK convention."""
    payload = json.dumps({"start_url": start_url, "session_name": session_name},
                         separators=(',', ':'), sort_keys=False)
    digest = hashlib.sha1(payload.encode("utf-8")).hexdigest()
    return "{}.json".format(digest)


def _parse_rfc3339(value):
    """Parse an RFC 3339 timestamp string into a datetime (UTC)."""
    value = value.strip()
    if not value:
        raise ValueError("expires_at is empty")
    # Python 3.7+ datetime.fromisoformat doesn't handle trailing Z
    if value.endswith("Z"):
        value = value[:-1] + "+00:00"
    try:
        return datetime.fromisoformat(value)
    except (ValueError, AttributeError):
        pass
    # Fallback for Python < 3.7 or unusual formats
    for fmt in ("%Y-%m-%dT%H:%M:%S%z", "%Y-%m-%dT%H:%M:%S.%f%z",
                "%Y-%m-%dT%H:%M:%S", "%Y-%m-%dT%H:%M:%S.%f"):
        try:
            return datetime.strptime(value, fmt)
        except ValueError:
            continue
    raise ValueError("cannot parse expires_at: {}".format(value))


def _write_json_file_atomic(path, data):
    """Write JSON data to a file atomically."""
    dir_name = os.path.dirname(path)
    fd, tmp_path = tempfile.mkstemp(dir=dir_name, prefix=".tmp-", suffix=".json")
    try:
        with os.fdopen(fd, 'w') as f:
            json.dump(data, f)
        os.chmod(tmp_path, 0o600)
        os.rename(tmp_path, path)
    except Exception:
        try:
            os.remove(tmp_path)
        except OSError:
            pass
        raise


class SsoCredentialProvider(Provider):
    """Obtains temporary credentials via the Volcengine SSO flow.

    Reads the SSO token cache, refreshes the access token if expired,
    then exchanges it for role credentials via the Portal API.
    """

    PROVIDER_NAME = "SsoCredentialProvider"

    def __init__(self, profile, start_url, session_name, region,
                 account_id, role_name, cache_dir):
        self._profile = profile
        self._start_url = start_url
        self._session_name = session_name
        self._region = region
        self._account_id = account_id
        self._role_name = role_name
        self._cache_dir = cache_dir

        self._credentials = None
        self._expiration = None  # epoch seconds
        self._lock = threading.Lock()

    def retrieve(self):
        return self.get_credentials()

    def is_expired(self):
        if self._credentials is None:
            return True
        if self._expiration is not None:
            return time.time() >= self._expiration - 60
        return False

    def refresh(self):
        with self._lock:
            if self.is_expired():
                self._do_refresh()

    def get_credentials(self):
        self.refresh()
        return self._credentials

    def _do_refresh(self):
        # Fast path: if profile has cached STS credentials that are still valid
        cred = self._try_cached_sts_credentials()
        if cred is not None:
            self._credentials = cred
            return

        # Load SSO token cache
        token_path = os.path.join(
            self._cache_dir,
            _token_cache_filename(self._start_url, self._session_name),
        )
        if not os.path.isfile(token_path):
            raise RuntimeError(
                "{}: SSO token cache file not found at '{}'.".format(
                    self.PROVIDER_NAME, token_path
                )
            )

        with open(token_path, 'r') as f:
            try:
                token_cache = json.load(f)
            except ValueError as e:
                raise RuntimeError(
                    "{}: failed to parse SSO token cache '{}': {}".format(
                        self.PROVIDER_NAME, token_path, e
                    )
                )

        access_token = (token_cache.get("access_token") or "").strip()
        if not access_token:
            raise RuntimeError(
                "{}: SSO token cache '{}' does not contain access_token.".format(
                    self.PROVIDER_NAME, token_path
                )
            )

        # Check if access token is expired
        expires_at = (token_cache.get("expires_at") or "").strip()
        token_expired = False
        if expires_at:
            try:
                exp_dt = _parse_rfc3339(expires_at)
                # Compare using calendar.timegm (UTC) — works on Python 2/3
                if exp_dt.tzinfo:
                    # aware datetime: convert to UTC tuple
                    utc_dt = exp_dt - exp_dt.utcoffset()
                    exp_epoch = calendar.timegm(utc_dt.timetuple())
                else:
                    # naive datetime assumed UTC
                    exp_epoch = calendar.timegm(exp_dt.timetuple())
                token_expired = time.time() > exp_epoch
            except ValueError as e:
                raise RuntimeError(
                    "{}: failed to parse expires_at in '{}': {}".format(
                        self.PROVIDER_NAME, token_path, e
                    )
                )

        if token_expired:
            access_token = self._refresh_access_token(token_cache, token_path)

        # Get role credentials from portal
        self._fetch_role_credentials(access_token)

    def _try_cached_sts_credentials(self):
        """Return CredentialValue from profile's cached STS creds if still valid."""
        sts_expiration = self._profile.get("sts-expiration", 0)
        if not sts_expiration or sts_expiration <= 0:
            return None

        exp_epoch = _unix_timestamp_to_epoch(sts_expiration)
        if time.time() >= exp_epoch:
            return None

        ak = (self._profile.get("access-key") or "").strip()
        sk = (self._profile.get("secret-key") or "").strip()
        if not ak or not sk:
            return None

        session_token = (self._profile.get("session-token") or "").strip() or None

        self._expiration = exp_epoch
        return CredentialValue(
            ak=ak,
            sk=sk,
            session_token=session_token,
            provider_name=self.PROVIDER_NAME,
        )

    def _refresh_access_token(self, token_cache, token_path):
        """Refresh the SSO access token using the OAuth token endpoint."""
        refresh_token = (token_cache.get("refresh_token") or "").strip()
        if not refresh_token:
            raise RuntimeError(
                "{}: SSO token cache '{}' does not contain refresh_token.".format(
                    self.PROVIDER_NAME, token_path
                )
            )

        # Check if refresh token itself is expired
        client_secret_expires_at = token_cache.get("client_secret_expires_at", 0)
        if client_secret_expires_at and client_secret_expires_at > 0:
            exp_epoch = _unix_timestamp_to_epoch(client_secret_expires_at)
            if time.time() >= exp_epoch:
                raise RuntimeError(
                    "{}: refresh token in '{}' has expired.".format(
                        self.PROVIDER_NAME, token_path
                    )
                )

        client_id = (token_cache.get("client_id") or "").strip()
        client_secret = (token_cache.get("client_secret") or "").strip()
        if not client_id or not client_secret:
            raise RuntimeError(
                "{}: SSO token cache '{}' does not contain client_id/client_secret.".format(
                    self.PROVIDER_NAME, token_path
                )
            )

        oauth_url = "{}/token".format(
            _OAUTH_BASE_URL_TEMPLATE.format(self._region)
        )

        # Pass a dict body; RESTClient auto-serializes with Content-Type:
        # application/json (see volcenginesdkcore/rest.py). Do NOT json.dumps
        # here or it will be double-encoded.
        resp_body = self._do_http_request(
            oauth_url,
            method="POST",
            data={
                "grant_type": "refresh_token",
                "client_id": client_id,
                "client_secret": client_secret,
                "refresh_token": refresh_token,
            },
            headers={"Content-Type": "application/json"},
            timeout=_HTTP_TIMEOUT,
            max_retries=_HTTP_MAX_RETRIES,
            retry_interval=_HTTP_RETRY_INTERVAL,
            request_name="OAuth token refresh",
            # OAuth refresh_token grants may rotate the refresh token on use;
            # replaying a successful-but-response-lost POST would invalidate
            # the local refresh_token. Fail fast on 5xx instead.
            retry_on_5xx=False,
        )

        try:
            resp_data = json.loads(resp_body)
        except ValueError as e:
            raise RuntimeError(
                "{}: failed to parse OAuth token response: {}".format(
                    self.PROVIDER_NAME, e
                )
            )

        new_access_token = (resp_data.get("access_token") or "").strip()
        if not new_access_token:
            raise RuntimeError(
                "{}: OAuth token response did not contain access_token.".format(
                    self.PROVIDER_NAME
                )
            )

        expires_in = resp_data.get("expires_in", 0)
        if expires_in <= 0:
            raise RuntimeError(
                "{}: OAuth token response did not contain valid expires_in.".format(
                    self.PROVIDER_NAME
                )
            )

        # Update the cache
        token_cache["access_token"] = new_access_token
        new_refresh = (resp_data.get("refresh_token") or "").strip()
        if new_refresh:
            token_cache["refresh_token"] = new_refresh
        token_cache["expires_at"] = time.strftime(
            "%Y-%m-%dT%H:%M:%SZ", time.gmtime(time.time() + expires_in)
        )

        _write_json_file_atomic(token_path, token_cache)

        return new_access_token

    def _fetch_role_credentials(self, access_token):
        """Exchange an SSO access token for temporary role credentials."""
        try:
            from urllib.parse import urlencode
        except ImportError:
            from urllib import urlencode

        portal_url = "{}/federation/credentials?{}".format(
            _PORTAL_BASE_URL_TEMPLATE.format(self._region),
            urlencode({"account_id": self._account_id, "role_name": self._role_name}),
        )

        resp_body = self._do_http_request(
            portal_url,
            method="GET",
            headers={
                "Accept": "application/json",
                _PORTAL_ACCESS_TOKEN_HEADER: access_token,
            },
            timeout=_HTTP_TIMEOUT,
            max_retries=_HTTP_MAX_RETRIES,
            retry_interval=_HTTP_RETRY_INTERVAL,
            request_name="Portal GetRoleCredentials",
        )

        try:
            resp_data = json.loads(resp_body)
        except ValueError as e:
            raise RuntimeError(
                "{}: failed to parse Portal response: {}".format(
                    self.PROVIDER_NAME, e
                )
            )

        result = resp_data.get("Result") or resp_data.get("result") or {}
        role_creds = result.get("RoleCredentials") or result.get("roleCredentials") or {}

        ak = (role_creds.get("AccessKeyId") or "").strip()
        sk = (role_creds.get("SecretAccessKey") or "").strip()
        token = (role_creds.get("sessionToken") or role_creds.get("SessionToken") or "").strip()

        if not ak or not sk:
            # Check ResponseMetadata for error
            meta = resp_data.get("ResponseMetadata", {})
            err = meta.get("Error", {})
            if err:
                raise RuntimeError(
                    "{}: Portal API error: {} - {}".format(
                        self.PROVIDER_NAME,
                        err.get("Code", ""),
                        err.get("Message", ""),
                    )
                )
            raise RuntimeError(
                "{}: Portal response missing AccessKeyId/SecretAccessKey.".format(
                    self.PROVIDER_NAME
                )
            )

        expiration = role_creds.get("Expiration", 0)
        if expiration and expiration > 0:
            self._expiration = _unix_timestamp_to_epoch(expiration)
        else:
            self._expiration = None

        self._credentials = CredentialValue(
            ak=ak,
            sk=sk,
            session_token=token or None,
            provider_name=self.PROVIDER_NAME,
        )
