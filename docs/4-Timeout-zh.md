[← Transport](3-Transport-zh.md) | 超时配置[(English)](4-Timeout.md) | [重试机制 →](5-Retry-zh.md)

---

# 超时配置
> **默认**
> * `connect_timeout` - 30s
> * `read_timeout` - 30s

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
configuration.connect_timeout=10 # 设置connect_timeout,单位秒
configuration.read_timeout=10 # 设置read_timeout,单位秒
volcenginesdkcore.Configuration.set_default(configuration)

# 接口级别运行时参数设置,会覆盖全局配置
runtime_options = RuntimeOption(
    connect_timeout=10, # 设置connect_timeout,单位秒
    read_timeout=20, # 设置read_timeout,单位秒
    client_side_validation = True, # 开启客户端校验,默认开启
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

---

[← Transport](3-Transport-zh.md) | 超时配置[(English)](4-Timeout.md) | [重试机制 →](5-Retry-zh.md)
