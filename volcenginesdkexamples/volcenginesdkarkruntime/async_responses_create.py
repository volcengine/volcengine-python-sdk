import asyncio
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
    image_path = "/path/to/your/image.jpg"
    # ==========================================================
    # 示例 1：多轮对话，开启 caching
    # ==========================================================
    print("Example 1: Use caching for multi-round chat")
    # ---------- 第 1 轮 ----------
    # 说明：开启 caching，store=True 表示把对话存储在服务端，以便后续引用
    stream = await client.responses.create(
        model="doubao-seed-1-6",
        input=[
            {
                "role": "system",
                "content": "你是豆包，是由字节跳动开发的 AI 人工智能助手",
            },
            {
                "role": "user",
                "content": [
                    # {
                    #     "type": "input_image",
                    #     # local image file path, will be automatically uploaded to file
                    #     "image_url": f"file://{image_path}"
                    # },
                    {"type": "input_text", "text": "图里有什么内容"}
                ],
            },
        ],
        caching={
            "type": "enabled",
        },
        store=True,
        stream=True,
    )
    response_id = ""
    async for event in stream:
        print(event)
        if isinstance(event, ResponseCompletedEvent):
            response_id = event.response.id

    # ---------- 第 2 轮 ----------
    # 说明：通过 previous_response_id 关联上一轮的上下文
    stream = await client.responses.create(
        model="doubao-seed-1-6",
        previous_response_id=response_id,
        input=[
            {"role": "user", "content": "上一轮对话里图里的内容是"},
        ],
        caching={
            "type": "enabled",
        },
        store=True,
        stream=True,
    )
    async for event in stream:
        print(event)

    # ==========================================================
    # 示例 2：函数调用 (Function Calling)
    # ==========================================================
    print("Example 2: Use responses API for function calling")

    # ---------- 第 1 轮 ----------
    # 用户询问北京天气，模型会触发工具调用
    stream = await client.responses.create(
        model="doubao-seed-1-6",
        input=[
            {"role": "user", "content": "请问北京今天天气怎么样"},
        ],
        tools=[
            {
                "type": "function",
                "name": "get_current_weather",
                "description": "获取当前城市的天气",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "城市名称，例如北京",
                        },
                        "unit": {
                            "type": "string",
                            "description": "温度单位，例如摄氏度",
                        },
                    },
                    "required": ["location"],
                },
            }
        ],
        caching={
            "type": "enabled",
        },
        store=True,
        stream=True,
    )
    call_id = ""
    response_id = ""
    async for event in stream:
        print(event)
        if isinstance(event, ResponseCompletedEvent):
            response_id = event.response.id
        if isinstance(event, ResponseOutputItemDoneEvent) and isinstance(
            event.item, ResponseFunctionToolCall
        ):
            call_id = event.item.call_id

    # ---------- 第 2 轮 ----------
    # 把函数返回结果传回模型，让它继续生成最终回答
    stream = await client.responses.create(
        model="doubao-seed-1-6",
        previous_response_id=response_id,
        input=[
            {
                "type": "function_call_output",
                "call_id": call_id,
                "output": '{"temperature": "30"}',
            },
        ],
        caching={
            "type": "enabled",
        },
        store=True,
        stream=True,
    )
    async for event in stream:
        print(event)

    # ==========================================================
    # 示例 3：Web 搜索工具
    # ==========================================================
    print("Example 3: Use responses API for web search")
    stream = await client.responses.create(
        model="doubao-seed-1-6",
        input=[
            {"role": "user", "content": "今天的新闻"},
        ],
        tools=[
            {
                "type": "web_search",
                "limit": 3,
                "sources": ["toutiao"],
                "user_location": {
                    "type": "approximate",
                    "city": "北京",
                    "country": "中国",
                    "region": "北京",
                },
            }
        ],
        store=True,
        stream=True,
    )
    async for event in stream:
        print(event)

    # ==========================================================
    # 示例 4：使用 MCP
    # ==========================================================
    # ---------- 第 1 轮 ----------
    # 用户询问repo信息，模型会触发mcp工具调用
    stream = await client.responses.create(
        model="doubao-seed-1-6",
        input=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "input_text",
                        "text": "查看这个 repo的文档 expressjs/express ",
                    }
                ],
            }
        ],
        tools=[
            {
                "type": "mcp",
                "server_label": "deepwiki-test",
                "server_url": "https://mcp.deepwiki.com/mcp",
                "require_approval": "always",
            }
        ],
        store=True,
        stream=True,
    )
    approval_id = ""
    response_id = ""
    async for event in stream:
        print(event)
        if isinstance(event, ResponseCompletedEvent):
            response_id = event.response.id
        if isinstance(event, ResponseOutputItemDoneEvent) and isinstance(
            event.item, McpApprovalRequest
        ):
            approval_id = event.item.id

    # ---------- 第 2 轮 ----------
    # 用户同意mcp工具调用，模型会继续生成最终回答
    stream = await client.responses.create(
        model="doubao-seed-1-6",
        input=[
            {
                "type": "mcp_approval_response",
                "approval_request_id": approval_id,
                "approve": True,
            }
        ],
        previous_response_id=response_id,
        tools=[
            {
                "type": "mcp",
                "server_label": "deepwiki-test",
                "server_url": "https://mcp.deepwiki.com/mcp",
                "require_approval": "always",
            }
        ],
        store=True,
        stream=True,
    )
    async for event in stream:
        print(event)


if __name__ == "__main__":
    asyncio.run(main())
