[← Credentials](1-Credentials.md) | Endpoint[(中文)](2-Endpoint-zh.md) | [Transport →](3-Transport.md)

---

## Endpoint Configuration

> **Default**
>
> If `Endpoint` is not specified, the SDK uses [Automatic Endpoint Resolution](#automatic-endpoint-resolution).

### Custom Endpoint

You can specify a custom endpoint when initializing the client:

```python
import volcenginesdkcore
configuration = volcenginesdkcore.Configuration()
configuration.ak = "Your ak"
configuration.sk = "Your sk"
configuration.host = "<example>.<regionId>.volcengineapi.com" # Custom Endpoint
volcenginesdkcore.Configuration.set_default(configuration)
```

### Custom RegionId

**Code Example:**

Supports both `configuration`-level global settings and API-level runtime parameter settings via `RuntimeOption`. `RuntimeOption` settings override the `configuration` global settings.

```python
import volcenginesdkcore, volcenginesdkecs
from volcenginesdkcore.rest import ApiException
from volcenginesdkcore.interceptor import RuntimeOption
configuration = volcenginesdkcore.Configuration()
configuration.ak = "Your ak"
configuration.sk = "Your sk"
configuration.region = "cn-beijing" # Custom RegionId
volcenginesdkcore.Configuration.set_default(configuration)

# API-level runtime parameter settings, overrides global configuration
runtime_options = RuntimeOption(
    region="cn-beijing",
    client_side_validation=True, # Enable client-side validation, enabled by default
)
api_instance = volcenginesdkecs.ECSApi()
create_command_request = volcenginesdkecs.CreateCommandRequest(
    command_content="ls -l",
    description="Your command description",
    name="Your command name",
    type="command",
    _configuration=runtime_options,  # Set runtime parameters
)
try:
    api_instance.create_command(create_command_request)
except ApiException as e:
    pass
```

### Automatic Endpoint Resolution

> **Default**
>
> Automatic resolution is enabled by default; no manual endpoint specification is needed.

To simplify user configuration, Volcengine provides a flexible automatic Endpoint resolution mechanism. Users do not need to manually specify service addresses; the SDK automatically constructs a reasonable access address based on the service name, region, and other information, and supports user-defined DualStack (dual-stack) settings.

#### Default Endpoint Resolution

##### Resolution Logic

1. **Whether to auto-resolve the Region**

    Built-in auto-resolution region list reference: [`./volcenginesdkcore/endpoint/providers/default_provider.py#bootstrap_region`](./volcenginesdkcore/endpoint/providers/default_provider.py#L458).

    The SDK only performs automatic resolution for certain preset regions (e.g., `cn-beijing-autodriving`, `ap-southeast-2`) or user-configured regions; other regions default to the endpoint: `open.volcengineapi.com`.

    Users can extend the region list via the environment variable `VOLC_BOOTSTRAP_REGION_LIST_CONF` or by specifying `custom_bootstrap_region` in code.

2. **DualStack Support (IPv6)**

    The SDK supports dual-stack network (IPv4 + IPv6) access addresses. Automatic enabling conditions: explicitly pass the `use_dual_stack` parameter, or set the environment variable `VOLC_ENABLE_DUALSTACK`. Priority: `use_dual_stack` > `VOLC_ENABLE_DUALSTACK`.

    When enabled, the domain suffix switches from `volcengineapi.com` to `volcengine-api.com`.

3. **Endpoint construction based on service name and region**

    - **Global services (e.g., `CDN`, `IAM`)**: Use `<ServiceName>.volcengineapi.com` (or `volcengine-api.com` when dual-stack is enabled). Example: `cdn.volcengineapi.com`.
    - **Regional services (e.g., `ECS`, `RDS`)**: Use `<ServiceName>.<Region>.volcengineapi.com` as the default endpoint. Example: `ecs.cn-beijing.volcengineapi.com`.

##### Code Example

```python
import volcenginesdkcore
configuration = volcenginesdkcore.Configuration()
configuration.ak = "Your ak"
configuration.sk = "Your sk"
configuration.use_dual_stack = True # Enable dual-stack network (IPv4 + IPv6) access, default is False
configuration.custom_bootstrap_region = {
    "custom_example_region1": {},
    "custom_example_region2": {},
} # Custom auto-resolution region list
volcenginesdkcore.Configuration.set_default(configuration)
```

##### Region and service validation

The region and service are concatenated into the endpoint host name (e.g., `{service}.{region}.volcengineapi.com`) and are part of the signature. To prevent values such as `cn-beijing@127.0.0.1` or `evil.com#` from changing the host the request is actually sent to (SSRF), the SDK checks, before resolving the endpoint, signing or sending the request, that the region and service are each a valid single host name label:

- only ASCII letters, digits, `-` and `_`;
- starts with a letter;
- does not end with `-` or `_`.

The rule is equivalent to the regular expression `^[A-Za-z]([A-Za-z0-9_-]*[A-Za-z0-9])?$` matched against the **whole** string (`re.fullmatch`, or `\A...\Z`; note that `re.match` with `$` would wrongly accept a trailing newline such as `"cn-beijing\n"`, the SDK rejects it). An empty string `''` or `None` is not rejected here and is left to the caller's existing handling of missing values; a non-string value (e.g., `42`, `b'cn-beijing'`) is always invalid. The service is validated before the region.

**Where it is checked:**

- Regular API calls: `ResolveEndpointInterceptor` validates the service and region before calling any endpoint provider (the region is the final value after any `RuntimeOption` override);
- Universal calls via `UniversalApi.do_call`: `UniversalInfo.service` is validated before the internal request path is built;
- Default resolution `DefaultEndpointProvider` (`endpoint_for`, `get_default_endpoint`), `ServiceEndpointInfo.get_endpoint_for` and standard resolution `StandardEndpointResolver.endpoint_for`: also validate when called directly;
- RDS auth token `build_auth_token`: validates the region before building the presigned token when `configuration.host` is not set;
- SSO credentials from the CLI config file (`SsoCredentialProvider`): validates the SSO region before building the OAuth refresh and Portal URLs and sending the request.

**When it is skipped:** regular API calls and universal calls skip the check when:

- `configuration.host` is set. For regular API calls, a request-level `RuntimeOption.endpoint_provider` clears the host, so the check still runs in that case. Universal calls do not support `RuntimeOption` (the request body of `UniversalApi.do_call` must be a plain `dict`), so only the configuration decides whether the check is skipped;
- the endpoint provider's type is **exactly** `HostEndpointProvider`. The code checks `type(provider) is not HostEndpointProvider`, so **subclasses of `HostEndpointProvider` are not skipped** and are still validated.

**Error type:**

A failed check raises `volcenginesdkcore.endpoint.validation.EndpointValidationError`, a subclass of `ValueError`:

- `e.code`: the error code, `InvalidRegion` (constant `ERR_CODE_INVALID_REGION`) or `InvalidService` (constant `ERR_CODE_INVALID_SERVICE`);
- `e.message`: the error description;
- `str(e)` is formatted as `Code: Message`, e.g., `InvalidRegion: invalid region "cn-beijing ": illegal character at index 10, region must start with a letter, end with a letter or digit, and contain only letters, digits, '-' and '_'`.

A non-string value raises the subclass `EndpointValidationTypeError` (also a `TypeError`) with the same `code` values.

On API calls the exception is raised as is before any request is sent; it is **not** wrapped in `ApiException`. When SSO credentials are obtained through the default credential chain `DefaultCredentialProvider`, the chain catches the exception and tries the next provider; if all providers fail, it raises `RuntimeError` (whose message includes this error).

```python
from volcenginesdkcore.endpoint.validation import EndpointValidationError
from volcenginesdkcore.rest import ApiException

try:
    api_instance.create_command(create_command_request)
except EndpointValidationError as e:
    # e.code is "InvalidRegion" or "InvalidService"
    print(e.code, e.message)
except ApiException as e:
    pass
```

**Behavior change:**

- A region with leading or trailing whitespace (e.g., `"cn-beijing "`, `"cn-beijing\n"`) is no longer accepted and raises `InvalidRegion`. The SDK did not reject such values before, but the signature used the raw value, so the request was already rejected: a value with a trailing space is rejected by the server with `InvalidAuthorization`, while a value containing a newline (such as `"cn-beijing\n"`) is never sent, because the HTTP client rejects the resulting invalid header value locally (`Invalid header value`) before sending the request (over HTTPS, a connection to the endpoint may already have been opened). Call `strip()` yourself before setting `configuration.region` or `RuntimeOption.region`. Regions read from the CLI config file (`region` of a RamRoleArn / OIDC profile, `region` of an `sso-session`) are already `strip()`ped before use and are not affected.
- Subclasses of `HostEndpointProvider` are validated too (see above).
- `StandardEndpointResolver` raises `EndpointValidationError` instead of `StandProviderError` for an invalid label (e.g., `"cn beijing"`); a valid label that is not a supported region still raises `StandProviderError` (`InvalidRegion`).
- New public validation functions `validate_region`, `validate_service` and `validate_service_and_region`, importable from `volcenginesdkcore.endpoint.validation`. They return nothing on success, raise `EndpointValidationError` on failure, and accept empty values (`''`, `None`).

#### Standard Endpoint Resolution

##### Resolution Rules

| Global Service | DualStack | Format |
|---|---|---|
| Yes | Yes | `{Service}.volcengine-api.com` |
| Yes | No | `{Service}.volcengineapi.com` |
| No | Yes | `{Service}.{region}.volcengine-api.com` |
| No | No | `{Service}.{region}.volcengineapi.com` |

Whether a service is global is determined by the service itself and cannot be modified. Reference list: [`./volcenginesdkcore/endpoint/providers/standard_provider.py#ServiceInfos`](./volcenginesdkcore/endpoint/providers/standard_provider.py#L51).

##### Code Example

```python
import volcenginesdkcore
from volcenginesdkcore.endpoint.providers.standard_provider import StandardEndpointResolver
configuration = volcenginesdkcore.Configuration()
configuration.ak = "Your ak"
configuration.sk = "Your sk"
configuration.endpoint_provider = StandardEndpointResolver() # Configure standard resolution
configuration.use_dual_stack = True # Configure dual-stack
configuration.region = "cn-beijing" # Configure region
volcenginesdkcore.Configuration.set_default(configuration)
```

---

[← Credentials](1-Credentials.md) | Endpoint[(中文)](2-Endpoint-zh.md) | [Transport →](3-Transport.md)
