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

from typing import Optional

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["DoubaoAppCallBlockOutputText"]


class DoubaoAppCallBlockOutputText(BaseModel):
    id: Optional[str] = None

    type: Literal["output_text"]

    text: str

    status: Literal["in_progress", "completed", "incomplete", "searching", "failed"]

    parent_id: Optional[str] = None
