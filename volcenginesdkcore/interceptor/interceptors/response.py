class Response:
    def __init__(self, http_response):
        self.http_response = http_response
        self.result = None
        self.metadata = None
