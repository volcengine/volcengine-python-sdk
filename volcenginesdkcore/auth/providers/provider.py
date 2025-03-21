# coding=utf-8
import abc


class CredentialValue:
    def __init__(self, ak, sk, session_token=None, provider_name=None):
        self.ak = ak
        self.sk = sk
        self.session_token = session_token
        self.provider_name = provider_name


class Provider(object):

    @abc.abstractmethod
    def retrieve(self):
        raise NotImplementedError()

    @abc.abstractmethod
    def is_expired(self):
        raise NotImplementedError()

    @abc.abstractmethod
    def refresh(self):
        raise NotImplementedError()
