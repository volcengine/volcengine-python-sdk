[← 超时配置](4-Timeout-zh.md) | 重试机制[(English)](5-Retry.md) | [异常处理 →](6-ErrorHandling-zh.md)

---

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
configuration.min_retry_delay_ms = 200 # 最小重试延迟毫秒，默认300毫秒
configuration.max_retry_delay_ms = 6000 # 最大重试延迟毫秒，默认300000毫秒
configuration.backoff_strategy = ExponentialWithRandomJitterBackoffStrategy() # 重试策略，默认ExponentialWithRandomJitterBackoffStrategy
configuration.retry_condition = DefaultRetryCondition() # 重试条件，默认DefaultRetryCondition
configuration.retry_error_codes = {"AccessDenied"} # 重试错误码，默认为空集合，需要用户自定义
volcenginesdkcore.Configuration.set_default(configuration)

# 接口级别配置
runtime_options = RuntimeOption(
    auto_retry = True, # 开启自动重试,默认开启
    num_max_retries = 4, # 最大重试次数，默认3次
    min_retry_delay_ms = 200, # 最小重试延迟毫秒，默认300毫秒
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

---

[← 超时配置](4-Timeout-zh.md) | 重试机制[(English)](5-Retry.md) | [异常处理 →](6-ErrorHandling-zh.md)
