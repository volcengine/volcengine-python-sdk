from __future__ import annotations

from ..._resource import SyncAPIResource
from ..._compat import cached_property

from .tasks import Tasks

__all__ = ["ContentGeneration"]


class ContentGeneration(SyncAPIResource):
    @cached_property
    def tasks(self) -> Tasks:
        return Tasks(self._client)