# coding=utf-8
class Credential(object):
    """凭证管理类"""

    def __init__(self, provider):
        self.provider = provider

    def get(self):
        if self.provider.is_expired():
            # 当凭证过期时自动刷新
            self.provider.refresh()
        return self.provider.retrieve()
