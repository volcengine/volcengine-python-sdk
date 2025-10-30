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

from typing import Optional

from typing_extensions import Literal, Required, TypedDict

from .audio_chunking_strategy_param import AudioChunkingStrategyParam

__all__ = ["ResponseInputAudioParam"]


class ResponseInputAudioParam(TypedDict, total=False):
    type: Required[Literal["input_audio"]]

    chunking_strategy: Optional[AudioChunkingStrategyParam]

    audio_url: Required[str]

    file_id: Optional[str]

    audio_bytes: Optional[bytes]
