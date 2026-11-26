# coding: utf-8
"""STS validation and diagnostics shared by the three credential providers."""
from __future__ import absolute_import

from datetime import datetime

import dateutil.parser
import dateutil.tz
import six

from volcenginesdkcore.error_details import snapshot_response
from volcenginesdkcore.rest import ApiException
from volcenginesdkcore.retryer.retry_condition import DefaultRetryCondition


class StsRetryCondition(DefaultRetryCondition):
    _DefaultRetryCondition__retry_status_codes = {"429", "502", "503", "504"}

    def __init__(self):
        super(StsRetryCondition, self).__init__({
            "ProvisionedThroughputExceededException", "Throttling", "ThrottlingException",
            "RequestLimitExceeded", "RequestThrottled", "RequestThrottledException",
            "TooManyRequestsException", "PriorRequestNotComplete",
            "TransactionInProgressException", "RequestError", "RequestTimeout",
            "ResponseTimeout", "RequestTimeoutException",
        })

    def _is_retryable_api_error_code(self, error, code):
        # A no-response classification is not a service business code, even
        # when nested inside a customer wrapper. Network causes are checked
        # separately; TLS/proxy rejection must not re-enter the code whitelist.
        if not getattr(error, "status", 0):
            return False
        return super(StsRetryCondition, self)._is_retryable_api_error_code(error, code)


class StsResult(dict):
    def __init__(self, result, response):
        super(StsResult, self).__init__(result)
        self._response_details = snapshot_response(response)


def parse_sts_credentials(result, expiration_key, response=None, status=0, headers=None,
                          fallback_key=None):
    """Validate all fields before either credential cache field is published."""
    details = snapshot_response(response) if response is not None else getattr(result, "_response_details", None)
    if details is not None:
        status, headers = details.status_code, details.headers
    body = details.body if details is not None else None

    def failure(code, message, cause=None):
        return ApiException(status=status, reason=message, body=body, headers=headers,
                            code=code, cause=cause, response_details=details)

    credentials = result.get("Credentials") if isinstance(result, dict) else None
    if isinstance(credentials, dict) and expiration_key not in credentials and fallback_key:
        expiration_key = fallback_key
    fields = ("AccessKeyId", "SecretAccessKey", "SessionToken", expiration_key)
    if not isinstance(credentials, dict) or any(
            not isinstance(credentials.get(key), six.string_types) or not credentials[key]
            for key in fields):
        raise failure("UnknownError", "failed to retrieve complete credentials from sts")
    try:
        expiration = dateutil.parser.parse(credentials[expiration_key])
        timestamp = (expiration - datetime(1970, 1, 1, tzinfo=dateutil.tz.tzutc())).total_seconds()
    except (ValueError, TypeError, OverflowError) as error:
        raise failure("SerializationError", "Failed to parse STS credential expiration: {}".format(error), error)
    return credentials, timestamp
