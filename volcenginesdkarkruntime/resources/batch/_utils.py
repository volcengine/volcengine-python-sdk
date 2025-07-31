import asyncio
import logging
import time
from datetime import datetime, timedelta
from random import random
from typing import Any, Awaitable, Callable, Optional, TypeVar

import httpx

from ..._constants import INITIAL_RETRY_DELAY, MAX_RETRY_DELAY
from ..._exceptions import ArkAPIConnectionError, ArkAPIStatusError, ArkAPITimeoutError
from ..._utils._model_breaker import ModelBreaker

log: logging.Logger = logging.getLogger(__name__)


def _calculate_retry_timeout(retry_times: int) -> float:
    nbRetries = min(retry_times, MAX_RETRY_DELAY / INITIAL_RETRY_DELAY)
    sleep_seconds = min(INITIAL_RETRY_DELAY * pow(2, nbRetries), MAX_RETRY_DELAY)
    # Apply some jitter, plus-or-minus half a second.
    jitter = 1 - 0.25 * random()
    timeout = sleep_seconds * jitter
    return timeout if timeout >= 0 else 0


def _get_retry_after(response: httpx.Response) -> Optional[int]:
    retry_after = response.headers.get("Retry-After")
    if retry_after is not None:
        if retry_after.isdigit():
            return int(retry_after)
    return None


def _should_retry(response: httpx.Response) -> bool:
    # Retry on request timeouts.
    if response.status_code == 408:
        return True

    # Retry on lock timeouts.
    if response.status_code == 409:
        return True

    # Retry on rate limits.
    if response.status_code == 429:
        return True

    # Retry internal errors.
    if response.status_code >= 500:
        return True

    return False


def get_request_last_time(
    client: httpx.Client, timeout: Optional[Any] = None
) -> datetime:
    if timeout is None:
        timeout = client.timeout
    timeoutSeconds = 0
    if isinstance(timeout, httpx.Timeout):
        timeoutSeconds = timeout.read
    elif isinstance(timeout, float):
        timeoutSeconds = timeout
    elif isinstance(timeout, int):
        timeoutSeconds = timeout
    else:
        raise TypeError("timeout type {} is not supported".format(type(timeout)))
    return datetime.now() + timedelta(seconds=timeoutSeconds)


R = TypeVar("R")


def with_batch_retry(
    deadline: datetime,
    breaker: ModelBreaker,
    func: Callable[..., R],
    *args,
    **kwargs,
) -> R:
    retry_times = 0
    while True:
        breaker.wait()
        if datetime.now() > deadline:
            raise ArkAPITimeoutError(None, None)
        try:
            return func(*args, **kwargs)
        except ArkAPIConnectionError:
            waitTime = _calculate_retry_timeout(retry_times)
            log.debug(
                "Retry due to connection error, wait time: %is, retry times: %i",
                waitTime,
                retry_times,
            )

            if datetime.now() + timedelta(seconds=waitTime) > deadline:
                raise ArkAPITimeoutError(None, None)
            time.sleep(waitTime)
        except ArkAPIStatusError as err:
            retry_after = _get_retry_after(err.response)
            log.debug(
                "Got status error, retry after: %is, retry times: %i, error: %s",
                retry_after,
                retry_times,
                err,
            )

            if retry_after is not None and retry_after > 0:
                breaker.reset(retry_after)
            if not _should_retry(err.response):
                raise err

        retry_times = retry_times + 1


async def async_with_batch_retry(
    deadline: datetime,
    breaker: ModelBreaker,
    func: Callable[..., Awaitable[R]],
    *args,
    **kwargs,
) -> R:
    retry_times = 0
    while True:
        await breaker.asyncwait()
        if datetime.now() > deadline:
            raise ArkAPITimeoutError(None, None)
        try:
            return await func(*args, **kwargs)
        except ArkAPIConnectionError:
            waitTime = _calculate_retry_timeout(retry_times)
            log.debug(
                "Retry due to connection error, wait time: %is, retry times: %i",
                waitTime,
                retry_times,
            )

            if datetime.now() + timedelta(seconds=waitTime) > deadline:
                raise ArkAPITimeoutError(None, None)
            await asyncio.sleep(waitTime)
        except ArkAPIStatusError as err:
            retry_after = _get_retry_after(err.response)
            log.debug(
                "Got status error, retry after: %is, retry times: %i, error: %s",
                retry_after,
                retry_times,
                err,
            )

            if retry_after is not None and retry_after > 0:
                breaker.reset(retry_after)
            if not _should_retry(err.response):
                raise err

        retry_times = retry_times + 1
