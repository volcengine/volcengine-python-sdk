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


from ..._models import BaseModel
from .doubao_app_feature_item import DoubaoAppFeatureItem

__all__ = ["DoubaoAppFeature"]


class DoubaoAppFeature(BaseModel):
    chat: Optional[DoubaoAppFeatureItem] = None

    deep_chat: Optional[DoubaoAppFeatureItem] = None

    ai_search: Optional[DoubaoAppFeatureItem] = None

    reasoning_search: Optional[DoubaoAppFeatureItem] = None
