[← 超时配置](5-Timeout-zh.md) | 重试机制[(English)](6-Retry.md) | [异常处理 →](7-ErrorHandling-zh.md)

---

## 重试机制

请求的处理逻辑内置了网络异常重试逻辑，即当遇到网络异常问题或限流错误时，系统会自动尝试重新发起请求，以确保服务的稳定性和可靠性。若请求因业务逻辑错误而报错，例如参数错误、资源不存在等情况，SDK 将不会执行重试操作，这是因为业务层面的错误通常需要应用程序根据具体的错误信息做出相应的处理或调整，而非简单地重复尝试。

### 重试代码配置

支持 `configuration` 级别全局配置和接口级别的运行时参数设置 `RuntimeOption`；`RuntimeOption` 设置会覆盖 `configuration` 全局配置。

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
configuration.backoff_strategy = ExponentialWithRandomJitterBackoffStrategy() # 重试策略，默认 ExponentialWithRandomJitterBackoffStrategy。
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

### 请求拦截器的重试生命周期

请求拦截器默认在每次 HTTP 尝试（包括重试）前执行。只希望在一次逻辑 SDK 调用中执行一次的
自定义拦截器，需要设置 `run_on_retry = False`。SDK 内置的请求构建、运行时参数和 Endpoint
解析拦截器只在首次尝试前执行。

### 重试条件

重试条件定义了哪些情况下需要进行重试。SDK 内置了默认的重试条件，用户也可以根据自己的业务需求，自定义重试条件。

#### 默认重试条件

默认重试条件 `DefaultRetryCondition`，其中包含以下重试条件：

1. 网络错误会进行重试。
2. 服务端限流错误会进行重试。
3. 包含客户自定义的错误码 `retry_error_codes`。

#### 自定义重试条件

用户可以根据自己的业务需求，自定义重试条件。

**代码示例：**

1. 继承基类 `RetryCondition`，实现 `def should_retry(self, response, err)`：

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

2. 复用默认 `DefaultRetryCondition` 逻辑：

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

### 退避策略

#### 包装错误与解析边界

默认重试识别 `ApiException`、Python `__cause__` / 未抑制的 `__context__` 和 urllib3 包装内的底层网络原因、状态码与配置的字符串业务码。循环保护、最多 256 个节点和 64 层限制遍历；`previous_exception` 仅用于诊断，不作为新请求的重试原因。TLS 失败与代理 407 等终止原因仍不可重试。

默认 TOP 解析器位于响应拦截器链首位时，在每次尝试中解析普通预读响应；客户响应拦截器仍在重试结束后执行，原异常对象不被统一包装。HTTP 200 的 HTML、JSON `null`、普通类型转换失败默认只尝试一次；明确的底层网络原因或客户配置的业务码可触发重试。普通 HTTP 500/429/502/503/504 保持既有状态码规则，`auto_retry=False` 禁用自动重试。

文件只在选定最终响应后写入一次，避免重试遗留临时文件。放弃的流式响应关闭并归还连接，不额外读体。客户替换、前置或继承解析器时，执行顺序沿用其拦截器链。旧签名的客户请求/传输覆写不要求新增 `_response_type` 参数。

STS Provider 的 `max_retries` 是总尝试次数，最少 1 次；仅 HTTP 429/502/503/504、限流/瞬时码及可识别网络原因触发重试。HTTP 500 缺少可重试码、TLS 及代理认证错误不重试；普通业务配置的 `num_max_retries` 仍是首次之后的重试次数。

默认重试会逐层检查响应 JSON 结构，仅将字符串业务码与配置匹配，异常字段类型不会掩盖最终的响应错误。已取得响应后读体失败的 `ApiException.cause` 仍参与原有网络重试判断；代理认证和 TLS 配置错误不会因此被当成可重试网络错误。

重试条件、退避计算或等待发生普通异常时停止重试，返回带当前 `cause` 的 `ApiException`；有前次响应 / 异常时保留其状态、正文、响应头、RequestId 及 `previous_exception`。失败时 SDK 放弃的流式响应会关闭并释放连接池槽位，不额外读取正文，清理错误不覆盖原始原因。`KeyboardInterrupt` / `SystemExit` 原样传播。详见[异常处理](7-ErrorHandling-zh.md)。

退避策略定义了在重试时，每次重试之间的延迟时间。SDK 内置了默认的退避策略，用户也可以根据自己的业务需求，自定义退避策略。

> **默认**
>
> - `ExponentialWithRandomJitterBackoffStrategy`

#### 内置退避策略

边界值说明：`min_retry_delay` 最小延迟时间，`max_retry_delay` 最大延迟时间，`n` 为重试次数。

| 策略名称 | 说明 | 公式 |
|---|---|---|
| `NoBackoffStrategy` | 不使用退避。每次重试立即执行，零延时。 | `delay = 0.0` |
| `ExponentialBackoffStrategy` | 每次重试延时按 2ⁿ 级数增长，受最小/最大延时约束。可快速降低请求频率。 | `delay = min(min_retry_delay * 2ⁿ, max_retry_delay)` |
| `ExponentialWithRandomJitterBackoffStrategy` | 在 `[base, 2·base]` 之间取值：始终 ≥ `base`，抖动幅度与基线等宽。 | `base = min(min_retry_delay · 2ⁿ, max_retry_delay)`<br/>`delay = base + U(0, base)` |

#### 自定义退避策略

用户可以根据自己的需求，自定义退避策略。

**代码示例：**

1. 继承基类 `BackoffStrategy`，实现函数 `def compute_delay(self, retry_count)`：

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

2. 也可以复用内置退避策略 `ExponentialBackoffStrategy` 或 `ExponentialWithRandomJitterBackoffStrategy`：

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

[← 超时配置](5-Timeout-zh.md) | 重试机制[(English)](6-Retry.md) | [异常处理 →](7-ErrorHandling-zh.md)
