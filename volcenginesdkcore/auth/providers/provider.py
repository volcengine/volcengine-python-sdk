# coding=utf-8
import abc
import json
import logging
import time

logger = logging.getLogger(__name__)


class CredentialValue:
    def __init__(self, ak, sk, session_token=None, provider_name=None):
        self.ak = ak
        self.sk = sk
        self.session_token = session_token
        self.provider_name = provider_name


class Provider(object):
    PROVIDER_NAME = "Provider"

    @abc.abstractmethod
    def retrieve(self):
        raise NotImplementedError()

    @abc.abstractmethod
    def is_expired(self):
        raise NotImplementedError()

    @abc.abstractmethod
    def refresh(self):
        raise NotImplementedError()

    @abc.abstractmethod
    def get_credentials(self):
        raise NotImplementedError()

    def _sts_call(self, action, version, params,
                  host=None, scheme='https', region='cn-beijing',
                  timeout=30, service='sts',
                  max_retries=3, retry_interval=1):
        """Invoke an STS federation endpoint (AssumeRoleWithOIDC / AssumeRoleWithSAML / etc.)
        through the SDK's main REST stack while explicitly disabling signing.

        This reuses `ApiClient.call_api` so TLS config (`verify_ssl`,
        `ssl_ca_cert`, `cert_file`, `assert_hostname`), proxy (`http_proxy` /
        `https_proxy` / env vars), connect/read timeouts, connection pooling
        and observability are all honored exactly as for any other SDK API call.

        Signing is skipped by passing `auth_settings=None`, which causes
        `SignRequestInterceptor.update_params_for_auth` to early-return. This
        is correct because OIDC / SAML federation entry points are unsigned
        by design (the OIDCToken / SAMLResp is the authentication material).

        Recursion is broken by zeroing `credential_provider` / `ak` / `sk` on
        the fresh Configuration copy, so the STS request does not itself
        invoke the provider that initiated it.

        Returns the unwrapped `Result` dict from the STS response. Business
        errors bubble up as `rest.ApiException` (matching master behavior).
        """
        # Late imports to avoid circular deps (this module is imported from
        # volcenginesdkcore/__init__.py indirectly via auth/providers).
        from volcenginesdkcore import ApiClient, Configuration

        # Configuration() via the TypeWithDefault metaclass returns a shallow
        # copy of the user's default configuration, so TLS/proxy/timeout
        # settings propagate to the STS call.
        fresh = Configuration()
        # Break recursion on three fronts:
        #   1. credential_provider=None so SignRequestInterceptor won't call
        #      back into this provider via get_credentials().
        #   2. Non-empty ak/sk sentinel so the feature branch's
        #      SignRequestInterceptor does NOT auto-attach a
        #      DefaultCredentialProvider (which would recurse through the
        #      whole credential chain back into us). The sentinel never
        #      reaches the wire because auth_settings=None short-circuits
        #      update_params_for_auth before signing.
        fresh.credential_provider = None
        fresh.ak = "_sts_bootstrap_unsigned"
        fresh.sk = "_sts_bootstrap_unsigned"
        fresh.session_token = ""
        # Per-call overrides from the provider
        if host:
            fresh.host = host
        fresh.scheme = scheme
        fresh.region = region
        fresh.read_timeout = timeout

        # Retry: apply provider-level retry semantics to this STS call only.
        # Deep-copy the retryer so we don't mutate the caller's default
        # retryer (DEFAULT_RETRYER is a module-level singleton shared across
        # Configurations). Configuration exposes retryer via a getter-only
        # property; swap the underlying __retryer via name mangling.
        import copy
        fresh._Configuration__retryer = copy.deepcopy(fresh.retryer)
        # Provider semantics: max_retries = TOTAL attempts (legacy from
        # _do_http_request's for-loop). Configuration semantics:
        # num_max_retries = retries AFTER the initial attempt. Convert.
        fresh.num_max_retries = max(max_retries - 1, 0)
        # Provider retry_interval is seconds; Configuration uses ms.
        # Collapse the exponential-backoff range to a fixed delay.
        delay_ms = int(retry_interval * 1000)
        fresh.min_retry_delay_ms = delay_ms
        fresh.max_retry_delay_ms = delay_ms

        client = ApiClient(fresh)
        # BuildRequestInterceptor parses resource_path by index:
        # [1]=Action [2]=Version [3]=service
        resource_path = '/{}/{}/{}/post/'.format(action, version, service)
        return client.call_api(
            resource_path,
            'POST',
            path_params={},
            query_params=[],
            header_params={
                'Accept': 'application/json',
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body=params,
            post_params=[],
            files={},
            response_type=object,
            auth_settings=None,            # skip signing
            async_req=False,
            _return_http_data_only=True,
            _preload_content=True,
            collection_formats={},
        )

    def _do_http_request(self, url, method="GET", data=None, headers=None, timeout=None,
                         max_retries=1, retry_interval=0, request_name=None,
                         retry_on_5xx=True):
        """Invoke an arbitrary HTTP(S) endpoint through the SDK's RESTClient.

        Routing through `RESTClientObject` (constructed from `Configuration()`)
        ensures the credential-provider transport honors the same TLS/proxy
        settings as every other SDK API call:
          - `verify_ssl`, `ssl_ca_cert`, `cert_file`, `key_file`,
            `assert_hostname`
          - `proxy` / `http_proxy` / `https_proxy` (plus HTTP_PROXY /
            HTTPS_PROXY environment variables)
          - `connect_timeout` / `read_timeout` / connection pool sizing

        Unlike `_sts_call` (which goes through `ApiClient`), this path skips
        the OpenAPI semantics layer (signing, Action/Version path parsing,
        response unwrapping) -- it's meant for non-OpenAPI endpoints such as
        the SSO OAuth token endpoint, the SSO Portal, and ECS IMDSv2.

        Args:
          url: Fully-qualified request URL. Query string may be pre-embedded;
               RESTClient will not second-encode it.
          method: HTTP method.
          data: Request body. When `Content-Type` is JSON, RESTClient will
                `json.dumps` a dict automatically; pass a str/bytes to
                bypass. For GET/HEAD, pass None.
          headers: Request headers dict.
          timeout: Total request timeout (seconds). Passed as
                   `_request_timeout` to RESTClient.
          max_retries: Total number of attempts (including the first).
          retry_interval: Seconds to sleep between retries.
          request_name: Human-readable name used in error messages.
          retry_on_5xx: If True (default) retry on HTTP 5xx responses. Pass
                        False for non-idempotent POSTs where replay may be
                        unsafe (e.g. OAuth refresh_token grants that rotate
                        the refresh token on use).

        Returns:
          Response body as a decoded str.

        Raises:
          RuntimeError on non-2xx HTTP response or transport failure.
        """
        # Late imports to avoid circular deps (auth.providers is imported
        # indirectly by volcenginesdkcore/__init__.py).
        from volcenginesdkcore import Configuration
        from volcenginesdkcore.rest import RESTClientObject, ApiException
        import urllib3

        attempts = max(max_retries, 1)
        # Configuration() returns a shallow copy of the user's default config
        # via TypeWithDefault, so TLS/proxy/timeout settings propagate.
        rest_client = RESTClientObject(Configuration())

        last_error = None
        for attempt in range(attempts):
            try:
                logger.debug(
                    "%s: RESTClient attempt %d/%d %s %s",
                    self.PROVIDER_NAME, attempt + 1, attempts, method, url,
                )
                r = rest_client.request(
                    method=method,
                    url=url,
                    body=data,
                    headers=headers,
                    _request_timeout=timeout,
                )
                body = r.data
                # Py3: already decoded by RESTClient; Py2: still bytes (== str).
                if isinstance(body, bytes):
                    try:
                        body = body.decode('utf-8')
                    except (UnicodeDecodeError, AttributeError):
                        pass
                return body
            except ApiException as e:
                status = e.status or 0
                err_body = e.body
                if isinstance(err_body, bytes):
                    try:
                        err_body = err_body.decode('utf-8')
                    except (UnicodeDecodeError, AttributeError):
                        err_body = repr(err_body)
                # status == 0 signals a transport-level failure (e.g. SSL,
                # DNS) converted by RESTClient; no point retrying.
                if status == 0:
                    raise RuntimeError(
                        "{}: {} failed at '{}' (transport error): {}".format(
                            self.PROVIDER_NAME, request_name or "request", url, e.reason,
                        )
                    )
                if retry_on_5xx and status >= 500:
                    last_error = RuntimeError(
                        "HTTP {}: {}".format(status, err_body)
                    )
                    logger.debug(
                        "%s: HTTP %s on attempt %d/%d: %s",
                        self.PROVIDER_NAME, status, attempt + 1, attempts, err_body,
                    )
                    if attempt < attempts - 1:
                        time.sleep(retry_interval)
                    continue
                raise RuntimeError(
                    "{}: {} failed with HTTP {}: {}".format(
                        self.PROVIDER_NAME, request_name or "request", status, err_body,
                    )
                )
            except (urllib3.exceptions.HTTPError, IOError, OSError) as e:
                last_error = e
                logger.debug(
                    "%s: transport error on attempt %d/%d: %r",
                    self.PROVIDER_NAME, attempt + 1, attempts, e,
                )
                if attempt < attempts - 1:
                    time.sleep(retry_interval)

        raise RuntimeError(
            "{}: failed to call {} at '{}' after {} retries: {}".format(
                self.PROVIDER_NAME, request_name or "request", url, attempts, last_error,
            )
        )

    def _parse_json_response(self, content, response_name="response"):
        try:
            resp = json.loads(content)
        except ValueError as e:
            raise RuntimeError(
                "{}: failed to parse {} as JSON: {}. raw={}".format(
                    self.PROVIDER_NAME, response_name, e, content
                )
            )

        if not isinstance(resp, dict):
            raise RuntimeError(
                "{}: unexpected {} type: {}".format(
                    self.PROVIDER_NAME, response_name, type(resp).__name__
                )
            )

        return resp

    def _unwrap_result(self, resp, response_name="response"):
        if 'Result' not in resp:
            return resp

        result = resp['Result']
        if not isinstance(result, dict):
            raise RuntimeError(
                "{}: unexpected {}.Result type: {}".format(
                    self.PROVIDER_NAME, response_name, type(result).__name__
                )
            )

        return result
