import json
import logging
import socket
import traceback
from abc import abstractmethod

import urllib3

from volcenginesdkcore.rest import ApiException, RESTResponse
from volcenginesdkcore.utils import six_utils

logger = logging.getLogger(__name__)


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
        if err is not None and isinstance(err, self.__retry_exceptions):
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
            return True
        # retryable error code
        code = None
        metadata = data.get("ResponseMetadata")
        if metadata:
            error = metadata.get("Error")
            if error:
                code = error.get("Code")
        if code in self.retry_error_codes:
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
            return json.loads(data)
        except Exception as e:
            logger.warning("Failed to parse response data as JSON: {}".format(e))
            logger.warning(traceback.format_exc())
        return {}
