[← 访问凭据](1-Credentials-zh.md) | Endpoint 配置[(English)](2-Endpoint.md) | [Transport →](3-Transport-zh.md)

---

# EndPoint配置

## 自定义Endpoint

> **默认**
> * 不指定endpoint时，走[自动化Endpoint寻址](#自动化endpoint寻址)

用户可以通过在初始化客户端时指定Endpoint


```python
import volcenginesdkcore
configuration = volcenginesdkcore.Configuration()
configuration.ak = "Your ak"
configuration.sk = "Your sk"
configuration.host = "<example>.<regionId>.volcengineapi.com" # 自定义Endpoint
volcenginesdkcore.Configuration.set_default(configuration)
```

## 自定义RegionId

**代码示例：**

支持`configuration`级别全局配置和接口级别的运行时参数设置`RuntimeOption`;`RuntimeOption`设置会覆盖`configuration`全局配置。
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

## 自动化Endpoint寻址

> **默认**
> * 默认支持自动寻址，无需手动指定Endpoint

为了简化用户配置，Vocoengine 提供了灵活的 Endpoint 自动寻址机制。用户无需手动指定服务地址，SDK 会根据服务名称、区域（Region）等信息自动拼接出合理的访问地址，并支持用户自定义DualStack（双栈）支持。
### Endpoint默认寻址
**Endpoint默认寻址逻辑**
1. 是否自动寻址Region
内置自动寻址Region列表代码:[./volcenginesdkcore/endpoint/providers/default_provider.py#bootstrap_region](./volcenginesdkcore/endpoint/providers/default_provider.py#L458)
SDK 仅对部分预设区域（如`cn-beijing-autodriving`、`ap-southeast-2`）或用户配置的区域执行自动寻址；其他区域默认返回Endpoint：`open.volcengineapi.com`。
用户可通过环境变量 `VOLC_BOOTSTRAP_REGION_LIST_CONF` 或代码中自定义 `custom_bootstrap_region` 来扩展控制区域列表。
2. DualStack 支持（IPv6）
SDK 支持双栈网络（IPv4 + IPv6）访问地址，自动启用条件如下：
显式传入参数`use_dual_stack`，或设置环境变量 `VOLC_ENABLE_DUALSTACK`，优先级`use_dual_stack`>`VOLC_ENABLE_DUALSTACK`
启用后，域名后缀将从 `volcengineapi.com` 切换为 `volcengine-api.com`。
3. 根据服务名和区域自动构造 Endpoint 地址，规则如下：
**全局服务（如 CDN、IAM）**
使用 `<服务名>.volcengineapi.com`（或启用双栈时使用 `volcengine-api.com`）。
示例：`cdn.volcengineapi.com`
**区域服务（如 ECS、RDS）**
使用 `<服务名>.<区域名>.volcengineapi.com` 作为默认 Endpoint。
示例：`ecs.cn-beijing.volcengineapi.com`

**代码示例：**

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

### Endpoint标准寻址
**标准寻址规则**

| Global服务 | 双栈 | 格式                                                                                                               |
|----------|----|------------------------------------------------------------------------------------------------------------------|
| 是        | 是  | `{Service}.volcengine-api.com`                                                                                   |
| 是        | 否  | `{Service}.volcengineapi.com`                                                                                    |
| 否        | 是  | `{Service}.{region}.volcengine-api.com`|
| 否        | 否  | `{Service}.{region}.volcengineapi.com` |

**代码示例：**

是否global服务根据具体调用的服务决定的，是否global无法修改的。
可以参考列表：[./volcenginesdkcore/endpoint/providers/standard_provider.py#ServiceInfos](./volcenginesdkcore/endpoint/providers/standard_provider.py#L51)
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
