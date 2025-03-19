# coding=utf-8
import abc


class Interceptor(object):
    """拦截器基类"""

    @abc.abstractmethod
    def name(self):
        raise NotImplementedError()

    @abc.abstractmethod
    def intercept(self, context):
        raise NotImplementedError()

    @abc.abstractmethod
    def is_common(self):
        raise NotImplementedError()

    @abc.abstractmethod
    def is_request(self):
        raise NotImplementedError()

    @abc.abstractmethod
    def is_response(self):
        raise NotImplementedError()
