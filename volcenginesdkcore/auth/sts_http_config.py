# coding: utf-8
"""Proxy / TLS customization shared by the STS credential providers.

This mirrors the Go SDK's ``ProxyConfig`` (see ``volcengine/credentials/
http_client.go``). It bundles the three public knobs used when reaching the
STS endpoint and knows how to project them onto an SDK ``Configuration``:

    proxy_url            -> configuration.proxy
    ca_file              -> configuration.ssl_ca_cert
    insecure_skip_verify -> configuration.verify_ssl (inverted)

Unlike the Go SDK -- which builds a dedicated ``*http.Transport`` -- the
Python SDK already routes every request (including STS federation calls)
through ``RESTClientObject``, which reads these ``Configuration`` fields
directly. So the only thing this helper needs to do is set the fields.

Proxy priority matches Go: an explicit ``proxy_url`` wins; when it is empty
the transport falls back to the standard ``HTTP_PROXY`` / ``HTTPS_PROXY`` /
``NO_PROXY`` environment variables.

TLS priority also matches Go's ``tls.Config``: ``insecure_skip_verify``
takes precedence over ``ca_file`` (when verification is skipped the custom
CA is irrelevant).
"""

from __future__ import absolute_import

from six.moves.urllib.parse import unquote, urlparse


class StsHttpConfig(object):
    """Carries proxy / TLS options for a single STS request path.

    :param proxy_url: Forward proxy address, ``scheme://[user:password@]host:port``.
                      Empty falls back to HTTP_PROXY / HTTPS_PROXY / NO_PROXY.
    :param ca_file: Path to a custom CA bundle (PEM) used to verify the STS
                    server certificate. Empty uses the default trust store.
    :param insecure_skip_verify: When True, skip TLS certificate/hostname
                    verification. For debugging only; never use in production.
    """

    def __init__(self, proxy_url=None, ca_file=None, insecure_skip_verify=False):
        self.proxy_url = proxy_url or None
        self.ca_file = ca_file or None
        self.insecure_skip_verify = bool(insecure_skip_verify)

    def is_empty(self):
        """True when no proxy/TLS option is configured.

        Callers use this to leave the underlying ``Configuration`` untouched,
        so existing behavior (including VOLCENGINE env-var proxies) is
        preserved when the user did not opt in. Mirrors Go's ``IsZero``.
        """
        return (not self.proxy_url) and (not self.ca_file) and (not self.insecure_skip_verify)

    def apply_to_configuration(self, configuration):
        """Project the configured options onto ``configuration`` in place.

        No-op when :meth:`is_empty` is True.
        """
        if self.is_empty():
            return configuration

        if self.proxy_url:
            # Highest-priority proxy source; RESTClientObject honors this over
            # http_proxy / https_proxy / env vars.
            configuration.proxy = self.proxy_url

        # TLS: insecure_skip_verify wins over ca_file (same as Go's tls.Config,
        # where RootCAs is ignored once InsecureSkipVerify is set).
        if self.insecure_skip_verify:
            configuration.verify_ssl = False
        elif self.ca_file:
            configuration.ssl_ca_cert = self.ca_file

        return configuration

    def proxy_authorization_header(self):
        """Return the ``Proxy-Authorization`` header value, or None.

        Delegates to :func:`build_proxy_authorization_header` using this
        config's ``proxy_url``.
        """
        return build_proxy_authorization_header(self.proxy_url)


def build_proxy_authorization_header(proxy_url):
    """Build a ``Basic`` ``Proxy-Authorization`` value from an embedded userinfo.

    urllib3 (v2) does NOT automatically forward the ``user:password@`` embedded
    in a proxy URL as a ``Proxy-Authorization`` header, whereas Go's
    ``http.ProxyURL`` / ``http.ProxyFromEnvironment`` do. To keep behavior
    aligned with the Go SDK, callers extract this header explicitly and pass it
    to ``ProxyManager(proxy_headers=...)``.

    Returns None when ``proxy_url`` is empty or carries no userinfo. Raises
    ``ValueError`` when ``proxy_url`` cannot be parsed.
    """
    if not proxy_url:
        return None

    try:
        parsed = urlparse(proxy_url)
    except (ValueError, AttributeError) as e:
        raise ValueError("invalid proxy url {0!r}: {1}".format(proxy_url, e))

    username = parsed.username
    if not username:
        return None
    password = parsed.password or ""

    # Go's http.Transport derives proxy Basic auth from url.Userinfo, whose
    # Username()/Password() return the PERCENT-DECODED values. urlparse keeps
    # userinfo raw, so decode here to stay byte-for-byte identical with the Go
    # SDK (e.g. a "p%40ss" password must be sent as "p@ss").
    username = unquote(username)
    password = unquote(password)

    # Match Go's basicAuth: base64("username:password") of the decoded userinfo.
    # urllib3.util.make_headers does exactly this encoding.
    import urllib3
    headers = urllib3.util.make_headers(
        proxy_basic_auth="{0}:{1}".format(username, password)
    )
    # make_headers lowercases the key; normalize to the canonical header name.
    value = headers.get("proxy-authorization") or headers.get("Proxy-Authorization")
    return value
