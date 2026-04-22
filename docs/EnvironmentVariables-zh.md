[← 概览](0-Overview-zh.md) | 环境变量[(English)](EnvironmentVariables.md)

---

# 环境变量

本页集中列出 SDK 支持的所有 credential 相关环境变量，便于部署/CI 环境注入。后续如需新增其他类别（Region、TLS 等），可直接追加章节。

## 设置方法

### Linux / macOS

临时（当前 shell 生效）：

```shell
export VOLCENGINE_ACCESS_KEY=your-ak
export VOLCENGINE_SECRET_KEY=your-sk
export VOLCENGINE_SESSION_TOKEN=your-session-token
```

持久化：将 `export` 写入 `~/.bashrc`、`~/.zshrc` 等 shell 启动文件。

校验：`echo $VOLCENGINE_ACCESS_KEY` 返回预期值即设置成功。

### Windows

命令行（以管理员身份运行）：

```cmd
setx VOLCENGINE_ACCESS_KEY your-ak /M
setx VOLCENGINE_SECRET_KEY your-sk /M
setx VOLCENGINE_SESSION_TOKEN your-session-token /M
```

`/M` 表示系统级；省略 `/M` 为用户级变量。

图形界面：**此电脑** 右键 → **属性** → **高级系统设置** → **环境变量** → **新建**。

校验：新开命令提示符执行 `echo %VOLCENGINE_ACCESS_KEY%`。

## Credentials

### 基础 AK/SK/Token

| 变量 | 说明 | 必填 |
|---|---|:-:|
| `VOLCENGINE_ACCESS_KEY` | Access Key | ✅ |
| `VOLCENGINE_SECRET_KEY` | Secret Key | ✅ |
| `VOLCENGINE_SESSION_TOKEN` | STS 临时凭证 Session Token | ❌ |

### OIDC（AssumeRoleWithOIDC）

| 变量 | 说明 | 必填 |
|---|---|:-:|
| `VOLCENGINE_OIDC_ROLE_TRN` | OIDC 扮演角色 TRN | ✅ |
| `VOLCENGINE_OIDC_TOKEN_FILE` | OIDC Token 文件路径 | ✅ |
| `VOLCENGINE_OIDC_ROLE_SESSION_NAME` | Session 名 | ❌ |
| `VOLCENGINE_OIDC_ROLE_POLICY` | 会话权限策略 JSON | ❌ |
| `VOLCENGINE_OIDC_STS_ENDPOINT` | STS 域名 | ❌ |

### ECS IMDS

| 变量 | 说明 |
|---|---|
| `VOLCENGINE_ECS_METADATA` | 指定 ECS 实例角色名；不设置则从 IMDS 自动探测 |
| `VOLCENGINE_ECS_METADATA_DISABLED` | 设为 `true` 禁用 IMDS 凭证获取 |

### CLI 配置文件

| 变量 | 说明 |
|---|---|
| `VOLCENGINE_CLI_CONFIG_FILE` | 配置文件路径，默认 `~/.volcengine/config.json` |
| `VOLCENGINE_PROFILE` | 使用的 profile 名 |

### 历史兼容变量（`VOLCSTACK_*`）

早期 SDK 使用 `VOLCSTACK_*` 前缀。当同名 `VOLCENGINE_*` 变量未设置时，下列变量会作为 fallback 生效。**新代码请统一使用 `VOLCENGINE_*`。**

| 变量 | 等价的 `VOLCENGINE_*` | Go | Java | PHP | Python |
|---|---|:-:|:-:|:-:|:-:|
| `VOLCSTACK_ACCESS_KEY_ID` / `VOLCSTACK_ACCESS_KEY` | `VOLCENGINE_ACCESS_KEY` | ✅ | ❌ | ✅ | ❌ |
| `VOLCSTACK_SECRET_ACCESS_KEY` / `VOLCSTACK_SECRET_KEY` | `VOLCENGINE_SECRET_KEY` | ✅ | ❌ | ✅ | ❌ |
| `VOLCSTACK_SESSION_TOKEN` | `VOLCENGINE_SESSION_TOKEN` | ✅ | ❌ | ✅ | ❌ |
| `VOLCSTACK_PROFILE` | `VOLCENGINE_PROFILE` | ✅ | ❌ | ✅ | ❌ |

> Go SDK 另有少量历史遗留 `VOLCSTACK_*` 变量（共享凭证文件路径、AssumeRole 角色等），未列入本页；建议迁移到本页列出的 `VOLCENGINE_*` 接口。

### 默认凭证链顺序

未显式配置凭证时，四端 SDK 均按以下顺序依次尝试，首个成功的 Provider 生效：

1. 环境变量 Provider（`VOLCENGINE_ACCESS_KEY` / `VOLCENGINE_SECRET_KEY`[/`VOLCENGINE_SESSION_TOKEN`]）
2. OIDC Provider（从 `VOLCENGINE_OIDC_*` 读取）
3. CLI 配置 Provider（`~/.volcengine/config.json`）
4. ECS IMDS Provider

### 优先级总表

| 项 | 优先级（高 → 低） |
|---|---|
| CLI 配置文件路径 | 构造参数 > `VOLCENGINE_CLI_CONFIG_FILE` > `~/.volcengine/config.json` |
| Profile | 构造参数 > `VOLCENGINE_PROFILE` > `VOLCSTACK_PROFILE`（仅 Go/PHP）> 配置中的 `current` > `default` |
| ECS Role 名称 | 构造参数 > `VOLCENGINE_ECS_METADATA` > IMDS 自动探测 |

## 相关文档

- [访问凭据](1-Credentials-zh.md) — 各 Provider 的代码级用法

---

[← 概览](0-Overview-zh.md) | 环境变量[(English)](EnvironmentVariables.md)
