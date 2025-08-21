
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
from .response_error_event import ResponseErrorEvent
from .response_failed_event import ResponseFailedEvent
from .response_created_event import ResponseCreatedEvent
from .response_completed_event import ResponseCompletedEvent
from .response_text_done_event import ResponseTextDoneEvent
from .response_incomplete_event import ResponseIncompleteEvent
from .response_text_delta_event import ResponseTextDeltaEvent
from .response_in_progress_event import ResponseInProgressEvent
from .response_output_item_done_event import ResponseOutputItemDoneEvent
from .response_content_part_done_event import ResponseContentPartDoneEvent
from .response_output_item_added_event import ResponseOutputItemAddedEvent
from .response_content_part_added_event import ResponseContentPartAddedEvent
from .response_reasoning_summary_part_done_event import ResponseReasoningSummaryPartDoneEvent
from .response_reasoning_summary_text_done_event import ResponseReasoningSummaryTextDoneEvent
from .response_function_call_arguments_done_event import ResponseFunctionCallArgumentsDoneEvent
from .response_reasoning_summary_part_added_event import ResponseReasoningSummaryPartAddedEvent
from .response_reasoning_summary_text_delta_event import ResponseReasoningSummaryTextDeltaEvent
from .response_function_call_arguments_delta_event import ResponseFunctionCallArgumentsDeltaEvent
from .response_web_search_call_in_progress_event import ResponseWebSearchCallInProgressEvent
from .response_web_search_call_searching_event import ResponseWebSearchCallSearchingEvent
from .response_web_search_call_completed_event import ResponseWebSearchCallCompletedEvent
from .response_annotation_added_event import ResponseOutputTextAnnotationAddedEvent

__all__ = ["ResponseStreamEvent"]

ResponseStreamEvent: TypeAlias = Annotated[
    Union[
        ResponseCreatedEvent,
        ResponseInProgressEvent,
        ResponseCompletedEvent,
        ResponseFailedEvent,
        ResponseIncompleteEvent,

        ResponseOutputItemAddedEvent,
        ResponseOutputItemDoneEvent,

        ResponseContentPartAddedEvent,
        ResponseContentPartDoneEvent,

        ResponseTextDeltaEvent,
        ResponseTextDoneEvent,

        ResponseReasoningSummaryPartAddedEvent,
        ResponseReasoningSummaryPartDoneEvent,
        ResponseReasoningSummaryTextDeltaEvent,
        ResponseReasoningSummaryTextDoneEvent,

        ResponseFunctionCallArgumentsDeltaEvent,
        ResponseFunctionCallArgumentsDoneEvent,

        ResponseErrorEvent,

        ResponseWebSearchCallInProgressEvent,
        ResponseWebSearchCallSearchingEvent,
        ResponseWebSearchCallCompletedEvent,
        ResponseOutputTextAnnotationAddedEvent,
    ],
    PropertyInfo(discriminator="type"),
]
