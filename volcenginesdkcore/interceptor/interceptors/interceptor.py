# coding=utf-8
import abc


class RequestInterceptor(object):

    @abc.abstractmethod
    def name(self):
        raise NotImplementedError()

    @abc.abstractmethod
    def intercept(self, context):
        raise NotImplementedError()


class ResponseInterceptor(object):

    @abc.abstractmethod
    def name(self):
        raise NotImplementedError()

    @abc.abstractmethod
    def intercept(self, context):
        raise NotImplementedError()
