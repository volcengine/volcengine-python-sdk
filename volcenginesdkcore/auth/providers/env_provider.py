# coding=utf-8
import os

from .provider import Provider, CredentialValue


class EnvironmentVariableCredentialProvider(Provider):
    """Reads AK/SK/STS Token from environment variables with dual-read fallback.

    Priority:
      AK:    VOLCENGINE_ACCESS_KEY
      SK:    VOLCENGINE_SECRET_KEY
      Token: VOLCENGINE_SESSION_TOKEN
    """

    PROVIDER_NAME = "EnvironmentVariableCredentialProvider"

    def retrieve(self):
        return self.get_credentials()

    def is_expired(self):
        return False

    def refresh(self):
        return

    def get_credentials(self):
        ak = os.environ.get("VOLCENGINE_ACCESS_KEY")
        sk = os.environ.get("VOLCENGINE_SECRET_KEY")

        if not ak or not sk:
            raise RuntimeError(
                "{}: unable to resolve credentials from environment variables. "
                "Please set VOLCENGINE_ACCESS_KEY and VOLCENGINE_SECRET_KEY.".format(
                    self.PROVIDER_NAME
                )
            )

        session_token = os.environ.get("VOLCENGINE_SESSION_TOKEN")

        return CredentialValue(
            ak=ak,
            sk=sk,
            session_token=session_token if session_token else None,
            provider_name=self.PROVIDER_NAME,
        )
