[← Endpoint](2-Endpoint.md) | Transport[(中文)](3-Transport-zh.md) | [Proxy →](4-Proxy.md)

---

## HTTP Connection Pool

> **Default**
>
> - `num_pools`: 4 — Maximum number of distinct host pools the underlying `PoolManager` keeps; increase this when your client talks to many different hosts.
> - `connection_pool_maxsize`: `multiprocessing.cpu_count() * 5` — Maximum connections kept per host; increase this when issuing many concurrent requests to the same host.

**Code Example:**

```python
import volcenginesdkcore
configuration = volcenginesdkcore.Configuration()
configuration.ak = "Your ak"
configuration.sk = "Your sk"
configuration.num_pools = 10 # Number of distinct host pools (PoolManager)
configuration.connection_pool_maxsize = 10 # Max connections per host
volcenginesdkcore.Configuration.set_default(configuration)
```

## HTTPS Request Configuration

### Specify Scheme

> **Default**
>
> - `scheme`: `https`

**Code Example:**

Supports both `configuration`-level global settings and API-level runtime parameter settings via `RuntimeOption`. `RuntimeOption` settings override the `configuration` global settings.

```python
import volcenginesdkcore, volcenginesdkecs
from volcenginesdkcore.rest import ApiException
from volcenginesdkcore.interceptor import RuntimeOption

# Global configuration
configuration = volcenginesdkcore.Configuration()
configuration.ak = "Your ak"
configuration.sk = "Your sk"
configuration.scheme = "http" # Specify scheme
volcenginesdkcore.Configuration.set_default(configuration)

# API-level runtime parameter settings, overrides global configuration
runtime_options = RuntimeOption(
    scheme="http",
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

### Ignore SSL Verification

> **Default**
>
> - `verify_ssl`: `True`

**Code Example:**

```python
import volcenginesdkcore
configuration = volcenginesdkcore.Configuration()
configuration.ak = "Your ak"
configuration.sk = "Your sk"
configuration.verify_ssl = False # Ignore SSL verification
volcenginesdkcore.Configuration.set_default(configuration)
```

---

[← Endpoint](2-Endpoint.md) | Transport[(中文)](3-Transport-zh.md) | [Proxy →](4-Proxy.md)
