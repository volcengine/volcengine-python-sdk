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

### Request Interceptor Retry Lifecycle

Request interceptors run once for every HTTP attempt, including retries. Custom
interceptors that should run only once for a logical SDK call must set
`run_on_retry = False`. The SDK's request building, runtime option, and endpoint
resolution interceptors run only for the first attempt.

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

#### Wrapped Errors and Parsing Boundaries

Default retry recognizes network causes, HTTP statuses and configured string business codes through `ApiException`, Python `__cause__` / unsuppressed `__context__` and urllib3 wrappers. Traversal is bounded to 256 nodes / 64 levels with cycle protection. `previous_exception` is diagnostic history, not a retry cause. Terminal TLS and proxy authentication failures remain nonretryable.

When the built-in TOP parser is first in the response chain, ordinary preloaded responses are parsed during each attempt. Customer response interceptors run after retries finish and their errors retain identity. HTTP 200 HTML, JSON null and ordinary conversion failures normally make one attempt; recognized network causes or configured business codes may retry. Ordinary HTTP 500/429/502/503/504 retain existing status rules; `auto_retry=False` disables retry.

Files are written only once, after selecting the final response. Abandoned streams are closed and returned to the pool without reading. Custom/reordered/subclassed parsers retain their interceptor order. Existing request/transport overrides need not accept the new `_response_type` argument.

STS Provider `max_retries` means total attempts, at least one. STS retries 429/502/503/504, throttling/transient codes and recognized network causes. HTTP 500 without a retryable code, TLS and proxy authentication failures do not retry. Ordinary `num_max_retries` still counts retries after the first attempt.

Default retry checks each JSON object level and matches only string business codes, so invalid field types do not obscure the final response error. An `ApiException.cause` from reading an available response still participates in the existing network retry rules; proxy authentication and TLS configuration errors are not treated as retryable network failures.

An ordinary exception from retry conditions, backoff calculation or waiting stops retries and returns `ApiException` with the current `cause`. Available prior status, body, headers, RequestId and `previous_exception` are retained. Streaming responses abandoned on failure are closed and their connection pool slots released without reading the body; cleanup errors do not replace the original cause. `KeyboardInterrupt` / `SystemExit` propagate unchanged. See [Error Handling](7-ErrorHandling.md).

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
