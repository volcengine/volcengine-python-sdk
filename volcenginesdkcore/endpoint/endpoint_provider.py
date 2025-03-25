# coding=utf-8

import abc


class ResolvedEndpoint:
    def __init__(self, host):
        self.host = host

    def url_for(self, scheme='https'):
        return scheme + '://' + self.host


class EndpointProvider(object):

    @abc.abstractmethod
    def endpoint_for(self, service, region):
        raise NotImplementedError()
