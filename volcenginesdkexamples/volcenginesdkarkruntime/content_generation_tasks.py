from volcenginesdkarkruntime import Ark

# Authentication
# 1.If you authorize your endpoint using an API key, you can set your api key to environment variable "ARK_API_KEY"
# or specify api key by Ark(api_key="${YOUR_API_KEY}").
# Note: If you use an API key, this API key will not be refreshed.
# To prevent the API from expiring and failing after some time, choose an API key with no expiration date.
client = Ark()

if __name__ == "__main__":
    print("----- create request -----")
    create_result = client.content_generation.tasks.create(
        model="${YOUR_MODEL_EP}",
        content=[
            {
                "type":"text",
                "text":"龙与地下城女骑士背景是起伏的平原，目光从镜头转向平原"
            },
            {
                "type":"image_url",
                "image_url": {
                    "url": "${YOUR_IMAGE_URL}"
                },
            }
        ]
    )
    print(create_result)

    print("----- get request -----")
    get_result = client.content_generation.tasks.get(task_id=create_result.id)
    print(get_result)

    print("----- list request -----")
    list_result = client.content_generation.tasks.list(
        page_num=1,
        page_size=10,
        status="queued",
        # model="${YOUR_MODEL_EP}", # Filter by model
        # task_ids=["test-id-1", "test-id-2"] # Filter by task_ids
    )
    print(list_result)

    print("----- delete request -----")
    try:
        client.content_generation.tasks.delete(task_id=create_result.id)
        print(create_result.id)
    except Exception as e:
        print(f"failed to delete task: {e}")