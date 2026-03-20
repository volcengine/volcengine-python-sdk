import json
class Response:
    def __init__(self, http_response):
        self.http_response = http_response
        self.result = None
        self.metadata = None
        self.__post_init__()

    def __post_init__(self):
        data = json.loads(self.http_response.data)
        self.result = data.get("Result")
        self.metadata = data.get("ResponseMetadata")
