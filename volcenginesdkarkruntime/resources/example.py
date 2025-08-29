import os

from volcenginesdkarkruntime import Ark
from volcenginesdkarkruntime.types.images.images import SequentialImageGenerationOptions

client = Ark(
    base_url="https://ark.cn-beijing.volces.com/api/v3",
    api_key=os.environ.get("ARK_API_KEY"),
)

if __name__ == "__main__":
    modelEp = "YOUR_ENDPOINT_ID"
    print("----- [Seedream] generate images (response format: url) -----")
    stream = client.images.generate(
        model=modelEp,
        prompt="星球大战, 需要三幅图片描绘不同的战斗场景",
        response_format= "url",
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
            if event.error and event.error.code and event.error.code.startswith("5"):
                break

        elif event.type == "image_generation.partial_succeeded":
            if event.error is None and event.url:
                print(f"recv.Size: {event.size}, recv.Url: {event.url}")

        elif event.type == "image_generation.completed":
            if event.error is None:
                print("Final completed event:")
                print("recv.Usage:", event.usage)

        elif event.type == "image_generation.partial_image":
            print(f"Partial image index={event.partial_image_index}, size={len(event.b64_json)}")
