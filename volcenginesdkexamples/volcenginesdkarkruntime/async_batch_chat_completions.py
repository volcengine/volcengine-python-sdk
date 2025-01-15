import asyncio
from datetime import datetime

from volcenginesdkarkruntime import AsyncArk

# Authentication
# 1.If you authorize your endpoint using an API key, you can set your api key to environment variable "ARK_API_KEY"
# or specify api key by Ark(api_key="${YOUR_API_KEY}").
# Note: If you use an API key, this API key will not be refreshed.
# To prevent the API from expiring and failing after some time, choose an API key with no expiration date.

# 2.If you authorize your endpoint with Volcengine Identity and Access Management（IAM), set your api key to environment variable "VOLC_ACCESSKEY", "VOLC_SECRETKEY"
# or specify ak&sk by Ark(ak="${YOUR_AK}", sk="${YOUR_SK}").
# To get your ak&sk, please refer to this document(https://www.volcengine.com/docs/6291/65568)
# For more information，please check this document（https://www.volcengine.com/docs/82379/1263279）
client = AsyncArk()


async def worker(semaphore, worker_id, task_num):
    async with semaphore:
        print(f"Worker {worker_id} is starting.")
        for i in range(task_num):
            print(f"Worker {worker_id} task {i} is running.")
            try:
                completion = await client.batch_chat.completions.create(
                    model="${YOUR_ENDPOINT_ID}",
                    messages=[
                        {"role": "system", "content": "你是豆包，是由字节跳动开发的 AI 人工智能助手"},
                        {"role": "user", "content": "常见的十字花科植物有哪些？"},
                    ],
                )
                print(completion.choices[0].message.content)
            except Exception as e:
                print(f"Worker {worker_id} task {i} failed with error: {e}")
            else:
                print(f"Worker {worker_id} task {i} is completed.")
        print(f"Worker {worker_id} is completed.")


async def main():
    start = datetime.now()
    max_concurrent_tasks = 1000
    task_num = 5
    semaphore = asyncio.Semaphore(max_concurrent_tasks)

    # 创建任务列表
    tasks = [worker(semaphore, i, task_num) for i in range(max_concurrent_tasks)]

    # 等待所有任务完成
    await asyncio.gather(*tasks)
    end = datetime.now()
    print(f"Total time: {end - start}, Total task: {max_concurrent_tasks * task_num}")


if __name__ == "__main__":
    asyncio.run(main())
