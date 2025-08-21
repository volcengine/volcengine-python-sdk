
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

from typing import Dict, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ResponseFormatJSONSchema", "JSONSchema"]


class JSONSchema(BaseModel):
    name: str
    """The name of the response format.

    Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length
    of 64.
    """

    description: Optional[str] = None
    """
    A description of what the response format is for, used by the model to determine
    how to respond in the format.
    """

    schema_: Optional[Dict[str, object]] = FieldInfo(alias="schema", default=None)
    """
    The schema for the response format, described as a JSON Schema object. Learn how
    to build JSON schemas [here](https://json-schema.org/).
    """

    strict: Optional[bool] = None
    """
    Whether to enable strict schema adherence when generating the output. If set to
    true, the model will always follow the exact schema defined in the `schema`
    field. Only a subset of JSON Schema is supported when `strict` is `true`. 
    """


class ResponseFormatJSONSchema(BaseModel):
    json_schema: JSONSchema
    """Structured Outputs configuration options, including a JSON Schema."""

    type: Literal["json_schema"]
    """The type of response format being defined. Always `json_schema`."""
