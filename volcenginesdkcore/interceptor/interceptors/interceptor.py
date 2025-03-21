# coding=utf-8
import abc


class RequestInterceptor(object):
    """请求拦截器"""

    @abc.abstractmethod
    def name(self):
        raise NotImplementedError()

    @abc.abstractmethod
    def intercept(self, context):
        raise NotImplementedError()


class ResponseInterceptor(object):
    """响应拦截器"""

    @abc.abstractmethod
    def name(self):
        raise NotImplementedError()

    @abc.abstractmethod
    def intercept(self, context):
        raise NotImplementedError()
