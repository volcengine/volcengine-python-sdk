[← 概览](0-Overview-zh.md) | 访问凭据[(English)](1-Credentials.md) | [Endpoint 配置 →](2-Endpoint-zh.md)

---

## 访问凭据

为保障资源访问安全，火山引擎 Python SDK 支持显式凭证和 `CredentialProvider` 自动解析两种方式。

### CredentialProvider 总览

| Provider | 用途 | 是否自动刷新 | 典型场景 |
| --- | --- | --- | --- |
| `StaticCredentialProvider` | 静态 AK/SK(/Token) | 否 | 服务端长期凭证 |
| `StsCredentialProvider` | STS AssumeRole | 是 | 角色扮演临时凭证 |
| `StsOidcCredentialProvider` | STS AssumeRoleWithOIDC | 是 | OIDC 联邦身份 |
| `StsSamlCredentialProvider` | STS AssumeRoleWithSAML | 是 | SAML 联邦身份 |
| `EnvironmentVariableCredentialProvider` | 读取环境变量 | 否 | CI/CD、容器注入 |
| `CLIConfigCredentialProvider` | 读取 `~/.volcengine/config.json` | 取决于 mode | 复用 CLI 配置 |
| `EcsRoleCredentialProvider` | 读取 ECS IMDS | 是 | ECS 实例角色 |
| `DefaultCredentialProvider` | 默认链包装 | 取决于代理 Provider | 业务代码不写 AK/SK |

### AK、SK设置

AK/SK 是由火山引擎用户在控制台创建的一对永久访问密钥。SDK 使用该密钥对每次请求进行签名，从而完成身份验证。

> ⚠️ **注意事项**
>
> 1. 不得在客户端嵌入或暴露 AK/SK。
> 2. 推荐使用配置中心或环境变量存储密钥。
> 3. 配置合理的最小权限访问策略。

**代码示例：**

支持`configuration`级别全局配置和接口级别的运行时参数设置`RuntimeOption`；`RuntimeOption`设置会覆盖`configuration`全局配置。

```python
import volcenginesdkcore,volcenginesdkecs
from volcenginesdkcore.rest import ApiException
from volcenginesdkcore.interceptor import RuntimeOption

# 全局设置
configuration = volcenginesdkcore.Configuration()
configuration.ak = "Your ak"
configuration.sk = "Your sk"
configuration.debug = True
volcenginesdkcore.Configuration.set_default(configuration)

# 接口级别运行时参数设置,会覆盖全局配置
runtime_options = RuntimeOption(
    ak="Your ak",
    sk="Your sk",
    client_side_validation=True, # 开启客户端校验,默认开启
)
api_instance = volcenginesdkecs.ECSApi()
create_command_request = volcenginesdkecs.CreateCommandRequest(
    command_content="ls -l",
    description="Your command description",
    name="Your command name",
    type="command",
    _configuration=runtime_options,  # 配置运行时参数
)
try:
    api_instance.create_command(create_command_request)
except ApiException as e:
    pass
```

### STS Token设置

STS（Security Token Service）是火山引擎提供的临时访问凭证机制。开发者通过服务端调用 STS 接口获取临时凭证（临时 AK、SK 和 Token），有效期可配置，适用于安全要求较高的场景。

> ⚠️ **注意事项**
>
> 1. 最小权限：仅授予调用方访问所需资源的最小权限，避免使用 * 通配符授予全资源、全操作权限。
> 2. 设置合理的有效期: 请根据实际情况设置合理有效期，越短越安全，建议不要超过1小时。

支持`configuration`级别全局配置和接口级别的运行时参数设置`RuntimeOption`；`RuntimeOption`设置会覆盖`configuration`全局配置。

**代码示例：**

```python
import volcenginesdkcore,volcenginesdkecs
from volcenginesdkcore.rest import ApiException
from volcenginesdkcore.interceptor import RuntimeOption

# 全局设置
configuration = volcenginesdkcore.Configuration()
configuration.ak = "Your ak"
configuration.sk = "Your sk"
configuration.session_token = "Your session token"
configuration.debug = True
volcenginesdkcore.Configuration.set_default(configuration)

# 接口级别运行时参数设置,会覆盖全局配置
runtime_options = RuntimeOption(
    ak="Your ak",
    sk="Your sk",
    session_token="Your session token",
    client_side_validation=True, # 开启客户端校验,默认开启
)
api_instance = volcenginesdkecs.ECSApi()
create_command_request = volcenginesdkecs.CreateCommandRequest(
    command_content="ls -l",
    description="Your command description",
    name="Your command name",
    type="command",
    _configuration=runtime_options,  # 配置运行时参数
)
try:
    api_instance.create_command(create_command_request)
except ApiException as e:
    pass
```

### STS AssumeRole示例

STS AssumeRole（Security Token Service）是火山引擎提供的临时访问凭证机制。开发者通过服务端调用 STS 接口获取临时凭证（临时 AK、SK 和 Token），有效期可配置，适用于安全要求较高的场景。

此接口使用IAM子账号角色进行 AssumeRole 操作后，获取到IAM子用户的信息后，发起真正的 API 请求，参考如下：

参考文档：https://www.volcengine.com/docs/6257/86374

> ⚠️ **注意事项**
>
> 1. 最小权限：仅授予调用方访问所需资源的最小权限，避免使用 * 通配符授予全资源、全操作权限。
> 2. 设置合理的有效期: 请根据实际情况设置合理有效期，越短越安全，建议不要超过1小时。

支持`configuration`级别全局配置和接口级别的运行时参数设置`RuntimeOption`；`RuntimeOption`设置会覆盖`configuration`全局配置。

**代码示例：**

```python
from __future__ import print_function
import volcenginesdkcore
import volcenginesdkvpc
from volcenginesdkcore.rest import ApiException
from volcenginesdkcore.auth.providers.sts_provider import StsCredentialProvider

if __name__ == '__main__':
    # 注意示例代码安全，代码泄漏会导致AK/SK泄漏，有极大的安全风险。
    configuration = volcenginesdkcore.Configuration()
    configuration.region = "cn-beijing"

    # 这里是使用STS ASSUMEROLE角色的方式
    configuration.credential_provider = StsCredentialProvider(
        ak="Your ak",  # 必填，子账号的ak
        sk="Your sk",  # 必填，子账号的sk
        role_name="Your role name",  # 必填，子账号的角色TRN，如trn:iam::2110400000:role/role123  ,此处填写role123
        account_id="Your account id",  # 必填，子账号的角色TRN，如trn:iam::2110400000:role/role123  ,此处填写2110400000
        duration_seconds=3600,  # 非必填，有效期默认3600秒
        scheme="https",  # 非必填，域名前缀，默认https
        host="sts.volcengineapi.com",  # 非必填，请求域名，默认sts.volcengineapi.com
        region="cn-beijing",  # 非必填，请求服务器区域地址，默认cn-beijing
        timeout=30,  # 非必填，请求超时时间，默认30秒
        expired_buffer_seconds=60, #非必填，session有效期前多久过期，剩余时间小于这个设置就要请求新的token了，默认60秒
        policy='{"Statement":[{"Effect":"Allow","Action":["vpc:CreateVpc"],"Resource":["*"],"Condition":{"StringEquals":{"volc:RequestedRegion":["cn-beijing"]}}}]}' # 非必填，授权策略，默认为空
    )

    # set default configuration
    volcenginesdkcore.Configuration.set_default(configuration)
    # use global default configuration
    api_instance = volcenginesdkvpc.VPCApi()
    create_vpc_request = volcenginesdkvpc.CreateVpcRequest(
        cidr_block="192.168.0.0/16",
        dns_servers=["10.0.0.1", "10.1.1.2"],
    )

    try:
        # 复制代码运行示例，请自行打印API返回值。
        api_instance.create_vpc(create_vpc_request)
    except ApiException as e:
        # 复制代码运行示例，请自行打印API错误信息。
        # print("Exception when calling api: %s\n" % e)
        pass
```

### STS AssumeRoleWithOidc示例

STS AssumeRoleOIDC（Security Token Service）是火山引擎提供的临时访问凭证机制。开发者通过oidc_token在服务端调用 STS 接口获取临时凭证（临时 AK、SK 和 Token），有效期可配置，适用于安全要求较高的场景。

此接口使用oidc身份提供商角色使用oidc_token进行 AssumeRoleWithOidc 操作后，获取到用户的信息后，发起真正的 API 请求，参考如下：

参考文档：https://www.volcengine.com/docs/6257/1494877

> ⚠️ **注意事项**
>
> 1. 最小权限：仅授予调用方访问所需资源的最小权限，避免使用 * 通配符授予全资源、全操作权限。
> 2. 设置合理的有效期: 请根据实际情况设置合理有效期，越短越安全，建议不要超过1小时。

支持`configuration`级别全局配置和接口级别的运行时参数设置`RuntimeOption`；`RuntimeOption`设置会覆盖`configuration`全局配置。

当前 SDK 的 OIDC 只有一个实现：`StsOidcCredentialProvider`。

- 兼容老用法：`role_name + account_id + oidc_token`（全部可选；传了 oidc_token 时不读环境变量）
- 新用法：`role_trn + oidc_token_file`（全部可选；缺失项自动从环境变量补齐）
- 所有参数均为可选。全部不传时，Provider 完全从环境变量读取。

支持的 OIDC 环境变量：

- `VOLCENGINE_OIDC_ROLE_TRN`
- `VOLCENGINE_OIDC_TOKEN_FILE`
- `VOLCENGINE_OIDC_ROLE_SESSION_NAME`
- `VOLCENGINE_OIDC_ROLE_POLICY`
- `VOLCENGINE_OIDC_STS_ENDPOINT`

**代码示例：**

```python
# Example Code generated by Beijing Volcanoengine Technology.
from __future__ import print_function
import volcenginesdkcore
import volcenginesdkvpc
from volcenginesdkcore.rest import ApiException
from volcenginesdkcore.auth.providers.sts_oidc_provider import StsOidcCredentialProvider

if __name__ == '__main__':
    # 注意示例代码安全，代码泄漏会导致AK/SK泄漏，有极大的安全风险。
    configuration = volcenginesdkcore.Configuration()
    configuration.region = "cn-beijing"

    # 这里是使用STS ASSUMEROLE_OIDC角色的方式
    configuration.credential_provider = StsOidcCredentialProvider(
        role_name="Your role name",  # 必填，账号的角色TRN，如trn:iam::2110400000:role/role123  ,此处填写role123
        account_id="Your account id",  # 必填，账号的角色TRN，如trn:iam::2110400000:role/role123  ,此处填写2110400000
        # 也可以直接传完整 role_trn（优先级高于 role_name + account_id）：
        # role_trn="trn:iam::2110400000:role/role123",
        oidc_token="your oidc token",  # 必填，生成的oidcToken，如ey********
        duration_seconds=3600,  # 非必填，有效期默认3600秒
        scheme="https",  # 非必填，域名前缀，默认https
        host="sts.volcengineapi.com",  # 非必填，请求域名，默认sts.volcengineapi.com
        region="cn-beijing",  # 非必填，请求服务器区域地址，默认cn-beijing
        timeout=30,  # 非必填，请求超时时间，默认30秒
        expired_buffer_seconds=60,  # 非必填，session有效期前多久过期，剩余时间小于这个设置就要请求新的token了，默认60秒
        policy='{"Statement":[{"Effect":"Allow","Action":["vpc:CreateVpc"],"Resource":["*"],"Condition":{"StringEquals":{"volc:RequestedRegion":["cn-beijing"]}}}]}', # 非必填，授权策略，默认为空
        max_retries=3,     # 非必填，HTTP 重试次数（最小 1），默认 3
        retry_interval=1,  # 非必填，重试间隔秒数，默认 1
    )

    # set default configuration
    volcenginesdkcore.Configuration.set_default(configuration)
    # use global default configuration
    api_instance = volcenginesdkvpc.VPCApi()
    create_vpc_request = volcenginesdkvpc.CreateVpcRequest(
        cidr_block="192.168.0.0/16",
        dns_servers=["10.0.0.1", "10.1.1.2"],
    )

    try:
        # 复制代码运行示例，请自行打印API返回值。
        api_instance.create_vpc(create_vpc_request)
    except ApiException as e:
        # 复制代码运行示例，请自行打印API错误信息。
        # print("Exception when calling api: %s\n" % e)
        pass

```

**环境变量回退用法示例：**

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

### STS AssumeRoleWithSaml示例

STS AssumeRoleWithSaml（Security Token Service）是火山引擎提供的临时访问凭证机制。开发者通过saml_token在服务端调用 STS 接口获取临时凭证（临时 AK、SK 和 Token），有效期可配置，适用于安全要求较高的场景。

此接口使用saml身份提供商角色使用saml_resp进行 AssumeRoleWithSaml 操作后，获取到用户的信息后，发起真正的 API 请求，参考如下：

参考文档：https://www.volcengine.com/docs/6257/1631607

> ⚠️ **注意事项**
>
> 1. 最小权限：仅授予调用方访问所需资源的最小权限，避免使用 * 通配符授予全资源、全操作权限。
> 2. 设置合理的有效期: 请根据实际情况设置合理有效期，越短越安全，建议不要超过1小时。

支持`configuration`级别全局配置和接口级别的运行时参数设置`RuntimeOption`；`RuntimeOption`设置会覆盖`configuration`全局配置。

角色 TRN 的解析优先级（与 OIDC 一致）：

- `role_trn`（显式）优先。
- 否则使用 `role_name + account_id` 拼成 `trn:iam::{account_id}:role/{role_name}`。

SAML Provider TRN 的解析优先级：

- `saml_provider_trn`（显式）优先。
- 否则使用 `account_id + provider_name` 拼成 `trn:iam::{account_id}:saml-provider/{provider_name}`。
- 如果只传 `role_trn + provider_name`，会从 `role_trn` 解析出 `account_id`，再和 `provider_name` 拼接。

**代码示例：**

```python
# Example Code generated by Beijing Volcanoengine Technology.
from __future__ import print_function
import volcenginesdkcore
import volcenginesdkvpc
from volcenginesdkcore.rest import ApiException
from volcenginesdkcore.auth.providers.sts_saml_provider import StsSamlCredentialProvider

if __name__ == '__main__':
    # 注意示例代码安全，代码泄漏会导致AK/SK泄漏，有极大的安全风险。
    configuration = volcenginesdkcore.Configuration()
    configuration.region = "cn-beijing"

    # 这里是使用STS ASSUMEROLE_SAML角色的方式
    configuration.credential_provider = StsSamlCredentialProvider(
        role_name="Your role name",  # 必填，账号的角色TRN，如trn:iam::2110400000:role/role123,此处填写role123
        account_id="Your account id",  # 必填，账号的角色TRN，如trn:iam::2110400000:saml-provider/role123,此处填写2110400000
        # 也可以直接传完整 role_trn（优先级高于 role_name + account_id）：
        # role_trn="trn:iam::2110400000:role/role123",
        provider_name="your provider name",# 必填，认证provider的TRN，如trn:iam::2110400000:saml-provider/provider123,此处填写provider123
        # 也可以直接传完整 saml_provider_trn（优先级高于 account_id + provider_name）：
        # saml_provider_trn="trn:iam::2110400000:saml-provider/provider123",
        saml_resp="your saml resp",  # 必填，认证获取到的SAML的断言
        duration_seconds=3600,  # 非必填，有效期默认3600秒
        scheme="https",  # 非必填，域名前缀，默认https
        host="sts.volcengineapi.com",  # 非必填，请求域名，默认sts.volcengineapi.com
        region="cn-beijing",  # 非必填，请求服务器区域地址，默认cn-beijing
        timeout=30,  # 非必填，请求超时时间，默认30秒
        expired_buffer_seconds=60,  # 非必填，session有效期前多久过期，剩余时间小于这个设置就要请求新的token了，默认60秒
        policy='{"Statement":[{"Effect":"Allow","Action":["vpc:CreateVpc"],"Resource":["*"],"Condition":{"StringEquals":{"volc:RequestedRegion":["cn-beijing"]}}}]}', # 非必填，授权策略，默认为空
        max_retries=3,     # 非必填，HTTP 重试次数（最小 1），默认 3
        retry_interval=1,  # 非必填，重试间隔秒数，默认 1
    )

    # set default configuration
    volcenginesdkcore.Configuration.set_default(configuration)
    # use global default configuration
    api_instance = volcenginesdkvpc.VPCApi()
    create_vpc_request = volcenginesdkvpc.CreateVpcRequest(
        cidr_block="192.168.0.0/16",
        dns_servers=["10.0.0.1", "10.1.1.2"],
    )

    try:
        # 复制代码运行示例，请自行打印API返回值。
        api_instance.create_vpc(create_vpc_request)
    except ApiException as e:
        # 复制代码运行示例，请自行打印API错误信息。
        # print("Exception when calling api: %s\n" % e)
        pass

```

### 环境变量凭证 Provider

`EnvironmentVariableCredentialProvider` 读取以下环境变量：

- `VOLCENGINE_ACCESS_KEY`
- `VOLCENGINE_SECRET_KEY`
- `VOLCENGINE_SESSION_TOKEN`（可选）

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

### CLI 配置凭证 Provider

`CLIConfigCredentialProvider` 默认读取 `~/.volcengine/config.json`。

- 配置文件优先级：构造参数 `config_path` > `VOLCENGINE_CLI_CONFIG_FILE` > `~/.volcengine/config.json`
- Profile 优先级：构造参数 `profile_name` > `VOLCENGINE_PROFILE` > 配置里的 `current` > `default`

支持的 mode（不区分大小写）：

- `AK` / 空值
- `StsToken`
- `RamRoleArn`（委托给 `StsCredentialProvider`）
- `OIDC`（委托给 `StsOidcCredentialProvider`）
- `EcsRole`（委托给 `EcsRoleCredentialProvider`）
- `SSO` 从 CLI sso 缓存读取 STS 凭证（SDK 自动在内存中刷新 access token，永不写入缓存文件） 
- `console-login` 从 CLI console-login 缓存读取 STS 凭证（SDK 通过 OAuth `refresh_token` 在内存中自动刷新，永不写入缓存文件）  

**主动指定 CLI Provider 示例：**

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

#### 运行时刷新行为（sso / console-login）

`sso` 与 `console-login` 模式下，SDK 自管理刷新，且**永不写入任何本地文件**：

- **只读磁盘**：`config.json`、`~/.volcengine/sso/cache/*.json` 与
  `~/.volcengine/login/cache/*.json` 仅在 bootstrap 时读取一次；console-login
  在服务端返回 `invalid_grant` 时会再读一次磁盘 fallback。SDK 永不写入。
- **内存刷新**：缓存的 `access_token` 进入到期窗口（60 秒）后，SDK 用内存中
  的 `refresh_token` 调 OAuth `/token` 端点续期，仅更新内存状态。SSO 模式还
  会接着调 Portal `GetRoleCredentials` 拿 STS 三元组。
- **invalid_grant fallback**（仅 console-login）：当服务端返回 HTTP 400
  `invalid_grant` 时，SDK 重新读取一次磁盘 cache。若磁盘上的 `refresh_token`
  与内存不同（说明 `ve login` 在期间更新过），则用磁盘 RT 再尝试一次刷新；
  否则报错并提示用户重跑 `ve login`。
- **refresh_token 过期**：当内存与磁盘上的 refresh_token 都被服务端拒绝时，
  SDK 抛出明确错误，提示用户重跑 `ve login`（console-login）或 `ve sso login`
  （SSO）。
- **并发**：每进程加锁，保证多个调用方共享单次 in-flight refresh。

完整契约见 [`cli-console-login-credential-plan.md`](./cli-console-login-credential-plan.md)。

### ECS Role 凭证 Provider

> 🚨 **当前版本限制**
>
> **当前版本暂不支持从 IMDS 自动探测角色名**，必须通过构造参数或 `VOLCENGINE_ECS_METADATA` 环境变量显式传入角色名。后续版本将支持自动探测，敬请关注版本发布通知。

`EcsRoleCredentialProvider` 从 ECS IMDS 获取临时凭证：

- `role_name` 优先级：构造参数 > `VOLCENGINE_ECS_METADATA` > 从 IMDS 自动探测
- 禁用开关：`VOLCENGINE_ECS_METADATA_DISABLED=true`

```python
import volcenginesdkcore
from volcenginesdkcore.auth.providers.ecs_role_provider import EcsRoleCredentialProvider

configuration = volcenginesdkcore.Configuration()
configuration.region = "cn-beijing"
configuration.credential_provider = EcsRoleCredentialProvider(role_name="your-ecs-role-name")
volcenginesdkcore.Configuration.set_default(configuration)
```

### 默认凭证 Provider

当 `ak`、`sk` 和 `credential_provider` 均未设置时，SDK 自动使用 `DefaultCredentialProvider`，无需手动配置。

如需自定义参数（如 `role_name`），也可显式指定。

默认链顺序：

1. `EnvironmentVariableCredentialProvider`
2. `StsOidcCredentialProvider`
3. `CLIConfigCredentialProvider`
4. `EcsRoleCredentialProvider`

默认 `reuse_last_provider_enabled=True`，后续请求会优先复用最近一次成功的 Provider。

```python
import volcenginesdkcore
from volcenginesdkcore.auth.providers.default_provider import DefaultCredentialProvider

configuration = volcenginesdkcore.Configuration()
configuration.region = "cn-beijing"
configuration.credential_provider = DefaultCredentialProvider()
volcenginesdkcore.Configuration.set_default(configuration)
```

---

[← 概览](0-Overview-zh.md) | 访问凭据[(English)](1-Credentials.md) | [Endpoint 配置 →](2-Endpoint-zh.md)
