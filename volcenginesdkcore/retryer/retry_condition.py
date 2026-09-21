import errno
import json
import logging
import socket
import ssl
import traceback
from abc import abstractmethod

import urllib3
from six.moves.http_client import BadStatusLine

from volcenginesdkcore.rest import ApiException, RESTResponse
from volcenginesdkcore.utils import six_utils
from volcenginesdkcore.observability.debugger import sdk_core_logger



class RetryCondition(six_utils.get_abstract_meta_class()):
    def __init__(self, retry_error_codes=None):
        # type: (set[str]) -> None
        """
        RetryCondition is the condition for the retryer.
        Args:
            :param retry_error_codes: The retry error codes.
        """
        if retry_error_codes is None:
            retry_error_codes = {}
        self.retry_error_codes = set(retry_error_codes)

    @abstractmethod
    def should_retry(self, response, err):
        # type: (RESTResponse, Exception) -> bool
        """
        should_retry checks if the request should be retried.
        Args:
            :param response: The response from the request.
            :param err: The error from the request.
        Returns:
            bool: True if the request should be retried, False otherwise.
        """
        pass


class DefaultRetryCondition(RetryCondition):
    """
        Standard retryable HTTP status codes:
        __retry_status_codes:
            - 429: Too Many Requests (rate limiting)
            - 502: Bad Gateway (upstream server error)
            - 503: Service Unavailable (temporary outage)
            - 504: Gateway Timeout (upstream server timeout)
        """
    __retry_status_codes = {"429", "502", "503", "504", "500"}
    __retry_exceptions = (
        # urllib3
        urllib3.exceptions.NewConnectionError,
        urllib3.exceptions.ConnectTimeoutError,
        urllib3.exceptions.ReadTimeoutError,
        urllib3.exceptions.ProtocolError,

        # builtin / socket
        socket.timeout,
        socket.gaierror,
    )

    def should_retry(
            self,
            response,
            err
    ):
        # type: (RESTResponse, Exception) -> bool
        """
        should_retry checks if the request should be retried.
        Args:
            :param response: The response from the request.
            :param err: The error from the request.
        Returns:
            bool: True if the request should be retried, False otherwise.
        """
        if err is not None and self._is_retryable_exception(err):
            sdk_core_logger.debug_retry("retry for retryable exception, err: %s", err)
            return True

        data = {}
        status_code = None
        if isinstance(err, ApiException):
            status_code = err.status
            data = DefaultRetryCondition.__json_loads(err.body)

        if isinstance(response, RESTResponse):
            status_code = response.status
            data = DefaultRetryCondition.__json_loads(response.data)

        # retryable status code
        if str(status_code) in self.__retry_status_codes:
            sdk_core_logger.debug_retry("retry for retryable status code, status_code: %s", status_code)
            return True
        # retryable error code
        code = None
        metadata = data.get("ResponseMetadata")
        if metadata:
            error = metadata.get("Error")
            if error:
                code = error.get("Code")
        if code in self.retry_error_codes:
            sdk_core_logger.debug_retry("retry for retryable error code, code: %s", code)
            return True

        sdk_core_logger.debug_retry( "no need to retry")

        return False

    @classmethod
    def _is_retryable_exception(cls, err):
        # Retry the underlying connection failure, not every proxy failure.
        # In particular, a CONNECT 407 or a TLS/configuration error must stop.
        seen = set()
        while isinstance(err, (urllib3.exceptions.ProxyError, urllib3.exceptions.MaxRetryError)):
            if id(err) in seen:
                return False
            seen.add(id(err))
            if isinstance(err, urllib3.exceptions.ProxyError):
                err = err.original_error
            else:
                err = err.reason
        if isinstance(err, (ssl.SSLError, urllib3.exceptions.SSLError)):
            return False
        if isinstance(err, cls.__retry_exceptions):
            return True
        # RemoteDisconnected on Python 3, empty BadStatusLine on Python 2.
        if isinstance(err, BadStatusLine) and err.line in ("", "''"):
            return True
        return isinstance(err, socket.error) and err.errno in (
            errno.ECONNRESET, errno.ECONNREFUSED, errno.ECONNABORTED,
            errno.EPIPE, errno.ETIMEDOUT, errno.ENETUNREACH, errno.EHOSTUNREACH,
        )

    @staticmethod
    def __json_loads(data):
        """
        __json_loads loads the response data as JSON.
        Args:
            :param data: The response data.
        Returns:
            dict: The response data as JSON.
        """
        if data is None:
            return {}
        try:
            return json.loads(data)
        except Exception as e:
            sdk_core_logger.debug_retry("Failed to parse response data as JSON: {}".format(e))
            sdk_core_logger.debug_retry(traceback.format_exc())
        return {}
