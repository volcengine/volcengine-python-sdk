[← Credentials](1-Credentials.md) | Endpoint[(中文)](2-Endpoint-zh.md) | [Transport →](3-Transport.md)

---

# Endpoint Configuration

## Custom Endpoint

> **Default**
> * When no endpoint is specified, the SDK uses [Automatic Endpoint Resolution](#automatic-endpoint-resolution).

You can specify a custom endpoint when initializing the client:

```python
import volcenginesdkcore
configuration = volcenginesdkcore.Configuration()
configuration.ak = "Your ak"
configuration.sk = "Your sk"
configuration.host = "<example>.<regionId>.volcengineapi.com" # Custom Endpoint
volcenginesdkcore.Configuration.set_default(configuration)
```

## Custom RegionId

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

## Automatic Endpoint Resolution

> **Default**
> * Automatic resolution is enabled by default; no manual endpoint specification is needed.

To simplify user configuration, Volcengine provides a flexible automatic Endpoint resolution mechanism. Users do not need to manually specify service addresses; the SDK automatically constructs a reasonable access address based on the service name, region, and other information, and supports user-defined DualStack (dual-stack) settings.

### Default Endpoint Resolution

**Default Endpoint Resolution Logic**

1. **Whether to auto-resolve the Region**
Built-in auto-resolution region list reference: [`./volcenginesdkcore/endpoint/providers/default_provider.py#bootstrap_region`](./volcenginesdkcore/endpoint/providers/default_provider.py#L458).
The SDK only performs automatic resolution for certain preset regions (e.g., `cn-beijing-autodriving`, `ap-southeast-2`) or user-configured regions; other regions default to the endpoint: `open.volcengineapi.com`.
Users can extend the region list via the environment variable `VOLC_BOOTSTRAP_REGION_LIST_CONF` or by specifying `custom_bootstrap_region` in code.

2. **DualStack Support (IPv6)**
The SDK supports dual-stack network (IPv4 + IPv6) access addresses. Automatic enabling conditions:
Explicitly pass the `use_dual_stack` parameter, or set the environment variable `VOLC_ENABLE_DUALSTACK`. Priority: `use_dual_stack` > `VOLC_ENABLE_DUALSTACK`.
When enabled, the domain suffix switches from `volcengineapi.com` to `volcengine-api.com`.

3. **Endpoint construction based on service name and region**, with the following rules:
**Global services (e.g., CDN, IAM)**
Use `<ServiceName>.volcengineapi.com` (or `volcengine-api.com` when dual-stack is enabled).
Example: `cdn.volcengineapi.com`
**Regional services (e.g., ECS, RDS)**
Use `<ServiceName>.<Region>.volcengineapi.com` as the default endpoint.
Example: `ecs.cn-beijing.volcengineapi.com`

**Code Example:**

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

### Standard Endpoint Resolution

**Standard Resolution Rules**

| Global Service | DualStack | Format |
|---|---|---|
| Yes | Yes | `{Service}.volcengine-api.com` |
| Yes | No | `{Service}.volcengineapi.com` |
| No | Yes | `{Service}.{region}.volcengine-api.com` |
| No | No | `{Service}.{region}.volcengineapi.com` |

**Code Example:**

Whether a service is global depends on the specific service being called and cannot be modified.
Reference list: [`./volcenginesdkcore/endpoint/providers/standard_provider.py#ServiceInfos`](./volcenginesdkcore/endpoint/providers/standard_provider.py#L51).

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
