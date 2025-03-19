# coding=utf-8


def check_common_request_interceptor(interceptor):
    if not interceptor.is_common():
        raise Exception("interceptor is not common")
    if not interceptor.is_request():
        raise Exception("interceptor is not for request")
    if not interceptor.name():
        raise Exception("interceptor name is not defined")


def check_common_response_interceptor(interceptor):
    if not interceptor.is_common():
        raise Exception("interceptor is not common")
    if not interceptor.is_response():
        raise Exception("interceptor is not for response")
    if not interceptor.name():
        raise Exception("interceptor name is not defined")


def check_request_interceptor(interceptor):
    if interceptor.is_common():
        raise Exception("interceptor is common")
    if not interceptor.is_request():
        raise Exception("interceptor is not for request")
    if not interceptor.name():
        raise Exception("interceptor name is not defined")


def check_response_interceptor(interceptor):
    if interceptor.is_common():
        raise Exception("interceptor is common")
    if not interceptor.is_response():
        raise Exception("interceptor is not for response")
    if not interceptor.name():
        raise Exception("interceptor name is not defined")


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
    """拦截器链"""

    def __init__(self):
        self.common_request_interceptors = []
        self.request_interceptors = []
        self.common_response_interceptors = []
        self.response_interceptors = []

    def append_common_request_interceptor(self, interceptor):
        check_common_request_interceptor(interceptor)
        self.common_request_interceptors.append(interceptor)
        return self

    def insert_common_request_interceptor(self, interceptor, after_name=''):
        check_common_request_interceptor(interceptor)
        self.common_request_interceptors = insert_interceptor(self.common_request_interceptors, interceptor, after_name)
        return self

    def append_request_interceptor(self, interceptor):
        check_request_interceptor(interceptor)
        self.request_interceptors.append(interceptor)
        return self

    def insert_request_interceptor(self, interceptor, after_name=''):
        check_request_interceptor(interceptor)
        self.request_interceptors = insert_interceptor(self.request_interceptors, interceptor, after_name)
        return self

    def append_common_response_interceptor(self, interceptor):
        check_common_response_interceptor(interceptor)
        self.common_response_interceptors.append(interceptor)
        return self

    def insert_common_response_interceptor(self, interceptor, after_name=''):
        check_common_response_interceptor(interceptor)
        self.common_response_interceptors = insert_interceptor(self.common_response_interceptors, interceptor,
                                                               after_name)

    def append_response_interceptor(self, interceptor):
        check_response_interceptor(interceptor)
        self.response_interceptors.append(interceptor)
        return self

    def insert_response_interceptor(self, interceptor, after_name=''):
        check_response_interceptor(interceptor)
        self.response_interceptors = insert_interceptor(self.response_interceptors, interceptor, after_name)

    def execute_request(self, context):
        for interceptor in self.common_request_interceptors:
            context = interceptor.intercept(context)

        for interceptor in self.request_interceptors:
            context = interceptor.intercept(context)

        return context

    def execute_response(self, context):
        for interceptor in self.common_response_interceptors:
            context = interceptor.intercept(context)

        for interceptor in self.response_interceptors:
            context = interceptor.intercept(context)

        return context
