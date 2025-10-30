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

from typing_extensions import Literal, Optional

from ..._models import BaseModel

__all__ = ["UserLocation"]


class UserLocation(BaseModel):
    type: Literal["approximate"]
    """The type of the user location. Always `approximate`."""
    city: Optional[str]
    """The city of the user location."""
    country: Optional[str]
    """The country of the user location."""
    region: Optional[str]
    """The region of the user location."""
    timezone: Optional[float]
    """The timezone of the user location."""
