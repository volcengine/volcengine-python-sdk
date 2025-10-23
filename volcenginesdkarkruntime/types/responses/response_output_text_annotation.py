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

from .responses_output_text_annotation_cover_image import (
    ResponsesOutputTextAnnotationCoverImage,
)

__all__ = ["ResponseOutputTextAnnotation"]


class ResponseOutputTextAnnotation(BaseModel):
    type: Literal["annotation"]
    """The type of the url_citation. Always `url_citation`."""
    title: Optional[str] = None
    """The title of the url_citation."""
    url: Optional[str] = None
    """The url of the url_citation."""
    logo_url: Optional[str] = None
    """The logo_url of the url_citation."""
    mobile_url: Optional[str] = None
    """The mobile_url of the url_citation."""
    site_name: Optional[str] = None
    """The site_name of the url_citation."""
    publish_time: Optional[str] = None
    """The publish_time of the url_citation."""
    summary: Optional[str] = None
    """The summary of the url_citation."""
    freshness_info: Optional[str] = None
    """The freshness_info of the url_citation."""
    cover_image: Optional[ResponsesOutputTextAnnotationCoverImage] = None
    """The cover_image of the url_citation."""
