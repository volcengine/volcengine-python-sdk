# coding=utf-8
import abc
import json
import time

try:
    from urllib.request import urlopen, Request
    from urllib.error import URLError, HTTPError
except ImportError:
    from urllib2 import urlopen, Request, URLError, HTTPError


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
        import copy as _copy
        fresh._Configuration__retryer = _copy.deepcopy(fresh.retryer)
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
                         max_retries=1, retry_interval=0, request_name=None):
        last_error = None

        for attempt in range(max(max_retries, 1)):
            try:
                req = Request(url, data=data)
                req.get_method = lambda m=method: m
                if headers:
                    for k, v in headers.items():
                        req.add_header(k, v)
                resp = urlopen(req, timeout=timeout)
                return resp.read().decode('utf-8')
            except HTTPError as e:
                # 5xx retry
                if e.code >= 500:
                    last_error = e
                    if attempt < max(max_retries, 1) - 1:
                        time.sleep(retry_interval)
                else:
                    content = e.read().decode('utf-8')
                    raise RuntimeError(
                        "{}: {} failed with HTTP {}: {}".format(
                            self.PROVIDER_NAME, request_name or "request", e.code, content
                        )
                    )
            except (URLError, IOError, OSError) as e:
                last_error = e
                if attempt < max(max_retries, 1) - 1:
                    time.sleep(retry_interval)

        raise RuntimeError(
            "{}: failed to call {} at '{}' after {} retries: {}".format(
                self.PROVIDER_NAME, request_name or "request", url, max(max_retries, 1), last_error
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
