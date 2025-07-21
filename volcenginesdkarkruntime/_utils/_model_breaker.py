
# Copyright (c) [2025] [OpenAI]
# Copyright (c) [2025] [ByteDance Ltd. and/or its affiliates.]
# SPDX-License-Identifier: Apache-2.0
#
# This file has been modified by [ByteDance Ltd. and/or its affiliates.] on 2025.7
#
# Original file was released under Apache License Version 2.0, with the full license text
# available at https://github.com/openai/openai-python/blob/main/LICENSE.
#
# This modified file is released under the same license.

import asyncio
import time
import uuid
import threading


class _QuerySet(object):
    def __init__(self):
        self._items = list()
        self._index = dict()
        self._lock = threading.Lock()

    def add(self, item: int) -> None:
        with self._lock:
            if item in self._index:
                return

            self._items.append(item)
            self._index[item] = len(self._items) - 1

    def remove(self, item: int) -> None:
        with self._lock:
            if item not in self._index:
                return

            index = self._index[item]
            self._items[index] = self._items[-1]
            self._index[self._items[-1]] = index
            self._items.pop()
            del self._index[item]

    def query(self, item: int) -> int:
        with self._lock:
            return self._index[item]


class ModelBreaker(object):
    def __init__(self):
        # 初始化 allow_time 为当前时间
        self._allow_time = time.perf_counter()
        self._waiters = _QuerySet()

    def _allow(self, id: int) -> bool:
        cur = time.perf_counter()
        # 如果当前时间小于等于 allow_time，不允许通过
        if cur <= self._allow_time:
            return 0
        # 如果当前时间与 allow_time 的差值大于 10，允许通过
        if cur - self._allow_time > 10:
            return True
        # 如果当前时间与 allow_time 的差值小于等于 10，慢启动通过
        return self._waiters.query(id) < 2 ** (cur - self._allow_time)

    def _get_allowed_duration(self) -> float:
        # 计算当前时间与 allow_time 之间的持续时间
        allow_duration = self._allow_time - time.perf_counter()

        # 至少有 1 秒的等待时间
        return max(allow_duration, 1)

    def _acquire(self) -> int:
        id = uuid.uuid4().int
        self._waiters.add(id)
        return id

    def _release(self, id: int) -> None:
        self._waiters.remove(id)

    def reset(self, duration: float) -> None:
        # 将 allow_time 重置为当前时间加上指定的持续时间
        self._allow_time = time.perf_counter() + duration

    def wait(self) -> None:
        id = self._acquire()
        while not self._allow(id):
            time.sleep(self._get_allowed_duration())
        self._release(id)

    async def asyncwait(self) -> None:
        id = self._acquire()
        while not self._allow(id):
            await asyncio.sleep(self._get_allowed_duration())
        self._release(id)
