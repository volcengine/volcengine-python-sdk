from typing_extensions import Literal

__all__ = ["ChatCompletionRole"]

ChatCompletionRole = Literal["system", "user", "assistant", "tool", "function"]
