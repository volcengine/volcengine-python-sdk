# coding: utf-8

from __future__ import absolute_import

import io
import copy
import json
import logging
import os
import re
import ssl

import certifi
# python 2 and python 3 compatibility library
import six
from six.moves.urllib.parse import urlencode
from urllib3 import Retry

from volcenginesdkcore.observability.debugger import sdk_core_logger, LogLevel

try:
    import urllib3
except ImportError:
    raise ImportError('Swagger python client requires urllib3.')

logger = logging.getLogger(__name__)


class RESTResponse(io.IOBase):

    def __init__(self, resp, data=None):
        self.urllib3_response = resp
        self.status = resp.status
        self.reason = resp.reason
        self.data = resp.data if data is None else data
        from volcenginesdkcore.error_details import snapshot_response
        self._response_details = snapshot_response(self, self.data)

    def getheaders(self):
        """Returns a dictionary of the response headers."""
        return self.urllib3_response.headers

    def getheader(self, name, default=None):
        """Returns a given response header."""
        return self.urllib3_response.headers.get(name, default)


def log_request(method, url, query_params, headers, body, post_params, request_time_out):
    sdk_core_logger.debug_request("request url: %s %s", method, url)
    if request_time_out:
        sdk_core_logger.debug_request("request timeout: %s", request_time_out)

    if query_params:
        sdk_core_logger.debug_request("query params: %s", query_params)

    if headers:
        sdk_core_logger.debug_request("headers:")
        for k, v in headers.items():
            sdk_core_logger.debug_request("    %s: %s", k, v)

    if post_params:
        sdk_core_logger.debug_request("post params: %s", post_params)

    if body:
        # body may be bytes and needs to be decoded
        if isinstance(body, bytes):
            try:
                body = body.decode("utf-8")
            except Exception:
                body = str(body)
        sdk_core_logger.debug_request("body: %s", body, is_body=True)


def log_response(r, _preload_content):
    headers = r.getheaders() if isinstance(r, RESTResponse) else r.headers
    sdk_core_logger.debugx(LogLevel.LOG_DEBUG_WITH_REQUEST_ID, "[Response] request id: %s", headers.get("X-Tt-Logid"))
    sdk_core_logger.debug_response("status: %s", r.status)
    sdk_core_logger.debug_response("reason: %s", r.reason)
    sdk_core_logger.debug_response("headers:")
    for k, v in headers.items():
        sdk_core_logger.debug_response("    %s: %s", k, v)
    if _preload_content:
        sdk_core_logger.debug_response("body: %s", r.data, is_body=True)
    else:
        preview_len = 2048
        # Stream not preloaded: avoid consuming the stream, just do a "peek"
        preview_bytes = b""
        try:
            # urllib3.HTTPResponse.peek(n) is usually available and does not advance the read pointer
            if hasattr(r, "peek"):
                preview_bytes = r.peek(preview_len) or b""
            else:
                # Some implementations may cache r.data (not read the underlying stream again)
                cached = getattr(r, "_body", b"")
                if cached:
                    preview_bytes = cached[:preview_len]
        except Exception:
            preview_bytes = b""

        if preview_bytes:
            try:
                preview_text = preview_bytes.decode("utf-8", errors="replace")
            except Exception:
                preview_text = repr(preview_bytes)
            sdk_core_logger.debug_response("response body (preview, %d bytes): %s", len(preview_bytes), preview_text, is_body=True)
        else:
            sdk_core_logger.debug_response("response body (preview): <streaming, not read>", is_body=True)


class RESTClientObject(object):

    def __init__(self, configuration, pools_size=4, maxsize=None):
        self._sts_network_errors = bool(getattr(configuration, "_sts_network_errors", False))
        # urllib3.PoolManager will pass all kw parameters to connectionpool
        # https://github.com/shazow/urllib3/blob/f9409436f83aeb79fbaf090181cd81b784f1b8ce/urllib3/poolmanager.py#L75  # noqa: E501
        # https://github.com/shazow/urllib3/blob/f9409436f83aeb79fbaf090181cd81b784f1b8ce/urllib3/connectionpool.py#L680  # noqa: E501
        # maxsize is the number of requests to host that are allowed in parallel  # noqa: E501
        # Custom SSL certificates and client certificates: http://urllib3.readthedocs.io/en/latest/advanced-usage.html  # noqa: E501

        proxy_url = self.__get_proxy(configuration)

        # cert_reqs
        if configuration.verify_ssl:
            cert_reqs = ssl.CERT_REQUIRED
        else:
            cert_reqs = ssl.CERT_NONE

        # ca_certs
        if configuration.ssl_ca_cert:
            ca_certs = configuration.ssl_ca_cert
        else:
            # if not set certificate file, use Mozilla's root certificates.
            ca_certs = certifi.where()

        addition_pool_args = {}
        if configuration.assert_hostname is not None:
            addition_pool_args['assert_hostname'] = configuration.assert_hostname  # noqa: E501

        if maxsize is None:
            if configuration.connection_pool_maxsize is not None:
                maxsize = configuration.connection_pool_maxsize
            else:
                maxsize = 4

        if configuration.num_pools is not None:
            pools_size = configuration.num_pools

        timeout = urllib3.Timeout(
            connect=configuration.connect_timeout,
            read=configuration.read_timeout,
        )

        if proxy_url:
            # urllib3 (v2) does not forward the ``user:password@`` embedded in
            # the proxy URL as a Proxy-Authorization header, unlike Go's
            # http.ProxyURL. Extract it explicitly so proxies requiring Basic
            # auth work the same way across SDKs.
            proxy_headers = self.__proxy_authorization_headers(proxy_url)
            self.pool_manager = urllib3.ProxyManager(
                num_pools=pools_size,
                maxsize=maxsize,
                cert_reqs=cert_reqs,
                ca_certs=ca_certs,
                cert_file=configuration.cert_file,
                key_file=configuration.key_file,
                proxy_url=proxy_url,
                proxy_headers=proxy_headers,
                timeout=timeout,
                retries=Retry(total=False),
                **addition_pool_args
            )
        else:
            self.pool_manager = urllib3.PoolManager(
                num_pools=pools_size,
                maxsize=maxsize,
                cert_reqs=cert_reqs,
                ca_certs=ca_certs,
                cert_file=configuration.cert_file,
                key_file=configuration.key_file,
                timeout=timeout,
                retries=Retry(total=False),
                **addition_pool_args
            )

    def __get_proxy(self, configuration):
        proxy_url = configuration.proxy
        if not proxy_url:
            if configuration.scheme == 'http':
                if configuration.http_proxy:
                    proxy_url = configuration.http_proxy
                elif os.getenv('HTTP_PROXY'):
                    proxy_url = os.getenv('HTTP_PROXY')
                elif os.getenv('http_proxy'):
                    proxy_url = os.getenv('http_proxy')
            elif configuration.scheme == 'https':
                if configuration.https_proxy:
                    proxy_url = configuration.https_proxy
                elif os.getenv('HTTPS_PROXY'):
                    proxy_url = os.getenv('HTTPS_PROXY')
                elif os.getenv('https_proxy'):
                    proxy_url = os.getenv('https_proxy')
        return proxy_url

    @staticmethod
    def __proxy_authorization_headers(proxy_url):
        """Build proxy_headers carrying Proxy-Authorization, or None.

        Returns a dict ``{'Proxy-Authorization': 'Basic ...'}`` when the proxy
        URL embeds a ``user:password@`` userinfo, otherwise None (so urllib3
        keeps its default empty proxy headers). Never raises: a malformed proxy
        URL simply yields no auth header and lets the connection attempt (and
        its clearer downstream error) proceed.
        """
        try:
            from volcenginesdkcore.auth.sts_http_config import (
                build_proxy_authorization_header,
            )
            value = build_proxy_authorization_header(proxy_url)
        except Exception:
            return None
        if not value:
            return None
        return {"Proxy-Authorization": value}

    def request(self, method, url, query_params=None, headers=None,
                body=None, post_params=None, _preload_content=True,
                _request_timeout=None, _response_type=None):
        """Perform requests.

        :param method: http request method
        :param url: http request url
        :param query_params: query parameters in the url
        :param headers: http request headers
        :param body: request json body, for `application/json`
        :param post_params: request post parameters,
                            `application/x-www-form-urlencoded`
                            and `multipart/form-data`
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        """
        method = method.upper()
        assert method in ['GET', 'HEAD', 'DELETE', 'POST', 'PUT',
                          'PATCH', 'OPTIONS']

        if post_params and body:
            raise ValueError(
                "body parameter cannot be used with post_params parameter."
            )

        post_params = post_params or {}
        headers = headers or {}

        timeout = None
        if _request_timeout:
            if isinstance(_request_timeout, (int, float) if six.PY3 else (int, long, float)):  # noqa: E501,F821
                timeout = urllib3.Timeout(total=_request_timeout)
            elif (isinstance(_request_timeout, tuple) and
                  len(_request_timeout) == 2):
                timeout = urllib3.Timeout(
                    connect=_request_timeout[0], read=_request_timeout[1])
            elif isinstance(_request_timeout, urllib3.Timeout):
                timeout = _request_timeout
        else:
            timeout = self.pool_manager.connection_pool_kw.get('timeout', None)

        if 'Content-Type' not in headers:
            headers['Content-Type'] = 'application/json'

        log_request(method, url, query_params, headers, body, post_params, timeout)

        try:
            # For `POST`, `PUT`, `PATCH`, `OPTIONS`, `DELETE`
            if method in ['POST', 'PUT', 'PATCH', 'OPTIONS', 'DELETE']:
                if query_params:
                    url += '?' + urlencode(query_params)
                if re.search('json', headers['Content-Type'], re.IGNORECASE):
                    request_body = '{}'
                    if body is not None:
                        request_body = json.dumps(body)
                    r = self._pool_request(
                        method, url,
                        body=request_body,
                        preload_content=False,
                        timeout=timeout,
                        headers=headers)
                elif headers['Content-Type'] == 'application/x-www-form-urlencoded':  # noqa: E501
                    r = self._pool_request(
                        method, url,
                        fields=post_params,
                        encode_multipart=False,
                        preload_content=False,
                        timeout=timeout,
                        headers=headers)
                elif headers['Content-Type'] == 'multipart/form-data':
                    # must del headers['Content-Type'], or the correct
                    # Content-Type which generated by urllib3 will be
                    # overwritten.
                    del headers['Content-Type']
                    r = self._pool_request(
                        method, url,
                        fields=post_params,
                        encode_multipart=True,
                        preload_content=False,
                        timeout=timeout,
                        headers=headers)
                # Pass a `string` parameter directly in the body to support
                # other content types than Json when `body` argument is
                # provided in serialized form
                elif isinstance(body, str):
                    request_body = body
                    r = self._pool_request(
                        method, url,
                        body=request_body,
                        preload_content=False,
                        timeout=timeout,
                        headers=headers)
                else:
                    # Cannot generate the request from given parameters
                    msg = """Cannot prepare a request message for provided
                             arguments. Please check that your arguments match
                             declared content type."""
                    raise ApiException(status=0, reason=msg)
            # For `GET`, `HEAD`
            else:
                r = self._pool_request(method, url,
                                              fields=query_params,
                                              preload_content=False,
                                              timeout=timeout,
                                              headers=headers)
        except urllib3.exceptions.SSLError as e:
            msg = "{0}\n{1}".format(type(e).__name__, str(e))
            raise ApiException(status=0, reason=msg, cause=e)

        if _preload_content or not 200 <= r.status <= 299:
            # Obtain the response headers before reading. read1 (urllib3 2.x)
            # returns available bytes without waiting to fill the whole chunk,
            # allowing a truncated body to retain the bytes already received.
            chunks = []
            try:
                if hasattr(r, "enforce_content_length"):
                    r.enforce_content_length = True
                read1 = getattr(r, "read1", None)
                if read1 is not None:
                    content = iter(lambda: read1(65536), b"")
                elif isinstance(r, urllib3.HTTPResponse):
                    # urllib3 1.26 may consume compressed bytes without
                    # producing output; stream() skips that output until EOF.
                    content = r.stream(65536, decode_content=True)
                else:
                    content = iter(lambda: r.read(65536), b"")
                for chunk in content:
                    chunks.append(chunk)
            except Exception as e:
                partial = getattr(e, "partial", None)
                if not isinstance(partial, bytes):
                    for argument in getattr(e, "args", ()):
                        candidate = getattr(argument, "partial", None)
                        if isinstance(candidate, bytes):
                            partial = candidate
                            break
                # IncompleteRead.partial is from the raw transport. It must
                # not be appended to chunks that have already been decoded.
                if isinstance(partial, bytes) and not r.headers.get("Content-Encoding"):
                    chunks.append(partial)
                try:
                    r.close()
                finally:
                    r.release_conn()
                raise ApiException(
                    status=r.status, reason="Failed to read response body: {0}".format(e),
                    body=b"".join(chunks), headers=r.headers, cause=e,
                    code="ReadError", response_details=self._snapshot(r, b"".join(chunks), False))
            except BaseException:
                try:
                    r.close()
                finally:
                    r.release_conn()
                raise
            r.release_conn()
            r = RESTResponse(r, b"".join(chunks))

            # In the python 3, the response.data is bytes.
            # we need to decode it to string.
            if six.PY3 and not (_response_type == "file" and 200 <= r.status <= 299):
                try:
                    r.data = r.data.decode('utf8')
                except UnicodeDecodeError as e:
                    raise ApiException(
                        status=r.status, reason="Failed to decode response body as UTF-8: {0}".format(e),
                        body=r.data, headers=r.getheaders(), cause=e,
                        code="SerializationError", response_details=r._response_details)

            # log response body
            logger.debug("response body: %s", r.data)
        log_response(r, _preload_content)
        if not 200 <= r.status <= 299:
            raise ApiException(http_resp=r)

        return r

    def _pool_request(self, *args, **kwargs):
        # Normalize only STS failures from the actual HTTP transport. Signing,
        # request preparation and customer request overrides remain untouched.
        try:
            return self.pool_manager.request(*args, **kwargs)
        except urllib3.exceptions.SSLError:
            raise
        except (urllib3.exceptions.HTTPError, IOError, OSError) as error:
            if getattr(self, "_sts_network_errors", False):
                raise ApiException(status=0, reason=str(error), cause=error, code="RequestError")
            raise

    @staticmethod
    def _snapshot(response, body, complete):
        from volcenginesdkcore.error_details import snapshot_response
        return snapshot_response(response, body, complete)

    def GET(self, url, headers=None, query_params=None, _preload_content=True,
            _request_timeout=None):
        return self.request("GET", url,
                            headers=headers,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            query_params=query_params)

    def HEAD(self, url, headers=None, query_params=None, _preload_content=True,
             _request_timeout=None):
        return self.request("HEAD", url,
                            headers=headers,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            query_params=query_params)

    def OPTIONS(self, url, headers=None, query_params=None, post_params=None,
                body=None, _preload_content=True, _request_timeout=None):
        return self.request("OPTIONS", url,
                            headers=headers,
                            query_params=query_params,
                            post_params=post_params,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            body=body)

    def DELETE(self, url, headers=None, query_params=None, body=None,
               _preload_content=True, _request_timeout=None):
        return self.request("DELETE", url,
                            headers=headers,
                            query_params=query_params,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            body=body)

    def POST(self, url, headers=None, query_params=None, post_params=None,
             body=None, _preload_content=True, _request_timeout=None):
        return self.request("POST", url,
                            headers=headers,
                            query_params=query_params,
                            post_params=post_params,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            body=body)

    def PUT(self, url, headers=None, query_params=None, post_params=None,
            body=None, _preload_content=True, _request_timeout=None):
        return self.request("PUT", url,
                            headers=headers,
                            query_params=query_params,
                            post_params=post_params,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            body=body)

    def PATCH(self, url, headers=None, query_params=None, post_params=None,
              body=None, _preload_content=True, _request_timeout=None):
        return self.request("PATCH", url,
                            headers=headers,
                            query_params=query_params,
                            post_params=post_params,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            body=body)


class ApiException(Exception):

    def __init__(self, status=None, reason=None, http_resp=None, body=None,
                 headers=None, response_metadata=None, cause=None,
                 previous_exception=None, code=None, message=None, response_details=None):
        self.cause = cause
        self.previous_exception = previous_exception
        # Attribute assignment keeps Python 2 syntax compatibility while
        # exposing the standard exception chain on Python 3.
        if cause is not None:
            self.__cause__ = cause
        if http_resp is not None:
            self.status = http_resp.status
            self.reason = http_resp.reason
            self.body = http_resp.data
            self.headers = http_resp.getheaders()
        else:
            self.status = status
            self.reason = reason
            self.body = body
            self.headers = headers
        from volcenginesdkcore.metadata import (
            ResponseMetadata, ensure_response_metadata, get_response_metadata,
        )
        # Apply the same fallback for response-based and manual construction.
        # Never add an id to the caller's metadata object in place.
        metadata = copy.copy(response_metadata) if isinstance(
            response_metadata, ResponseMetadata) else None
        try:
            body_metadata = get_response_metadata(json.loads(self.body))
        except Exception:
            body_metadata = None
        if body_metadata is not None:
            if metadata is None:
                metadata = body_metadata
            else:
                for field in ResponseMetadata.swagger_types:
                    value = getattr(body_metadata, field)
                    if value and (field == "request_id" or not getattr(metadata, field)):
                        setattr(metadata, field, value)
        self.response_metadata = ensure_response_metadata(metadata, self.headers)
        from volcenginesdkcore.error_details import (
            ResponseDetails, classify_top, snapshot_response,
        )
        self.code, self.message = classify_top(self.body) if self.body is not None else (
            "RequestError" if not self.status else "UnknownError", self.reason)
        if code is not None:
            self.code = code
            self.message = self.reason
        if message is not None:
            self.message = message
        self._response_details = copy.deepcopy(response_details)
        if self._response_details is None:
            if http_resp is not None:
                self._response_details = snapshot_response(http_resp)
            elif self.status or self.body is not None or self.headers:
                self._response_details = ResponseDetails(
                    status_code=self.status or 0, headers=self.headers, body=self.body,
                    body_captured=self.body is not None, body_complete=self.body is not None)
        if self._response_details is not None:
            request_id = getattr(self.response_metadata, "request_id", None)
            if request_id:
                self._response_details.request_id = request_id

    @property
    def response_details(self):
        """Return a copy of the captured response; never read the stream."""
        return copy.deepcopy(getattr(self, "_response_details", None))

    def __str__(self):
        """Custom error messages for exception"""
        error_message = "({0})\n" \
                        "Reason: {1}\n".format(self.status, self.reason)
        request_id = getattr(getattr(self, "response_metadata", None), "request_id", None)
        if request_id:
            error_message += "RequestId: {0}\n".format(request_id)

        if self.headers:
            error_message += "HTTP response headers: {0}\n".format(
                self.headers)

        if self.body:
            error_message += "HTTP response body: {0}\n".format(self.body)

        return error_message
