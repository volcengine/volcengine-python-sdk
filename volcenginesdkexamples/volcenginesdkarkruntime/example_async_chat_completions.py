import asyncio

from volcenginesdkarkruntime import AsyncArk

# fetch ak&sk from environmental variables "VOLC_ACCESSKEY", "VOLC_SECRETKEY"
# or specify ak&sk by Ark(ak="${YOUR_AK}", sk="${YOUR_SK}").
# you can get ak&sk follow this document(https://www.volcengine.com/docs/6291/65568)
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
