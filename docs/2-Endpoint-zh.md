[← 访问凭据](1-Credentials-zh.md) | Endpoint 配置[(English)](2-Endpoint.md) | [Transport →](3-Transport-zh.md)

---

## EndPoint 配置

> **默认**
>
> 不指定 Endpoint 时，走 [自动化 Endpoint 寻址](#自动化-endpoint-寻址)。

### 自定义 Endpoint

用户可以通过在初始化客户端时指定 Endpoint：

```python
import volcenginesdkcore
configuration = volcenginesdkcore.Configuration()
configuration.ak = "Your ak"
configuration.sk = "Your sk"
configuration.host = "<example>.<regionId>.volcengineapi.com" # 自定义Endpoint
volcenginesdkcore.Configuration.set_default(configuration)
```

### 自定义 RegionId

**代码示例：**

支持 `configuration` 级别全局配置和接口级别的运行时参数设置 `RuntimeOption`；`RuntimeOption` 设置会覆盖 `configuration` 全局配置。

```python
import volcenginesdkcore,volcenginesdkecs
from volcenginesdkcore.rest import ApiException
from volcenginesdkcore.interceptor import RuntimeOption
configuration = volcenginesdkcore.Configuration()
configuration.ak = "Your ak"
configuration.sk = "Your sk"
configuration.region = "cn-beijing" # 自定义RegionId
volcenginesdkcore.Configuration.set_default(configuration)

# 接口级别运行时参数设置,会覆盖全局配置
runtime_options = RuntimeOption(
    region="cn-beijing",
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

### 自动化 Endpoint 寻址

> **默认**
>
> 默认支持自动寻址，无需手动指定 Endpoint。

为了简化用户配置，Volcengine 提供了灵活的 Endpoint 自动寻址机制。用户无需手动指定服务地址，SDK 会根据服务名称、区域（Region）等信息自动拼接出合理的访问地址，并支持用户自定义 DualStack（双栈）。

#### Endpoint 默认寻址

##### 寻址逻辑

1. **是否自动寻址 Region**

    内置自动寻址 Region 列表代码：[`./volcenginesdkcore/endpoint/providers/default_provider.py#bootstrap_region`](./volcenginesdkcore/endpoint/providers/default_provider.py#L458)

    SDK 仅对部分预设区域（如 `cn-beijing-autodriving`、`ap-southeast-2`）或用户配置的区域执行自动寻址；其他区域默认返回 Endpoint：`open.volcengineapi.com`。

    用户可通过环境变量 `VOLC_BOOTSTRAP_REGION_LIST_CONF` 或代码中自定义 `custom_bootstrap_region` 来扩展控制区域列表。

2. **DualStack 支持（IPv6）**

    SDK 支持双栈网络（IPv4 + IPv6）访问地址，自动启用条件如下：显式传入参数 `use_dual_stack`，或设置环境变量 `VOLC_ENABLE_DUALSTACK`。优先级：`use_dual_stack` > `VOLC_ENABLE_DUALSTACK`。

    启用后，域名后缀将从 `volcengineapi.com` 切换为 `volcengine-api.com`。

3. **根据服务名和区域自动构造 Endpoint 地址**

    - **全局服务（如 `CDN`、`IAM`）**：使用 `<服务名>.volcengineapi.com`（或启用双栈时使用 `volcengine-api.com`）。示例：`cdn.volcengineapi.com`。
    - **区域服务（如 `ECS`、`RDS`）**：使用 `<服务名>.<区域名>.volcengineapi.com` 作为默认 Endpoint。示例：`ecs.cn-beijing.volcengineapi.com`。

##### 代码示例

```python
import volcenginesdkcore
configuration = volcenginesdkcore.Configuration()
configuration.ak = "Your ak"
configuration.sk = "Your sk"
configuration.use_dual_stack = True # // 定义是否启用双栈网络（IPv4 + IPv6）访问地址，默认false
configuration.custom_bootstrap_region = {
    "custom_example_region1": {},
    "custom_example_region2": {},
} # 自定义自动寻址Region列表
volcenginesdkcore.Configuration.set_default(configuration)
```

##### region / service 合法性校验

region 和 service 会被拼接进 Endpoint 域名（如 `{service}.{region}.volcengineapi.com`），同时参与签名。为防止 `cn-beijing@127.0.0.1`、`evil.com#` 这类值改变请求实际发往的主机（SSRF），SDK 会在寻址、签名和发送请求之前，校验 region 和 service 是否为合法的单个主机名标签：

- 只能包含 ASCII 字母、数字、`-` 和 `_`；
- 必须以字母开头；
- 不能以 `-` 或 `_` 结尾。

规则等价于对**整个字符串**做匹配的正则 `^[A-Za-z]([A-Za-z0-9_-]*[A-Za-z0-9])?$`（使用 `re.fullmatch` 或 `\A...\Z`；注意 `re.match` 加 `$` 会错误放行末尾换行，如 `"cn-beijing\n"`，而 SDK 会拒绝它）。空字符串 `''` 和 `None` 不会在这里报错，交由调用方原有的空值处理；非字符串值（如 `42`、`b'cn-beijing'`）一律视为非法。service 先于 region 校验。

**校验入口：**

- 普通 API 调用：`ResolveEndpointInterceptor` 在调用任何 endpoint provider 之前校验 service 和 region（region 为 `RuntimeOption` 覆盖后的最终值）；
- 通用调用 `UniversalApi.do_call`：在拼接内部请求路径之前校验 `UniversalInfo.service`；
- 默认寻址 `DefaultEndpointProvider`（`endpoint_for`、`get_default_endpoint`）、`ServiceEndpointInfo.get_endpoint_for` 和标准寻址 `StandardEndpointResolver.endpoint_for`：直接调用时同样校验；
- RDS 鉴权 Token `build_auth_token`：未设置 `configuration.host` 时，在生成预签名 Token 之前校验 region；
- CLI 配置文件中的 SSO 凭证（`SsoCredentialProvider`）：在构造 OAuth 刷新地址和 Portal 地址并发起请求之前校验 SSO region。

**跳过校验：** 普通 API 调用和通用调用在以下情况不校验：

- 设置了 `configuration.host`。对常规 API 调用，请求级 `RuntimeOption.endpoint_provider` 会清空 host，此时仍会校验；Universal 调用不支持 `RuntimeOption`（`UniversalApi.do_call` 的请求体必须是普通 `dict`），是否跳过校验只取决于配置；
- endpoint provider 的类型**恰好是** `HostEndpointProvider`。代码使用 `type(provider) is not HostEndpointProvider` 判断，因此 `HostEndpointProvider` 的**子类不会跳过**，仍会校验。

**错误类型：**

校验失败抛出 `volcenginesdkcore.endpoint.validation.EndpointValidationError`，它继承自 `ValueError`：

- `e.code`：错误码，`InvalidRegion`（常量 `ERR_CODE_INVALID_REGION`）或 `InvalidService`（常量 `ERR_CODE_INVALID_SERVICE`）；
- `e.message`：错误描述；
- `str(e)` 格式为 `Code: Message`，例如 `InvalidRegion: invalid region "cn-beijing ": illegal character at index 10, region must start with a letter, end with a letter or digit, and contain only letters, digits, '-' and '_'`。

非字符串值抛出其子类 `EndpointValidationTypeError`（同时继承 `TypeError`），`code` 含义相同。

API 调用时该异常在请求发出之前原样抛出，**不会**被包装成 `ApiException`。通过默认凭证链 `DefaultCredentialProvider` 获取 SSO 凭证时，该异常会被凭证链捕获并继续尝试后续 provider，全部失败时抛出 `RuntimeError`（消息中包含该错误）。

```python
from volcenginesdkcore.endpoint.validation import EndpointValidationError
from volcenginesdkcore.rest import ApiException

try:
    api_instance.create_command(create_command_request)
except EndpointValidationError as e:
    # e.code 为 "InvalidRegion" 或 "InvalidService"
    print(e.code, e.message)
except ApiException as e:
    pass
```

**与旧版本不同：**

- 带首尾空白的 region（如 `"cn-beijing "`、`"cn-beijing\n"`）不再被接受，直接抛出 `InvalidRegion`。此前 SDK 不拒绝这类值，但签名使用的是原值，请求本就无法成功：带尾部空格的值会被服务端以 `InvalidAuthorization` 拒绝，而包含换行的值（如 `"cn-beijing\n"`）根本发不出去，HTTP 客户端会在本地因请求头非法（`Invalid header value`）而报错。请在设置 `configuration.region` 或 `RuntimeOption.region` 之前自行 `strip()`。CLI 配置文件中的 region（RamRoleArn / OIDC profile 的 `region`、`sso-session` 的 `region`）在使用前已做 `strip()`，不受影响。
- `HostEndpointProvider` 的子类也会被校验（见上）。
- `StandardEndpointResolver` 收到非法标签（如 `"cn beijing"`）时，抛出 `EndpointValidationError`，不再是 `StandProviderError`；标签合法但不在支持范围内的 region 仍抛出 `StandProviderError`（`InvalidRegion`）。
- 新增公开校验函数 `validate_region`、`validate_service`、`validate_service_and_region`，导入路径为 `volcenginesdkcore.endpoint.validation`。校验通过时无返回值，失败时抛出 `EndpointValidationError`，空值（`''`、`None`）视为通过。

#### Endpoint 标准寻址

##### 标准寻址规则

| Global 服务 | 双栈 | 格式 |
|---|---|---|
| 是 | 是 | `{Service}.volcengine-api.com` |
| 是 | 否 | `{Service}.volcengineapi.com` |
| 否 | 是 | `{Service}.{region}.volcengine-api.com` |
| 否 | 否 | `{Service}.{region}.volcengineapi.com` |

服务是否为 Global 由具体服务决定，不可修改。可以参考列表：[`./volcenginesdkcore/endpoint/providers/standard_provider.py#ServiceInfos`](./volcenginesdkcore/endpoint/providers/standard_provider.py#L51)。

##### 代码示例

```python
import volcenginesdkcore
from volcenginesdkcore.endpoint.providers.standard_provider import StandardEndpointResolver
configuration = volcenginesdkcore.Configuration()
configuration.ak = "Your ak"
configuration.sk = "Your sk"
configuration.endpoint_provider = StandardEndpointResolver() # 配置标准寻址
configuration.use_dual_stack = True # 配置是否双栈
configuration.region = "cn-beijing" # 配置region
volcenginesdkcore.Configuration.set_default(configuration)
```

---

[← 访问凭据](1-Credentials-zh.md) | Endpoint 配置[(English)](2-Endpoint.md) | [Transport →](3-Transport-zh.md)
