"""Client-local bindings for the concrete built-in STS providers."""
import copy
import threading

from six.moves.urllib.parse import urlparse


def new_sts_configuration(provider):
    from volcenginesdkcore.configuration import Configuration

    snapshot = getattr(provider, '_sts_base_configuration', None)
    configuration = copy.copy(snapshot) if snapshot is not None else Configuration()
    configuration.credential_provider = None
    return configuration


def bind_credential_provider(provider, configuration):
    from .providers.sts_provider import StsCredentialProvider
    from .providers.sts_oidc_provider import StsOidcCredentialProvider
    from .providers.sts_saml_provider import StsSamlCredentialProvider

    # Unknown subclasses can own resources or custom copy behavior.
    if type(provider) not in (
            StsCredentialProvider, StsOidcCredentialProvider, StsSamlCredentialProvider):
        return provider

    with provider._lock:
        bound = copy.copy(provider)
        bound.policy = copy.deepcopy(provider.policy)
        bound.credentials = None
        bound.expired_time = None
        bound._lock = threading.Lock()
        bound._sts_base_configuration = new_sts_configuration(provider)
        # Endpoint resolution accepts a scheme embedded in host.
        scheme = urlparse(bound.host).scheme if bound.host and '://' in bound.host else bound.scheme
        bound.scheme = scheme
        fallback = configuration.proxy
        if not fallback and scheme in ('http', 'https'):
            fallback = getattr(configuration, scheme + '_proxy')
        # Do not turn environment proxy settings into explicit overrides.
        bound._proxy_fallback = fallback or None
    return bound
