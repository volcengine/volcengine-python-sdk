[← Transport](3-Transport-zh.md) | 代理配置[(English)](4-Proxy.md) | [超时配置 →](5-Timeout-zh.md)

---

## HTTP(S) 代理配置

> **默认**
>
> - 无代理

### 配置 HTTP(S) 代理

```python
import volcenginesdkcore,volcenginesdkecs
configuration = volcenginesdkcore.Configuration()
configuration.ak = "Your AK"
configuration.sk = "Your SK"

configuration.http_proxy = "http://your_proxy:8080"
configuration.https_proxy = "http://your_proxy:8080"

volcenginesdkcore.Configuration.set_default(configuration)

api_instance = volcenginesdkecs.ECSApi()
```

### 注意事项

支持通过以下环境变量配置代理：

- `http_proxy` / `HTTP_PROXY`
- `https_proxy` / `HTTPS_PROXY`

优先级：代码 > 环境变量。当前 REST 代理解析器不实现 `no_proxy` / `NO_PROXY` 绕过。

---

## STS 凭证 Provider 的代理与 TLS 配置

上面的 `configuration.http_proxy` / `https_proxy` 作用于**业务 API 请求**。而 STS 凭证 Provider（`StsCredentialProvider` / `StsOidcCredentialProvider` / `StsSamlCredentialProvider`）在**换取临时凭证时**会向 STS 端点单独发起请求，这条请求的代理与 TLS 可通过下面三个构造参数独立配置。

| 参数 | 类型 | 默认 | 说明 |
|---|---|---|---|
| `proxy_url` | str | `None` | 访问 STS 端点使用的正向代理，格式 `scheme://[user:password@]host:port`。留空时使用客户端回退，再保留默认配置及环境变量行为。 |
| `ca_file` | str | `None` | 用于校验 STS 服务端证书的自定义 CA 证书文件路径（PEM 格式）。留空时使用系统默认根证书信任库。 |
| `insecure_skip_verify` | bool | `False` | 是否跳过 STS 服务端 TLS 证书校验。仅限联调，生产环境禁用，否则存在中间人攻击风险。 |

> ⚠️ **注意事项**
>
> - 三个参数均为可选；全部不设置时保持默认行为（含环境变量代理回退）。
> - `insecure_skip_verify` 优先级高于 `ca_file`：一旦跳过校验，`ca_file` 将被忽略。
> - 代理地址携带 `user:password@` 时会自动附加 `Proxy-Authorization: Basic` 请求头（urllib3 默认不会携带，此处对齐 Go SDK 行为）；无需认证时去掉即可。

### 示例

```python
import volcenginesdkcore
from volcenginesdkcore.auth.providers.sts_provider import StsCredentialProvider

configuration = volcenginesdkcore.Configuration()
configuration.region = "cn-beijing"
configuration.credential_provider = StsCredentialProvider(
    ak="Your ak",
    sk="Your sk",
    role_name="Your role name",
    account_id="Your account id",
    proxy_url="http://user:pass@10.0.0.1:8080",  # 经代理访问 STS；留空回退环境变量
    ca_file="/path/to/ca.pem",                   # 可选：自定义 CA 校验 STS 证书
    insecure_skip_verify=False,                  # 仅联调可 True，生产禁用
)
volcenginesdkcore.Configuration.set_default(configuration)
```

`StsOidcCredentialProvider` 与 `StsSamlCredentialProvider` 支持完全相同的 `proxy_url` / `ca_file` / `insecure_skip_verify` 三个参数，用法一致。

### 代理回退优先级

`ApiClient` 构造时为三个内置 STS Provider 的具体类型创建私有绑定，不修改源 Provider。凭证刷新的代理优先级从高到低：

1. Provider 上显式设置的 `proxy_url`；
2. 绑定时的 `Configuration.proxy`；
3. 按 **STS 端点的 scheme**（而非业务请求）匹配：`http` 取绑定时的 `Configuration.http_proxy`，`https` 取绑定时的 `Configuration.https_proxy`；
4. 绑定时快照保存的 STS 默认配置，再回退到对应的环境变量 `HTTP_PROXY` / `HTTPS_PROXY`。

环境变量代理保留为传输层回退，不固化为 Provider 的显式设置。当前 REST 解析器不实现 `NO_PROXY` 绕过。

### 绑定生命周期

每个客户端拥有独立的空凭证缓存和刷新锁，即使共享源 Provider 或使用 `Configuration.set_default` 也不例外。普通请求、重试和 RDS `build_auth_token` 复用客户端绑定，不会每次请求重建缓存。

Provider 参数、已解析的 OIDC 模式和环境输入、显式客户端代理回退均为绑定时快照。OIDC token **文件内容**仍在每次刷新时读取，支持 token 轮换。修改或替换 `client.configuration`、其 `credential_provider` 或 Provider 设置后，调用 `client.rebind_credential_provider()` 安装新绑定并清空新绑定缓存。已创建的请求及其重试保留旧绑定；不要在绑定时并发修改源配置。该方法只更新凭证绑定，重建业务 HTTP 传输需要创建新客户端。

回退值与显式 `proxy_url` 分开保存；以空客户端回退重新绑定会清除旧回退。自定义 Provider、子类及默认/CLI 凭证链不被复制或注入代理设置，原有无参数 `get_credentials()` 调用契约不变。

---

[← Transport](3-Transport-zh.md) | 代理配置[(English)](4-Proxy.md) | [超时配置 →](5-Timeout-zh.md)
