from typing import Optional

from volcenginesdkwaf import CheckLLMResponseStreamResponse


class LLMStreamSession:
    """对应 Java 中的 LLMStreamSession 类"""

    def __init__(
            self,
            stream_buf: str = "",
            stream_send_len: int = 0,
            msg_id: str = "",
            default_body: Optional[CheckLLMResponseStreamResponse] = None
    ):
        self.stream_buf = stream_buf
        self.stream_send_len = stream_send_len
        self.msg_id = msg_id
        self.default_body = default_body

    def get_stream_buf(self) -> str:
        return self.stream_buf

    def set_stream_buf(self, stream_buf: str) -> None:
        self.stream_buf = stream_buf

    def get_stream_send_len(self) -> int:
        return self.stream_send_len

    def set_stream_send_len(self, stream_send_len: int) -> None:
        self.stream_send_len = stream_send_len

    def get_msg_id(self) -> str:
        return self.msg_id

    def set_msg_id(self, msg_id: str) -> None:
        self.msg_id = msg_id

    def get_default_body(self) -> Optional[CheckLLMResponseStreamResponse]:
        return self.default_body

    def set_default_body(self, default_body: Optional[CheckLLMResponseStreamResponse]) -> None:
        self.default_body = default_body

    def append_stream_buf(self, text: Optional[str]) -> None:
        """追加文本到流缓冲区并更新发送长度"""
        if text is not None:
            self.stream_buf += text
            self.stream_send_len += len(text)
