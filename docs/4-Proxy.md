[← Transport](3-Transport.md) | Proxy[(中文)](4-Proxy-zh.md) | [Timeout →](5-Timeout.md)

---

## HTTP(S) Proxy

> **Default**
>
> - No proxy

### Configure HTTP(S) Proxy

```python
import volcenginesdkcore, volcenginesdkecs
configuration = volcenginesdkcore.Configuration()
configuration.ak = "Your AK"
configuration.sk = "Your SK"

configuration.http_proxy = "http://your_proxy:8080"
configuration.https_proxy = "http://your_proxy:8080"

volcenginesdkcore.Configuration.set_default(configuration)

api_instance = volcenginesdkecs.ECSApi()
```

### Notes

Supported environment variables for proxy configuration:

- `http_proxy` / `HTTP_PROXY`
- `https_proxy` / `HTTPS_PROXY`

Priority: code > environment variables. The current REST proxy resolver does not
implement `no_proxy` / `NO_PROXY` bypass.

---

## Proxy & TLS for STS credential providers

The `configuration.http_proxy` / `https_proxy` above apply to **business API requests**. STS credential providers (`StsCredentialProvider` / `StsOidcCredentialProvider` / `StsSamlCredentialProvider`) issue a **separate request to the STS endpoint** when exchanging for temporary credentials. That request's proxy and TLS can be configured independently via the three constructor parameters below.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `proxy_url` | str | `None` | Forward proxy for reaching the STS endpoint, `scheme://[user:password@]host:port`. Empty uses the client fallback, then existing default configuration/environment behavior. |
| `ca_file` | str | `None` | Custom CA bundle (PEM) for verifying STS. Empty inherits `ssl_ca_cert` from the STS default configuration; if unset, REST uses the `certifi` CA bundle. |
| `insecure_skip_verify` | bool | `False` | Skip TLS verification of the STS server certificate. For debugging only; never use in production (MITM risk). |

> ⚠️ **Notes**
>
> - All three are optional. Empty options preserve inherited transport fields, including `verify_ssl=False` and proxy fallback; the binding lifetime below still applies.
> - `insecure_skip_verify=True` disables verification and ignores both explicit and inherited CA files. Otherwise, a nonempty `ca_file` enables verification even if the STS default has `verify_ssl=False`. With no CA and `False`, TLS settings remain inherited.
> - When the proxy URL contains userinfo, a `Proxy-Authorization: Basic` header is attached automatically. Percent-decoded username/password values use UTF-8; an empty username or password is supported. The proxy must accept this encoding. Omit userinfo when authentication is unnecessary.

### Example

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
    proxy_url="http://user:pass@10.0.0.1:8080",  # empty: client fallback, then STS defaults/environment
    ca_file="/path/to/ca.pem",                   # optional: custom CA to verify the STS cert
    insecure_skip_verify=False,                  # True for debugging only; disable in production
)
volcenginesdkcore.Configuration.set_default(configuration)
```

`StsOidcCredentialProvider` and `StsSamlCredentialProvider` accept the exact same `proxy_url` / `ca_file` / `insecure_skip_verify` parameters, used the same way.

### Proxy fallback priority

`ApiClient` binds a private copy of each concrete built-in STS provider at construction. The source provider is not modified. Proxy priority for credential refresh, highest first:

1. Explicit `proxy_url` set on the provider;
2. Bind-time `Configuration.proxy`;
3. By the **STS endpoint scheme**, not the business request scheme: `http` uses bind-time `Configuration.http_proxy`, `https` uses bind-time `Configuration.https_proxy`;
4. Existing STS default configuration (snapshotted at binding), then the corresponding `HTTP_PROXY` / `HTTPS_PROXY` environment variable.

Environment proxies remain transport fallbacks, not explicit provider settings. `NO_PROXY` bypass is not implemented by the current REST resolver.

### Binding lifetime

Each client owns a fresh credential cache and refresh lock, even when clients share a source provider or use `Configuration.set_default`. Normal requests, retries, and RDS `build_auth_token` reuse that client's binding; they do not create a new cache per request.

Migration note: credentials already cached on the source provider are not copied into a new client, and client refreshes do not populate the source cache. Creating clients or rebinding can therefore increase STS calls. Reuse clients when possible, and explicitly rebind after configuration changes.

Provider settings, resolved OIDC mode/environment inputs, and explicit proxy fallback are snapshots. OIDC token **file contents** are still read at every refresh so token rotation works. After changing or replacing `client.configuration`, its `credential_provider`, or provider settings, call `client.rebind_credential_provider()` to install a new binding and empty cache. Existing requests and their retries keep the old binding. Do not mutate configuration concurrently with binding. This method only updates credential binding; create a new client to rebuild the business HTTP transport.

Fallback is kept separate from explicit `proxy_url`; rebinding with an empty client fallback clears the previous fallback. Custom providers, subclasses, and default/CLI provider chains are not copied or injected with proxy settings; their existing no-argument `get_credentials()` contract is unchanged.

### Retries

For all three STS providers, `max_retries` is the total number of attempts (minimum one); `retry_interval` is in seconds. Credential requests retain these settings even when global business `auto_retry=False`. Business requests continue to honor their own retry switch.

The default retry condition recognizes recoverable proxy connection failures and their urllib3 wrappers. Proxy authentication failures (407), certificate errors, and invalid proxy configuration are not automatically retried.

---

[← Transport](3-Transport.md) | Proxy[(中文)](4-Proxy-zh.md) | [Timeout →](5-Timeout.md)
