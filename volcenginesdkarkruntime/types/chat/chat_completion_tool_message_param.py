from __future__ import annotations

from typing import Optional, Union, Iterable

from typing_extensions import Literal, Required, TypedDict
from .chat_completion_content_part_param import ChatCompletionContentPartParam

__all__ = ["ChatCompletionToolMessageParam"]


class ChatCompletionToolMessageParam(TypedDict, total=False):
    content: Required[Union[str, Iterable[ChatCompletionContentPartParam]]]
    """The contents of the tool message."""

    role: Required[Literal["tool"]]
    """The role of the messages author, in this case `tool`."""

    name: Optional[str]
    """An optional name for the participant.

    Provides the model information to differentiate between participants of the same
    role.
    """

    tool_call_id: Required[str]
    """Tool call that this message is responding to."""
