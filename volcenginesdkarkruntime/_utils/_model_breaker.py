import asyncio
import math
import time


class ModelBreaker(object):
    def __init__(self):
        # 初始化 allow_time 为当前时间
        self._allow_time = time.perf_counter()

        self._waiters = 0
        self._permits = 0
        self._base = 0

    def _allow(self) -> bool:
        # 检查当前时间是否在 allow_time 之后
        return time.perf_counter() > self._allow_time

    def _get_allowed_duration(self) -> float:
        # 计算当前时间与 allow_time 之间的持续时间
        allow_duration = self._allow_time - time.perf_counter()

        # 如果持续时间为负，返回零
        if allow_duration < 0:
            return 0
        return allow_duration

    def _acquire(self) -> int:
        self._waiters += 1
        return self._waiters

    def _release(self) -> None:
        self._waiters -= 1
        self._permits += 1

    def _jitter(self, i: int) -> float:
        if i <= self._base:
            return 0
        return math.log2(i - self._base)

    def reset(self, duration: float) -> None:
        # 将 allow_time 重置为当前时间加上指定的持续时间
        self._allow_time = time.perf_counter() + duration
        self._base = self._permits

    def wait(self) -> None:
        i = self._acquire()
        while not self._allow():
            time.sleep(self._get_allowed_duration() + self._jitter(i))
        self._release()

    async def asyncwait(self) -> None:
        i = self._acquire()
        while not self._allow():
            await asyncio.sleep(self._get_allowed_duration() + self._jitter(i))
        self._release()
