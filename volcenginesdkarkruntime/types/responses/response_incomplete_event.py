
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

from typing_extensions import Literal

from .response import Response
from ..._models import BaseModel

__all__ = ["ResponseIncompleteEvent"]


class ResponseIncompleteEvent(BaseModel):
    response: Response
    """The response that was incomplete."""

    type: Literal["response.incomplete"]
    """The type of the event. Always `response.incomplete`."""
