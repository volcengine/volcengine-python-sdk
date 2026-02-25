English | [中文](SDK_Integration_zh.md)

# Table of Contents

- [SDK Integration](#sdk-integration)
- [Requirements](#requirements)
- [Credentials](#credentials)
  - [AK/SK](#aksk)
  - [STS Token](#sts-token)
  - [STS AssumeRole](#sts-assumerole)
  - [STS AssumeRoleWithOidc](#sts-assumerolewithoidc)
  - [STS AssumeRoleWithSaml](#sts-assumerolewithsaml)
- [Endpoint Configuration](#endpoint-configuration)
  - [Custom Endpoint](#custom-endpoint)
  - [Custom RegionId](#custom-regionid)
  - [Automatic Endpoint Resolution](#automatic-endpoint-resolution)
    - [Default Endpoint Resolution](#default-endpoint-resolution)
    - [Standard Endpoint Resolution](#standard-endpoint-resolution)
- [HTTP Connection Pool](#http-connection-pool)
- [HTTPS Request Configuration](#https-request-configuration)
  - [Specify Scheme](#specify-scheme)
- [HTTP(S) Proxy](#https-proxy)
  - [Configure HTTP(S) Proxy](#configure-https-proxy)
  - [Notes](#notes)
  - [Ignore SSL Verification](#ignore-ssl-verification)
- [Timeouts](#timeouts)
- [Retries](#retries)
  - [Retry Code Configuration](#retry-code-configuration)
  - [Retry Conditions](#retry-conditions)
    - [Default Retry Conditions](#default-retry-conditions)
    - [Custom Retry Conditions](#custom-retry-conditions)
  - [Backoff Strategy](#backoff-strategy)
    - [Built-in Backoff Strategies](#built-in-backoff-strategies)
    - [Custom Backoff Strategies](#custom-backoff-strategies)
- [Error Handling](#error-handling)
- [Debugging](#debugging)
  - [Enable Debug Mode](#enable-debug-mode)
  - [Set Debug Level](#set-debug-level)
- [Log Output](#log-output)

# SDK Integration

When calling APIs, it is recommended to integrate the SDK in your project. Using the SDK simplifies development, speeds up integration, and reduces long-term maintenance costs.

# Requirements

1. Python version **>= 2.7**.
2. If using Ark runtime (`volcenginesdkarkruntime`), Python version **>= 3.6** is required.

# Credentials

For secure access, the Volcengine Python SDK supports authentication with `AK/SK` and `STS Token`.

## AK/SK

AK/SK is a pair of permanent access keys created in the Volcengine console. The SDK signs each request to authenticate.

> ⚠️ Notes
>
> 1. Do not embed or expose AK/SK in client-side applications.
> 2. Use a configuration center or environment variables.
> 3. Follow least privilege principles.

The SDK supports both global `configuration` and per-request runtime options (`RuntimeOption`). Runtime options override global configuration.

```python
import volcenginesdkcore, volcenginesdkecs
from volcenginesdkcore.rest import ApiException
from volcenginesdkcore.interceptor import RuntimeOption

# Global configuration
configuration = volcenginesdkcore.Configuration()
configuration.ak = "Your ak"
configuration.sk = "Your sk"
configuration.debug = True
volcenginesdkcore.Configuration.set_default(configuration)

# Per-request runtime options (override global configuration)
runtime_options = RuntimeOption(
  ak="Your ak",
  sk="Your sk",
  client_side_validation=True,
)

api_instance = volcenginesdkecs.ECSApi()
create_command_request = volcenginesdkecs.CreateCommandRequest(
    command_content="ls -l",
    description="Your command description",
    name="Your command name",
    type="command",
    _configuration=runtime_options,
)

try:
    api_instance.create_command(create_command_request)
except ApiException:
    pass
```

## STS Token

STS (Security Token Service) provides temporary credentials (temporary AK/SK and Token).

> ⚠️ Notes
>
> 1. Least privilege.
> 2. Use a reasonable TTL. Shorter is safer; avoid exceeding 1 hour.

```python
import volcenginesdkcore, volcenginesdkecs
from volcenginesdkcore.rest import ApiException
from volcenginesdkcore.interceptor import RuntimeOption

# Global configuration
configuration = volcenginesdkcore.Configuration()
configuration.ak = "Your ak"
configuration.sk = "Your sk"
configuration.session_token = "Your session token"
configuration.debug = True
volcenginesdkcore.Configuration.set_default(configuration)

# Per-request runtime options
runtime_options = RuntimeOption(
  ak="Your ak",
  sk="Your sk",
  session_token="Your session token",
  client_side_validation=True,
)

api_instance = volcenginesdkecs.ECSApi()
create_command_request = volcenginesdkecs.CreateCommandRequest(
    command_content="ls -l",
    description="Your command description",
    name="Your command name",
    type="command",
    _configuration=runtime_options,
)

try:
    api_instance.create_command(create_command_request)
except ApiException:
    pass
```

## STS AssumeRole

STS AssumeRole obtains temporary credentials by assuming an IAM role. Use the role credentials to perform actual API calls.

Reference: https://www.volcengine.com/docs/6257/86374

```python
from __future__ import print_function
import volcenginesdkcore
import volcenginesdkvpc
from volcenginesdkcore.rest import ApiException
from volcenginesdkcore.auth.providers.sts_provider import StsCredentialProvider

if __name__ == '__main__':
    # Do NOT leak credentials in example code.
    configuration = volcenginesdkcore.Configuration()
    configuration.region = "cn-beijing"

    configuration.credential_provider = StsCredentialProvider(
        ak="Your ak",
        sk="Your sk",
        role_name="Your role name",
        account_id="Your account id",
        duration_seconds=3600,
        scheme="https",
        host="sts.volcengineapi.com",
        region="cn-beijing",
        timeout=30,
        expired_buffer_seconds=60,
        policy='{"Statement":[{"Effect":"Allow","Action":["vpc:CreateVpc"],"Resource":["*"],"Condition":{"StringEquals":{"volc:RequestedRegion":["cn-beijing"]}}}]}'
    )

    volcenginesdkcore.Configuration.set_default(configuration)
    api_instance = volcenginesdkvpc.VPCApi()
    create_vpc_request = volcenginesdkvpc.CreateVpcRequest(
        cidr_block="192.168.0.0/16",
        dns_servers=["10.0.0.1", "10.1.1.2"],
    )

    try:
        api_instance.create_vpc(create_vpc_request)
    except ApiException:
        pass
```

## STS AssumeRoleWithOidc

STS AssumeRoleWithOidc obtains temporary credentials via an OIDC token.

Reference: https://www.volcengine.com/docs/6257/1494877

```python
from __future__ import print_function
import volcenginesdkcore
import volcenginesdkvpc
from volcenginesdkcore.rest import ApiException
from volcenginesdkcore.auth.providers.sts_oidc_provider import StsOidcCredentialProvider

if __name__ == '__main__':
    configuration = volcenginesdkcore.Configuration()
    configuration.region = "cn-beijing"

    configuration.credential_provider = StsOidcCredentialProvider(
        role_name="Your role name",
        account_id="Your account id",
        oidc_token="your oidc token",
        duration_seconds=3600,
        scheme="https",
        host="sts.volcengineapi.com",
        region="cn-beijing",
        timeout=30,
        expired_buffer_seconds=60,
        policy='{"Statement":[{"Effect":"Allow","Action":["vpc:CreateVpc"],"Resource":["*"],"Condition":{"StringEquals":{"volc:RequestedRegion":["cn-beijing"]}}}]}'
    )

    volcenginesdkcore.Configuration.set_default(configuration)
    api_instance = volcenginesdkvpc.VPCApi()
    create_vpc_request = volcenginesdkvpc.CreateVpcRequest(
        cidr_block="192.168.0.0/16",
        dns_servers=["10.0.0.1", "10.1.1.2"],
    )

    try:
        api_instance.create_vpc(create_vpc_request)
    except ApiException:
        pass
```

## STS AssumeRoleWithSaml

STS AssumeRoleWithSaml obtains temporary credentials via a SAML assertion.

Reference: https://www.volcengine.com/docs/6257/1631607

```python
from __future__ import print_function
import volcenginesdkcore
import volcenginesdkvpc
from volcenginesdkcore.rest import ApiException
from volcenginesdkcore.auth.providers.sts_saml_provider import StsSamlCredentialProvider

if __name__ == '__main__':
    configuration = volcenginesdkcore.Configuration()
    configuration.region = "cn-beijing"

    configuration.credential_provider = StsSamlCredentialProvider(
        role_name="Your role name",
        account_id="Your account id",
        provider_name="your provider name",
        saml_resp="your saml resp",
        duration_seconds=3600,
        scheme="https",
        host="sts.volcengineapi.com",
        region="cn-beijing",
        timeout=30,
        expired_buffer_seconds=60,
        policy='{"Statement":[{"Effect":"Allow","Action":["vpc:CreateVpc"],"Resource":["*"],"Condition":{"StringEquals":{"volc:RequestedRegion":["cn-beijing"]}}}]}'
    )

    volcenginesdkcore.Configuration.set_default(configuration)
    api_instance = volcenginesdkvpc.VPCApi()
    create_vpc_request = volcenginesdkvpc.CreateVpcRequest(
        cidr_block="192.168.0.0/16",
        dns_servers=["10.0.0.1", "10.1.1.2"],
    )

    try:
        api_instance.create_vpc(create_vpc_request)
    except ApiException:
        pass
```

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

# Timeouts

> **Default**
> - `connect_timeout`: 30s
> - `read_timeout`: 30s

```python
import volcenginesdkcore
from volcenginesdkcore.interceptor import RuntimeOption

configuration = volcenginesdkcore.Configuration()
configuration.ak = "Your ak"
configuration.sk = "Your sk"
configuration.connect_timeout = 10
configuration.read_timeout = 10
volcenginesdkcore.Configuration.set_default(configuration)

runtime_options = RuntimeOption(
  connect_timeout=10,
  read_timeout=20,
  client_side_validation=True,
)
```

# Retries

The SDK retries on network errors and throttling. Business logic errors are not retried.

## Retry Code Configuration

```python
import volcenginesdkcore
from volcenginesdkcore.retryer.backoff_strategy import ExponentialWithRandomJitterBackoffStrategy
from volcenginesdkcore.retryer.retry_condition import DefaultRetryCondition

configuration = volcenginesdkcore.Configuration()
configuration.ak = "Your ak"
configuration.sk = "Your sk"
configuration.auto_retry = True
configuration.num_max_retries = 4
configuration.min_retry_delay_ms = 200
configuration.max_retry_delay_ms = 6000
configuration.backoff_strategy = ExponentialWithRandomJitterBackoffStrategy()
configuration.retry_condition = DefaultRetryCondition()
configuration.retry_error_codes = {"AccessDenied"}
volcenginesdkcore.Configuration.set_default(configuration)
```

## Retry Conditions

### Default Retry Conditions

The default retry condition includes:

1. Retry on network errors.
2. Retry on server throttling errors.
3. Retry on user-specified error codes (`retry_error_codes`).

### Custom Retry Conditions

1. Implement your own retry condition:

```python
from volcenginesdkcore.retryer.retry_condition import RetryCondition

class CustomRetryCondition(RetryCondition):
  def should_retry(self, response, err):
      retry_error_codes = self.retry_error_codes
      return False
```

2. Reuse the default condition logic:

```python
from volcenginesdkcore.retryer.retry_condition import DefaultRetryCondition

class CustomRetryCondition(DefaultRetryCondition):
  def should_retry(self, response, err):
      should_retry = super(CustomRetryCondition, self).should_retry(response, err)
      return False
```

## Backoff Strategy

### Built-in Backoff Strategies

| Name | Description | Formula |
|---|---|---|
| `NoBackoffStrategy` | No backoff, retry immediately | `delay=0.0` |
| `ExponentialBackoffStrategy` | Exponential backoff with bounds | `delay=min(min_retry_delay*2^n, max_retry_delay)` |
| `ExponentialWithRandomJitterBackoffStrategy` | Exponential with jitter | `base=min(min_retry_delay*2^n, max_retry_delay)`; `delay=base+U(0,base)` |

### Custom Backoff Strategies

1. Implement your own strategy:

```python
from volcenginesdkcore.retryer.backoff_strategy import BackoffStrategy

class CustomBackoffStrategy(BackoffStrategy):
    def compute_delay(self, retry_count):
        min_retry_delay = self.min_retry_delay
        max_retry_delay = self.max_retry_delay
        return 0.0
```

2. Reuse built-in strategy:

```python
from volcenginesdkcore.retryer.backoff_strategy import ExponentialBackoffStrategy

class CustomBackoffStrategy(ExponentialBackoffStrategy):
    def compute_delay(self, retry_count):
        delay = super(CustomBackoffStrategy, self).compute_delay(retry_count)
        return 0.0
```

# Error Handling

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
    print("Network/timeout error:{}".format(e))
except ValueError as e:
    print("Client-side error:{}".format(e))
except ApiException as e:
    if e.status == 0:
        print("Client-side SSL error:{}".format(e.reason))
    else:
        print("Server-side error:")
        if e.body is not None:
            response_meta_data = json.loads(e.body).get("ResponseMetadata")
            print("RequestId:{}".format(response_meta_data.get("RequestId")))
            print("Error Code: {}".format(response_meta_data.get("Error").get("Code")))
            print("Error Message: {}".format(response_meta_data.get("Error").get("Message")))
except Exception as e:
    print("Other error:%s" % e)
```

# Debugging

## Enable Debug Mode

```python
import volcenginesdkcore
configuration = volcenginesdkcore.Configuration()
configuration.ak = "Your AK"
configuration.sk = "Your SK"
configuration.debug = True
volcenginesdkcore.Configuration.set_default(configuration)
```

## Set Debug Level

```python
import volcenginesdkcore
from volcenginesdkcore.observability.debugger import LogLevel

configuration = volcenginesdkcore.Configuration()
configuration.ak = "Your AK"
configuration.sk = "Your SK"
configuration.debug = True
configuration.log_level = LogLevel.LOG_DEBUG_WITH_CONFIG.mask | LogLevel.LOG_DEBUG_WITH_REQUEST.mask | LogLevel.LOG_DEBUG_WITH_RESPONSE.mask
volcenginesdkcore.Configuration.set_default(configuration)
```

# Log Output

```python
import volcenginesdkcore
configuration = volcenginesdkcore.Configuration()
configuration.ak = "Your AK"
configuration.sk = "Your SK"
configuration.logger_file = "app.log"
configuration.logger_format = "%(asctime)s %(levelname)s %(message)s"
volcenginesdkcore.Configuration.set_default(configuration)
```
