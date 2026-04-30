[← Endpoint](2-Endpoint.md) | Transport[(中文)](3-Transport-zh.md) | [Timeout →](4-Timeout.md)

---

# HTTP Connection Pool

> **Default**
> - `num_pools`: 4 — Maximum number of hosts supported; increase this when making concurrent requests to the same host.
> - `connection_pool_maxsize`: `multiprocessing.cpu_count() * 5` — Maximum connections per host; increase this when connecting to many different hosts simultaneously.

**Code Example:**

```python
import volcenginesdkcore
configuration = volcenginesdkcore.Configuration()
configuration.ak = "Your ak"
configuration.sk = "Your sk"
configuration.num_pools = 10 # Maximum number of hosts
configuration.connection_pool_maxsize = 10 # Maximum connections per host
volcenginesdkcore.Configuration.set_default(configuration)
```

# HTTPS Request Configuration

## Specify Scheme

> **Default**: `scheme=https`

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

# HTTP(S) Proxy

> **Default**
> No proxy.

## Configure HTTP(S) Proxy

```python
import volcenginesdkcore, volcenginesdkecs
configuration = volcenginesdkcore.Configuration()
configuration.ak = "Your AK"
configuration.sk = "Your SK"

configuration.http_proxy = "http://your_proxy:8080"
configuration.https_proxy = "http://your_proxy:8080"

volcenginesdkcore.Configuration.set_default(configuration)

api_instance = volcenginesdkecs.ECSApi()
```

## Notes

Supported environment variables for proxy configuration:

- `http_proxy`/`HTTP_PROXY`, `https_proxy`/`HTTPS_PROXY`, `no_proxy`/`NO_PROXY`

Priority: code > environment variables.

## Ignore SSL Verification

> **Default**: `verify_ssl=True`

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

[← Endpoint](2-Endpoint.md) | Transport[(中文)](3-Transport-zh.md) | [Timeout →](4-Timeout.md)
