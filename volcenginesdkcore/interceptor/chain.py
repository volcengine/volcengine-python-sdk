# coding=utf-8
from .interceptors import RequestInterceptor, ResponseInterceptor


def check_request_interceptor(interceptor):
    if not issubclass(interceptor.__class__, RequestInterceptor):
        raise Exception("interceptor is not for request")


def check_response_interceptor(interceptor):
    if not issubclass(interceptor.__class__, ResponseInterceptor):
        raise Exception("interceptor is not for response")


def insert_interceptor(chain, interceptor, after_name=''):
    if after_name == '':
        chain.insert(0, interceptor)
        return chain

    for i in range(len(chain)):
        if chain[i].name() == after_name:
            chain.insert(i + 1, interceptor)
            return chain

    raise Exception("interceptor insert after name not found")


class InterceptorChain:

    def __init__(self):
        self.request_interceptors = []
        self.response_interceptors = []

    def append_request_interceptor(self, interceptor):
        check_request_interceptor(interceptor)
        self.request_interceptors.append(interceptor)
        return self

    def insert_request_interceptor(self, interceptor, after_name=''):
        check_request_interceptor(interceptor)
        self.request_interceptors = insert_interceptor(self.request_interceptors, interceptor, after_name)
        return self

    def append_response_interceptor(self, interceptor):
        check_response_interceptor(interceptor)
        self.response_interceptors.append(interceptor)
        return self

    def insert_response_interceptor(self, interceptor, after_name=''):
        check_response_interceptor(interceptor)
        self.response_interceptors = insert_interceptor(self.response_interceptors, interceptor, after_name)

    def execute_request(self, context):
        for interceptor in self.request_interceptors:
            context = interceptor.intercept(context)

        return context

    def execute_response(self, context):
        for interceptor in self.response_interceptors:
            context = interceptor.intercept(context)

        return context
