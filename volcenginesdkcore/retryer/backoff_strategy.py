# coding: utf-8

import random
from abc import abstractmethod

from volcenginesdkcore.utils import six_utils


class BackoffStrategy(six_utils.get_abstract_meta_class()):
    """
    Abstract base class for all backoff strategies.
    Defines the interface for computing retry delays.
    """

    def __init__(self,
                 min_retry_delay_ms=30,
                 max_retry_delay_ms=300 * 1000
                 ):
        # type:(float, float) -> None
        """
        Initializes the BackoffStrategy with a min_retry_delay_ms and max_retry_delay_ms values.
        Args:
            :param min_retry_delay_ms: The minimum retry delay in milliseconds.
            :param max_retry_delay_ms: The maximum retry delay in milliseconds.
       """
        self.min_retry_delay_ms = min_retry_delay_ms
        self.max_retry_delay_ms = max_retry_delay_ms

    @abstractmethod
    def compute_delay(self, retry_count):
        # type: (int) -> float
        """
        Args:
            :param retry_count: The number of retries.
        Returns:
            float: The computed delay in milliseconds.
        """
        pass


class NoBackoffStrategy(BackoffStrategy):
    """
    A backoff strategy that implements no delay between retries.
    """

    def compute_delay(self, retry_count):
        # type: (int) -> float
        """
        Args:
            :param retry_count: The number of retries.
        Returns:
            float: The computed delay in milliseconds.
        """
        return 0.0


class ExponentialBackoffStrategy(BackoffStrategy):
    """
    A backoff strategy that increases the delay exponentially with each retry.
    The delay is calculated as: min_retry_delay_ms * (2 ** retry_count),
    capped by max_retry_delay_ms.
    """

    def compute_delay(self, retry_count):
        # type: (int) -> float
        """
        Args:
            :param retry_count: The number of retries.
        Returns:
            float: The computed delay in milliseconds.
        """
        min_retry_delay_ms = self.min_retry_delay_ms
        max_retry_delay_ms = self.max_retry_delay_ms
        delay = min(min_retry_delay_ms * (2 ** retry_count), max_retry_delay_ms)
        return delay


class ExponentialWithRandomJitterBackoffStrategy(ExponentialBackoffStrategy):
    """
    An exponential backoff strategy with random jitter.
    The delay is calculated as: base + random_uniform(0, base),
    capped by max_retry_delay_ms.
    This effectively means the delay is a random value between base and 2*base,
    then capped by max_retry_delay_ms.
    """

    def compute_delay(self, retry_count):
        # type: (int) -> float
        """
        Args:
            :param retry_count: The number of retries.
        Returns:
            float: The computed delay in milliseconds.
        """
        base = super(ExponentialWithRandomJitterBackoffStrategy, self).compute_delay(retry_count)
        jitter = base + random.uniform(0, base)
        max_retry_delay_ms = self.max_retry_delay_ms
        return min(max_retry_delay_ms, jitter)
