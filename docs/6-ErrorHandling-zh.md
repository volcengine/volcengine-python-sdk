[← 重试机制](5-Retry-zh.md) | 异常处理[(English)](6-ErrorHandling.md) | [Debug 机制 →](7-Debugging-zh.md)

---

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

---

[← 重试机制](5-Retry-zh.md) | 异常处理[(English)](6-ErrorHandling.md) | [Debug 机制 →](7-Debugging-zh.md)
