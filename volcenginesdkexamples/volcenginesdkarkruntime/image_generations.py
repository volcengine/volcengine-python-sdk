from volcenginesdkarkruntime import Ark
from volcenginesdkarkruntime.types.images.images import SequentialImageGenerationOptions

# Authentication
# 1.If you authorize your endpoint using an API key, you can set your api key to environment variable "ARK_API_KEY"
# or specify api key by Ark(api_key="${YOUR_API_KEY}").
# Note: If you use an API key, this API key will not be refreshed.
# To prevent the API from expiring and failing after some time, choose an API key with no expiration date.
client = Ark()

if __name__ == "__main__":
    print("----- [Seedream] generate images -----")

    result = client.images.generate(
        model="${YOUR_SEEDREAM_ENDPOINT_ID}",
        prompt="龙与地下城女骑士背景是起伏的平原，目光从镜头转向平原",
        seed=1234567890,
        watermark=True,
        size="1024x1024",
    )

    print(result)

    print("----- [Seededit] generate images -----")

    result = client.images.generate(
        model="${YOUR_SEEDREAM_ENDPOINT_ID}",
        prompt="龙与地下城女骑士背景是起伏的平原，目光从镜头转向平原",
        # image="${YOUR_IMAGE_URL}",
        seed=1234567890,
        watermark=True,
        size="1024x1024",
    )

    print(result)

    print("----- [Seedream] generate images (response format: url) -----")

    stream = client.images.generate(
        model="${YOUR_SEEDREAM_ENDPOINT_ID}",
        prompt="星球大战, 需要三幅图片描绘不同的战斗场景",
        response_format="url",
        # image=["YOUR_IMAGE_URL_HERE", "YOUR_IMAGE_URL_HERE"],
        seed=1234567890,
        watermark=True,
        size="1024x1024",
        stream=True,
        sequential_image_generation="auto",
        sequential_image_generation_options=SequentialImageGenerationOptions(max_images=3),
    )

    for event in stream:
        if event is None:
            continue

        if event.type == "image_generation.partial_failed":
            print(f"Stream generate images error: {event.error}")
            if event.error is not None and event.error.code.equal("InternalServiceError"):
                break

        elif event.type == "image_generation.partial_succeeded":
            if event.error is None and event.url:
                print(f"recv.Size: {event.size}, recv.Url: {event.url}")

        elif event.type == "image_generation.completed":
            if event.error is None:
                print("Final completed event:")
                print("recv.Usage:", event.usage)
