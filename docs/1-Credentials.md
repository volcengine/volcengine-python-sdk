[← Overview](0-Overview.md) | Credentials[(中文)](1-Credentials-zh.md) | [Endpoint →](2-Endpoint.md)

---

## Credentials

The Volcengine Python SDK supports explicit credentials and `CredentialProvider`-based automatic resolution.

### Credential Providers Overview

| Provider | Purpose | Refresh Support | Typical Scenario |
| --- | --- | --- | --- |
| `StaticCredentialProvider` | Static AK/SK(/Token) | No | Long-lived server-side credentials |
| `StsCredentialProvider` | STS AssumeRole | Yes | Role-based temporary credentials |
| `StsOidcCredentialProvider` | STS AssumeRoleWithOIDC | Yes | OIDC federation |
| `StsSamlCredentialProvider` | STS AssumeRoleWithSAML | Yes | SAML federation |
| `EnvironmentVariableCredentialProvider` | Read from env vars | No | CI/CD and container env injection |
| `CLIConfigCredentialProvider` | Read from `~/.volcengine/config.json` | Depends on mode | Reuse CLI login/profile |
| `EcsRoleCredentialProvider` | Read from ECS IMDS | Yes | ECS instance role credentials |
| `DefaultCredentialProvider` | Chain wrapper | Depends on delegated provider | No AK/SK in application code |

### AK/SK

AK/SK is a pair of permanent access keys created in the Volcengine console. The SDK signs each request to authenticate.

> ⚠️ **Notes**
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

### STS Token

STS (Security Token Service) provides temporary credentials (temporary AK/SK and Token).

> ⚠️ **Notes**
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

### STS AssumeRole

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

### STS AssumeRoleWithOidc

STS AssumeRoleWithOidc obtains temporary credentials via an OIDC token.

Reference: https://www.volcengine.com/docs/6257/1494877

The SDK has a single OIDC implementation: `StsOidcCredentialProvider`.

- Backward-compatible mode: `role_name + account_id + oidc_token` (all optional; missing values do NOT read env vars)
- Env-aware mode: `role_trn + oidc_token_file` (all optional; missing values fall back to env vars)
- All parameters are optional. When none are provided, the provider reads entirely from environment variables.

Supported OIDC env vars:

- `VOLCENGINE_OIDC_ROLE_TRN`
- `VOLCENGINE_OIDC_TOKEN_FILE`
- `VOLCENGINE_OIDC_ROLE_SESSION_NAME`
- `VOLCENGINE_OIDC_ROLE_POLICY`
- `VOLCENGINE_OIDC_STS_ENDPOINT`

Backward-compatible example:

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
        # Alternatively, pass the full role_trn directly (overrides role_name + account_id):
        # role_trn="trn:iam::2110400000:role/role123",
        oidc_token="your oidc token",
        duration_seconds=3600,
        scheme="https",
        host="sts.volcengineapi.com",
        region="cn-beijing",
        timeout=30,
        expired_buffer_seconds=60,
        policy='{"Statement":[{"Effect":"Allow","Action":["vpc:CreateVpc"],"Resource":["*"],"Condition":{"StringEquals":{"volc:RequestedRegion":["cn-beijing"]}}}]}',
        max_retries=3,     # optional, HTTP retry attempts (min 1), defaults to 3
        retry_interval=1,  # optional, seconds between retries, defaults to 1
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

Env-aware example:

```python
import os
import volcenginesdkcore
from volcenginesdkcore.auth.providers.sts_oidc_provider import StsOidcCredentialProvider

os.environ["VOLCENGINE_OIDC_ROLE_TRN"] = "trn:iam::1234567890:role/oidc-role"
os.environ["VOLCENGINE_OIDC_TOKEN_FILE"] = "/var/run/secrets/oidc/token"

configuration = volcenginesdkcore.Configuration()
configuration.region = "cn-beijing"
configuration.credential_provider = StsOidcCredentialProvider()
volcenginesdkcore.Configuration.set_default(configuration)
```

### STS AssumeRoleWithSaml

STS AssumeRoleWithSaml obtains temporary credentials via a SAML assertion.

Reference: https://www.volcengine.com/docs/6257/1631607

Role TRN resolution (same style as OIDC):

- `role_trn` (explicit) takes priority.
- Otherwise `role_name + account_id` is assembled into `trn:iam::{account_id}:role/{role_name}`.

SAML Provider TRN resolution:

- `saml_provider_trn` (explicit) takes priority.
- Otherwise `account_id + provider_name` is assembled into `trn:iam::{account_id}:saml-provider/{provider_name}`.
- When only `role_trn + provider_name` are passed, `account_id` is parsed out of `role_trn` and combined with `provider_name`.

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
        # Alternatively, pass the full role_trn directly (overrides role_name + account_id):
        # role_trn="trn:iam::2110400000:role/role123",
        provider_name="your provider name",
        # Alternatively, pass the full saml_provider_trn directly (overrides account_id + provider_name):
        # saml_provider_trn="trn:iam::2110400000:saml-provider/provider123",
        saml_resp="your saml resp",
        duration_seconds=3600,
        scheme="https",
        host="sts.volcengineapi.com",
        region="cn-beijing",
        timeout=30,
        expired_buffer_seconds=60,
        policy='{"Statement":[{"Effect":"Allow","Action":["vpc:CreateVpc"],"Resource":["*"],"Condition":{"StringEquals":{"volc:RequestedRegion":["cn-beijing"]}}}]}',
        max_retries=3,     # optional, HTTP retry attempts (min 1), defaults to 3
        retry_interval=1,  # optional, seconds between retries, defaults to 1
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

### Environment Variable Credential Provider

`EnvironmentVariableCredentialProvider` reads credentials from:

- `VOLCENGINE_ACCESS_KEY`
- `VOLCENGINE_SECRET_KEY`
- `VOLCENGINE_SESSION_TOKEN` (optional)

```python
import os
import volcenginesdkcore
from volcenginesdkcore.auth.providers.env_provider import EnvironmentVariableCredentialProvider

os.environ["VOLCENGINE_ACCESS_KEY"] = "YourAK"
os.environ["VOLCENGINE_SECRET_KEY"] = "YourSK"

configuration = volcenginesdkcore.Configuration()
configuration.region = "cn-beijing"
configuration.credential_provider = EnvironmentVariableCredentialProvider()
volcenginesdkcore.Configuration.set_default(configuration)
```

### CLI Config Credential Provider

`CLIConfigCredentialProvider` reads `~/.volcengine/config.json` by default.

- Config path priority: constructor `config_path` > `VOLCENGINE_CLI_CONFIG_FILE` > `~/.volcengine/config.json`
- Profile priority: constructor `profile_name` > `VOLCENGINE_PROFILE` > `current` in config > `default`

Supported modes in profile (case-insensitive):

- `AK` / empty
- `StsToken`
- `RamRoleArn` (delegates to `StsCredentialProvider`)
- `OIDC` (delegates to `StsOidcCredentialProvider`)
- `EcsRole` (delegates to `EcsRoleCredentialProvider`)
- `SSO` Reads STS credentials from the CLI sso cache (SDK refreshes access token in-memory, never writes the cache file) 
- `console-login` Reads STS credentials from the CLI console-login cache (SDK refreshes via OAuth `refresh_token` in-memory, never writes the cache file) 

Example: explicitly use CLI provider with a specified profile and config path.

```python
import os

import volcenginesdkcore
from volcenginesdkcore.auth.providers.cli_config_provider import CLIConfigCredentialProvider

configuration = volcenginesdkcore.Configuration()
configuration.region = "cn-beijing"
configuration.credential_provider = CLIConfigCredentialProvider(
    profile_name="prod",
    config_path=os.path.expanduser("~/.volcengine/config.json"),
)
volcenginesdkcore.Configuration.set_default(configuration)
```

#### Runtime Refresh Behavior (sso / console-login)

For `sso` and `console-login` modes the SDK now owns refresh in-memory and
never writes any local file. Key invariants:

- **Read-only on disk**: `config.json`, `~/.volcengine/sso/cache/*.json` and
  `~/.volcengine/login/cache/*.json` are read on bootstrap and (for
  console-login) once more if the signin service rejects the in-memory
  refresh token. They are never written by the SDK.
- **In-memory refresh**: when the cached `access_token` is past its expiry
  buffer (60 seconds), the SDK exchanges the cached `refresh_token` at the
  OAuth `/token` endpoint and updates its in-memory state. SSO then calls
  the Portal `GetRoleCredentials` API for the STS triple.
- **Invalid-grant fallback** (console-login only): on HTTP 400
  `invalid_grant`, the SDK re-reads the cache file once. If the disk
  `refresh_token` differs from the in-memory one (i.e. `ve login` rotated
  it under the SDK), the SDK retries with the disk RT; otherwise it
  reports an actionable error pointing at `ve login`.
- **Refresh-token expiry**: when the SDK exhausts both the in-memory and
  disk refresh tokens, it raises a clear error instructing the user to run
  `ve login` (console-login) or `ve sso login` (SSO).
- **Concurrency**: a per-process lock serializes refreshes so concurrent
  callers share a single in-flight refresh.

See [`cli-console-login-credential-plan.md`](./cli-console-login-credential-plan.md)
for the full contract.

### ECS Role Credential Provider

`EcsRoleCredentialProvider` reads temporary credentials from ECS IMDS.

- `role_name` priority: constructor arg > `VOLCENGINE_ECS_METADATA` > auto-detect from IMDS
- disable switch: `VOLCENGINE_ECS_METADATA_DISABLED=true`

```python
import volcenginesdkcore
from volcenginesdkcore.auth.providers.ecs_role_provider import EcsRoleCredentialProvider

configuration = volcenginesdkcore.Configuration()
configuration.region = "cn-beijing"
# Omit role_name to read VOLCENGINE_ECS_METADATA or auto-detect the role name from IMDS.
configuration.credential_provider = EcsRoleCredentialProvider(role_name="your-ecs-role-name")
volcenginesdkcore.Configuration.set_default(configuration)
```

### Default Credential Provider

When `ak`, `sk`, and `credential_provider` are all unset, the SDK automatically uses `DefaultCredentialProvider` — no manual configuration is needed.

You can also explicitly set it if you need to customize options (e.g., `role_name`).

Default chain order:

1. `EnvironmentVariableCredentialProvider`
2. `StsOidcCredentialProvider`
3. `CLIConfigCredentialProvider`
4. `EcsRoleCredentialProvider`

By default, `reuse_last_provider_enabled=True`, so the last successful provider is reused first on later calls.

```python
import volcenginesdkcore
from volcenginesdkcore.auth.providers.default_provider import DefaultCredentialProvider

configuration = volcenginesdkcore.Configuration()
configuration.region = "cn-beijing"
configuration.credential_provider = DefaultCredentialProvider()
volcenginesdkcore.Configuration.set_default(configuration)
```

---

[← Overview](0-Overview.md) | Credentials[(中文)](1-Credentials-zh.md) | [Endpoint →](2-Endpoint.md)
