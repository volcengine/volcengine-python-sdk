import datetime
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
client = Ark(api_key="${YOUR_API_KEY}")

if __name__ == "__main__":
    # Create context with 30 minutes cache:
    print("----- create context -----")
    response = client.context.create(
        model="${YOUR_ENDPOINT_ID}",
        messages=[
            {"role": "system", "content": "你是豆包，是由字节跳动开发的 AI 人工智能助手"},
        ],
        ttl=datetime.timedelta(minutes=30),
    )
    print(response)

    # Streaming:
    print("----- streaming request -----")
    stream = client.context.completions.create(
        context_id=response.id,
        model="${YOUR_ENDPOINT_ID}",
        messages=[
            {"role": "user", "content": "你是谁？"},
        ],
        stream=True
    )
    for chunk in stream:
        if not chunk.choices:
            continue
        print(chunk.choices[0].delta.content, end="")
