import unittest

from volcenginesdkarkruntime.types.images.image_gen_completed_event import (
    Usage as CompletedUsage,
)
from volcenginesdkarkruntime.types.images.images import Usage


class TestImageGenerationUsageCompatibility(unittest.TestCase):
    def test_usage_allows_missing_input_images(self):
        usage = Usage(generated_images=1)

        self.assertIsNone(usage.input_images)

    def test_completed_usage_allows_missing_input_images(self):
        usage = CompletedUsage(generated_images=1, output_tokens=2, total_tokens=2)

        self.assertIsNone(usage.input_images)


if __name__ == "__main__":
    unittest.main()
