# coding=utf-8
import logging
import threading

from .provider import Provider

logger = logging.getLogger(__name__)


class DefaultCredentialProvider(Provider):
    """4-step default credential chain:

    1. EnvironmentVariableCredentialProvider  (env AK/SK/STS)
    2. StsOidcCredentialProvider              (env OIDC)
    3. CLIConfigCredentialProvider            (CLI config.json)
    4. EcsRoleCredentialProvider              (IMDS)

    When reuse_last_provider_enabled is True (default), the chain caches the
    last successful provider and tries it first on subsequent calls.
    """

    PROVIDER_NAME = "DefaultCredentialProvider"

    def __init__(self, role_name=None,
                 reuse_last_provider_enabled=True,
                 providers=None):
        if providers is not None:
            # Custom provider chain
            self._providers = list(providers)
        else:
            # Default 4-step chain
            from .env_provider import EnvironmentVariableCredentialProvider
            from .sts_oidc_provider import StsOidcCredentialProvider
            from .cli_config_provider import CLIConfigCredentialProvider
            from .ecs_role_provider import EcsRoleCredentialProvider

            self._providers = [
                EnvironmentVariableCredentialProvider(),
                StsOidcCredentialProvider(),
                CLIConfigCredentialProvider(),
                EcsRoleCredentialProvider(role_name=role_name),
            ]
        self._reuse_last_provider_enabled = reuse_last_provider_enabled
        self._last_provider = None
        self._lock = threading.Lock()

    def retrieve(self):
        return self.get_credentials()

    def is_expired(self):
        provider = self._last_provider
        if provider is not None:
            return provider.is_expired()
        return True

    def refresh(self):
        provider = self._last_provider
        if provider is not None:
            try:
                provider.refresh()
                return
            except Exception:
                with self._lock:
                    self._last_provider = None
        self.get_credentials()

    def get_credentials(self):
        # Fast path: reuse last successful provider
        if self._reuse_last_provider_enabled:
            provider = self._last_provider
            if provider is not None:
                try:
                    creds = provider.get_credentials()
                    if creds is not None:
                        return creds
                except Exception:
                    with self._lock:
                        self._last_provider = None

        # Full chain traversal
        errors = []
        for provider in self._providers:
            try:
                creds = provider.get_credentials()
                if creds is not None:
                    if self._reuse_last_provider_enabled:
                        with self._lock:
                            self._last_provider = provider
                    return creds
            except Exception as e:
                errors.append("{}: {}".format(type(provider).__name__, str(e)))
                continue

        error_details = "\n  ".join(errors) if errors else "no providers configured"
        raise RuntimeError(
            "{}: unable to resolve credentials from any provider in the chain.\n"
            "Attempted providers:\n  {}".format(self.PROVIDER_NAME, error_details)
        )
