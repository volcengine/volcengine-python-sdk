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
