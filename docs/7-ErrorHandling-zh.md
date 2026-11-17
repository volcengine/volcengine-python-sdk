[← 重试机制](6-Retry-zh.md) | 异常处理[(English)](7-ErrorHandling.md) | [Debug 机制 →](8-Debugging-zh.md)

---

## 异常处理

在调用接口时，可能会返回不同类型的错误。客户可根据具体的错误类型和错误码，采取有针对性的处理策略。例如，对于网络异常可选择重试，对于业务逻辑错误则应根据错误信息进行参数调整或业务逻辑修正，从而提升系统的健壮性和用户体验。

### 错误分类

| 错误类型    | 错误描述               | 返回错误类型                                                                                                                                                                                                  | 说明 |
|---------|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|
| `1.网络/超时错误` | DNS解析错误、连接超时或响应读取中断 | 无可用响应时沿用网络异常类型；已有响应的读体失败返回 `volcenginesdkcore.rest.ApiException` | 读体失败的原始网络原因保存在 `e.cause`，默认重试继续识别该原因 |
| `2.客户端错误` | 请求未到达服务端的一些参数认证       | `volcenginesdkcore.rest.ApiException` `ValueError`                                                                                                                                                      | 客户端参数验证 |
| `3.响应处理错误` | HTTP / 业务错误、响应格式错误或模型转换失败 | `volcenginesdkcore.rest.ApiException` | 有响应时保存真实 HTTP 状态，200 也可能抛异常；不等同于服务端业务错误 |
| `4.其它错误`  | 未包含在前 3 类错误中的其他错误处理   | `Exception`                                                                                                                                                                                             | 兜底错误 |

### 代码示例

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
    print("1.网络/超时错误:{}".format(e))
except ValueError as e:
    print("2.客户端错误（参数认证错误）:{}".format(e))
except ApiException as e:
    if e.status == 0:
        print("2.客户端错误（SSL认证错误）:{}".format(e.reason))
    else:
        print("3.响应处理错误:")
        print("HTTP Status:{}".format(e.status))
        # response_metadata 对标准与非标准响应均可用，RequestId 由响应体或网关响应头解析得到
        if e.response_metadata is not None:
            print("RequestId:{}".format(e.response_metadata.request_id))
        # 标准 TOP 错误响应可从正文解析出 Error Code / Message；非标准响应（如 504 返回
        # HTML、非 TOP 标准 JSON）正文可能不是 JSON，此时直接打印原始正文用于排查
        if e.body is not None:
            error = None
            try:
                payload = json.loads(e.body)
            except (ValueError, TypeError, UnicodeError):
                payload = None
            if isinstance(payload, dict):
                metadata = payload.get("ResponseMetadata")
                if isinstance(metadata, dict) and isinstance(metadata.get("Error"), dict):
                    error = metadata["Error"]
            if isinstance(error, dict):
                print("Error Code: {}".format(error.get("Code")))
                print("Error Message: {}".format(error.get("Message")))
            else:
                print("Response Body: {}".format(e.body))
        if e.cause is not None:
            print("Original Cause: {!r}".format(e.cause))
        if e.previous_exception is not None:
            print("Previous Exception: {}".format(e.previous_exception))
except Exception as e:
    print("4.其它错误:%s" % e)
```

### 非标准错误响应的诊断信息

当服务端或网关返回**非标准响应**时（例如 504 网关返回 HTML/纯文本、或不含 TOP `ResponseMetadata` 的 JSON），SDK 会将其统一封装为 `volcenginesdkcore.rest.ApiException`，并保留完整诊断信息，便于定位问题：

| 字段 | 含义 |
|---|---|
| `e.status` | 真实的 HTTP 状态码（如 504），不再被固定为 200 |
| `e.body` | 原始响应正文（含非 JSON 内容） |
| `e.headers` | 响应头 |
| `e.response_metadata` | `ResponseMetadata` 对象，`e.response_metadata.request_id` 为请求 ID |
| `e.cause` | JSON 解析、转换、解码、读体、文件处理或重试处理的原始原因；没有底层异常时为 `None` |
| `e.previous_exception` | 重试处理失败时的前次异常；转换已有 `ApiException` 时可保留该异常 |
| `str(e)` | 汇总输出，依次包含状态码、`RequestId`、响应头与响应正文 |

`ApiException` 的所有构造方式均解析 RequestId：正文中的非空 `ResponseMetadata.RequestId` → 显式传入的元数据 ID → `X-Top-Requestid` → `X-Top-Request-Id` → `X-Tt-Logid`。头名称忽略大小写，候选头值为列表或元组时取首值。传入的元数据对象不会被原地修改；正文和头部没有 ID 时保持为空。

### 响应转换、读取与重试诊断

VE 与 BytePlus Python SDK 使用相同的异常处理规则：

- 自动重试逐层检查 JSON 对象和业务码类型，`null`、数组及错误字段类型不会打断重试判断；异常响应继续交给解析层处理。
- 非法 `ResponseMetadata`、Result / 模型转换、元数据回填、日期解析及文件处理失败统一返回 `ApiException`，保留完整 TOP 正文、真实状态、响应头、RequestId 和原始原因。合法转换回退、合法 `Result:null` 或缺少 Result 的返回行为保持不变。
- Python 3 的普通响应仍按 UTF-8 解码，不按 `Content-Type` 的 charset 切换编码；Python 2 的 REST 层保留原始 `str` 字节，非法 JSON 在反序列化阶段封装为 `ApiException`。Python 3 解码失败时 `e.body` 为原始字节；已有响应的读体失败时为实际保留的字节片段，并关闭失败连接。兼容 urllib3 1.26 和 2.x 的分段解压，解压暂时无输出不会提前结束读取；压缩响应截断时只保留已解压片段，不混入原始压缩字节。`Content-Length` 不完整会报读体失败，不能保证拿到尚未收到的数据。Python 2.7 使用 urllib3 1.26.x，urllib3 2.x 不支持 Python 2.7。
- `call_api(response_type="file")` 的成功预读响应一路保留二进制字节，再写入临时目录中的唯一文件。仅保留 `Content-Disposition` 安全 basename 中由 1～16 个 ASCII 字母或数字组成的扩展名，其余使用默认临时文件名，避免长文件名、路径穿越和重名覆盖；失败时清理未完成文件。非 2xx 仍按错误响应处理。
- 重试条件、退避计算或等待抛出普通异常时停止重试，返回 `ApiException`。有前次响应或异常时附带其诊断，当前原始原因在 `e.cause`，前次异常在 `e.previous_exception`。SDK 放弃的流式响应会关闭并归还连接池槽位，不额外读取正文，清理错误不覆盖回调原因。每轮使用当次响应，避免旧响应覆盖后续网络错误。

Python 3 的 `e.__cause__` 与 `e.cause` 指向同一原始原因；完整堆栈可用 `traceback.print_exception(type(e), e, e.__traceback__)` 打印。`str(e)` 不展开原因堆栈，也不额外合成业务错误码。

未取得响应的连接 / DNS 错误沿用原有网络类型与重试规则；SSL 错误沿用 `status=0` 的 `ApiException`，并保留原因。请求前的参数、凭证、签名及客户自定义拦截器错误保持各自契约；`KeyboardInterrupt`、`SystemExit` 等进程控制异常原样传播。未指定响应类型或 `_preload_content=False` 的成功响应跳过普通反序列化；`call_api` 的既有结果契约保持不变，不承诺直接返回底层 `HTTPResponse`。异步错误在任务 `.get()` 外捕获。

### 全量异常详情与 Go 对齐

```python
import sys
from volcenginesdkcore import print_error, get_error_details

try:
    result = api_instance.create_command(create_command_request)
except Exception as e:
    print_error(sys.stderr, e)
    details = get_error_details(e)  # 独立副本，可脱敏后交给自己的日志系统
```

`PrintError` / `GetErrorDetails` 是上述函数的同义别名。`print_error(writer, None)` 不输出；普通 `error` 也可直接打印。打印失败或短写抛出原始写入错误或 `IOError`，不改变业务异常。输出为缩进 JSON，末尾追加换行：

| 字段 | 含义 |
|---|---|
| `type` / `error` | 异常类型与原 `str(e)` 文本 |
| `code` / `message` | 结构化诊断码与描述；`ApiException` 同时提供 `e.code` / `e.message` |
| `response` | HTTP 响应快照；没有响应时为 `null` |
| `causes` | 底层原因与 `previous_exception`，没有原因时省略 |

`e.response_details` 返回独立的 `ResponseDetails` 副本，提供 `status_code`、`status`、`proto`、`request_id`、多值 `headers` / `trailers`、原始字节 `body`、`body_captured` / `body_complete`。HTTP 200 业务错误保留 200。urllib3 未提供协议或 trailers 时对应字段为空，不伪造信息。已读空正文为 `body_captured=true`、正文 `""`；未读流式响应为 false。UTF-8 字节在 JSON 中显示为文本，其他字节以可还原的 Base64 与 `body_encoding` 输出。

诊断复用当次读取，不额外请求或重读关闭后的正文。读体中断保留实际已读字节，`body_complete=false`，原因在 `causes`；原始 TOP 字节不会被模型转换结果替换。不同尝试与不同请求的错误快照相互独立。

| 场景 | `e.code` |
|---|---|
| 标准 TOP 业务错误，包括 HTTP 200 | 服务端非空 `Code`，无有效码时 `UnknownError` |
| 简易 `{"errorcode":"Denied","message":"..."}` | 非空 `errorcode` |
| HTML、空正文、数组、非法 JSON 或元数据字段类型不兼容 | `SerializationError` |
| 正文 JSON `null` 或可解析但没有有效错误码 | `UnknownError` |
| 响应读取中断 | `ReadError` |
| Result / 模型 / 文件转换失败 | `SerializationError` |
| 重试条件、退避或等待失败 | `RetryError` |

即使其他元数据字段类型不兼容，仍独立提取正文中的非空字符串 `RequestId`；随后使用显式元数据及既有响应头顺序兜底。错误码与描述独立于旧 `reason`：现有 `ApiException.__str__` 格式及现有异常的 `reason` 保持不变；新增字段校验产生的异常使用新的诊断描述。

错误树支持 `cause`、`previous_exception`、Python `__cause__` / 未抑制的 `__context__`、urllib3 包装及 Python 3.11 异常组，按对象身份去重，最多 256 个节点、64 层。客户异常不自动包装或修改；可选 `response_details` 属性或无参方法可提供快照，返回 `None` 时退回实际已有状态和 RequestId。普通错误只有自身文本和原因。完整正文可能包含凭证，调用方可修改详情副本后输出。

### STS、AssumeRole、OIDC、SAML

三条凭证路径统一保存 HTTP / 业务 / 读取 / 解析错误的快照，HTTP 状态始终来自真实响应，正文 `HTTPCode` 不覆盖状态。缺失或空的 AK、SK、SessionToken、过期时间返回 `UnknownError`；过期时间无法解析返回 `SerializationError` 并保留解析原因。所有凭证字段和时间验证完成后才更新缓存，失败保留原缓存。

SDK 内置 HTTP 传输未取得响应的 STS 网络异常归一为 `ApiException(status=0, code="RequestError")`，快照为空、原因保留。归一仅发生在实际传输调用处；本地参数、令牌文件、客户凭证、签名回调及客户请求/传输覆写异常仍按原契约处理，保留对象身份。普通业务请求的无响应网络异常仍沿用原类型，SSL 异常仍为 `ApiException(status=0)`。原先 STS 凭证缺失的 `RuntimeError`、时间解析原生错误和最终网络错误现在可统一捕获为 `ApiException`；这些新归一路径的显示文本随类型变化，其他既有异常文本保持不变。

STS 重试 HTTP 429/502/503/504、限流及瞬时错误码、可识别的底层网络原因；HTTP 500 无可重试错误码时不重试。原因树中每个无响应异常均只按网络原因判定，不让 `RequestError` 白名单覆盖 TLS/代理拒绝；旧式客户异常缺少可选诊断字段也可正常处理。Provider 的 `max_retries` 保持 Python 原语义：总尝试次数，最少 1 次；与普通配置的“首次之后重试次数”不同。VE OIDC/SAML 使用 `Expiration`，BP 保留字段缺失时使用 `ExpiredTime` 的既有兼容行为。代理、TLS、客户端缓存隔离与 rebind 保持原规则。

ECS/IMDS、CLI OAuth/Portal、客户拦截器和未接入的原生读取/解析错误只打印实际已有信息，不承诺完整快照。

---

[← 重试机制](6-Retry-zh.md) | 异常处理[(English)](7-ErrorHandling.md) | [Debug 机制 →](8-Debugging-zh.md)
