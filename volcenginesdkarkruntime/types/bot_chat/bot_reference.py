
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

from typing import Optional, Dict
from ..._models import BaseModel


class CoverImage(BaseModel):
    url: str = ""
    width: int = 0
    height: int = 0


class Reference(BaseModel):
    # browsing plus/pro related reference
    url: Optional[str] = None
    """
    url stands for the url of the browsing plugin returned by the browsing plugin
    """
    logo_url: Optional[str] = None
    """
    logo_url stands for the logo url of the browsing plugin returned by the browsing plugin
    """
    mobile_url: Optional[str] = None
    """
    mobile_url stands for the mobile url of the browsing plugin returned by the browsing plugin
    """
    site_name: Optional[str] = None
    """
    site_name stands for the source type & site name returned by the browsing plugin
    """
    title: Optional[str] = None
    """
    title stands for the title of the search result returned by the browsing plugin
    """
    summary: Optional[str] = None
    """
    summary stands for the summary of the search result returned by the browsing plugin
    """
    publish_time: Optional[str] = None
    """
    publish_time stands for the publish time of the search result returned by the browsing plugin
    """
    cover_image: Optional[CoverImage] = None
    """
    cover_image stands for the cover image of the search result returned by the browsing plugin
    """
    extra: Optional[Dict[str, object]] = None
    """
    extra stands for the non-common fields of the search result returned by the browsing plugin, such as weather
    """

    # knowledgebase related reference
    doc_id: Optional[str] = None
    """
    doc_id stands for the retrieved doc id of the knowledgebase returned by the knowledgebase plugin
    """
    doc_name: Optional[str] = None
    """
    doc_name stands for the retrieved doc name of the knowledgebase returned by the knowledgebase plugin
    """
    doc_type: Optional[str] = None
    """
    doc_type stands for the retrieved doc type of the knowledgebase returned by the knowledgebase plugin
    """
    doc_title: Optional[str] = None
    """
    doc_title stands for the retrieved doc title of the knowledgebase returned by the knowledgebase plugin
    """
    chunk_title: Optional[str] = None
    """
    chunk_title stands for the retrieved chunk title of the knowledgebase returned by the knowledgebase plugin
    """
    chunk_id: Optional[str] = None
    """
    chunk_id stands for the retrieved chunk id of the knowledgebase returned by the knowledgebase plugin
    """
    collection_name: Optional[str] = None
    """
    collection_name stands for the collection name that the retrieved chunk belongs to
    """
    project: Optional[str] = None
    """
    project stands for the project that the collection belongs to
    """
