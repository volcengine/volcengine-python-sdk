# coding: utf-8
from typing import TYPE_CHECKING
from volcenginesdkcore.retryer.backoff_strategy import ExponentialWithRandomJitterBackoffStrategy
from volcenginesdkcore.retryer.retry_condition import DefaultRetryCondition

if TYPE_CHECKING:
    from volcenginesdkcore.rest import RESTResponse
    from volcenginesdkcore.retryer.backoff_strategy import BackoffStrategy
    from volcenginesdkcore.retryer.retry_condition import RetryCondition

_DEFAULT_BACKOFF_STRATEGY = ExponentialWithRandomJitterBackoffStrategy(
    min_retry_delay_ms=300,
    max_retry_delay_ms=300 * 1000,
)

_DEFAULT_RETRY_CONDITION = DefaultRetryCondition(retry_error_codes=set())


class Retryer:
    def __init__(
            self,
            num_max_retries=3,
            backoff_strategy=_DEFAULT_BACKOFF_STRATEGY,
            retry_condition=_DEFAULT_RETRY_CONDITION,
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
        self.backoff_strategy = backoff_strategy
        self.retry_condition = retry_condition

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
