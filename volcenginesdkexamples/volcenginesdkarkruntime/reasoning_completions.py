from volcenginesdkarkruntime import Ark

# Authentication
# 1.If you authorize your endpoint using an API key, you can set your api key to environment variable "ARK_API_KEY"
# or specify api key by Ark(api_key="${YOUR_API_KEY}").
# Note: If you use an API key, this API key will not be refreshed.
# To prevent the API from expiring and failing after some time, choose an API key with no expiration date.

# 2.If you authorize your endpoint with Volcengine Identity and Access Management（IAM),
# set your api key to environment variable "VOLC_ACCESSKEY", "VOLC_SECRETKEY"
# or specify ak&sk by Ark(ak="${YOUR_AK}", sk="${YOUR_SK}").
# To get your ak&sk, please refer to this document(https://www.volcengine.com/docs/6291/65568)
# For more information，please check this document（https://www.volcengine.com/docs/82379/1263279）
client = Ark()

if __name__ == "__main__":
    # Streaming:
    print("----- streaming request -----")
    stream = client.chat.completions.create(
        model="${YOUR_ENDPOINT_ID}",
        messages=[
            {"role": "user", "content": "How many Rs are there in the word 'strawberry'?"},
        ],
        thinking={"type": "enabled"},
        stream=True
    )
    for chunk in stream:
        if not chunk.choices:
            continue
        if chunk.choices[0].delta.reasoning_content:
            print(chunk.choices[0].delta.reasoning_content, end="")
        else:
            print(chunk.choices[0].delta.content, end="")
    print()

    # Non-streaming:
    print("----- standard request -----")
    completion = client.chat.completions.create(
        model="${YOUR_ENDPOINT_ID}",
        messages=[
            {"role": "user", "content": "How many Rs are there in the word 'strawberry'?"},
        ],
        thinking={"type": "enabled"},
    )
    print(completion.choices[0].message.reasoning_content)
    print(completion.choices[0].message.content)
