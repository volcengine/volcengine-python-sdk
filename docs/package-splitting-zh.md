# Python SDK 分包设计

## 结论

采用与 Alibaba Cloud Python SDK 相同的“公共 Core + 独立产品发行包”模型，同时保留
`volcengine-python-sdk` 作为全量安装的兼容元包。源代码继续放在一个仓库，由同一份
清单生成所有发行制品，不复制生成代码，也不改变现有 Python 导入路径。

| 层级 | PyPI 发行包 | Python 导入包 | 职责 |
| --- | --- | --- | --- |
| Core | `volcenginesdk-core` | `volcenginesdkcore` | 鉴权、请求、配置、重试等公共能力 |
| 产品 | `volcenginesdk-ecs` | `volcenginesdkecs` | 单个产品的 API、模型和客户端 |
| 全量兼容 | `volcengine-python-sdk` | 无 | 精确依赖本次发布的全部分包 |

用户只使用 ECS 时安装 `volcenginesdk-ecs`；pip 会自动安装
`volcenginesdk-core`。原来安装 `volcengine-python-sdk` 的用户仍会得到全部服务，
业务代码中的 `import volcenginesdkecs` 不变。

## 与 Alibaba Cloud 方案的取舍

[Alibaba Cloud Python SDK](https://github.com/aliyun/alibabacloud-python-sdk)
为每个产品维护独立目录和 `setup.py`，产品发行包只包含自身模块并依赖公共运行时。
这种发行边界清晰，但直接照搬会在本仓库产生一百多份重复配置。
本方案保留相同的 PyPI 和运行时边界，用 `split-packages.json` 与统一构建脚本生成临时
构建目录。这样生成器仍输出当前目录结构，依赖、包名和发布范围则只有一个事实来源。

## 包范围和依赖

`split-packages.json` 显式列出 136 个发布模块。发行包名按以下规则生成：

- `volcenginesdkcore` 映射为 `volcenginesdk-core`。
- 其他 `volcenginesdk<product>` 映射为 `volcenginesdk-<product>`。
- `volcenginesdkexamples` 仅作为源码示例，不进入运行时发行包。
- `volcenginesdkarkruntime` 的发行名在 PyPI 上与一个已删除项目的 ultranormalized 名冲突（见 pypi/support#12626），暂不发布；方舟运行时请使用官方独立包 `arkruntime`。
- TOS SDK 已由独立的 `tos` 项目发布，不纳入本仓库分包。

内部依赖由构建脚本从绝对 import 中提取并精确锁定到同一 SDK 版本。当前只有以下非
标准依赖链：

- `volcenginesdk-llmshield` 依赖 `volcenginesdk-sts` 和 Core。
- `volcenginesdk-wafruntime` 依赖 `volcenginesdk-waf`，后者依赖 Core。

产品包直接安装时可以独立升级；全量元包使用精确版本形成一次发布的 BOM，避免从不同
SDK 版本拼出未经验证的全量环境。精确锁定是迁移期的保守选择，放宽路径见下文
「演进：core 兼容承诺与部分发布」一节。LLM Shield 只在 Python 3.8 及以上安装。其他包维持现有
`Python >= 2.7` 元数据。

## 构建和校验

构建工具至少使用 Python 3.7。运行以下命令校验清单覆盖、包名唯一性、跨包 import、
依赖环和 Core 可达性：

```sh
python3 scripts/build_split_packages.py validate
```

构建全部 wheel 和 sdist：

```sh
python3 scripts/build_split_packages.py build \
  --version 5.0.45 \
  --output-dir dist/split
python3 -m twine check dist/split/*
```

CI 已预装 `build`、`setuptools` 和 wheel 构建能力时，可传入 `--no-isolation`
复用该工具环境。此选项会跳过构建依赖安装，流水线必须自行保证工具版本。

可重复传入 `--package` 构建指定模块或发行包。测试发布可以只构建 wheel：

```sh
python3 scripts/build_split_packages.py build \
  --version 5.0.45.post1 \
  --formats wheel \
  --output-dir dist/testpypi
```

## 发布流程

PyPI 不支持多项目原子发布，流水线必须按以下顺序执行：

1. 校验清单并构建全部制品。
2. 对全部制品执行 `twine check`，在干净容器中做离线 wheel 安装和导入测试。
3. 先上传 Core，再上传全部产品包。
4. 确认所有产品版本可见后，最后上传 `volcengine-python-sdk` 元包。
5. 从公开索引创建新的干净环境，分别验证按需安装与全量兼容安装。

元包最后发布且精确锁版本，即使中途上传失败，也不会产生一个可安装但缺包的全量版本。
PyPI 制品不可覆盖；失败后应修复并发布新版本，不复用已有版本号。

多项目上传可使用带哈希校验和限速重试的工具。它会根据 wheel 的 `Requires-Dist` 按
依赖拓扑排序，因此 Core 和被依赖产品先上传、元包最后上传。远端同名文件只有
SHA-256 与本地一致时才允许断点续传：

```sh
python3 scripts/upload_split_packages.py \
  dist/split \
  --repository testpypi \
  --index-url https://test.pypi.org
```

[Warehouse 默认配置](https://github.com/pypi/warehouse/blob/main/warehouse/config.py)
按用户限制每小时创建 20 个新项目、按 IP 限制每小时创建 40 个新项目，实际部署值可能
不同。首次预占 136 个分包名必须分批执行并支持跨小时恢复，不能把项目创建放在正式
发布窗口；日常向已存在项目上传新版本不受这个“新项目”限制。

TestPyPI 不镜像第三方依赖。不要用 `--extra-index-url` 混合 TestPyPI 与正式 PyPI，
因为 pip 会在两个索引间选择最高版本，可能从 TestPyPI 安装同名第三方包。验证时先只
从正式 PyPI 安装外部依赖，再以 `--no-deps` 只从 TestPyPI 安装待测 SDK 包：

```sh
python -m pip install \
  --index-url https://pypi.org/simple/ \
  certifi python-dateutil six urllib3
python -m pip install --no-deps \
  --index-url https://test.pypi.org/simple/ \
  volcenginesdk-core==5.0.45.post1 \
  volcenginesdk-ecs==5.0.45.post1
python -m pip check
```

## 兼容与迁移

- 分包流程不修改 API、模型、签名、鉴权和生成目录，仅改变 wheel 的文件归属。本次验证
  另行去除了三个 VPN 模型中已有的 `local_bgp_ip` 重复生成项，否则原模块无法解析；
  保留重复字典键原本最终生效的 `LocalBgpIp` 映射。
- 全量用户继续安装 `volcengine-python-sdk`；新用户优先安装所需产品包。
- 不应让旧版单体包与分包长期共存，因为它们拥有相同文件。升级全量元包前，pip 应先
  卸载旧单体版本；从单体包迁移到单个产品包时，应显式卸载单体包后再安装分包。
- 发布前需在正式 PyPI 预占全部发行包名，并把产品到发行包的映射同步到 API Explorer、
  SDK 下载页和发布后台。
- 单产品体积门禁以 `volcenginesdk-core` 与该产品 wheel 的总大小计算，ECS 目标不超过
  15 MB；全量元包自身只含元数据。

## 演进：core 兼容承诺与部分发布

当前产品包对 core、元包对全部分包均用 `==` 精确锁定。这是从单体包迁移的保守
选择——版本号继续标识“一组同次生成、经过测试的代码”，代价是每次发布重发全部
136 个包，core 的修复也必须整车才能到达用户。长期应收敛到 core 独立发布、产品
按需发布，前提是 core 建立兼容承诺。

### 耦合面

产品生成代码对 core 的依赖面很窄，兼容边界可控：

- 每个产品仅 `from volcenginesdkcore.configuration import Configuration`（数百处）
  和 `*_api.py` 中的 `volcenginesdkcore.ApiClient()` 无参构造；
- 模型不继承 core，签名、传输、重试（signv4、rest、retryer 等）均为 core 内部
  模块，产品不直接引用。

因此兼容承诺的范围是 `Configuration` 的构造参数与属性、`ApiClient` 的行为；
内部实现可自由演进。

### 目标模型

- core 遵循语义化版本：上述边界的破坏性变更走 major，内部演进走 minor/patch；
- 产品包对 core 的依赖从 `==` 放宽为 `~=`，同一 major 内的新 core 自动适用；
- 版本归属各服务目录：每个模块在 `__init__.py` 中维护 `__version__`，由 codegen
  在重新生成时按 spec diff 自动 bump；core 是手写模块，版本人工维护；
- 只有代码变更（版本上涨）的产品才发版；core 修复独立发布，老产品无需重发；
- 元包版本与产品版本脱钩，仅在 BOM 组合变化时发版，内容为构建时汇总的各产品
  当前版本。

### 实施顺序

1. codegen 侧实现版本维护：重新生成且产物有变更时，按 spec diff 决定 semver 级别
   （新增 API、新增可选参数为 minor；删除或修改既有参数、类型为 major，或先标记
   由人工确认），把版本写入模块 `__init__.py` 的 `__version__`；core 确立语义化
   版本纪律，版本人工维护；
2. 构建脚本改为从各模块目录读取版本（AST 解析，不导入）；产品对 core 的依赖下限
   同样由 codegen 写在模块目录（如 `__core_requires__ = ">=5.1.0,<6"`），构建脚本
   读取后生成 `~=` 约束——codegen 模板使用 core 新特性时必须同步抬高该下限；
3. `split-packages.json` 去掉全局版本号，只保留模块清单、依赖和 `python_requires`；
   元包 `install_requires` 在构建时汇总各目录版本生成；
4. CI 增加兼容性矩阵：以“最新 core + 上一版产品”跑安装导入与冒烟调用，
   `verify_split_install.py` 参数化后可复用；
5. validate 增加版本纪律检查：模块目录自上次 release tag 有变更但 `__version__`
   未涨时构建失败，兜住人工修改生成目录的情况。

### 版本维护

- 版本号放在代码旁边，由 codegen 生成和 bump，不设集中注册表，避免 136 个条目
  挤在一个文件里成为合并热点；
- codegen 只在“产物有变化”的重新生成时 bump，产物无变化不动版本；两次发布之间
  的多次重新生成会累积多次 bump，PyPI 上版本号不连续，属正常；
- core 没有 codegen，版本由发布流程人工维护，对 core 的手工修复同样需要 bump；
- 发布时构建并上传版本号高于 PyPI 的模块加元包；release tag 标记发布基线，
  validate 用它检查“代码变了但版本没涨”；
- 根目录 `meta.json` 的全局版本号在该模型下废弃，元包版本由构建时按 BOM 变化
  独立生成。

### 风险边界

需要警惕的方向是“新产品 + 旧 core”：产品用新 core 生成和测试，运行时却拉到旧
core，这个组合同样未经验证。`~=` 的下限必须如实反映生成时使用的 core 特性，
不能随意放宽。

该模型接近 Alibaba Cloud 的 `darabonba-core>=1.0.0,<2.0.0` 范围依赖方案，区别
是本仓库保留元包作为一次发布的 BOM。

## CI 门禁

后续应把以下检查加入发布流水线：清单与源码目录一致、跨包依赖无环、全部 wheel 文件
归属唯一、Core + 每个产品均可在干净环境安装和导入、全量元包可解析全部精确依赖、
ECS 体积不超过 15 MB。产品目录新增或删除而未同步清单时，发布必须失败。

容器安装完成后可运行统一的导入校验：

```sh
python scripts/verify_split_install.py \
  --manifest split-packages.json \
  --version 5.0.45 \
  --expect-meta
```
