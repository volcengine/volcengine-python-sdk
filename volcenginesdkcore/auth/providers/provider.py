# coding=utf-8
import abc
import json


class CredentialValue:
    def __init__(self, ak, sk, session_token=None, provider_name=None):
        self.ak = ak
        self.sk = sk
        self.session_token = session_token
        self.provider_name = provider_name


class Provider(object):
    PROVIDER_NAME = "Provider"

    @abc.abstractmethod
    def retrieve(self):
        raise NotImplementedError()

    @abc.abstractmethod
    def is_expired(self):
        raise NotImplementedError()

    @abc.abstractmethod
    def refresh(self):
        raise NotImplementedError()

    @abc.abstractmethod
    def get_credentials(self):
        raise NotImplementedError()

    def _parse_json_response(self, content, response_name="response"):
        try:
            resp = json.loads(content)
        except ValueError as e:
            raise RuntimeError(
                "{}: failed to parse {} as JSON: {}. raw={}".format(
                    self.PROVIDER_NAME, response_name, e, content
                )
            )

        if not isinstance(resp, dict):
            raise RuntimeError(
                "{}: unexpected {} type: {}".format(
                    self.PROVIDER_NAME, response_name, type(resp).__name__
                )
            )

        return resp

    def _unwrap_result(self, resp, response_name="response"):
        if 'Result' not in resp:
            return resp

        result = resp['Result']
        if not isinstance(result, dict):
            raise RuntimeError(
                "{}: unexpected {}.Result type: {}".format(
                    self.PROVIDER_NAME, response_name, type(result).__name__
                )
            )

        return result
