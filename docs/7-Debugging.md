[← Error Handling](6-ErrorHandling.md) | Debugging[(中文)](7-Debugging-zh.md) | [Overview →](0-Overview.md)

---

## Debugging

To help with troubleshooting and debugging when handling requests, the SDK supports logging with multiple levels. Configure your logging settings based on your needs to get detailed request/response information and improve observability.

### Enable Debug Mode

> **Default**
>
> - `debug` - `False`

```python
import volcenginesdkcore
configuration = volcenginesdkcore.Configuration()
configuration.ak = "Your AK"
configuration.sk = "Your SK"
configuration.debug = True  # enable debug mode
volcenginesdkcore.Configuration.set_default(configuration)
```

### Set Debug Level

By default, when debug is enabled the SDK emits all debug logs. To filter the output, configure `configuration.log_level` as follows:

```python
import volcenginesdkcore
from volcenginesdkcore.observability.debugger import LogLevel

configuration = volcenginesdkcore.Configuration()
configuration.ak = "Your AK"
configuration.sk = "Your SK"
configuration.debug = True  # enable debug mode
configuration.log_level = LogLevel.LOG_DEBUG_WITH_CONFIG.mask | LogLevel.LOG_DEBUG_WITH_REQUEST.mask | LogLevel.LOG_DEBUG_WITH_RESPONSE.mask
volcenginesdkcore.Configuration.set_default(configuration)
```

#### Supported Log Levels

| Constant | Parent level (logged together with parent) | Logged content |
|---|---|---|
| `LOG_DEBUG_WITH_REQUEST` | — | Request line and basic info: `HTTP method`, `URL (with query params)`, `headers` |
| `LOG_DEBUG_WITH_REQUEST_BODY` | `LOG_DEBUG_WITH_REQUEST` | `Request body` |
| `LOG_DEBUG_WITH_REQUEST_ID` | `LOG_DEBUG_WITH_REQUEST` | `RequestId` |
| `LOG_DEBUG_WITH_RESPONSE` | `LOG_DEBUG_WITH_REQUEST` | `Response status code`, `response headers` |
| `LOG_DEBUG_WITH_RESPONSE_BODY` | `LOG_DEBUG_WITH_RESPONSE` | `Response body` |
| `LOG_DEBUG_WITH_SIGNING` | `LOG_DEBUG_WITH_REQUEST` | `Signing process` |
| `LOG_DEBUG_WITH_ENDPOINT` | `LOG_DEBUG_WITH_REQUEST` | `Endpoint resolution` |
| `LOG_DEBUG_WITH_REQUEST_RETRIES` | `LOG_DEBUG_WITH_REQUEST` | `Retry information` |
| `LOG_DEBUG_WITH_CONFIG` | `LOG_DEBUG_WITH_REQUEST` | `Key configuration info` |
| `LOG_DEBUG_ALL` | — | `All of the above` |

### Log Output

> **Default**
>
> - `logger_file` - `None` (logs to console by default; no file output)
> - `logger_format` - `%(asctime)s %(levelname)s %(message)s`

```python
import volcenginesdkcore
configuration = volcenginesdkcore.Configuration()
configuration.ak = "Your AK"
configuration.sk = "Your SK"
configuration.logger_file = "app.log"  # specify log file path
configuration.logger_format = "%(asctime)s %(levelname)s %(message)s"  # specify log format
volcenginesdkcore.Configuration.set_default(configuration)
```

---

[← Error Handling](6-ErrorHandling.md) | Debugging[(中文)](7-Debugging-zh.md) | [Overview →](0-Overview.md)
