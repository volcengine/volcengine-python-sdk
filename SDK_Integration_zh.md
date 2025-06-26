# 目录
- [集成SDK](#集成sdk)
  - [环境要求](#环境要求)
  - [访问凭据](#访问凭据)
    - [AK、SK设置](#aksk设置)
  - [EndPoint配置](#endpoint配置)
    - [自定义Endpoint](#自定义endpoint)
    - [自定义RegionId](#自定义regionid)
    - [自动化Endpoint寻址](#自动化endpoint寻址)
      - [Endpoint默认寻址](#endpoint默认寻址)
  - [Http连接池配置](#http连接池配置)
  - [Https请求配置](#https请求配置)
    - [指定scheme](#指定scheme)
    - [忽略SSL验证](#忽略ssl验证)
  - [超时配置](#超时配置)
  - [重试机制](#重试机制)
    - [重试代码配置](#重试代码配置)
    - [重试条件](#重试条件)
      - [默认重试条件](#默认重试条件)
      - [自定义重试条件](#自定义重试条件)
    - [退避策略](#退避策略)
      - [内置退避策略](#内置退避策略)
      - [自定义退避策略](#自定义退避策略)
  - [异常处理](#异常处理)
  - [Debug机制](#debug机制)
  - [指定日志Logger](#指定日志logger)

# 集成SDK

在调用接口时，推荐在项目中集成 SDK 的方式进行接入。通过使用 SDK，不仅可以简化开发流程、加快功能集成速度，还能有效降低后期的维护成本。火山引擎 SDK 的集成主要包括以下三个步骤：引入 SDK、配置访问凭证，以及编写接口调用代码。本文将结合常见使用场景，详细说明各步骤的实现方法及注意事项。

# 环境要求

1. Python环境版本>=2.7
2. 如使用方舟服务(volcenginesdkarkruntime)，需要使用 >=3.6 的 Python 环境

# 访问凭据

为保障资源访问安全，火山引擎 Python SDK 目前暂时只支持 **AK/SK**认证设置。

## AK、SK设置

AK/SK 是由火山引擎用户在控制台创建的一对永久访问密钥。SDK 使用该密钥对每次请求进行签名，从而完成身份验证。

> ⚠️ 注意事项
>
> 1. 不得在客户端嵌入或暴露 AK/SK。
> 2. 推荐使用配置中心或环境变量存储密钥。
> 3. 配置合理的最小权限访问策略。

**代码示例：**  

支持`configuration`级别全局配置和接口级别的运行时参数设置`RuntimeOption`;`RuntimeOption`设置会覆盖`configuration`全局配置。
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
  ak =  "Your ak", 
  sk = "Your sk", 
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
  region =  "cn-beijing",
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
  scheme =  "http",
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

# 重试机制

请求的处理逻辑内置了网络异常重试逻辑，即当遇到网络异常问题或限流错误时，系统会自动尝试重新发起请求，以确保服务的稳定性和可靠性。若请求因业务逻辑错误而报错，例如参数错误、资源不存在等情况，SDK将不会执行重试操作，这是因为业务层面的错误通常需要应用程序根据具体的错误信息做出相应的处理或调整，而非简单地重复尝试。
## 重试代码配置
支持`configuration`级别全局配置和接口级别的运行时参数设置`RuntimeOption`;`RuntimeOption`设置会覆盖`configuration`全局配置。
```python
import volcenginesdkcore,volcenginesdkecs
from volcenginesdkcore.rest import ApiException
from volcenginesdkcore.interceptor import RuntimeOption
from volcenginesdkcore.retryer.backoff_strategy import ExponentialWithRandomJitterBackoffStrategy
from volcenginesdkcore.retryer.retry_condition import DefaultRetryCondition
configuration = volcenginesdkcore.Configuration()
configuration.ak = "Your ak"
configuration.sk = "Your sk"
# 全局配置
configuration.auto_retry = True # 开启自动重试,默认开启
configuration.num_max_retries = 4 # 最大重试次数，默认3次
configuration.min_retry_delay_ms = 200 # 最小重试延迟毫秒，默认30毫秒
configuration.max_retry_delay_ms = 6000 # 最大重试延迟毫秒，默认300000毫秒
configuration.backoff_strategy = ExponentialWithRandomJitterBackoffStrategy() # 重试策略，默认ExponentialWithRandomJitterBackoffStrategy
configuration.retry_condition = DefaultRetryCondition() # 重试条件，默认DefaultRetryCondition
configuration.retry_error_codes = {"AccessDenied"} # 重试错误码，默认为空集合，需要用户自定义
volcenginesdkcore.Configuration.set_default(configuration)

# 接口级别配置
runtime_options = RuntimeOption(
  auto_retry = True, # 开启自动重试,默认开启
  num_max_retries = 4, # 最大重试次数，默认3次
  min_retry_delay_ms = 200, # 最小重试延迟毫秒，默认30毫秒
  max_retry_delay_ms = 6000, # 最大重试延迟毫秒，默认300000毫秒
  backoff_strategy = ExponentialWithRandomJitterBackoffStrategy(), # 重试策略，默认ExponentialWithRandomJitterBackoffStrategy
  retry_condition = DefaultRetryCondition(), # 重试条件，默认DefaultRetryCondition
  retry_error_codes = {"AccessDenied"}, # 重试错误码，默认为空集合，需要用户自定义
  client_side_validation = True, # 开启客户端校验,默认开启
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
except ApiException as e:
    pass

```

## 重试条件
重试条件定义了哪些情况下需要进行重试。SDK内置了默认的重试条件，用户也可以根据自己的业务需求，自定义重试条件。
### 默认重试条件
默认重试条件`DefaultRetryCondition`，其中包含以下重试条件：
1. 网络错误会进行重试
2. 服务端限流错误会进行重试
3. 包含客户自定义的错误码`retry_error_codes`

### 自定义重试条件
用户可以根据自己的业务需求，自定义重试条件。  

**代码示例：**  
1. 继承基类RetryCondition 实现def should_retry(self, response, err)
```python
from volcenginesdkcore.retryer.retry_condition import RetryCondition
class CustomRetryCondition(RetryCondition):
  def should_retry(
          self,
          response,
          err
  ):
      # type: (RESTResponse, Exception) -> bool
      retry_error_codes = self.retry_error_codes # 可以获取到用户自定义的错误码
      #................实现自己逻辑

      return False
```
2. 复用默认DefaultRetryCondition逻辑
```python
from volcenginesdkcore.retryer.retry_condition import DefaultRetryCondition
class CustomRetryCondition(DefaultRetryCondition):
  def should_retry(
          self,
          response,
          err
  ):
      # type: (RESTResponse, Exception) -> bool
      should_retry = super(CustomRetryCondition, self).should_retry(response, err)  
      #..................实现自己逻辑

      return False
```

## 退避策略
退避策略定义了在重试时，每次重试之间的延迟时间。SDK内置了默认的退避策略，用户也可以根据自己的业务需求，自定义退避策略。
> **默认**  
> * ExponentialWithRandomJitterBackoffStrategy
### 内置退避策略
| 策略名称 | 说明 | 公式（边界值：`min_retry_delay` 最小延迟时间，`max_retry_delay` 最大延迟时间）                                                     |
| -------- | ---- |-------------------------------------------------------------------------------------|
| `NoBackoffStrategy` | 不使用退避。每次重试立即执行，零延时。 | `delay=0.0`                                                                           |
| `ExponentialBackoffStrategy` | 每次重试延时按 2ⁿ 级数增长，受最小/最大延时约束。可快速降低请求频率。 | `delay=min(min_retry_delay*2ⁿ, max_retry_delay)`                                      |
| `ExponentialWithRandomJitterBackoffStrategy` |    在 [base, 2·base] 之间取值：始终 ≥ base，抖动幅度与基线等宽。 | `base = min(min_retry_delay · 2ⁿ,  max_retry_delay )`  <br/>`delay = base + U(0, base)` |

### 自定义退避策略
用户可以根据自己的需求，自定义退避策略。  

**代码示例：**
1. 继承基类`BackoffStrategy`，实现函数`def compute_delay(self, retry_count)` 
```python
from volcenginesdkcore.retryer.backoff_strategy import BackoffStrategy
class CustomBackoffStrategy(BackoffStrategy):
    def compute_delay(self, retry_count):
        # type: (int) -> float
        
        min_retry_delay = self.min_retry_delay
        max_retry_delay = self.max_retry_delay
        #.....实现自己逻辑
        return 0.0
```
2. 也可以复用内置退避策略`ExponentialBackoffStrategy`或`ExponentialWithRandomJitterBackoffStrategy`
```python
from volcenginesdkcore.retryer.backoff_strategy import ExponentialBackoffStrategy
class CustomBackoffStrategy(ExponentialBackoffStrategy):
    def compute_delay(self, retry_count):
        # type: (int) -> float
        delay = super(CustomBackoffStrategy, self).compute_delay(retry_count)
        #.....实现自己逻辑
        return 0.0
```

# 异常处理

在调用接口时，可能会返回不同类型的错误。客户可根据具体的错误类型和错误码，采取有针对性的处理策略。例如，对于网络异常可选择重试，对于业务逻辑错误则应根据错误信息进行参数调整或业务逻辑修正，从而提升系统的健壮性和用户体验。

错误分类：


| 错误类型    | 错误描述               | 返回错误类型                                                                                                                                                                                                  | 说明 |
|---------|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|
| `1.网络/超时错误` | DNS解析错误或请求超时       | (`urllib3.exceptions.NewConnectionError`, `urllib3.exceptions.ConnectTimeoutError`, <br/>`urllib3.exceptions.ReadTimeoutError`, `urllib3.exceptions.ProtocolError`,`socket.timeout`, `socket.gaierror`) | 包含在元组中错误表示网络错误 |
| `2.客户端错误` | 请求未到达服务端的一些参数认证       | `volcenginesdkcore.rest.ApiException` `ValueError`                                                                                                                                                      | 客户端参数验证 |
| `3.服务端错误` | 请求成功到达服务器，返回业务逻辑错误 | `volcenginesdkcore.rest.ApiException`                                                                                                                                                                   | status!=0表示服务端错误 |
| `4.其它错误`  | 未包含在前4中错误的其它错误处理   | `Exception`                                                                                                                                                                                             | 兜底错误 |

**代码示例：**

```python
import json
import socket
import urllib3
import volcenginesdkcore,volcenginesdkecs
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
network_error_exceptions = (urllib3.exceptions.NewConnectionError, urllib3.exceptions.ConnectTimeoutError,
                                    urllib3.exceptions.ReadTimeoutError, urllib3.exceptions.ProtocolError,
                                    socket.timeout, socket.gaierror)

try:
    api_instance.create_command(create_command_request)
except network_error_exceptions as e:
    print("1.网络/超时错误:{}".format(e))
except ValueError as e:
    print("2.客户端错误（参数认证错误）:{}".format(e))
except ApiException as e:
    if e.status == 0:
        print("2.客户端错误（SSL认证错误）:{}".format(e.reason))
    else:
        print("3.服务端错误:")
        if e.body is not None:
            response_meta_data = json.loads(e.body).get("ResponseMetadata")
            print("RequestId:{}".format(response_meta_data.get("RequestId")))
            print("Error Code: {}".format(response_meta_data.get("Error").get("Code")))
            print("Error Message: {}".format(response_meta_data.get("Error").get("Message")))
except Exception as e:
    print("4.其它错误:%s", e)

```

# Debug机制

为便于客户在处理请求时进行问题排查和调试，SDK 支持日志功能，并提供多种日志级别设置。客户可根据实际需求配置日志级别，获取详细的请求与响应信息，以提升排障效率和系统可 observability（可观测性）。

> **默认**  
> * `debug` - `False`  

**代码示例：**
```python
import volcenginesdkcore
configuration = volcenginesdkcore.Configuration()
configuration.ak = "Your AK"
configuration.sk = "Your SK"
configuration.debug = True  # 开启debug模式
volcenginesdkcore.Configuration.set_default(configuration)
```

# 指定日志Logger

> **默认**  
> * `logger_file` - `None` (默认不输出到文件,控制台输出)  
> * `logger_format` - `%(asctime)s %(levelname)s %(message)s` (默认日志格式)

**代码示例：**
```python
import volcenginesdkcore
configuration = volcenginesdkcore.Configuration()
configuration.ak = "Your AK"
configuration.sk = "Your SK"
configuration.logger_file = "app.log" # 指定日志路径
configuration.logger_format = "%(asctime)s %(levelname)s %(message)s" # 指定日志格式
volcenginesdkcore.Configuration.set_default(configuration)
```

