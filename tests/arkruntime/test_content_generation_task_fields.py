import unittest

from volcenginesdkarkruntime._compat import get_model_fields, model_parse
from volcenginesdkarkruntime.types.content_generation.content_generation_task import (
    ContentGenerationTask,
)


class ContentGenerationTaskFieldsTest(unittest.TestCase):
    def setUp(self):
        self.payload = {
            "id": "task-123",
            "model": "test-model",
            "status": "succeeded",
            "error": {"message": "", "code": ""},
            "content": {
                "video_url": "https://example.com/video.mp4",
                "last_frame_url": "https://example.com/last-frame.png",
                "file_url": "https://example.com/output.mp4",
            },
            "usage": {"completion_tokens": 42},
            "subdivisionlevel": "1",
            "fileformat": "mp4",
            "frames": 120,
            "framespersecond": 24,
            "created_at": 1_700_000_000,
            "updated_at": 1_700_000_100,
            "seed": 12345,
            "revised_prompt": "A revised prompt",
            "service_tier": "default",
            "execution_expires_after": 3600,
            "priority": 1,
            "generate_audio": True,
            "duration": 5,
            "ratio": "16:9",
            "resolution": "1080p",
            "draft": False,
            "draft_task_id": "draft-123",
            "tools": [{"type": "camera"}],
        }

    def test_output_format_is_declared_field(self):
        self.assertIn("output_format", get_model_fields(ContentGenerationTask))

    def test_parses_output_format(self):
        payload = {**self.payload, "output_format": "mp4"}

        task = model_parse(ContentGenerationTask, payload)

        self.assertEqual(task.output_format, "mp4")

    def test_output_format_defaults_to_none(self):
        task = model_parse(ContentGenerationTask, self.payload)

        self.assertIsNone(task.output_format)


if __name__ == "__main__":
    unittest.main()
