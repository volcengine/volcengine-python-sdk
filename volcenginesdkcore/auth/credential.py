# coding=utf-8
class Credential(object):

    def __init__(self, provider):
        self.provider = provider

    def get(self):
        """
        .. deprecated::
            Use provider.get_credentials() instead.
        """
        if self.provider.is_expired():
            # refresh if expired
            self.provider.refresh()
        return self.provider.retrieve()
