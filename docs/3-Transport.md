[← Endpoint](2-Endpoint.md) | Transport[(中文)](3-Transport-zh.md) | [Timeout →](4-Timeout.md)

---

# HTTP Connection Pool

> **Default**
> - `num_pools`: 4
> - `connection_pool_maxsize`: `multiprocessing.cpu_count() * 5`

```python
import volcenginesdkcore
configuration = volcenginesdkcore.Configuration()
configuration.ak = "Your ak"
configuration.sk = "Your sk"
configuration.num_pools = 10
configuration.connection_pool_maxsize = 10
volcenginesdkcore.Configuration.set_default(configuration)
```

# HTTPS Request Configuration

## Specify Scheme

> **Default**: `scheme=https`

```python
import volcenginesdkcore
from volcenginesdkcore.interceptor import RuntimeOption

configuration = volcenginesdkcore.Configuration()
configuration.ak = "Your ak"
configuration.sk = "Your sk"
configuration.scheme = "http"
volcenginesdkcore.Configuration.set_default(configuration)

runtime_options = RuntimeOption(
  scheme="http",
  client_side_validation=True,
)
```

# HTTP(S) Proxy

## Configure HTTP(S) Proxy

```python
import volcenginesdkcore
configuration = volcenginesdkcore.Configuration()
configuration.ak = "Your AK"
configuration.sk = "Your SK"
configuration.http_proxy = "http://your_proxy:8080"
configuration.https_proxy = "http://your_proxy:8080"
volcenginesdkcore.Configuration.set_default(configuration)
```

## Notes

Supported environment variables:

- `http_proxy`/`HTTP_PROXY`, `https_proxy`/`HTTPS_PROXY`, `no_proxy`/`NO_PROXY`

Priority: code > environment variables.

## Ignore SSL Verification

```python
import volcenginesdkcore
configuration = volcenginesdkcore.Configuration()
configuration.ak = "Your ak"
configuration.sk = "Your sk"
configuration.verify_ssl = False
volcenginesdkcore.Configuration.set_default(configuration)
```

---

[← Endpoint](2-Endpoint.md) | Transport[(中文)](3-Transport-zh.md) | [Timeout →](4-Timeout.md)
