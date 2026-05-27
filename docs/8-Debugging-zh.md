[← 异常处理](7-ErrorHandling-zh.md) | Debug 机制[(English)](8-Debugging.md) | [概览 →](0-Overview-zh.md)

---

## Debug 机制

为便于客户在处理请求时进行问题排查和调试，SDK 支持日志功能，并提供多种日志级别设置。客户可根据实际需求配置日志级别，获取详细的请求与响应信息，以提升排障效率和系统可观测性。

### 开启 Debug 模式

> **默认**
>
> - `debug` - `False`

**代码示例：**

```python
import volcenginesdkcore
configuration = volcenginesdkcore.Configuration()
configuration.ak = "Your AK"
configuration.sk = "Your SK"
configuration.debug = True  # 开启debug模式
volcenginesdkcore.Configuration.set_default(configuration)
```

### 设置 Debug 级别

默认情况下开启 debug 日志后，会输出所有的 debug 日志；为了按需输出日志，可以调用 `configuration.log_level` 进行以下设置：

```python
import volcenginesdkcore
from volcenginesdkcore.observability.debugger import LogLevel
configuration = volcenginesdkcore.Configuration()
configuration.ak = "Your AK"
configuration.sk = "Your SK"
configuration.debug = True  # 开启debug模式
configuration.log_level = LogLevel.LOG_DEBUG_WITH_CONFIG.mask | LogLevel.LOG_DEBUG_WITH_REQUEST.mask | LogLevel.LOG_DEBUG_WITH_RESPONSE.mask
volcenginesdkcore.Configuration.set_default(configuration)
```

#### 支持的日志级别

| 枚举项 | 父级日志（同时打印父级日志） | 打印的内容 |
|---|---|---|
| `LOG_DEBUG_WITH_REQUEST` | — | 请求行与基础请求信息：`HTTP 方法`、`URL（含查询参数）`、`请求头` |
| `LOG_DEBUG_WITH_REQUEST_BODY` | `LOG_DEBUG_WITH_REQUEST` | `请求体` |
| `LOG_DEBUG_WITH_REQUEST_ID` | `LOG_DEBUG_WITH_REQUEST` | `RequestId` |
| `LOG_DEBUG_WITH_RESPONSE` | `LOG_DEBUG_WITH_REQUEST` | `响应状态码`、`响应头` |
| `LOG_DEBUG_WITH_RESPONSE_BODY` | `LOG_DEBUG_WITH_RESPONSE` | `响应体` |
| `LOG_DEBUG_WITH_SIGNING` | `LOG_DEBUG_WITH_REQUEST` | `签名过程` |
| `LOG_DEBUG_WITH_ENDPOINT` | `LOG_DEBUG_WITH_REQUEST` | `Endpoint 选择过程` |
| `LOG_DEBUG_WITH_REQUEST_RETRIES` | `LOG_DEBUG_WITH_REQUEST` | `重试信息` |
| `LOG_DEBUG_WITH_CONFIG` | `LOG_DEBUG_WITH_REQUEST` | `关键配置信息` |
| `LOG_DEBUG_ALL` | — | `包含上面所有信息` |

### 指定日志 Logger

> **默认**
>
> - `logger_file` - `None`（默认不输出到文件，控制台输出）
> - `logger_format` - `%(asctime)s %(levelname)s %(message)s`（默认日志格式）

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

---

[← 异常处理](7-ErrorHandling-zh.md) | Debug 机制[(English)](8-Debugging.md) | [概览 →](0-Overview-zh.md)
