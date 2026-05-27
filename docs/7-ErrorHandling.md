[← Retry](6-Retry.md) | Error Handling[(中文)](7-ErrorHandling-zh.md) | [Debugging →](8-Debugging.md)

---

## Error Handling

When calling APIs, different types of errors may be returned. You can adopt targeted handling strategies based on the specific error type and error code. For example, you can retry on network errors, and adjust parameters or fix business logic for business errors, thereby improving system robustness and user experience.

### Error Classification

| Error Type | Description | Returned Error Type | Notes |
|---|---|---|---|
| `1. Network/Timeout Error` | DNS resolution error or request timeout | (`urllib3.exceptions.NewConnectionError`, `urllib3.exceptions.ConnectTimeoutError`, <br/>`urllib3.exceptions.ReadTimeoutError`, `urllib3.exceptions.ProtocolError`, `socket.timeout`, `socket.gaierror`) | Errors contained in the tuple indicate network errors |
| `2. Client Error` | Parameter/authentication errors before reaching the server | `volcenginesdkcore.rest.ApiException` `ValueError` | Client-side parameter validation |
| `3. Server Error` | Request reaches the server, returns a business logic error | `volcenginesdkcore.rest.ApiException` | status != 0 indicates a server-side error |
| `4. Other Errors` | Any other errors not covered above | `Exception` | Catch-all error handling |

### Code Example

```python
import json
import socket
import urllib3
import volcenginesdkcore, volcenginesdkecs
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

network_error_exceptions = (
    urllib3.exceptions.NewConnectionError,
    urllib3.exceptions.ConnectTimeoutError,
    urllib3.exceptions.ReadTimeoutError,
    urllib3.exceptions.ProtocolError,
    socket.timeout,
    socket.gaierror,
)

try:
    api_instance.create_command(create_command_request)
except network_error_exceptions as e:
    print("1. Network/timeout error:{}".format(e))
except ValueError as e:
    print("2. Client error (parameter validation error):{}".format(e))
except ApiException as e:
    if e.status == 0:
        print("2. Client error (SSL authentication error):{}".format(e.reason))
    else:
        print("3. Server error:")
        if e.body is not None:
            response_meta_data = json.loads(e.body).get("ResponseMetadata")
            print("RequestId:{}".format(response_meta_data.get("RequestId")))
            print("Error Code: {}".format(response_meta_data.get("Error").get("Code")))
            print("Error Message: {}".format(response_meta_data.get("Error").get("Message")))
except Exception as e:
    print("4. Other error:%s" % e)
```

---

[← Retry](6-Retry.md) | Error Handling[(中文)](7-ErrorHandling-zh.md) | [Debugging →](8-Debugging.md)
