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

from ..._utils import PropertyInfo
from .response_input_audio import ResponseInputAudio
from .response_input_file import ResponseInputFile
from .response_input_image import ResponseInputImage
from .response_input_text import ResponseInputText
from .response_input_video import ResponseInputVideo

__all__ = ["ResponseInputContent"]

ResponseInputContent: TypeAlias = Annotated[
    Union[
        ResponseInputText,
        ResponseInputImage,
        ResponseInputVideo,
        ResponseInputAudio,
        ResponseInputFile,
    ],
    PropertyInfo(discriminator="type"),
]
