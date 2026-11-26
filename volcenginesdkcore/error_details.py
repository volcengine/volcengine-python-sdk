# coding: utf-8
"""Read-only error diagnostics. Collect response bytes while they are available."""
from __future__ import absolute_import

import base64
import copy
import json

import six

from volcenginesdkcore.metadata import resolve_request_id_from_headers

_UNSET = object()


def _headers(headers):
    if headers is None:
        return None
    result = {}
    for key in headers:
        values = headers.getlist(key) if hasattr(headers, "getlist") else headers[key]
        result[key] = list(values) if isinstance(values, (list, tuple)) else [values]
    return copy.deepcopy(result)


class ResponseDetails(object):
    """A detached HTTP response snapshot; ``body`` contains the original bytes."""

    def __init__(self, status_code=0, status=None, proto=None, request_id=None,
                 headers=None, trailers=None, body=None, body_captured=False,
                 body_complete=False):
        self.status_code = status_code
        self.status = status
        self.proto = proto
        self.request_id = request_id or ""
        self.headers = _headers(headers)
        self.trailers = _headers(trailers)
        if isinstance(body, six.text_type):
            body = body.encode("utf-8")
        elif isinstance(body, bytearray):
            body = bytes(body)
        self.body = body
        self.body_captured = bool(body_captured) and body is not None
        self.body_complete = self.body_captured and bool(body_complete)

    def to_dict(self):
        result = copy.deepcopy(self.__dict__)
        body = result["body"]
        if self.body_captured and body is not None:
            try:
                result["body"] = body.decode("utf-8")
                result["body_encoding"] = "utf-8"
            except UnicodeDecodeError:
                result["body"] = base64.b64encode(body).decode("ascii")
                result["body_encoding"] = "base64"
        return result


def snapshot_response(response, body=_UNSET, body_complete=True):
    """Copy cached information without reading an HTTP stream."""
    details = getattr(response, "_response_details", None)
    if details is not None:
        return copy.deepcopy(details)
    raw = getattr(response, "urllib3_response", response)
    headers = response.getheaders() if hasattr(response, "getheaders") else getattr(raw, "headers", None)
    if body is _UNSET:
        body = vars(response).get("data", getattr(raw, "_body", None))
    status = getattr(response, "status", 0)
    reason = getattr(response, "reason", None)
    version = getattr(raw, "version", None)
    proto = {10: "HTTP/1.0", 11: "HTTP/1.1", 20: "HTTP/2"}.get(version)
    return ResponseDetails(
        status_code=status, status="{} {}".format(status, reason or "").rstrip(),
        proto=proto, headers=headers, request_id=resolve_request_id_from_headers(headers),
        body=body, body_captured=body is not None,
        body_complete=body is not None and body_complete)


def classify_top(body):
    """Return diagnostic code/message; never change ApiException.reason."""
    try:
        data = json.loads(body)
        if data is None:
            return "UnknownError", "Response body is null"
        if not isinstance(data, dict):
            raise ValueError("Response body must be a JSON object")
        meta = data.get("ResponseMetadata")
        if meta is not None:
            if not isinstance(meta, dict):
                raise ValueError("ResponseMetadata must be a JSON object")
            for key in ("RequestId", "Service", "Action", "Version", "Region"):
                if meta.get(key) is not None and not isinstance(meta[key], six.string_types):
                    raise ValueError("ResponseMetadata.{} must be a string".format(key))
            error = meta.get("Error")
            if error is not None:
                if not isinstance(error, dict):
                    raise ValueError("ResponseMetadata.Error must be a JSON object")
                for key in ("Code", "Message"):
                    if error.get(key) is not None and not isinstance(error[key], six.string_types):
                        raise ValueError("ResponseMetadata.Error.{} must be a string".format(key))
                http_code = error.get("HTTPCode")
                if http_code is not None and (isinstance(http_code, bool) or not isinstance(http_code, six.integer_types)):
                    raise ValueError("ResponseMetadata.Error.HTTPCode must be an integer")
                return error.get("Code") or "UnknownError", error.get("Message") or ""
        elif data.get("errorcode"):
            if not isinstance(data["errorcode"], six.string_types) or (
                    data.get("message") is not None and not isinstance(data["message"], six.string_types)):
                raise ValueError("Simple error code/message must be strings")
            return data["errorcode"], data.get("message") or ""
        return "UnknownError", "Response does not contain an error code"
    except (ValueError, TypeError, UnicodeError, RuntimeError) as error:
        return "SerializationError", six.text_type(error)


def exception_causes(error, include_previous=True):
    """Inspect a bounded number of explicit and standard Python causes."""
    seen = set()
    for name in ("cause", "previous_exception", "__cause__", "original_error", "reason"):
        if name == "previous_exception" and not include_previous:
            continue
        cause = getattr(error, name, None)
        if isinstance(cause, BaseException) and id(cause) not in seen:
            seen.add(id(cause))
            yield cause
    if getattr(error, "__cause__", None) is None and not getattr(error, "__suppress_context__", False):
        cause = getattr(error, "__context__", None)
        if isinstance(cause, BaseException) and id(cause) not in seen:
            yield cause
    # Python 3.11 exception groups, without importing a Python 3-only class.
    grouped = getattr(error, "exceptions", ())
    if not isinstance(grouped, (list, tuple)):
        grouped = ()
    for cause in grouped[:256]:
        if isinstance(cause, BaseException) and id(cause) not in seen:
            seen.add(id(cause))
            yield cause


def get_error_details(error):
    """Return a detached dict, limited to 256 nodes and 64 levels."""
    seen = set()

    def build(current, depth):
        if current is None or id(current) in seen or len(seen) >= 256 or depth >= 64:
            return None
        seen.add(id(current))
        details = getattr(current, "response_details", None)
        if callable(details):
            details = details()
        if isinstance(details, ResponseDetails):
            details = details.to_dict()
        elif details is not None:
            details = copy.deepcopy(details)
        else:
            status = getattr(current, "status", None)
            metadata = getattr(current, "response_metadata", None)
            request_id = getattr(metadata, "request_id", None)
            if status or request_id:
                details = ResponseDetails(status_code=status or 0, request_id=request_id).to_dict()
        node = {
            "type": "{}.{}".format(type(current).__module__, type(current).__name__),
            "error": str(current),
            "code": getattr(current, "code", None),
            "message": getattr(current, "message", str(current)),
            "response": details,
        }
        causes = []
        for cause in exception_causes(current):
            if len(seen) >= 256:
                break
            child = build(cause, depth + 1)
            if child is not None:
                causes.append(child)
        if causes:
            node["causes"] = causes
        return node

    return build(error, 0)


def print_error(writer, error):
    """Write indented JSON plus a newline. Propagate encoding/write failures."""
    if error is None:
        return
    text = json.dumps(get_error_details(error), ensure_ascii=True, indent=2) + "\n"
    written = writer.write(text)
    if written is not None and written != len(text):
        raise IOError("Short write while printing error details")


# Go-style spellings are aliases of the idiomatic Python entry points.
PrintError = print_error
GetErrorDetails = get_error_details
