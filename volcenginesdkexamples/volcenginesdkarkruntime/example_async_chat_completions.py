import asyncio

from volcenginesdkarkruntime import AsyncArk

# Support ak&sk or api key
# 1. Fetch ak&sk from environmental variables "VOLC_ACCESSKEY", "VOLC_SECRETKEY"
# or specify ak&sk by Ark(ak="${YOUR_AK}", sk="${YOUR_SK}").
# you can get ak&sk follow this document(https://www.volcengine.com/docs/6291/65568)
#
# 2. Fetch api key from environmental variables "ARK_API_KEY"
# or specify api key by Ark(api_key="${YOUR_API_KEY}").
# Note: if you support api key，this api key will not be refreshed.
# If you don't want the api to fail after a period of time, to the api key that never expires.
client = AsyncArk()


async def main():
    stream = await client.chat.completions.create(
        model="${YOUR_ENDPOINT_ID}",
        messages=[
            {
                "role": "user",
                "content": "Say this is a test",
            },
        ],
        stream=True
    )
    async for completion in stream:
        print(completion.choices[0].delta.content, end="")


if __name__ == "__main__":
    asyncio.run(main())
