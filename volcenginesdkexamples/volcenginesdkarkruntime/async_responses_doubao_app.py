import asyncio
import time
from volcenginesdkarkruntime import AsyncArk
from volcenginesdkarkruntime.types.responses.response_completed_event import (
    ResponseCompletedEvent,
)
from volcenginesdkarkruntime.types.responses.response_output_item_done_event import (
    ResponseOutputItemDoneEvent,
)
from volcenginesdkarkruntime.types.responses.response_function_tool_call import (
    ResponseFunctionToolCall,
)
from volcenginesdkarkruntime.types.responses.response_mcp_item import McpApprovalRequest

"""
示例代码：演示 Responses API 的常见用法
-------------------------------------------------
1. 多轮对话中使用缓存 (caching)
2. 调用外部函数 (function calling)
3. Web 搜索工具 (web search)
4. 使用MCP工具 (MCP)
"""

client = AsyncArk()


async def main():
    # ==========================================================
    # 示例：使用豆包助手
    # ==========================================================
    print("Example: Use doubao assistant")
    # ---------- 第 1 轮 ----------
    # 选择一种feature 测试
    stream = await client.responses.create(
        model="doubao-seed-1-6",
        input=[
            {"role": "user", "content": "你好请你介绍你自己"},
        ],
        tools=[
            {
                "type": "doubao_app",
                "feature": {
                    # "ai_search": {"type": "enabled"}
                    # "reasoning_search": {"type": "enabled"}
                    # "deep_chat": {"type": "enabled"}
                    "chat": {"type": "enabled"}
                },
            }
        ],
        store=True,
        stream=True,
    )
    response_id = ""
    async for event in stream:
        print(event)
        if isinstance(event, ResponseCompletedEvent):
            response_id = event.response.id

    time.sleep(1)
    print("Starting second round")
    # ---------- 第 2 轮 ----------
    # 说明：通过 previous_response_id 关联上一轮的上下文
    stream = await client.responses.create(
        model="doubao-seed-1-6",
        previous_response_id=response_id,
        input=[
            {"role": "user", "content": "上一轮对话里我们说了什么"},
        ],
        tools=[
            {
                "type": "doubao_app",
                "feature": {
                    # "ai_search": {"type": "enabled"}
                    # "reasoning_search": {"type": "enabled"}
                    # "deep_chat": {"type": "enabled"}
                    "chat": {"type": "enabled"}
                },
            }
        ],
        store=True,
        stream=True,
    )
    async for event in stream:
        print(event)


if __name__ == "__main__":
    asyncio.run(main())
