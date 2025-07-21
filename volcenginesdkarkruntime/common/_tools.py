
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

from typing import Any, Dict, cast

import pydantic

from ._pydantic import to_strict_json_schema
from ..types.chat import ChatCompletionToolParam
from ..types.shared_params import FunctionDefinition


class PydanticFunctionTool(Dict[str, Any]):
    """Dictionary wrapper so we can pass the given base model
    throughout the entire request stack without having to special
    case it.
    """

    model: type[pydantic.BaseModel]

    def __init__(
        self, defn: FunctionDefinition, model: type[pydantic.BaseModel]
    ) -> None:
        super().__init__(defn)
        self.model = model

    def cast(self) -> FunctionDefinition:
        return cast(FunctionDefinition, self)


def pydantic_function_tool(
    model: type[pydantic.BaseModel],
    *,
    name: str | None = None,  # inferred from class name by default
    description: str | None = None,  # inferred from class docstring by default
) -> ChatCompletionToolParam:
    if description is None:
        # note: we intentionally don't use `.getdoc()` to avoid
        # including pydantic's docstrings
        description = model.__doc__

    function = PydanticFunctionTool(
        {
            "name": name or model.__name__,
            "strict": True,
            "parameters": to_strict_json_schema(model),
        },
        model,
    ).cast()

    if description is not None:
        function["description"] = description

    return {
        "type": "function",
        "function": function,
    }
