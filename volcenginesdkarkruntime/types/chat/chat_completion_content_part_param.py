from __future__ import annotations

from typing import Union

from .chat_completion_content_part_text_param import ChatCompletionContentPartTextParam
from .chat_completion_content_part_image_param import (
    ChatCompletionContentPartImageParam,
)
from .chat_completion_content_part_video_param import (
    ChatCompletionContentPartVideoParam,
)

__all__ = ["ChatCompletionContentPartParam"]

ChatCompletionContentPartParam = Union[
    ChatCompletionContentPartTextParam,
    ChatCompletionContentPartImageParam,
    ChatCompletionContentPartVideoParam,
]
