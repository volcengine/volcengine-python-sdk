[← Overview](0-Overview.md) | Environment Variables[(中文)](EnvironmentVariables-zh.md)

---

## Environment Variables

This page consolidates all credential-related environment variables supported by the SDK, for easy deployment / CI injection. Other categories (Region, TLS, etc.) can be appended here as new sections later.

### How to Set

#### Linux / macOS

Temporary (current shell only):

```shell
export VOLCENGINE_ACCESS_KEY=your-ak
export VOLCENGINE_SECRET_KEY=your-sk
export VOLCENGINE_SESSION_TOKEN=your-session-token
```

To persist, put the `export` lines in `~/.bashrc`, `~/.zshrc`, or your shell's startup file.

Verify with `echo $VOLCENGINE_ACCESS_KEY`.

#### Windows

Command line (run as Administrator):

```cmd
setx VOLCENGINE_ACCESS_KEY your-ak /M
setx VOLCENGINE_SECRET_KEY your-sk /M
setx VOLCENGINE_SESSION_TOKEN your-session-token /M
```

`/M` sets system-level variables; omit `/M` for user-level.

GUI: **This PC** → right-click → **Properties** → **Advanced system settings** → **Environment Variables** → **New**.

Verify: open a new command prompt and run `echo %VOLCENGINE_ACCESS_KEY%`.

### Credentials

#### Basic AK/SK/Token

| Variable | Description | Required |
|---|---|:-:|
| `VOLCENGINE_ACCESS_KEY` | Access Key | ✅ |
| `VOLCENGINE_SECRET_KEY` | Secret Key | ✅ |
| `VOLCENGINE_SESSION_TOKEN` | STS session token | ❌ |

#### OIDC (AssumeRoleWithOIDC)

| Variable | Description | Required |
|---|---|:-:|
| `VOLCENGINE_OIDC_ROLE_TRN` | OIDC role TRN | ✅ |
| `VOLCENGINE_OIDC_TOKEN_FILE` | OIDC token file path | ✅ |
| `VOLCENGINE_OIDC_ROLE_SESSION_NAME` | Session name | ❌ |
| `VOLCENGINE_OIDC_ROLE_POLICY` | Session policy JSON | ❌ |
| `VOLCENGINE_OIDC_STS_ENDPOINT` | STS endpoint host | ❌ |

#### ECS IMDS

| Variable | Description |
|---|---|
| `VOLCENGINE_ECS_METADATA` | ECS instance role name; if unset, auto-discovered from IMDS |
| `VOLCENGINE_ECS_METADATA_DISABLED` | Set to `true` to disable IMDS credential retrieval |

#### CLI Config File

| Variable | Description |
|---|---|
| `VOLCENGINE_CLI_CONFIG_FILE` | Config file path; defaults to `~/.volcengine/config.json` |
| `VOLCENGINE_PROFILE` | Profile name to use |

#### Legacy Compatibility Variables (`VOLCSTACK_*`)

Early SDKs used the `VOLCSTACK_*` prefix. When the corresponding `VOLCENGINE_*` variable is unset, the following are used as fallbacks. **New code should use `VOLCENGINE_*` only.**

| Variable | Equivalent `VOLCENGINE_*` | Go | Java | PHP | Python |
|---|---|:-:|:-:|:-:|:-:|
| `VOLCSTACK_ACCESS_KEY_ID` / `VOLCSTACK_ACCESS_KEY` | `VOLCENGINE_ACCESS_KEY` | ✅ | ❌ | ✅ | ❌ |
| `VOLCSTACK_SECRET_ACCESS_KEY` / `VOLCSTACK_SECRET_KEY` | `VOLCENGINE_SECRET_KEY` | ✅ | ❌ | ✅ | ❌ |
| `VOLCSTACK_SESSION_TOKEN` | `VOLCENGINE_SESSION_TOKEN` | ✅ | ❌ | ✅ | ❌ |
| `VOLCSTACK_PROFILE` | `VOLCENGINE_PROFILE` | ✅ | ❌ | ✅ | ❌ |

> The Go SDK has a few additional legacy `VOLCSTACK_*` variables (shared-credentials file path, legacy AssumeRole settings, etc.) that are not listed here. Please migrate to the `VOLCENGINE_*` interfaces documented on this page.

#### Default Credential Chain

When no credentials are explicitly configured, all four SDKs try the following providers in order; the first one that succeeds is used:

1. Environment Variable Provider (`VOLCENGINE_ACCESS_KEY` / `VOLCENGINE_SECRET_KEY`[/`VOLCENGINE_SESSION_TOKEN`])
2. OIDC Provider (reads `VOLCENGINE_OIDC_*`)
3. CLI Config Provider (`~/.volcengine/config.json`)
4. ECS IMDS Provider

#### Priority Summary

| Item | Priority (high → low) |
|---|---|
| CLI config file path | constructor arg > `VOLCENGINE_CLI_CONFIG_FILE` > `~/.volcengine/config.json` |
| Profile | constructor arg > `VOLCENGINE_PROFILE` > `VOLCSTACK_PROFILE` (Go/PHP only) > `current` field in config > `default` |
| ECS role name | constructor arg > `VOLCENGINE_ECS_METADATA` > IMDS auto-discovery |

### See Also

- [Credentials](1-Credentials.md) — Per-provider code-level usage

---

[← Overview](0-Overview.md) | Environment Variables[(中文)](EnvironmentVariables-zh.md)
