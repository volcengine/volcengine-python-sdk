# coding=utf-8

import abc


class ResolvedEndpoint:
    def __init__(self, host, scheme="https"):
        self.host = host
        self.scheme = scheme

    @property
    def full_url(self):
        return self.scheme + '://' + self.host


class EndpointProvider(object):
    """接口类：确定服务请求的终端节点"""

    @abc.abstractmethod
    def endpoint_for(self, service, region):
        """返回指定服务和区域的终端节点"""
        raise NotImplementedError()
