[← Endpoint 配置](2-Endpoint-zh.md) | Transport[(English)](3-Transport.md) | [代理配置 →](4-Proxy-zh.md)

---

## HTTP 连接池配置

> **默认**
>
> - `num_pools` - 4：底层 `PoolManager` 同时保留的不同 host 连接池数量上限；适用场景：当你的客户端需要访问大量不同主机时，增大此值
> - `connection_pool_maxsize` - `multiprocessing.cpu_count() * 5`：单个 host 内保持的最大连接数；适用场景：当你对同一主机发起大量并发请求时，增大此值

**代码示例：**

```python
import volcenginesdkcore
configuration = volcenginesdkcore.Configuration()
configuration.ak = "Your ak"
configuration.sk = "Your sk"
configuration.num_pools=10 # 最大支持的主机数量
configuration.connection_pool_maxsize=10 # 每个主机最大连接数
volcenginesdkcore.Configuration.set_default(configuration)
```

## HTTPS 请求配置

### 指定 scheme

> **默认**
>
> - `scheme` - `https`

**代码示例：**

支持 `configuration` 级别全局配置和接口级别的运行时参数设置 `RuntimeOption`；`RuntimeOption` 设置会覆盖 `configuration` 全局配置。

```python
import volcenginesdkcore,volcenginesdkecs
from volcenginesdkcore.rest import ApiException
from volcenginesdkcore.interceptor import RuntimeOption
# 全局配置
configuration = volcenginesdkcore.Configuration()
configuration.ak = "Your ak"
configuration.sk = "Your sk"
configuration.scheme="http" # 指定scheme
volcenginesdkcore.Configuration.set_default(configuration)

# 接口级别运行时参数设置,会覆盖全局配置
runtime_options = RuntimeOption(
    scheme="http",
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

### 忽略 SSL 验证

> **默认**
>
> - `verify_ssl` - `True`

**代码示例：**

```python
import volcenginesdkcore
configuration = volcenginesdkcore.Configuration()
configuration.ak = "Your ak"
configuration.sk = "Your sk"
configuration.verify_ssl=False # 忽略SSL验证
volcenginesdkcore.Configuration.set_default(configuration)
```

---

[← Endpoint 配置](2-Endpoint-zh.md) | Transport[(English)](3-Transport.md) | [代理配置 →](4-Proxy-zh.md)
