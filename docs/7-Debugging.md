[← Error Handling](6-ErrorHandling.md) | Debugging[(中文)](7-Debugging-zh.md) | [SDK Integration →](../SDK_Integration.md)

---

# Debugging

## Enable Debug Mode

```python
import volcenginesdkcore
configuration = volcenginesdkcore.Configuration()
configuration.ak = "Your AK"
configuration.sk = "Your SK"
configuration.debug = True
volcenginesdkcore.Configuration.set_default(configuration)
```

## Set Debug Level

```python
import volcenginesdkcore
from volcenginesdkcore.observability.debugger import LogLevel

configuration = volcenginesdkcore.Configuration()
configuration.ak = "Your AK"
configuration.sk = "Your SK"
configuration.debug = True
configuration.log_level = LogLevel.LOG_DEBUG_WITH_CONFIG.mask | LogLevel.LOG_DEBUG_WITH_REQUEST.mask | LogLevel.LOG_DEBUG_WITH_RESPONSE.mask
volcenginesdkcore.Configuration.set_default(configuration)
```

# Log Output

```python
import volcenginesdkcore
configuration = volcenginesdkcore.Configuration()
configuration.ak = "Your AK"
configuration.sk = "Your SK"
configuration.logger_file = "app.log"
configuration.logger_format = "%(asctime)s %(levelname)s %(message)s"
volcenginesdkcore.Configuration.set_default(configuration)
```

---

[← Error Handling](6-ErrorHandling.md) | Debugging[(中文)](7-Debugging-zh.md) | [SDK Integration →](../SDK_Integration.md)
