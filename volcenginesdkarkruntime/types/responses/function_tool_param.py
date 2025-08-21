
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

from typing import Dict, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["FunctionToolParam"]


class FunctionToolParam(TypedDict, total=False):
    name: Required[str]
    """The name of the function to call."""

    parameters: Required[Optional[Dict[str, object]]]
    """A JSON schema object describing the parameters of the function."""

    type: Required[Literal["function"]]
    """The type of the function tool. Always `function`."""

    description: Optional[str]
    """A description of the function.

    Used by the model to determine whether or not to call the function.
    """
