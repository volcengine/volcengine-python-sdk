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
from .response_completed_event import ResponseCompletedEvent
from .response_content_part_added_event import ResponseContentPartAddedEvent
from .response_content_part_done_event import ResponseContentPartDoneEvent
from .response_created_event import ResponseCreatedEvent
from .response_doubao_app_call_block_added_event import (
    ResponseDoubaoAppCallBlockAddedEvent,
)
from .response_doubao_app_call_block_done_event import (
    ResponseDoubaoAppCallBlockDoneEvent,
)
from .response_doubao_app_call_completed_event import (
    ResponseDoubaoAppCallCompletedEvent,
)
from .response_doubao_app_call_failed_event import ResponseDoubaoAppCallFailedEvent
from .response_doubao_app_call_in_progress_event import (
    ResponseDoubaoAppCallInProgressEvent,
)
from .response_doubao_app_call_output_text_delta_event import (
    ResponseDoubaoAppCallOutputTextDeltaEvent,
)
from .response_doubao_app_call_output_text_done_event import (
    ResponseDoubaoAppCallOutputTextDoneEvent,
)
from .response_doubao_app_call_reasoning_search_completed_event import (
    ResponseDoubaoAppCallReasoningSearchCompletedEvent,
)
from .response_doubao_app_call_reasoning_search_in_progress_event import (
    ResponseDoubaoAppCallReasoningSearchInProgressEvent,
)
from .response_doubao_app_call_reasoning_search_searching_event import (
    ResponseDoubaoAppCallReasoningSearchSearchingEvent,
)
from .response_doubao_app_call_reasoning_text_delta_event import (
    ResponseDoubaoAppCallReasoningTextDeltaEvent,
)
from .response_doubao_app_call_reasoning_text_done_event import (
    ResponseDoubaoAppCallReasoningTextDoneEvent,
)
from .response_doubao_app_call_search_completed_event import (
    ResponseDoubaoAppCallSearchCompletedEvent,
)
from .response_doubao_app_call_search_in_progress_event import (
    ResponseDoubaoAppCallSearchInProgressEvent,
)
from .response_doubao_app_call_search_searching_event import (
    ResponseDoubaoAppCallSearchSearchingEvent,
)
from .response_error_event import ResponseErrorEvent
from .response_failed_event import ResponseFailedEvent
from .response_function_call_arguments_delta_event import (
    ResponseFunctionCallArgumentsDeltaEvent,
)
from .response_function_call_arguments_done_event import (
    ResponseFunctionCallArgumentsDoneEvent,
)
from .response_image_process_call_completed_event import (
    ResponseImageProcessCallCompletedEvent,
)
from .response_image_process_call_in_progress_event import (
    ResponseImageProcessCallInProgressEvent,
)
from .response_image_process_call_processing_event import (
    ResponseImageProcessCallProcessingEvent,
)
from .response_in_progress_event import ResponseInProgressEvent
from .response_incomplete_event import ResponseIncompleteEvent
from .response_knowledge_search_call_completed_event import (
    ResponseKnowledgeSearchCallCompletedEvent,
)
from .response_knowledge_search_call_failed_event import (
    ResponseKnowledgeSearchCallFailedEvent,
)
from .response_knowledge_search_call_in_progress_event import (
    ResponseKnowledgeSearchCallInProgressEvent,
)
from .response_knowledge_search_call_searching_event import (
    ResponseKnowledgeSearchCallSearchingEvent,
)
from .response_mcp_call_arguments_delta_event import ResponseMcpCallArgumentsDeltaEvent
from .response_mcp_call_arguments_done_event import ResponseMcpCallArgumentsDoneEvent
from .response_mcp_call_completed_event import ResponseMcpCallCompletedEvent
from .response_mcp_call_failed_event import ResponseMcpCallFailedEvent
from .response_mcp_call_in_progress_event import ResponseMcpCallInProgressEvent
from .response_mcp_list_tools_completed_event import ResponseMcpListToolsCompletedEvent
from .response_mcp_list_tools_in_progress_event import (
    ResponseMcpListToolsInProgressEvent,
)
from .response_output_item_added_event import ResponseOutputItemAddedEvent
from .response_output_item_done_event import ResponseOutputItemDoneEvent
from .response_output_text_annotation_added_event import (
    ResponseOutputTextAnnotationAddedEvent,
)
from .response_reasoning_summary_part_added_event import (
    ResponseReasoningSummaryPartAddedEvent,
)
from .response_reasoning_summary_part_done_event import (
    ResponseReasoningSummaryPartDoneEvent,
)
from .response_reasoning_summary_text_delta_event import (
    ResponseReasoningSummaryTextDeltaEvent,
)
from .response_reasoning_summary_text_done_event import (
    ResponseReasoningSummaryTextDoneEvent,
)
from .response_text_delta_event import ResponseTextDeltaEvent
from .response_text_done_event import ResponseTextDoneEvent
from .response_web_search_call_completed_event import (
    ResponseWebSearchCallCompletedEvent,
)
from .response_web_search_call_in_progress_event import (
    ResponseWebSearchCallInProgressEvent,
)
from .response_web_search_call_searching_event import (
    ResponseWebSearchCallSearchingEvent,
)

__all__ = ["ResponseStreamEvent"]

ResponseStreamEvent: TypeAlias = Annotated[
    Union[
        ResponseCreatedEvent,
        ResponseOutputItemAddedEvent,
        ResponseContentPartAddedEvent,
        ResponseTextDeltaEvent,
        ResponseReasoningSummaryPartAddedEvent,
        ResponseReasoningSummaryTextDeltaEvent,
        ResponseFunctionCallArgumentsDeltaEvent,
        ResponseErrorEvent,
        ResponseWebSearchCallInProgressEvent,
        ResponseWebSearchCallSearchingEvent,
        ResponseWebSearchCallCompletedEvent,
        ResponseOutputTextAnnotationAddedEvent,
        ResponseImageProcessCallInProgressEvent,
        ResponseImageProcessCallProcessingEvent,
        ResponseImageProcessCallCompletedEvent,
        ResponseMcpListToolsInProgressEvent,
        ResponseMcpListToolsCompletedEvent,
        ResponseMcpCallInProgressEvent,
        ResponseMcpCallArgumentsDeltaEvent,
        ResponseMcpCallArgumentsDoneEvent,
        ResponseMcpCallCompletedEvent,
        ResponseMcpCallFailedEvent,
        ResponseKnowledgeSearchCallInProgressEvent,
        ResponseKnowledgeSearchCallSearchingEvent,
        ResponseKnowledgeSearchCallCompletedEvent,
        ResponseKnowledgeSearchCallFailedEvent,
        ResponseInProgressEvent,
        ResponseCompletedEvent,
        ResponseFailedEvent,
        ResponseIncompleteEvent,
        ResponseOutputItemDoneEvent,
        ResponseContentPartDoneEvent,
        ResponseTextDoneEvent,
        ResponseReasoningSummaryPartDoneEvent,
        ResponseReasoningSummaryTextDoneEvent,
        ResponseFunctionCallArgumentsDoneEvent,
        ResponseDoubaoAppCallInProgressEvent,
        ResponseDoubaoAppCallCompletedEvent,
        ResponseDoubaoAppCallFailedEvent,
        ResponseDoubaoAppCallOutputTextDeltaEvent,
        ResponseDoubaoAppCallOutputTextDoneEvent,
        ResponseDoubaoAppCallSearchInProgressEvent,
        ResponseDoubaoAppCallSearchSearchingEvent,
        ResponseDoubaoAppCallSearchCompletedEvent,
        ResponseDoubaoAppCallReasoningTextDeltaEvent,
        ResponseDoubaoAppCallReasoningTextDoneEvent,
        ResponseDoubaoAppCallReasoningSearchInProgressEvent,
        ResponseDoubaoAppCallReasoningSearchSearchingEvent,
        ResponseDoubaoAppCallReasoningSearchCompletedEvent,
        ResponseDoubaoAppCallBlockAddedEvent,
        ResponseDoubaoAppCallBlockDoneEvent,
    ],
    PropertyInfo(discriminator="type"),
]
