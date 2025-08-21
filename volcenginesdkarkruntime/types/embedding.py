
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

from typing import List
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Embedding"]


class Embedding(BaseModel):
    embedding: List[float]
    """The embedding vector, which is a list of floats.

    The length of vector depends on the model as listed in the
    """

    index: int
    """The index of the embedding in the list of embeddings."""

    object: Literal["embedding"]
    """The object type, which is always "embedding"."""
