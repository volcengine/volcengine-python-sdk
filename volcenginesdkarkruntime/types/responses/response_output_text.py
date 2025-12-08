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

from typing_extensions import Literal, Optional, List

from ..._models import BaseModel

from .response_output_text_annotation import (
    ResponseOutputTextAnnotation,
)

__all__ = ["ResponseOutputText", "ResponseOutputTextAnnotation"]


class ResponseOutputText(BaseModel):
    text: str
    """The text output from the model."""

    type: Literal["output_text"]
    """The type of the output text. Always `output_text`."""

    annotations: Optional[List[ResponseOutputTextAnnotation]]
    """The annotation of the output text."""
