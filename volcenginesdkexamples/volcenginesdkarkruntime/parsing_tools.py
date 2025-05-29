import asyncio
import volcenginesdkarkruntime as ark
from pydantic import BaseModel
import rich
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


class GetWeather(BaseModel):
    city: str
    country: str


async def main():
    # Non-stream parsing
    print("----- standard request -----")
    completion = await client.beta.chat.completions.parse(
        model="${YOUR_ENDPOINT_ID}",
        messages=[
            {"role": "user", "content": "What's the weather like in hangzhou?"}
        ],
        tools=[
            ark.pydantic_function_tool(GetWeather),
        ],
    )

    tool_call = (completion.choices[0].message.tool_calls or [])[0]
    rich.print(tool_call.function)
    assert isinstance(tool_call.function.parsed_arguments, GetWeather)
    print(tool_call.function.parsed_arguments.city)
    print("----\n")

    # stream parsing
    print("----- streaming request -----")
    async with client.beta.chat.completions.stream(
            model="${YOUR_ENDPOINT_ID}",
            messages=[
                {"role": "user", "content": "What's the weather like in hangzhou?"}
            ],
            tools=[
                ark.pydantic_function_tool(GetWeather, name="get_weather"),
            ],
    ) as stream:
        async for event in stream:
            if event.type == "tool_calls.function.arguments.delta" or event.type == "tool_calls.function.arguments.done":
                rich.get_console().print(event, width=80)
    print("----\n")
    rich.print(await stream.get_final_completion())


if __name__ == "__main__":
    asyncio.run(main())
