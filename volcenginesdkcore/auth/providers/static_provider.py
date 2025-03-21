# coding=utf-8
from .provider import Provider, CredentialValue


class StaticCredentialProvider(Provider):
    """静态凭证提供者"""

    def _refresh(self):
        return

    def __init__(self, access_key_id, secret_access_key, session_token=None):
        self.credentials = CredentialValue(
            access_key_id,
            secret_access_key,
            session_token,
            "StaticCredentialProvider"
        )

    def retrieve(self):
        return self.credentials

    def is_expired(self):
        return False

    def refresh(self):
        return
