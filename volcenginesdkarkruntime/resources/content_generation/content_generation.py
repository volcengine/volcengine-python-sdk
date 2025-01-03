from __future__ import annotations

from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._compat import cached_property

from .tasks import Tasks, AsyncTasks


class ContentGeneration(SyncAPIResource):
    @cached_property
    def tasks(self) -> Tasks:
        return Tasks(self._client)

class AsyncContentGeneration(AsyncAPIResource):
    @cached_property
    def tasks(self) -> AsyncTasks:
        return AsyncTasks(self._client)