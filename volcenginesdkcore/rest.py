# coding: utf-8

from __future__ import absolute_import

import io
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

    def __init__(self, resp):
        self.urllib3_response = resp
        self.status = resp.status
        self.reason = resp.reason
        self.data = resp.data

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
    sdk_core_logger.debugx(LogLevel.LOG_DEBUG_WITH_REQUEST_ID, "[Response] request id: %s", r.getheader("X-Tt-Logid"))
    sdk_core_logger.debug_response("status: %s", r.status)
    sdk_core_logger.debug_response("reason: %s", r.reason)
    sdk_core_logger.debug_response("headers:")
    for k, v in r.getheaders().items():
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
                cached = getattr(r, "data", b"")
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
            self.pool_manager = urllib3.ProxyManager(
                num_pools=pools_size,
                maxsize=maxsize,
                cert_reqs=cert_reqs,
                ca_certs=ca_certs,
                cert_file=configuration.cert_file,
                key_file=configuration.key_file,
                proxy_url=proxy_url,
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

    def request(self, method, url, query_params=None, headers=None,
                body=None, post_params=None, _preload_content=True,
                _request_timeout=None):
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
                    r = self.pool_manager.request(
                        method, url,
                        body=request_body,
                        preload_content=_preload_content,
                        timeout=timeout,
                        headers=headers)
                elif headers['Content-Type'] == 'application/x-www-form-urlencoded':  # noqa: E501
                    r = self.pool_manager.request(
                        method, url,
                        fields=post_params,
                        encode_multipart=False,
                        preload_content=_preload_content,
                        timeout=timeout,
                        headers=headers)
                elif headers['Content-Type'] == 'multipart/form-data':
                    # must del headers['Content-Type'], or the correct
                    # Content-Type which generated by urllib3 will be
                    # overwritten.
                    del headers['Content-Type']
                    r = self.pool_manager.request(
                        method, url,
                        fields=post_params,
                        encode_multipart=True,
                        preload_content=_preload_content,
                        timeout=timeout,
                        headers=headers)
                # Pass a `string` parameter directly in the body to support
                # other content types than Json when `body` argument is
                # provided in serialized form
                elif isinstance(body, str):
                    request_body = body
                    r = self.pool_manager.request(
                        method, url,
                        body=request_body,
                        preload_content=_preload_content,
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
                r = self.pool_manager.request(method, url,
                                              fields=query_params,
                                              preload_content=_preload_content,
                                              timeout=timeout,
                                              headers=headers)
        except urllib3.exceptions.SSLError as e:
            msg = "{0}\n{1}".format(type(e).__name__, str(e))
            raise ApiException(status=0, reason=msg)

        if _preload_content:
            r = RESTResponse(r)

            # In the python 3, the response.data is bytes.
            # we need to decode it to string.
            if six.PY3:
                r.data = r.data.decode('utf8')

            # log response body
            logger.debug("response body: %s", r.data)
        log_response(r, _preload_content)
        if not 200 <= r.status <= 299:
            raise ApiException(http_resp=r)

        return r

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

    def __init__(self, status=None, reason=None, http_resp=None):
        if http_resp:
            self.status = http_resp.status
            self.reason = http_resp.reason
            self.body = http_resp.data
            self.headers = http_resp.getheaders()
        else:
            self.status = status
            self.reason = reason
            self.body = None
            self.headers = None

    def __str__(self):
        """Custom error messages for exception"""
        error_message = "({0})\n" \
                        "Reason: {1}\n".format(self.status, self.reason)
        if self.headers:
            error_message += "HTTP response headers: {0}\n".format(
                self.headers)

        if self.body:
            error_message += "HTTP response body: {0}\n".format(self.body)

        return error_message
