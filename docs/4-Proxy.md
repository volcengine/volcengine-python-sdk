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
| `ca_file` | str | `None` | Path to a custom CA bundle (PEM) used to verify the STS server certificate. Empty uses the default trust store. |
| `insecure_skip_verify` | bool | `False` | Skip TLS verification of the STS server certificate. For debugging only; never use in production (MITM risk). |

> ⚠️ **Notes**
>
> - All three are optional; when none is set, behavior is unchanged (including env-var proxy fallback).
> - `insecure_skip_verify` takes precedence over `ca_file`: once verification is skipped, `ca_file` is ignored.
> - When the proxy URL embeds `user:password@`, a `Proxy-Authorization: Basic` header is attached automatically (urllib3 does not do this by default; this matches the Go SDK). Drop the userinfo if the proxy needs no authentication.

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
    proxy_url="http://user:pass@10.0.0.1:8080",  # reach STS via proxy; empty falls back to env vars
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

Provider settings, resolved OIDC mode/environment inputs, and explicit proxy fallback are snapshots. OIDC token **file contents** are still read at every refresh so token rotation works. After changing or replacing `client.configuration`, its `credential_provider`, or provider settings, call `client.rebind_credential_provider()` to install a new binding and empty cache. Existing requests and their retries keep the old binding. Do not mutate configuration concurrently with binding. This method only updates credential binding; create a new client to rebuild the business HTTP transport.

Fallback is kept separate from explicit `proxy_url`; rebinding with an empty client fallback clears the previous fallback. Custom providers, subclasses, and default/CLI provider chains are not copied or injected with proxy settings; their existing no-argument `get_credentials()` contract is unchanged.

---

[← Transport](3-Transport.md) | Proxy[(中文)](4-Proxy-zh.md) | [Timeout →](5-Timeout.md)
