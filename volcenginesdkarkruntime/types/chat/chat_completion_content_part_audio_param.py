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

from typing_extensions import Literal, Optional, Required, TypedDict

__all__ = ["ChatCompletionContentPartAudioParam", "AudioURL"]


class AudioURL(TypedDict, total=False):
    url: Optional[str]
    """Either a URL of the audio."""
    data: Optional[str]
    """Base64 encoded audio data."""
    format: Required[str]
    """audio encoding format"""


class ChatCompletionContentPartAudioParam(TypedDict, total=False):
    audio_url: Required[AudioURL]

    type: Required[Literal["input_audio"]]
    """The type of the content part."""
