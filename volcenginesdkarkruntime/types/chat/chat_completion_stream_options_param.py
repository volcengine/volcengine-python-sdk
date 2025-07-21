
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

from typing_extensions import TypedDict

__all__ = ["ChatCompletionStreamOptionsParam"]


class ChatCompletionStreamOptionsParam(TypedDict, total=False):
    include_usage: bool
    """If set, an additional chunk will be streamed before the `data: [DONE]` message.

    The `usage` field on this chunk shows the token usage statistics for the entire
    request, and the `choices` field will always be an empty array. All other chunks
    will also include a `usage` field, but with a null value.
    """

    chunk_include_usage: bool
    """if set, each data chunk will include a `usage` field 
    representing the current cumulative token usage for the entire request.
    """
