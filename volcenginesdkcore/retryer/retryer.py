# coding: utf-8
import copy

try:
    from typing import TYPE_CHECKING
except ImportError:
    TYPE_CHECKING = False
from volcenginesdkcore.retryer.backoff_strategy import (
    ExponentialBackoffStrategy,
    ExponentialWithRandomJitterBackoffStrategy,
    NoBackoffStrategy,
)
from volcenginesdkcore.retryer.retry_condition import DefaultRetryCondition

if TYPE_CHECKING:
    from volcenginesdkcore.rest import RESTResponse
    from volcenginesdkcore.retryer.backoff_strategy import BackoffStrategy
    from volcenginesdkcore.retryer.retry_condition import RetryCondition

DEFAULT_NUM_MAX_RETRIES = 3
DEFAULT_MIN_RETRY_DELAY_MS = 300
DEFAULT_MAX_RETRY_DELAY_MS = 300 * 1000
_UNSET = object()

_BUILT_IN_BACKOFF_STRATEGIES = (
    NoBackoffStrategy,
    ExponentialBackoffStrategy,
    ExponentialWithRandomJitterBackoffStrategy,
)


def new_backoff_strategy(backoff_strategy=_UNSET, min_retry_delay_ms=None, max_retry_delay_ms=None):
    if backoff_strategy is _UNSET:
        strategy_type = ExponentialWithRandomJitterBackoffStrategy
        current_min_retry_delay_ms = DEFAULT_MIN_RETRY_DELAY_MS
        current_max_retry_delay_ms = DEFAULT_MAX_RETRY_DELAY_MS
    elif type(backoff_strategy) in _BUILT_IN_BACKOFF_STRATEGIES:
        strategy_type = type(backoff_strategy)
        current_min_retry_delay_ms = backoff_strategy.min_retry_delay_ms
        current_max_retry_delay_ms = backoff_strategy.max_retry_delay_ms
    else:
        # Custom strategy (including subclasses of the built-in ones): keep the
        # caller's instance as-is unless scalar overrides are requested, in which
        # case apply them to a shallow copy so the caller's object is never mutated.
        if backoff_strategy is None or (min_retry_delay_ms is None and max_retry_delay_ms is None):
            return backoff_strategy
        backoff_strategy = copy.copy(backoff_strategy)
        if min_retry_delay_ms is not None:
            backoff_strategy.min_retry_delay_ms = min_retry_delay_ms
        if max_retry_delay_ms is not None:
            backoff_strategy.max_retry_delay_ms = max_retry_delay_ms
        return backoff_strategy

    return strategy_type(
        min_retry_delay_ms=(min_retry_delay_ms
                            if min_retry_delay_ms is not None else current_min_retry_delay_ms),
        max_retry_delay_ms=(max_retry_delay_ms
                            if max_retry_delay_ms is not None else current_max_retry_delay_ms),
    )


def new_retry_condition(retry_condition=_UNSET, retry_error_codes=None):
    if retry_condition is _UNSET:
        return DefaultRetryCondition(retry_error_codes=retry_error_codes)
    if type(retry_condition) is DefaultRetryCondition:
        error_codes = retry_error_codes \
            if retry_error_codes is not None else retry_condition.retry_error_codes
        return DefaultRetryCondition(retry_error_codes=error_codes)
    # Custom condition (including subclasses of DefaultRetryCondition): keep the
    # caller's instance as-is unless retry_error_codes is requested, in which case
    # apply it to a shallow copy so the caller's object is never mutated.
    if retry_condition is None or retry_error_codes is None:
        return retry_condition
    retry_condition = copy.copy(retry_condition)
    retry_condition.retry_error_codes = set(retry_error_codes)
    return retry_condition


def new_retryer(num_max_retries=DEFAULT_NUM_MAX_RETRIES,
                backoff_strategy=_UNSET,
                retry_condition=_UNSET,
                retry_error_codes=None,
                min_retry_delay_ms=None,
                max_retry_delay_ms=None):
    return Retryer(
        num_max_retries=num_max_retries,
        backoff_strategy=new_backoff_strategy(
            backoff_strategy,
            min_retry_delay_ms=min_retry_delay_ms,
            max_retry_delay_ms=max_retry_delay_ms,
        ),
        retry_condition=new_retry_condition(
            retry_condition,
            retry_error_codes=retry_error_codes,
        ),
    )


class Retryer:
    def __init__(
            self,
            num_max_retries=DEFAULT_NUM_MAX_RETRIES,
            backoff_strategy=_UNSET,
            retry_condition=_UNSET,
    ):
        # type: (int, BackoffStrategy, RetryCondition) -> None
        """
        Retryer is the retryer for the SDK.
        Args:
            :param num_max_retries: The maximum number of retries.
            :param backoff_strategy: The backoff strategy to use.
            :param retry_condition: The retry condition to use.
        """
        self.num_max_retries = num_max_retries
        self.backoff_strategy = new_backoff_strategy() \
            if backoff_strategy is _UNSET else backoff_strategy
        self.retry_condition = new_retry_condition() \
            if retry_condition is _UNSET else retry_condition

    def should_retry(
            self,
            response,
            retry_count,
            err
    ):
        # type: (RESTResponse, int, Exception) -> bool
        """
        should_retry checks if the request should be retried.
        Args:
            :param response: The response from the request.
            :param retry_count: The number of retries.
            :param err: The error from the request.
        Returns:
            bool: True if the request should be retried, False otherwise.
        """
        if retry_count < self.num_max_retries and self.retry_condition is not None:
            return self.retry_condition.should_retry(response, err)
        return False

    def get_backoff_delay(
            self,
            retry_count,
    ):
        # type: (int) -> float
        """
        get_backoff_delay returns the backoff delay for the retry.
        Args:
            :param retry_count: The number of retries.
        Returns:
            float: The backoff delay.
        """
        if retry_count >= self.num_max_retries:
            raise ValueError("Retry count exceeds maximum limit")
        if self.backoff_strategy is not None:
            return self.backoff_strategy.compute_delay(retry_count)
        return 0.0


DEFAULT_RETRYER = Retryer()
