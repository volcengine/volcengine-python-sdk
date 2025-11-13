from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from ..shared.reasoning_effort import ReasoningEffort

__all__ = ["Reasoning"]


class Reasoning(TypedDict, total=False):
    effort: Optional[ReasoningEffort]
