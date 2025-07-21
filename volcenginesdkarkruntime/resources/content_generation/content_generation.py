
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

from __future__ import annotations

from .tasks import Tasks, AsyncTasks
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource


class ContentGeneration(SyncAPIResource):
    @cached_property
    def tasks(self) -> Tasks:
        return Tasks(self._client)


class AsyncContentGeneration(AsyncAPIResource):
    @cached_property
    def tasks(self) -> AsyncTasks:
        return AsyncTasks(self._client)
