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

from typing import Union

from typing_extensions import Annotated, TypeAlias

from ..._utils import PropertyInfo
from .doubao_app_call_block_output_text import DoubaoAppCallBlockOutputText
from .doubao_app_call_block_reasoning_search import DoubaoAppCallBlockReasoningSearch
from .doubao_app_call_block_reasoning_text import DoubaoAppCallBlockReasoningText
from .doubao_app_call_block_search import DoubaoAppCallBlockSearch

__all__ = ["DoubaoAppCallBlock"]

DoubaoAppCallBlock: TypeAlias = Annotated[
    Union[
        DoubaoAppCallBlockOutputText,
        DoubaoAppCallBlockReasoningText,
        DoubaoAppCallBlockSearch,
        DoubaoAppCallBlockReasoningSearch,
    ],
    PropertyInfo(discriminator="type"),
]
