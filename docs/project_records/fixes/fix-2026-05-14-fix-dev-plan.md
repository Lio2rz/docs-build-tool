# 修复报告：开发计划审计

- 日期：2026-05-14
- 审计报告：`docs/project_records/audits/audit-report-2026-05-14-plan-audit.md`
- 审计范围：`docs/plan/index.md` 与 `docs/plan/01-cli-entrypoint.md` ~ `docs/plan/12-review-progress-governance.md`
- 审计结果：共发现 20+ 项问题；经两轮修复全部处理完毕。

## 第一轮修复（首次审计后）

来源：审计报告第 2、3 节

| 审计项 | 严重级别 | 修复内容 | 涉及文件 | 状态 |
| --- | --- | --- | --- | --- |
| 2.1 `archive --output zip` 语义冲突 | 高 | `--output zip`（格式）改为 `--format zip`；`--output` 统一为目录 | `08-archive-zip.md`, `index.md` | 已修复 |
| 2.2 CLI 安装路线未定 | 中 | 新增"实施决策"段落：`package-mode = true` + `[project.scripts]` + `__main__.py` | `01-cli-entrypoint.md` | 已修复 |
| 2.3 PyPI 元数据表述不严谨 | 中 | 验收标准改为"不引入 publish/twine 流程，保留 [project] 元数据" | `01-cli-entrypoint.md`, `index.md` | 已修复 |
| 2.4 `serve` site_dir 语义误导 | 中 | 步骤中注明 `site_dir` 仅作配置一致性占位，预览不落盘 | `06-serve-preview.md` | 已修复 |
| 2.5 PDF output_path 未配置 | 中 | 实现步骤明确设置 `output_path: docs.pdf` | `04-pdf-build.md` | 已修复 |
| 2.6 `exclude_docs` 合并策略不清 | 中 | 明确为**追加**策略，不覆盖用户原值 | `02-source-config-resolution.md` | 已修复 |
| 2.7 用户文档复用策略不清 | 中 | 新增"实施决策"：保留示例，以新增页形式挂入 CLI 文档 | `11-user-documentation.md` | 已修复 |
| 2.8 PDF 跨平台 smoke test 矛盾 | 中 | 约定 Linux 必跑，Windows/macOS 标记 `integration` 可选 | `04-pdf-build.md` | 已修复 |
| 3.1 退出码不具体 | 低 | 定义 0/1/2/3 退出码语义 | `01-cli-entrypoint.md` | 已修复 |
| 3.2 未提到 `rich` | 低 | 在 `01` 和 `08` 输出环节明确使用 `rich` | `01-cli-entrypoint.md`, `08-archive-zip.md` | 已修复 |
| 3.3 未规划 `--version` | 低 | 增加 `--version` 选项与测试用例 | `01-cli-entrypoint.md` | 已修复 |
| 3.4 未规划 `-m` 入口 | 低 | 增加 `__main__.py` + `python -m docsbuildtool` 支持 | `01-cli-entrypoint.md` | 已修复 |
| 3.5 `--verbose/--debug` 未单独成项 | 低 | 在接口/行为与实现步骤中增加全局开关说明 | `01-cli-entrypoint.md` | 已修复 |
| 3.9 `08` 排除旧 archive | 低 | 已进入实现步骤 5 | `08-archive-zip.md` | 已修复 |
| 3.10 CI 矩阵未挂里程碑 | 低 | 跨平台文档中已记录差距 | `09-cross-platform-behavior.md`, `10-tests-ci-quality.md` | 已记录 |

遗留至第二轮：

| 审计项 | 原因 |
| --- | --- |
| 3.6 strict 默认值未定 | 风险部分点到但未决策 |
| 3.7 clean 不安全路径措辞 | `02` 与 `07` 措辞模糊且不一致 |
| 3.8 `05` 部分成功退出码 | 仅说"返回非零"，未区分 HTML/PDF 失败 |
| 3.11 `index.md` 测试用例未覆盖 shell | 缺少 PowerShell/CMD/POSIX 兼容测试 |
| 3.2 延伸 `03/04/05` 未提 `rich` | `01` 和 `08` 已补，其余遗漏 |

## 第二轮修复（二次审计补充）

来源：对 `docs/plan` 的二次审查，以及首次审计遗留项

| 审计项 | 严重级别 | 修复内容 | 涉及文件 | 状态 |
| --- | --- | --- | --- | --- |
| 旧语法残留 `--output zip` (05) | 高 | `docs archive --output zip` → `docs archive --format zip` | `05-build-all-output-layout.md` | 已修复 |
| 旧语法残留 `--output zip` (11) | 高 | `docs archive --output zip` → `docs archive --format zip` | `11-user-documentation.md` | 已修复 |
| 旧语法残留 `--output zip` (08 目标) | 高 | `docs archive --output zip` → `docs archive --format zip` | `08-archive-zip.md` | 已修复 |
| strict 模式默认值未定 (3.6) | 中 | 默认非 strict，CI 中 `mkdocs build --strict` | `03-html-build.md` | 已修复 |
| `05` 部分成功退出码未区分 (3.8) | 中 | PDF 失败时退出码 `1`，终端标注"部分成功" | `05-build-all-output-layout.md` | 已修复 |
| `02` 不安全路径措辞 (3.7) | 中 | 替换为具体路径列表（Path.home()、磁盘根、WINDIR、/） | `02-source-config-resolution.md` | 已修复 |
| `07` 不安全路径措辞 (3.7) | 中 | 补充 Path.home() 与系统路径检查 | `07-clean-generated-files.md` | 已修复 |
| `03/04/05` 未提 `rich` (3.2 延伸) | 低 | 在输出步骤中增加 `rich` 渲染说明 | `03-html-build.md`, `04-pdf-build.md`, `05-build-all-output-layout.md` | 已修复 |
| `08` 风险段和/或不一致 | 低 | "html 和 pdf" → "html 或 pdf" | `08-archive-zip.md` | 已修复 |
| `index.md` 测试用例未覆盖 shell (3.11) | 低 | 增加 PowerShell/CMD/POSIX shell 兼容测试项 | `index.md` | 已修复 |

## 验证

- `grep` 确认 `docs/plan` 目录下无残留 `--output zip` 语法
- `poetry run mkdocs build --strict` 构建通过
- 涉及文件共计 10 个（`index.md`, `01` ~ `08`, `11`）

## 结论

`docs/plan` 开发计划文档已通过两轮审计修复，当前处于一致状态，可进入开发实施阶段。
