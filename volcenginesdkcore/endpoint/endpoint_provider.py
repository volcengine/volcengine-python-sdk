# coding=utf-8

import abc


class ResolvedEndpoint:
    def __init__(self, host):
        self.host = host

    def url_for(self, scheme='https'):
        return scheme + '://' + self.host


class EndpointProvider(object):
    """接口类：确定服务请求的终端节点"""

    @abc.abstractmethod
    def endpoint_for(self, service, region):
        """返回指定服务和区域的终端节点"""
        raise NotImplementedError()
