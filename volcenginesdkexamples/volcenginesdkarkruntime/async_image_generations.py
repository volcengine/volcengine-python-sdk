import asyncio

from volcenginesdkarkruntime import AsyncArk

# Authentication
# 1.If you authorize your endpoint using an API key, you can set your api key to environment variable "ARK_API_KEY"
# or specify api key by Ark(api_key="${YOUR_API_KEY}").
# Note: If you use an API key, this API key will not be refreshed.
# To prevent the API from expiring and failing after some time, choose an API key with no expiration date.
client = AsyncArk()


async def main():
    print("----- [Seedream] async generate images -----")

    result = client.images.generate(
        model="${YOUR_SEEDREAM_ENDPOINT_ID}",
        prompt="龙与地下城女骑士背景是起伏的平原，目光从镜头转向平原",
        seed=1234567890,
        watermark=True,
        size="512x512",
        guidance_scale=2.5,
    )

    print(await result)

    print("----- [Seededit] async generate images async -----")

    result = client.images.generate(
        model="${YOUR_SEEDEDIT_ENDPOINT_ID}",
        prompt="龙与地下城女骑士背景是起伏的平原，目光从镜头转向平原",
        image="${YOUR_IMAGE_URL}",
        seed=1234567890,
        watermark=True,
        size="adaptive",
        guidance_scale=2.5,
    )

    print(await result)

if __name__ == "__main__":
    asyncio.run(main())
