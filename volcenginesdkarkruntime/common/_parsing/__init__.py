
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

from ._completions import (
    ResponseFormatT as ResponseFormatT,
    has_parseable_input as has_parseable_input,
    maybe_parse_content as maybe_parse_content,
    validate_input_tools as validate_input_tools,
    parse_chat_completion as parse_chat_completion,
    get_input_tool_by_name as get_input_tool_by_name,
    solve_response_format_t as solve_response_format_t,
    parse_function_tool_arguments as parse_function_tool_arguments,
    type_to_response_format_param as type_to_response_format_param,
)
