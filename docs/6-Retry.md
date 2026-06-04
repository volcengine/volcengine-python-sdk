[← Timeout](5-Timeout.md) | Retry[(中文)](6-Retry-zh.md) | [Error Handling →](7-ErrorHandling.md)

---

## Retries

The SDK retries on network errors and throttling. Business logic errors are not retried.

### Retry Code Configuration

```python
import volcenginesdkcore
from volcenginesdkcore.retryer.backoff_strategy import ExponentialWithRandomJitterBackoffStrategy
from volcenginesdkcore.retryer.retry_condition import DefaultRetryCondition

configuration = volcenginesdkcore.Configuration()
configuration.ak = "Your ak"
configuration.sk = "Your sk"
configuration.auto_retry = True
configuration.num_max_retries = 4
configuration.min_retry_delay_ms = 200
configuration.max_retry_delay_ms = 6000
configuration.backoff_strategy = ExponentialWithRandomJitterBackoffStrategy()
configuration.retry_condition = DefaultRetryCondition()
configuration.retry_error_codes = {"AccessDenied"}
volcenginesdkcore.Configuration.set_default(configuration)
```

### Retry Conditions

#### Default Retry Conditions

The default retry condition includes:

1. Retry on network errors.
2. Retry on server throttling errors.
3. Retry on user-specified error codes (`retry_error_codes`).

#### Custom Retry Conditions

1. Implement your own retry condition:

```python
from volcenginesdkcore.retryer.retry_condition import RetryCondition

class CustomRetryCondition(RetryCondition):
    def should_retry(self, response, err):
        retry_error_codes = self.retry_error_codes
        return False
```

2. Reuse the default condition logic:

```python
from volcenginesdkcore.retryer.retry_condition import DefaultRetryCondition

class CustomRetryCondition(DefaultRetryCondition):
    def should_retry(self, response, err):
        should_retry = super(CustomRetryCondition, self).should_retry(response, err)
        return False
```

### Backoff Strategy

#### Built-in Backoff Strategies

| Name | Description | Formula |
|---|---|---|
| `NoBackoffStrategy` | No backoff, retry immediately | `delay = 0.0` |
| `ExponentialBackoffStrategy` | Exponential backoff with bounds | `delay = min(min_retry_delay * 2ⁿ, max_retry_delay)` |
| `ExponentialWithRandomJitterBackoffStrategy` | Exponential with jitter | `base = min(min_retry_delay · 2ⁿ, max_retry_delay)`<br/>`delay = base + U(0, base)` |

#### Custom Backoff Strategies

1. Implement your own strategy:

```python
from volcenginesdkcore.retryer.backoff_strategy import BackoffStrategy

class CustomBackoffStrategy(BackoffStrategy):
    def compute_delay(self, retry_count):
        min_retry_delay = self.min_retry_delay
        max_retry_delay = self.max_retry_delay
        return 0.0
```

2. Reuse built-in strategy:

```python
from volcenginesdkcore.retryer.backoff_strategy import ExponentialBackoffStrategy

class CustomBackoffStrategy(ExponentialBackoffStrategy):
    def compute_delay(self, retry_count):
        delay = super(CustomBackoffStrategy, self).compute_delay(retry_count)
        return 0.0
```

---

[← Timeout](5-Timeout.md) | Retry[(中文)](6-Retry-zh.md) | [Error Handling →](7-ErrorHandling.md)
