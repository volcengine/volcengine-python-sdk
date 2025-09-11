
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

from typing_extensions import TypeAlias

from ....types.chat import (
    ParsedChoice,
    ParsedChatCompletion,
    ParsedChatCompletionMessage,
)

ParsedChatCompletionSnapshot: TypeAlias = ParsedChatCompletion[object]
"""Snapshot type representing an in-progress accumulation of
a `ParsedChatCompletion` object.
"""

ParsedChatCompletionMessageSnapshot: TypeAlias = ParsedChatCompletionMessage[object]
"""Snapshot type representing an in-progress accumulation of
a `ParsedChatCompletionMessage` object.

If the content has been fully accumulated, the `.parsed` content will be
the `response_format` instance, otherwise it'll be the raw JSON parsed version.
"""

ParsedChoiceSnapshot: TypeAlias = ParsedChoice[object]
