from __future__ import annotations

from typing import Optional

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ChatCompletionSystemMessageParam"]


class ChatCompletionSystemMessageParam(TypedDict, total=False):
    content: Required[str]
    """The contents of the system message."""

    role: Required[Literal["system"]]
    """The role of the messages author, in this case `system`."""

    name: Optional[str]
    """An optional name for the participant.

    Provides the model information to differentiate between participants of the same
    role.
    """
