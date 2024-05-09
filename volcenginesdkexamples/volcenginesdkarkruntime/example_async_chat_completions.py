import asyncio

from volcenginesdkarkruntime import AsyncArk

# gets API Key from environment variable ARK_API_KEY
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
        stream=True,
    )
    async for completion in stream:
        print(completion.choices[0].delta.content, end="")


if __name__ == '__main__':
    asyncio.run(main())
