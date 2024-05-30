from volcenginesdkarkruntime import Ark

# Support ak&sk or api key
# 1. Fetch ak&sk from environmental variables "VOLC_ACCESSKEY", "VOLC_SECRETKEY"
# or specify ak&sk by Ark(ak="${YOUR_AK}", sk="${YOUR_SK}").
# you can get ak&sk follow this document(https://www.volcengine.com/docs/6291/65568)
#
# 2. Fetch api key from environmental variables "ARK_API_KEY"
# or specify api key by Ark(api_key="${YOUR_API_KEY}").
# Note: if you support api key，this api key will not be refreshed.
# If you don't want the api to fail after a period of time, to the api key that never expires.
client = Ark()

if __name__ == "__main__":
    # Non-streaming:
    print("----- standard request -----")
    completion = client.chat.completions.create(
        model="${YOUR_ENDPOINT_ID}",
        messages=[
            {
                "role": "user",
                "content": "Say this is a test",
            },
        ]
    )
    print(completion.choices[0].message.content)

    print("----- multiple rounds request -----")
    completion = client.chat.completions.create(
        model="${YOUR_ENDPOINT_ID}",
        messages=[
            {
                "role": "user",
                "content": "Say this is a test",
            },
            {
                "role": "assistant",
                "content": "this is a test",
            },
            {
                "role": "user",
                "content": "what have you say?",
            },
        ]
    )
    print(completion.choices[0].message.content)

    # Streaming:
    print("----- streaming request -----")
    stream = client.chat.completions.create(
        model="${YOUR_ENDPOINT_ID}",
        messages=[
            {
                "role": "user",
                "content": "How do I output all files in a directory using Python?",
            },
        ],
        stream=True
    )
    for chunk in stream:
        if not chunk.choices:
            continue

        print(chunk.choices[0].delta.content, end="")
    print()
