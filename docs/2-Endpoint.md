[← Credentials](1-Credentials.md) | Endpoint[(中文)](2-Endpoint-zh.md) | [Transport →](3-Transport.md)

---

# Endpoint Configuration

## Custom Endpoint

```python
import volcenginesdkcore
configuration = volcenginesdkcore.Configuration()
configuration.ak = "Your ak"
configuration.sk = "Your sk"
configuration.host = "<example>.<regionId>.volcengineapi.com"
volcenginesdkcore.Configuration.set_default(configuration)
```

## Custom RegionId

```python
import volcenginesdkcore
configuration = volcenginesdkcore.Configuration()
configuration.ak = "Your ak"
configuration.sk = "Your sk"
configuration.region = "cn-beijing"
volcenginesdkcore.Configuration.set_default(configuration)
```

## Automatic Endpoint Resolution

The SDK can automatically resolve endpoints based on region and service, and supports DualStack.

### Default Endpoint Resolution

Implementation reference: `./volcenginesdkcore/endpoint/providers/default_provider.py#bootstrap_region`.

```python
import volcenginesdkcore
configuration = volcenginesdkcore.Configuration()
configuration.ak = "Your ak"
configuration.sk = "Your sk"
configuration.use_dual_stack = True
configuration.custom_bootstrap_region = {
  "custom_example_region1": {},
  "custom_example_region2": {},
}
volcenginesdkcore.Configuration.set_default(configuration)
```

### Standard Endpoint Resolution

Implementation reference: `./volcenginesdkcore/endpoint/providers/standard_provider.py#ServiceInfos`.

```python
import volcenginesdkcore
from volcenginesdkcore.endpoint.providers.standard_provider import StandardEndpointResolver
configuration = volcenginesdkcore.Configuration()
configuration.ak = "Your ak"
configuration.sk = "Your sk"
configuration.endpoint_provider = StandardEndpointResolver()
configuration.use_dual_stack = True
configuration.region = "cn-beijing"
volcenginesdkcore.Configuration.set_default(configuration)
```

---

[← Credentials](1-Credentials.md) | Endpoint[(中文)](2-Endpoint-zh.md) | [Transport →](3-Transport.md)
