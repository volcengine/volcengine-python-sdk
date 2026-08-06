import unittest

from volcenginesdkarkruntime.resources.content_generation.tasks import AsyncTasks, Tasks


class FakeSyncClient:
    api_key = "test"

    def __init__(self):
        self.body = None

    def post(self, path, *, body, **kwargs):
        self.body = body
        return object()

    def get(self, *args, **kwargs):
        return object()

    def delete(self, *args, **kwargs):
        return object()

    def post_without_retry(self, *args, **kwargs):
        return object()

    def get_api_list(self, *args, **kwargs):
        return object()


class FakeAsyncClient:
    api_key = "test"

    def __init__(self):
        self.body = None

    async def post(self, path, *, body, **kwargs):
        self.body = body
        return object()

    def get(self, *args, **kwargs):
        return object()

    def delete(self, *args, **kwargs):
        return object()

    def post_without_retry(self, *args, **kwargs):
        return object()

    def get_api_list(self, *args, **kwargs):
        return object()


class TasksOutputFormatTest(unittest.TestCase):
    def test_create_includes_optional_output_format(self):
        client = FakeSyncClient()
        tasks = Tasks(client)

        tasks.create(model="test-model", content=[], output_format="mp4")
        self.assertEqual(client.body["output_format"], "mp4")

        tasks.create(model="test-model", content=[])
        self.assertIsNone(client.body["output_format"])


class AsyncTasksOutputFormatTest(unittest.IsolatedAsyncioTestCase):
    async def test_create_includes_optional_output_format(self):
        client = FakeAsyncClient()
        tasks = AsyncTasks(client)

        await tasks.create(model="test-model", content=[], output_format="mp4")
        self.assertEqual(client.body["output_format"], "mp4")

        await tasks.create(model="test-model", content=[])
        self.assertIsNone(client.body["output_format"])


if __name__ == "__main__":
    unittest.main()
