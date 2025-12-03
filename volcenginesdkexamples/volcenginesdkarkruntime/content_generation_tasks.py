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
                "type": "text",
                "text": "龙与地下城女骑士背景是起伏的平原，目光从镜头转向平原"
            },
            {
                "type": "image_url",
                "image_url": {
                    "url": "${YOUR_IMAGE_URL}"
                },
                # "role": "first_frame"
            }
        ],
        service_tier="default",
        execution_expires_after=3600,
        # callback_url="${YOUR_CALLBACK_URL}"
    )
    print(create_result)

    print("----- get request -----")
    get_result = client.content_generation.tasks.get(task_id=create_result.id)
    print(get_result)
    print("ServiceTier:", getattr(get_result, "service_tier", None))
    print("ExecutionExpiresAfter:", getattr(get_result, "execution_expires_after", None))

    print("----- list request -----")
    list_result = client.content_generation.tasks.list(
        page_num=1,
        page_size=10,
        status="queued",  # succeeded, failed, running, cancelled
        # model="${YOUR_MODEL_EP}", # Filter by model
        # task_ids=["test-id-1", "test-id-2"] # Filter by task_ids
    )
    print(list_result)
    if list_result.items:
        print("List Item ServiceTier:", getattr(list_result.items[0], "service_tier", None))
        print("List Item ExecutionExpiresAfter:", getattr(list_result.items[0], "execution_expires_after", None))

    print("----- delete request -----")
    try:
        client.content_generation.tasks.delete(task_id=create_result.id)
        print(create_result.id)
    except Exception as e:
        print(f"failed to delete task: {e}")

    # ---- flex tier flow: create + GET + LIST + DELETE ----
    print("----- create request (flex) -----")
    create_result_flex = client.content_generation.tasks.create(
        model="${YOUR_MODEL_EP}",
        content=[
            {
                "type": "text",
                "text": "使用 flex 级别进行内容生成测试，验证 service_tier 与 expire 字段"
            }
        ],
        service_tier="flex",
        execution_expires_after=3600,
    )
    print(create_result_flex)

    print("----- get request (flex) -----")
    get_result_flex = client.content_generation.tasks.get(task_id=create_result_flex.id)
    print(get_result_flex)
    print("Flex ServiceTier:", getattr(get_result_flex, "service_tier", None))
    print("Flex ExecutionExpiresAfter:", getattr(get_result_flex, "execution_expires_after", None))

    print("----- list request (flex) -----")
    list_result_flex = client.content_generation.tasks.list(
        page_num=1,
        page_size=10,
        service_tier="flex",
    )
    print(list_result_flex)
    if list_result_flex.items:
        print("Flex List Item ServiceTier:", getattr(list_result_flex.items[0], "service_tier", None))
        print("Flex List Item ExecutionExpiresAfter:", getattr(list_result_flex.items[0], "execution_expires_after", None))

    print("----- delete request (flex) -----")
    try:
        client.content_generation.tasks.delete(task_id=create_result_flex.id)
        print(create_result_flex.id)
    except Exception as e:
        print(f"failed to delete flex task: {e}")
