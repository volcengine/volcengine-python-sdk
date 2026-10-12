# coding: utf-8
"""Validation of the region and service used to build endpoint host names.

The region and service are concatenated into the endpoint host name (for
example ``{service}.{region}.volcengineapi.com``) and are part of the signing
credential scope. A value such as ``cn-beijing@127.0.0.1`` or ``evil.com#``
could change the host the request is actually sent to (SSRF), so both values
are validated before any endpoint is resolved, signed or sent.

A valid value is equivalent to the regular expression
``^[A-Za-z]([A-Za-z0-9_-]*[A-Za-z0-9])?$``:

- it only contains ASCII letters, digits, ``-`` and ``_``
- it starts with a letter
- it does not end with ``-`` or ``_``

An empty value (``''`` or ``None``) is allowed, the caller keeps its own
handling of missing values.
"""

import unicodedata

import six

ERR_CODE_INVALID_REGION = 'InvalidRegion'
ERR_CODE_INVALID_SERVICE = 'InvalidService'

_ENDPOINT_LABEL_RULE = ("must start with a letter, end with a letter or digit, "
                        "and contain only letters, digits, '-' and '_'")

_LETTERS = frozenset(bytearray(b'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'))
_DIGITS = frozenset(bytearray(b'0123456789'))
_TRAILING_FORBIDDEN = frozenset(bytearray(b'-_'))
_LABEL_CHARS = _LETTERS | _DIGITS | _TRAILING_FORBIDDEN

_GO_ESCAPES = {
    u'"': u'\\"', u'\\': u'\\\\', u'\a': u'\\a', u'\b': u'\\b',
    u'\f': u'\\f', u'\n': u'\\n', u'\r': u'\\r', u'\t': u'\\t', u'\v': u'\\v',
}


class EndpointValidationError(ValueError):
    """Raised when the region or service can not be safely used in a host name.

    ``code`` is ``InvalidRegion`` or ``InvalidService``; ``str(error)`` is
    formatted as ``Code: Message``.
    """

    def __init__(self, code, message):
        ValueError.__init__(self, '%s: %s' % (code, message))
        self.code = code
        self.message = message

    def __str__(self):
        text = u'%s: %s' % (self.code, self.message)
        if six.PY2 and isinstance(text, six.text_type):
            return text.encode('utf-8')
        return text


class EndpointValidationTypeError(EndpointValidationError, TypeError):
    """Raised when the region or service is not a string.

    Python is dynamically typed, so unlike the statically typed SDKs a value
    such as ``42`` or ``b'cn-beijing'`` can reach the endpoint resolution. It
    is both a ``TypeError`` (Python convention for a wrong type) and an
    ``EndpointValidationError`` keeping the ``InvalidRegion`` /
    ``InvalidService`` code, like ``io.UnsupportedOperation(OSError, ValueError)``.
    """


def _go_quote(value):
    """Quote value like Go's ``%q`` so that control characters stay visible."""
    if isinstance(value, six.binary_type):
        value = value.decode('utf-8', 'replace')
    out = [u'"']
    for ch in value:
        o = ord(ch)
        if ch in _GO_ESCAPES:
            out.append(_GO_ESCAPES[ch])
        elif o < 0x20 or o == 0x7f:
            out.append(u'\\x%02x' % o)
        elif o < 0x7f:
            out.append(ch)
        elif unicodedata.category(ch)[0] in ('C', 'Z'):
            # Not printable for Go (control, format, separator, unassigned...).
            out.append(u'\\u%04x' % o if o <= 0xffff else u'\\U%08x' % o)
        else:
            out.append(ch)
    out.append(u'"')
    return u''.join(out)


def _to_bytes(value):
    """Return the UTF-8 bytes of value, the validation works byte by byte."""
    if isinstance(value, six.text_type):
        return bytearray(value.encode('utf-8', 'surrogatepass' if six.PY3 else 'strict'))
    return bytearray(value)


def _validate_endpoint_label(value):
    """Return '' if value is a valid endpoint label, otherwise the reason."""
    data = _to_bytes(value)
    if len(data) == 0:
        return ''
    # Check the character set first, it is the one that prevents SSRF.
    for i, c in enumerate(data):
        if c not in _LABEL_CHARS:
            return 'illegal character at index %d' % i
    if data[0] not in _LETTERS:
        return 'must start with a letter'
    if data[-1] in _TRAILING_FORBIDDEN:
        return "must not end with '-' or '_'"
    return ''


def _validate(value, name, code):
    if value is None:
        return
    if not isinstance(value, six.string_types):
        # A non string value can never be a host name label.
        raise EndpointValidationTypeError(
            code, 'invalid %s %r: must be a string, not %s, %s %s'
                  % (name, value, type(value).__name__, name, _ENDPOINT_LABEL_RULE))
    reason = _validate_endpoint_label(value)
    if reason:
        raise EndpointValidationError(
            code, u'invalid %s %s: %s, %s %s' % (name, _go_quote(value), reason, name, _ENDPOINT_LABEL_RULE))


def validate_region(region):
    """Check that region is safe to be used when building an endpoint host.

    An empty region ('' or None) is allowed and is left to the caller.

    :raises EndpointValidationError: with code ``InvalidRegion``.
    """
    _validate(region, 'region', ERR_CODE_INVALID_REGION)


def validate_service(service):
    """Check that service is safe to be used when building an endpoint host.

    An empty service ('' or None) is allowed and is left to the caller.

    :raises EndpointValidationError: with code ``InvalidService``.
    """
    _validate(service, 'service', ERR_CODE_INVALID_SERVICE)


def validate_service_and_region(service, region):
    """Validate service first, then region."""
    validate_service(service)
    validate_region(region)
