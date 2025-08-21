import queue
import sys
from datetime import datetime
from multiprocessing.pool import ThreadPool

from volcenginesdkarkruntime import Ark

# Authentication
# 1.If you authorize your endpoint using an API key, you can set your api key to environment variable "ARK_API_KEY"
# or specify api key by Ark(api_key="${YOUR_API_KEY}").
# Note: If you use an API key, this API key will not be refreshed.
# To prevent the API from expiring and failing after some time, choose an API key with no expiration date.

# 2.If you authorize your endpoint with Volcengine Identity and Access Management（IAM), set your api key to environment variable "VOLC_ACCESSKEY", "VOLC_SECRETKEY"
# or specify ak&sk by Ark(ak="${YOUR_AK}", sk="${YOUR_SK}").
# To get your ak&sk, please refer to this document(https://www.volcengine.com/docs/6291/65568)
# For more information，please check this document（https://www.volcengine.com/docs/82379/1263279）


def worker(
    worker_id: int,
    client: Ark,
    requests: "queue.Queue[dict]",
):
    print(f"Worker {worker_id} is starting.")

    while True:
        request = requests.get()

        # check for signal of no more request
        if not request:
            # put back on the queue for other workers
            requests.put(request)
            return

        try:
            # do request
            completion = client.batch.chat.completions.create(**request)
            print(completion)
        except Exception as e:
            print(e, file=sys.stderr)
        finally:
            requests.task_done()


def main():
    start = datetime.now()
    max_concurrent_tasks, task_num = 10, 100

    requests = queue.Queue()
    client = Ark(timeout=24 * 3600)

    # mock `task_num` tasks
    for _ in range(task_num):
        requests.put(
            {
                "model": "${YOUR_ENDPOINT_ID}",
                "messages": [
                    {
                        "role": "system",
                        "content": "你是豆包，是由字节跳动开发的 AI 人工智能助手",
                    },
                    {"role": "user", "content": "常见的十字花科植物有哪些？"},
                ],
            }
        )

    # put a signal of no more request
    requests.put(None)

    # create `max_concurrent_tasks` workers and start them
    with ThreadPool(max_concurrent_tasks) as pool:
        for i in range(max_concurrent_tasks):
            pool.apply_async(worker, args=(i, client, requests))

        # wait for all request to done
        pool.close()
        pool.join()

    client.close()

    end = datetime.now()
    print(f"Total time: {end - start}, Total task: {task_num}")


if __name__ == "__main__":
    main()
