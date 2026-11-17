[← Retry](6-Retry.md) | Error Handling[(中文)](7-ErrorHandling-zh.md) | [Debugging →](8-Debugging.md)

---

## Error Handling

When calling APIs, different types of errors may be returned. You can adopt targeted handling strategies based on the specific error type and error code. For example, you can retry on network errors, and adjust parameters or fix business logic for business errors, thereby improving system robustness and user experience.

### Error Classification

| Error Type | Description | Returned Error Type | Notes |
|---|---|---|---|
| `1. Network/Timeout Error` | DNS / connection failure or interrupted response reading | Existing network exceptions without a response; `volcenginesdkcore.rest.ApiException` for failures while reading an available response | The original read error is in `e.cause`; the default retry condition still recognizes retryable network causes |
| `2. Client Error` | Parameter/authentication errors before reaching the server | `volcenginesdkcore.rest.ApiException` `ValueError` | Client-side parameter validation |
| `3. Response Processing Error` | HTTP / business error, invalid response structure or model conversion failure | `volcenginesdkcore.rest.ApiException` | Preserves the actual HTTP status, including 200; this does not necessarily indicate a server business error |
| `4. Other Errors` | Any other errors not covered above | `Exception` | Catch-all error handling |

### Code Example

```python
import json
import socket
import urllib3
import volcenginesdkcore, volcenginesdkecs
from volcenginesdkcore.rest import ApiException

configuration = volcenginesdkcore.Configuration()
configuration.ak = "Your ak"
configuration.sk = "Your sk"
volcenginesdkcore.Configuration.set_default(configuration)

api_instance = volcenginesdkecs.ECSApi()
create_command_request = volcenginesdkecs.CreateCommandRequest(
    command_content="ls -l",
    description="Your command description",
    name="Your command name",
    type="command",
)

network_error_exceptions = (
    urllib3.exceptions.NewConnectionError,
    urllib3.exceptions.ConnectTimeoutError,
    urllib3.exceptions.ReadTimeoutError,
    urllib3.exceptions.ProtocolError,
    socket.timeout,
    socket.gaierror,
)

try:
    api_instance.create_command(create_command_request)
except network_error_exceptions as e:
    print("1. Network/timeout error:{}".format(e))
except ValueError as e:
    print("2. Client error (parameter validation error):{}".format(e))
except ApiException as e:
    if e.status == 0:
        print("2. Client error (SSL authentication error):{}".format(e.reason))
    else:
        print("3. Response processing error:")
        print("HTTP Status:{}".format(e.status))
        # response_metadata works for both standard and non-standard responses;
        # RequestId is resolved from the response body or the gateway headers.
        if e.response_metadata is not None:
            print("RequestId:{}".format(e.response_metadata.request_id))
        # A standard TOP error response carries Error Code/Message in the body;
        # a non-standard response (e.g. a 504 returning HTML, or non-TOP JSON)
        # may not be JSON, so fall back to printing the raw body.
        if e.body is not None:
            error = None
            try:
                payload = json.loads(e.body)
            except (ValueError, TypeError, UnicodeError):
                payload = None
            if isinstance(payload, dict):
                metadata = payload.get("ResponseMetadata")
                if isinstance(metadata, dict) and isinstance(metadata.get("Error"), dict):
                    error = metadata["Error"]
            if isinstance(error, dict):
                print("Error Code: {}".format(error.get("Code")))
                print("Error Message: {}".format(error.get("Message")))
            else:
                print("Response Body: {}".format(e.body))
        if e.cause is not None:
            print("Original Cause: {!r}".format(e.cause))
        if e.previous_exception is not None:
            print("Previous Exception: {}".format(e.previous_exception))
except Exception as e:
    print("4. Other error:%s" % e)
```

### Diagnostics for Non-standard Error Responses

When the server or gateway returns a **non-standard response** (e.g. a 504 gateway returning HTML/plain text, or JSON without a TOP `ResponseMetadata`), the SDK wraps it into a `volcenginesdkcore.rest.ApiException` that preserves full diagnostic information for troubleshooting:

| Field | Meaning |
|---|---|
| `e.status` | The real HTTP status code (e.g. 504), no longer forced to 200 |
| `e.body` | The raw response body (including non-JSON content) |
| `e.headers` | The response headers |
| `e.response_metadata` | A `ResponseMetadata` object; `e.response_metadata.request_id` is the request ID |
| `e.cause` | The original JSON, conversion, decoding, reading, file or retry processing exception; `None` when no underlying exception exists |
| `e.previous_exception` | The previous error when retry processing fails; may also retain an existing `ApiException` enriched during conversion |
| `str(e)` | A summary containing the status code, `RequestId`, response headers and body |

Every `ApiException` constructor path resolves RequestId in this order: nonempty body `ResponseMetadata.RequestId` → explicitly supplied metadata ID → `X-Top-Requestid` → `X-Top-Request-Id` → `X-Tt-Logid`. Header names are case insensitive; list / tuple header values use the first item. Supplied metadata objects are not modified in place. If neither body nor headers provide an ID, it remains empty.

### Response Conversion, Reading and Retry Diagnostics

Volcengine and BytePlus Python SDKs use the same rules:

- Automatic retry checks JSON object types at every level and only matches string business codes. `null`, arrays and invalid field types do not interrupt retry checks; invalid responses continue to response deserialization.
- Invalid `ResponseMetadata`, Result / model conversion, metadata assignment, date parsing and file processing failures return `ApiException` with the complete TOP body, actual status, headers, RequestId and original cause. Existing legal conversion fallbacks and valid null / missing Result behavior remain unchanged.
- On Python 3, ordinary responses still use UTF-8; `Content-Type` charset does not change it. On Python 2, the REST layer keeps raw `str` bytes, and invalid JSON is wrapped in `ApiException` during deserialization. Python 3 decoding failures keep raw bytes in `e.body`; reading failures with an available response keep retained byte fragments and close the failed connection. Incremental decompression works with urllib3 1.26 and 2.x: temporarily empty decoded output does not end reading. Truncated compressed responses retain only decoded fragments, without appending raw compressed bytes. An incomplete `Content-Length` causes a read error; bytes never received cannot be recovered. Python 2.7 uses urllib3 1.26.x; urllib3 2.x does not support Python 2.7.
- Successful preloaded `call_api(response_type="file")` responses retain binary bytes throughout reading and saving to a unique temporary file. Only an extension of 1–16 ASCII letters or digits from the safe `Content-Disposition` basename is retained; otherwise the default temporary name is used. This avoids long filename limits, path traversal and name collisions; incomplete files are removed on failure. Non-2xx responses still follow error handling.
- Ordinary exceptions from retry conditions, backoff calculation or waiting stop retries and return `ApiException`. Available prior response diagnostics are retained; the current cause is in `e.cause`, and the prior error in `e.previous_exception`. Abandoned streaming responses are closed and their connection pool slots released without reading the body; cleanup errors do not replace the callback cause. Each attempt uses its own response, preventing an earlier response from replacing a later network error.

On Python 3, `e.__cause__` and `e.cause` reference the same original exception. Print the complete traceback with `traceback.print_exception(type(e), e, e.__traceback__)`. `str(e)` does not expand cause tracebacks or synthesize business error codes.

Connection / DNS failures without a response retain their existing exception types and retry rules. SSL failures retain `ApiException(status=0)` and now retain the cause. Parameter, credential, signing and customer interceptor errors keep their own contracts. Process control exceptions such as `KeyboardInterrupt` and `SystemExit` propagate unchanged. Successful calls without a response type or with `_preload_content=False` skip ordinary deserialization; `call_api` retains its existing result contract and does not promise to directly return the underlying `HTTPResponse`. Catch asynchronous errors around the task's `.get()`.

### Complete Error Details

```python
import sys
from volcenginesdkcore import print_error, get_error_details

try:
    result = api_instance.create_command(create_command_request)
except Exception as e:
    print_error(sys.stderr, e)
    details = get_error_details(e)  # Detached copy for redaction or your logger.
```

`PrintError` / `GetErrorDetails` are aliases. Printing `None` writes nothing. Printing accepts ordinary exceptions too; write failures propagate and short writes raise `IOError`. Indented JSON ends with a newline and contains `type`, original `error` text, diagnostic `code` / `message`, `response` and optional `causes`.

`ApiException.code` / `.message` are separate from the existing `reason` and `str(e)` format. `.response_details` returns a detached `ResponseDetails`: `status_code`, `status`, `proto`, `request_id`, multivalue `headers` / `trailers`, original byte `body`, `body_captured` / `body_complete`. HTTP 200 errors keep status 200. Protocol/trailers unavailable from urllib3 remain null. Captured empty bodies are distinct from unread streams. JSON uses UTF-8 text or reversible Base64 with `body_encoding`.

Standard TOP errors keep the nonempty service code; simple `errorcode` / `message` responses keep their code. Missing error codes or a JSON null body use `UnknownError`. Invalid JSON, HTML, empty bodies, arrays, incompatible metadata field types and result/model/file conversion failures use `SerializationError`. Interrupted reads use `ReadError`; retry condition/backoff/wait failures use `RetryError`. Existing exception text and reasons remain unchanged; newly rejected field types have new diagnostics.

Snapshots reuse bytes read during the relevant attempt, preserve partial reads (`body_complete=false`), and retain the original TOP body after conversion failures. Printing never rereads closed bodies or sends requests. Nonempty string body `RequestId` is extracted independently of other malformed fields, before explicit metadata and the existing header fallbacks. Snapshots from different requests and attempts are independent.

The error tree follows `cause`, `previous_exception`, Python `__cause__` / unsuppressed `__context__`, urllib3 wrappers and Python 3.11 exception groups. Identity deduplication, 256 nodes and 64 levels bound traversal. Customer exceptions are not automatically wrapped or modified. An optional `response_details` property or no-argument method may provide a snapshot; null falls back to the actual status/RequestId available. Ordinary exceptions expose only their existing information. Complete bodies may contain credentials; redact a detached details copy before logging.

### STS, AssumeRole, OIDC and SAML

All three credential paths preserve snapshots for HTTP/business/read/parse errors. Status comes from the actual response, never body `HTTPCode`. Missing/empty AK, SK, SessionToken or expiration returns `UnknownError`; invalid expiration returns `SerializationError` with its cause. Both cache fields are published only after complete validation; failure preserves the previous cache.

STS network errors without a response from the SDK HTTP transport become `ApiException(status=0, code="RequestError")` with a cause and null response. Normalization occurs only at the actual transport call. Local parameter/token-file errors, customer credential/signing callbacks and customer request/transport overrides retain their contracts and exception identity. Ordinary service connection/DNS errors retain their original types; SSL failures retain `ApiException(status=0)`. Former STS missing-credential `RuntimeError`, native expiration failures and final network failures can now be caught uniformly as `ApiException`; those newly normalized paths change their display text, while existing error displays remain unchanged.

STS retries HTTP 429/502/503/504, throttling/transient codes and recognized underlying network failures. HTTP 500 without a retryable code does not retry. Each no-response node in a cause tree is checked only for network causes, preventing the `RequestError` whitelist from overriding TLS/proxy rejection. Legacy customer exceptions may omit optional diagnostic fields. Python Provider `max_retries` still means total attempts, at least one, unlike ordinary configuration retries after the first attempt. VE OIDC/SAML use `Expiration`; BP retains its existing `ExpiredTime` fallback when the field is absent. Proxy/TLS rules, client cache isolation and rebind remain unchanged.

ECS/IMDS, CLI OAuth/Portal, customer interceptors and other unintegrated native read/parse failures expose only their existing information, without a full-snapshot guarantee.

---

[← Retry](6-Retry.md) | Error Handling[(中文)](7-ErrorHandling-zh.md) | [Debugging →](8-Debugging.md)
