# 开发计划审计报告

- 日期：2026-05-14
- 审计范围：`docs/plan/index.md` 与 `docs/plan/01-cli-entrypoint.md` ~ `docs/plan/12-review-progress-governance.md`
- 审计对照物：`pyproject.toml`、`mkdocs.yml`、`src/docsbuildtool/`、`tests/`、`.github/workflows/`、`docs/summary.md`
- 结论：结构完整、顺序合理、与当前仓库现状基本一致，但存在 1 项 CLI 语义冲突、2 项实施路线模糊以及若干次要问题，建议在动工前修订。

## 1. 总体评价

- 13 份文档统一采用「目标 / 接口·行为 / 实现步骤 / 影响范围 / 测试用例 / 验收标准 / 风险」七段式，符合 `index.md` 的验收标准。
- 顺序合理：CLI → 配置解析 → HTML → PDF → all → serve → clean → archive → 跨平台 → 测试/CI → 用户文档 → 治理，依赖关系自洽。
- 与现状一致项：`mkdocs-with-pdf`、`mkdocs-material`、`mkdocs-literate-nav`、`mkdocs-section-index`、`typer`、`rich` 已在 `pyproject.toml`；CI 已具备 lint、test 雏形；`docs/summary.md` 已挂载「开发计划」导航。

## 2. 关键问题（建议在实现前修订）

### 2.1 `docs archive --output zip` 与全局 `--output` 语义冲突（🔴 必改）

- `02`、`03`、`07` 中 `--output <directory>` 表示**目录**。
- `08-archive-zip.md` 第 14–18 行同时出现 `--output zip`（**格式**）和 `--output-dir <directory>`（目录），与全局约定冲突；`index.md` 命令列表也未提到 `--output-dir`。
- 建议二选一：
  1. 把格式参数改名为 `--format zip`（与 `build --format` 对齐），保留 `--output <directory>`；或
  2. 在 `08` 显式声明「`archive` 子命令的 `--output` 语义独立」，并在 `index.md` 中标出。

### 2.2 CLI 安装路线与 `package-mode = false` 的冲突未定方案（🟡 应改）

- `pyproject.toml` 当前 `[tool.poetry] package-mode = false`，无 `[project.scripts]`。
- `01-cli-entrypoint.md` 步骤 4–5 仅写「恢复本地可安装 console script」，未给出技术路线（切换 `package-mode = true`？使用 `[project.scripts]` + `pip install -e .`？仍用 Poetry？）。
- 建议在 `01` 增加「实施决策」段落，避免实现者再次回到该争议。

### 2.3 `[project]` 元数据与「不发布 PyPI」表述不严谨（🟡 应改）

- `pyproject.toml` 已含 `keywords`、`classifiers`、`authors` 等典型 PyPI 元数据。
- `01` 的验收标准「项目没有 PyPI 发布配置或发布流程」字面与现状不符。建议改为「不增加 `publish`/`twine` 流程，元数据保留」。

### 2.4 `serve` 的 `site_dir` 语义与 MkDocs 实际行为不符（🟡 应改）

- `06-serve-preview.md` 步骤 2「将 `site_dir` 指向 `<output>/html`」。
- `mkdocs serve` 默认内存渲染，不会向 `site_dir` 写盘；该字段对 serve 几乎无效，反而易让人误以为预览会污染输出。
- 建议改为「serve 复用同一配置解析，`site_dir` 仅作配置一致性占位，预览内容不落盘」。

### 2.5 `mkdocs-with-pdf` 输出文件名未配置（🟡 应改）

- `04-pdf-build.md` 仅写「PDF 文件路径 `<output>/pdf/docs.pdf`」。
- `mkdocs-with-pdf` 默认输出 `pdf/document.pdf`，需显式设置 `output_path: docs.pdf` 或在构建后重命名。
- 建议在「实现步骤」中明确「插件 `output_path` 配置为 `docs.pdf`」。

### 2.6 `exclude_docs` 合并策略未澄清（🟡 必改）

- 当前 `mkdocs.yml` 使用 MkDocs 1.6 的 gitignore 风格 `exclude_docs: |\n  /summary.md`。
- `02-source-config-resolution.md` 步骤 5「覆盖 `exclude_docs`」未说明合并/追加/替换策略，可能误删用户排除规则。
- 建议明确「在用户已有 `exclude_docs` 上追加 `/summary.md` 与临时导航文件」。

### 2.7 用户文档复用策略不清（🟡 应改）

- `11-user-documentation.md` 计划写入 `docs/getting_started/`、`docs/build_and_deployment/`、`docs/troubleshooting/`。
- 这三个目录现存自动生成示例（描述「被构建的软件」而非 `docsbuildtool` 本身）。
- 计划未说明是「覆盖示例」「另起子目录」还是「保留示例并新增 CLI 用户指南」。建议补一条决策。

### 2.8 PDF 跨平台 smoke test 立场矛盾（🟡 应改）

- `04` 测试用例要求「Windows/macOS/Linux 至少执行轻量 PDF smoke test」。
- `09` 风险又指出「PDF 渲染跨平台依赖较复杂，可能需要单独标记集成测试」。
- 建议在 `04` 显式约定「Linux 必跑；Windows/macOS 标 `integration` 标签可选」。

## 3. 次要问题（可在实现时一并处理）

- **退出码不具体**：`01` 仅说「用户输入错误为非零」。建议固定一组语义（如 `0/1/2/3` ↔ 成功/构建失败/用户输入错误/依赖缺失）。
- **未提到 `rich`**：`rich` 已在主依赖，建议在 `01/03/04/05` 输出环节明确使用 `rich` 渲染产物路径与摘要。
- **未规划 `docs --version`**：常见 CLI 能力，建议补入 `01`。
- **未规划 `python -m docsbuildtool` 入口**：与裸命令并行的备用调用方式，可写入 `01` 或 `09`。
- **`--verbose/--debug` 控制 traceback 输出**：`01` 提到「调试模式」但未单独成项。
- **`docs build` strict 模式默认值未定**：`03` 风险部分点到但未决策。建议默认非 strict、CI 中 `mkdocs build --strict`。
- **`clean` 的「不安全系统路径」措辞**：`02` 与 `07` 略不一致；建议在 `07` 列举具体规则（不等于 `Path.home()`、不等于驱动器根、不在 `$env:WINDIR`/`/`、不在用户 HOME）。
- **`05` 部分成功的退出码**：写了「返回非零」但未区分 HTML/PDF 失败。
- **`08` 的「排除旧 archive 目录」**：风险中提到，但未进入实现步骤；建议把「生成 zip 时跳过 `<output>/archive`」加入步骤 5。
- **CI 矩阵**：当前 `.github/workflows/tests.yml`、`lint.yml` 仅 `ubuntu-latest`，`09/10` 已记录差距，但未挂里程碑。
- **`index.md` 测试用例**：未覆盖「`docs --help` 在 PowerShell/CMD/POSIX shell 均可识别」。

## 4. 一致性确认（✅ 通过）

- `index.md` 默认值表（源目录 `docs`、输出根 `site`、HTML→`site/html`、PDF→`site/pdf/docs.pdf`、归档→`site/archive/docs.zip`）在 `03/04/05/07/08` 全部一致。
- 输出目录三件套 `html/pdf/archive` 在 `05/07/08` 互相呼应。
- `docs/summary.md` 中「开发计划」分组顺序与文件名 01–12 一致。
- 全部 12 份功能文档均覆盖了 `index.md` 验收标准要求的七个章节。
- 拼写 `archive` vs `achive` 处理明确（`08` 验收标准 + `11` 测试用例双重保险）。
- `mkdocs-with-pdf` 已在 `doc-group`，无遗漏依赖。

## 5. 修订优先级建议

1. **必做**：2.1（`--output zip` 语义）、2.2（CLI 安装方案）、2.6（`exclude_docs` 合并）。
2. **建议做**：2.3、2.4、2.5、2.7、2.8。
3. **可在实现 PR 中顺手处理**：第 3 节全部条目。

## 6. 发现摘要表

| 日期 | 范围 | 发现 | 严重级别 | 状态 |
| --- | --- | --- | --- | --- |
| 2026-05-14 | `docs/plan/08-archive-zip.md`, `docs/plan/index.md` | `archive --output zip` 与全局 `--output <dir>` 语义冲突 | 高 | 待处理 |
| 2026-05-14 | `docs/plan/01-cli-entrypoint.md`, `pyproject.toml` | 裸 `docs` 命令安装路线与 `package-mode=false` 冲突未决 | 中 | 待处理 |
| 2026-05-14 | `docs/plan/02-source-config-resolution.md`, `mkdocs.yml` | `exclude_docs` 合并/追加/覆盖策略未澄清 | 中 | 待处理 |
| 2026-05-14 | `docs/plan/01-cli-entrypoint.md` | 「无 PyPI 发布配置」与现有 `[project]` 元数据矛盾 | 中 | 待处理 |
| 2026-05-14 | `docs/plan/06-serve-preview.md` | `mkdocs serve` 不写 `site_dir`，步骤描述误导 | 中 | 待处理 |
| 2026-05-14 | `docs/plan/04-pdf-build.md` | 未指明 `mkdocs-with-pdf` `output_path: docs.pdf` | 中 | 待处理 |
| 2026-05-14 | `docs/plan/11-user-documentation.md` | 与现存示例文档的复用/覆盖策略未定 | 中 | 待处理 |
| 2026-05-14 | `docs/plan/04-pdf-build.md`, `docs/plan/09-cross-platform-behavior.md` | PDF 跨平台 smoke test 立场前后矛盾 | 中 | 待处理 |
| 2026-05-14 | `docs/plan/*` | 退出码、`--version`、`-m` 入口、`--verbose`、strict 默认值、clean 安全路径细化等 | 低 | 待处理 |
