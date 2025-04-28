from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .chat_completion_content_part_param import ChatCompletionContentPartParam

__all__ = ["ChatCompletionSystemMessageParam"]


class ChatCompletionSystemMessageParam(TypedDict, total=False):
    content: Required[Union[str, Iterable[ChatCompletionContentPartParam]]]
    """The contents of the system message."""

    role: Required[Literal["system"]]
    """The role of the messages author, in this case `system`."""

    name: Optional[str]
    """An optional name for the participant.

    Provides the model information to differentiate between participants of the same
    role.
    """
