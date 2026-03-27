[← Retry](5-Retry.md) | Error Handling[(中文)](6-ErrorHandling-zh.md) | [Debugging →](7-Debugging.md)

---

# Error Handling

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
    print("Network/timeout error:{}".format(e))
except ValueError as e:
    print("Client-side error:{}".format(e))
except ApiException as e:
    if e.status == 0:
        print("Client-side SSL error:{}".format(e.reason))
    else:
        print("Server-side error:")
        if e.body is not None:
            response_meta_data = json.loads(e.body).get("ResponseMetadata")
            print("RequestId:{}".format(response_meta_data.get("RequestId")))
            print("Error Code: {}".format(response_meta_data.get("Error").get("Code")))
            print("Error Message: {}".format(response_meta_data.get("Error").get("Message")))
except Exception as e:
    print("Other error:%s" % e)
```

---

[← Retry](5-Retry.md) | Error Handling[(中文)](6-ErrorHandling-zh.md) | [Debugging →](7-Debugging.md)
