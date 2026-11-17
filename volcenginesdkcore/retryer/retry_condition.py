import errno
import json
import logging
import socket
import ssl
import traceback
from abc import abstractmethod

import urllib3
import six
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
        for wrapped in self._walk_exceptions(err):
            if isinstance(wrapped, ApiException):
                if str(wrapped.status) in self.__retry_status_codes:
                    return True
                from volcenginesdkcore.error_details import classify_top
                wrapped_code = getattr(wrapped, "code", None)
                if wrapped_code is None:
                    wrapped_code = classify_top(getattr(wrapped, "body", None))[0]
                if self._is_retryable_api_error_code(wrapped, wrapped_code):
                    return True

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
        if isinstance(metadata, dict):
            error = metadata.get("Error")
            if isinstance(error, dict):
                code = error.get("Code")
        if isinstance(code, six.string_types) and code in self.retry_error_codes:
            sdk_core_logger.debug_retry("retry for retryable error code, code: %s", code)
            return True

        sdk_core_logger.debug_retry( "no need to retry")

        return False

    def _is_retryable_api_error_code(self, error, code):
        return isinstance(code, six.string_types) and code in self.retry_error_codes

    @classmethod
    def _walk_exceptions(cls, err):
        from volcenginesdkcore.error_details import exception_causes
        pending = [(err, 0)]
        seen = set()
        while pending and len(seen) < 256:
            current, depth = pending.pop()
            if not isinstance(current, BaseException) or id(current) in seen or depth >= 64:
                continue
            seen.add(id(current))
            yield current
            if isinstance(current, (ssl.SSLError, urllib3.exceptions.SSLError)):
                continue
            if isinstance(current, urllib3.exceptions.ProxyError):
                children = (current.original_error,)
            elif isinstance(current, urllib3.exceptions.MaxRetryError):
                children = (current.reason,)
            else:
                children = exception_causes(current, include_previous=False)
            for child in children:
                if len(pending) + len(seen) >= 256:
                    break
                pending.append((child, depth + 1))

    @classmethod
    def _is_retryable_exception(cls, err):
        # Retry the underlying connection failure, not every proxy failure.
        # In particular, a CONNECT 407 or a TLS/configuration error must stop.
        for current in cls._walk_exceptions(err):
            if isinstance(current, (ssl.SSLError, urllib3.exceptions.SSLError)):
                continue
            if isinstance(current, cls.__retry_exceptions):
                return True
            if isinstance(current, BadStatusLine) and current.line in ("", "''"):
                return True
            if isinstance(current, socket.error) and current.errno in (
                    errno.ECONNRESET, errno.ECONNREFUSED, errno.ECONNABORTED,
                    errno.EPIPE, errno.ETIMEDOUT, errno.ENETUNREACH, errno.EHOSTUNREACH):
                return True
        return False

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
            parsed = json.loads(data)
            return parsed if isinstance(parsed, dict) else {}
        except Exception as e:
            sdk_core_logger.debug_retry("Failed to parse response data as JSON: {}".format(e))
            sdk_core_logger.debug_retry(traceback.format_exc())
        return {}
