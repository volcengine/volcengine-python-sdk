[← Endpoint 配置](2-Endpoint-zh.md) | Transport[(English)](3-Transport.md) | [超时配置 →](4-Timeout-zh.md)

---

# Http连接池配置

> **默认**
> * `num_pools` - 4  最多支持的主机数量；适用场景：当你对同一主机发起多个并发请求时，应该增大此值
> * `connection_pool_maxsize` - `multiprocessing.cpu_count() * 5` 每个主机最大连接数；适用场景：当你需要同时连接多个不同主机时，应该增大此值

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

# Https请求配置

## 指定scheme

> **默认**
> * `scheme` - `https`

**代码示例：**

支持`configuration`级别全局配置和接口级别的运行时参数设置`RuntimeOption`;`RuntimeOption`设置会覆盖`configuration`全局配置。
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

# Http(s)代理配置

> - **默认**
>   无代理

## 配置Http(s)代理

```python
import volcenginesdkcore,volcenginesdkecs
configuration = volcenginesdkcore.Configuration()
configuration.ak = "Your AK"
configuration.sk = "Your SK"

configuration.http_proxy = "http://your_proxy:8080"
configuration.https_proxy = "http://your_proxy:8080"

volcenginesdkcore.Configuration.set_default(configuration)

api_instance = volcenginesdkecs.ECSApi()
```

## 注意事项

支持通过以下环境变量配置代理:

http_proxy/HTTP_PROXY, https_proxy/HTTPS_PROXY, no_proxy/NO_PROXY

优先级：代码 > 环境变量


## 忽略SSL验证

> **默认**
> * `verify_ssl` - `True`

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

[← Endpoint 配置](2-Endpoint-zh.md) | Transport[(English)](3-Transport.md) | [超时配置 →](4-Timeout-zh.md)
