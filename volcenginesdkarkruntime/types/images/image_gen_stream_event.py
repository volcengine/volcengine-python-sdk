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

from typing import Union
from typing_extensions import Annotated, TypeAlias

from volcenginesdkarkruntime._utils import PropertyInfo
from .image_gen_completed_event import ImageGenCompletedEvent
from .image_gen_generating_event import ImageGenGeneratingEvent

__all__ = ["ImageGenStreamEvent"]

ImageGenStreamEvent: TypeAlias = Annotated[
    Union[ImageGenGeneratingEvent, ImageGenCompletedEvent],
    PropertyInfo(discriminator="type"),
]
