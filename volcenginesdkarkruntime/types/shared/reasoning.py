from typing import Optional

from volcenginesdkarkruntime._models import BaseModel
from .reasoning_effort import ReasoningEffort

__all__ = ["Reasoning"]


class Reasoning(BaseModel):
    effort: Optional[ReasoningEffort] = None
