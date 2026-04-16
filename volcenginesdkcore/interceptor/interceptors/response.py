import json
class Response:
    def __init__(self, http_response):
        self.http_response = http_response
        self.result = None
        self.metadata = None
        self.__post_init__()

    def __post_init__(self):
        data = getattr(self.http_response, "data", None)
        if data is None:
            return

        # If data is bytes-like, attempt to decode to text before JSON parsing.
        if isinstance(data, (bytes, bytearray)):
            try:
                data = data.decode("utf-8")
            except Exception:
                # Non-textual or undecodable data; leave result/metadata as None.
                return

        # Only attempt JSON parsing on string data.
        if not isinstance(data, str):
            return

        try:
            parsed = json.loads(data)
        except (ValueError, TypeError):
            # Invalid JSON content; leave result/metadata as None.
            return

        if isinstance(parsed, dict):
            self.result = parsed.get("Result")
            self.metadata = parsed.get("ResponseMetadata")
