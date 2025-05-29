import asyncio
from pydantic import BaseModel
from typing import List
from volcenginesdkarkruntime import AsyncArk

# Authentication
# 1.If you authorize your endpoint using an API key, you can set your api key to environment variable "ARK_API_KEY"
# or specify api key by Ark(api_key="${YOUR_API_KEY}").
# Note: If you use an API key, this API key will not be refreshed.
# To prevent the API from expiring and failing after some time, choose an API key with no expiration date.

# 2.If you authorize your endpoint with Volcengine Identity and Access Management（IAM), set your api key to environment variable "VOLC_ACCESSKEY", "VOLC_SECRETKEY"
# or specify ak&sk by Ark(ak="${YOUR_AK}", sk="${YOUR_SK}").
# To get your ak&sk, please refer to this document(https://www.volcengine.com/docs/6291/65568)
# For more information，please check this document（https://www.volcengine.com/docs/82379/1263279）

client = AsyncArk()


class MeetingInfo(BaseModel):
    time: str
    participants: List[str]


async def main():
    # Non-stream parsing
    print("----- standard request -----")
    completion = await client.beta.chat.completions.parse(
        model="${YOUR_ENDPOINT_ID}",
        messages=[
            {"role": "system", "content": "提取会议信息"},
            {"role": "user", "content": "周三下午3点产品组会议，参加人员：张三、李四"}
        ],
        response_format=MeetingInfo
    )

    message = completion.choices[0].message
    if message.parsed:
        meeting = completion.choices[0].message.parsed
        print(f"会议时间：{meeting.time}")
    print("---------------")

    # stream parsing
    print("----- streaming request -----")
    async with client.beta.chat.completions.stream(
            model="${YOUR_ENDPOINT_ID}",
            messages=[
                {"role": "system", "content": "提取会议信息"},
                {"role": "user", "content": "周三下午3点产品组会议，参加人员：张三、李四"}
            ],
            response_format=MeetingInfo,
    ) as stream:
        async for event in stream:
            if event.type == "content.delta":
                print(event.delta, end="", flush=True)
            elif event.type == "content.done":
                print("\n")
                if event.parsed is not None:
                    print(f"会议时间: {event.parsed.time}")

    print("---------------")


if __name__ == "__main__":
    asyncio.run(main())
