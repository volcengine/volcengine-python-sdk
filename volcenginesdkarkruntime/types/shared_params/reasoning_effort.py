from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypeAlias

__all__ = ["ReasoningEffort"]

ReasoningEffort: TypeAlias = Optional[Literal["minimal", "low", "medium", "high"]]
