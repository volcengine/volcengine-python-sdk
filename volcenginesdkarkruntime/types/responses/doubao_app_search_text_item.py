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


from ..._models import BaseModel

__all__ = ["DoubaoAppSearchTextItem"]


class DoubaoAppSearchTextItem(BaseModel):
    id: int

    summary: str

    title: str

    sitename: str

    url: str

    logo_url: str

    doc_id: str

    image_url: str

    has_image: bool

    publish_time_second: str

    original_doc_rank: int

    source_from: int

    source_id: str

    source_for_baike: str

    index: int
