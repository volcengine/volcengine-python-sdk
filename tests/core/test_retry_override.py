# coding: utf-8
"""Regression tests for per-request retry overrides on top of custom retry objects.

These tests never touch the network: ``ApiClient.request`` is replaced with a stub
that fails once with HTTP 500 and then succeeds.
"""
import unittest

import volcenginesdkcore
import volcenginesdkcore.api_client as api_client_module
from volcenginesdkcore import rest
from volcenginesdkcore.api_client import ApiClient
from volcenginesdkcore.interceptor.interceptors.request import RuntimeOption
from volcenginesdkcore.retryer.backoff_strategy import (
    BackoffStrategy,
    ExponentialBackoffStrategy,
    NoBackoffStrategy,
)
from volcenginesdkcore.retryer.retry_condition import DefaultRetryCondition
from volcenginesdkcore.retryer.retryer import new_backoff_strategy, new_retry_condition
import volcenginesdkbilling


class SubclassBackoff(ExponentialBackoffStrategy):
    """Documented pattern: reuse a built-in strategy."""

    def compute_delay(self, retry_count):
        return 0.0


class PlainBackoff(BackoffStrategy):
    """Documented pattern: implement BackoffStrategy directly."""

    def compute_delay(self, retry_count):
        return 0.0


class SubclassCondition(DefaultRetryCondition):
    """Documented pattern: reuse the default condition."""

    def should_retry(self, response, err):
        return super(SubclassCondition, self).should_retry(response, err)


class _FakeHttpResponse(object):
    def __init__(self, status, data):
        self.status = status
        self.reason = 'stub'
        self.data = data
        self.headers = {}


_OK = '{"ResponseMetadata":{"RequestId":"r"},"Result":{}}'
_ERR = '{"ResponseMetadata":{"RequestId":"r","Error":{"Code":"InternalError","Message":"m"}}}'


class RetryOverrideTest(unittest.TestCase):

    def setUp(self):
        self._orig_request = ApiClient.request
        self._orig_sleep = api_client_module.sleep
        self._orig_default = volcenginesdkcore.Configuration._default
        api_client_module.sleep = lambda seconds: None
        self.attempts = []
        self.effective_retryers = []

        tests = self

        def request(client, method, url, query_params=None, headers=None, post_params=None, body=None,
                    _preload_content=True, _request_timeout=None):
            tests.attempts.append(dict(headers))
            status = 500 if len(tests.attempts) == 1 else 200
            resp = rest.RESTResponse(_FakeHttpResponse(status, _OK if status == 200 else _ERR))
            if status != 200:
                raise rest.ApiException(http_resp=resp)
            return resp

        ApiClient.request = request

        # capture the retryer actually used by the retry loop
        orig_request_retry = ApiClient.request_retry

        def request_retry(client, response_data, retry_count, retry_err, retryer):
            tests.effective_retryers.append(retryer)
            return orig_request_retry(client, response_data, retry_count, retry_err, retryer)

        self._orig_request_retry = orig_request_retry
        ApiClient.request_retry = request_retry

        volcenginesdkcore.Configuration._default = None
        self.configuration = volcenginesdkcore.Configuration()
        self.configuration.ak = 'ak'
        self.configuration.sk = 'sk'
        self.configuration.region = 'cn-beijing'

    def tearDown(self):
        ApiClient.request = self._orig_request
        ApiClient.request_retry = self._orig_request_retry
        api_client_module.sleep = self._orig_sleep
        volcenginesdkcore.Configuration._default = self._orig_default

    def _call(self, runtime_option=None):
        volcenginesdkcore.Configuration.set_default(self.configuration)
        api = volcenginesdkbilling.BILLINGApi()
        api.query_balance_acct(volcenginesdkbilling.QueryBalanceAcctRequest(_configuration=runtime_option))
        self.assertEqual(2, len(self.attempts))
        # request_retry is consulted after every attempt (500 -> retry, 200 -> stop)
        self.assertEqual(2, len(self.effective_retryers))
        self.assertIs(self.effective_retryers[0], self.effective_retryers[1])
        return self.effective_retryers[0]

    # -- documented custom subclasses on Configuration + RuntimeOption scalars ------------------

    def test_subclass_backoff_with_runtime_min_max(self):
        original = SubclassBackoff(min_retry_delay_ms=1, max_retry_delay_ms=2)
        self.configuration.backoff_strategy = original
        retryer = self._call(RuntimeOption(True, min_retry_delay_ms=11, max_retry_delay_ms=22))
        used = retryer.backoff_strategy
        self.assertIsInstance(used, SubclassBackoff)
        self.assertEqual((11, 22), (used.min_retry_delay_ms, used.max_retry_delay_ms))
        self.assertIsNot(original, used)
        self.assertEqual((1, 2), (original.min_retry_delay_ms, original.max_retry_delay_ms))

    def test_plain_backoff_with_runtime_max(self):
        original = PlainBackoff(min_retry_delay_ms=1, max_retry_delay_ms=2)
        self.configuration.backoff_strategy = original
        retryer = self._call(RuntimeOption(True, max_retry_delay_ms=22))
        used = retryer.backoff_strategy
        self.assertIsInstance(used, PlainBackoff)
        self.assertEqual((1, 22), (used.min_retry_delay_ms, used.max_retry_delay_ms))
        self.assertEqual(2, original.max_retry_delay_ms)

    def test_subclass_condition_with_runtime_error_codes(self):
        original = SubclassCondition(retry_error_codes={'Base'})
        self.configuration.retry_condition = original
        retryer = self._call(RuntimeOption(True, retry_error_codes={'Override'}))
        used = retryer.retry_condition
        self.assertIsInstance(used, SubclassCondition)
        self.assertEqual({'Override'}, used.retry_error_codes)
        self.assertIsNot(original, used)
        self.assertEqual({'Base'}, original.retry_error_codes)

    def test_runtime_custom_objects_with_scalars(self):
        retryer = self._call(RuntimeOption(True,
                                           backoff_strategy=SubclassBackoff(),
                                           min_retry_delay_ms=5,
                                           retry_condition=SubclassCondition(),
                                           retry_error_codes={'X'}))
        self.assertEqual(5, retryer.backoff_strategy.min_retry_delay_ms)
        self.assertEqual({'X'}, retryer.retry_condition.retry_error_codes)

    # -- identity is preserved when no scalar override is requested ------------------------------

    def test_custom_objects_keep_identity_without_scalars(self):
        strategy = PlainBackoff()
        condition = SubclassCondition()
        self.configuration.backoff_strategy = strategy
        self.configuration.retry_condition = condition
        retryer = self._call(RuntimeOption(True, num_max_retries=2))
        self.assertIs(strategy, retryer.backoff_strategy)
        self.assertIs(condition, retryer.retry_condition)
        self.assertEqual(2, retryer.num_max_retries)

    # -- built-in behaviour unchanged --------------------------------------------------------------

    def test_builtin_with_scalars_unchanged(self):
        self.configuration.backoff_strategy = NoBackoffStrategy()
        retryer = self._call(RuntimeOption(True, min_retry_delay_ms=7, retry_error_codes={'Y'}))
        self.assertIs(NoBackoffStrategy, type(retryer.backoff_strategy))
        self.assertEqual(7, retryer.backoff_strategy.min_retry_delay_ms)
        self.assertIs(DefaultRetryCondition, type(retryer.retry_condition))
        self.assertEqual({'Y'}, retryer.retry_condition.retry_error_codes)

    # -- factory-level unit checks -----------------------------------------------------------------

    def test_factories_never_raise_for_custom_objects(self):
        strategy = PlainBackoff(min_retry_delay_ms=1, max_retry_delay_ms=2)
        copied = new_backoff_strategy(strategy, min_retry_delay_ms=3)
        self.assertIsNot(strategy, copied)
        self.assertEqual((3, 2), (copied.min_retry_delay_ms, copied.max_retry_delay_ms))
        self.assertIs(strategy, new_backoff_strategy(strategy))
        self.assertIsNone(new_backoff_strategy(None, min_retry_delay_ms=3))

        condition = SubclassCondition(retry_error_codes={'A'})
        copied = new_retry_condition(condition, retry_error_codes=['B'])
        self.assertIsNot(condition, copied)
        self.assertEqual({'B'}, copied.retry_error_codes)
        self.assertEqual({'A'}, condition.retry_error_codes)
        self.assertIs(condition, new_retry_condition(condition))
        self.assertIsNone(new_retry_condition(None, retry_error_codes={'B'}))


if __name__ == '__main__':
    unittest.main()
