# coding=utf-8


class InterceptorContext:
    """拦截器上下文"""

    def __init__(self, request=None, response=None):
        self.request = request
        self.response = response
        self.metadata = {}  # 元数据可用于在拦截器之间传递信息

    def get_request(self):
        return self.request

    def get_response(self):
        return self.response

    def get_metadata(self):
        return self.metadata

    def set_request(self, request):
        self.request = request

    def set_response(self, response):
        self.response = response

    def set_metadata(self, metadata):
        self.metadata = metadata
