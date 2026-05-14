# 开发计划总览

<!-- BEGIN: auto-generated -->

## 目标

为 `docsbuildtool` 后续功能开发建立可执行的文档化计划。计划只描述实现方案，不在本阶段实现功能代码。

本计划围绕以下能力拆分：

- 跨平台 `docs` 命令行入口。
- Markdown 源目录解析与 MkDocs 配置生成。
- HTML、PDF、all 三种构建模式。
- 本地预览、清理、归档。
- 跨平台行为、测试、CI、用户文档、代码审查和进度治理。

## 接口/行为

计划覆盖的最终 CLI 接口：

```powershell
docs --help
docs build
docs build --format html
docs build --format pdf
docs build --format all
docs build --output <directory>
docs build --source <directory>
docs serve
docs clean
docs archive --format zip
docs archive --format zip --output <directory>
```

默认值：

| 项 | 默认值 |
| --- | --- |
| 源目录 | `docs` |
| 输出根目录 | `site` |
| `docs build` 默认格式 | `html` |
| HTML 输出 | `<output>/html` |
| PDF 输出 | `<output>/pdf/docs.pdf` |
| 归档输出 | `<output>/archive/docs.zip` |
| `docs archive` 默认格式 | `zip` |

## 实现步骤

1. 先实现 CLI 入口和参数解析，锁定用户接口。
2. 实现源目录与 MkDocs 配置解析，作为所有命令的共享基础。
3. 依次实现 HTML 构建、PDF 构建、all 构建。
4. 实现 serve、clean、archive 三个操作命令。
5. 补齐跨平台路径和子进程行为。
6. 完成测试、CI、用户文档和代码审查流程。
7. 按本目录文档持续更新进度和风险。

## 影响范围

- `src/docsbuildtool/`：新增 CLI、构建服务、配置解析、归档和清理逻辑。
- `tests/`：新增 CLI、单元、集成和跨平台行为测试。
- `.github/workflows/`：扩展测试矩阵和文档构建质量门禁。
- `docs/`：新增命令使用说明、示例和功能开发记录。
- `pyproject.toml`：后续实现裸 `docs` 命令时，需要恢复本地可安装 CLI 入口；仍不增加 PyPI 发布流程。

## 测试用例

- `docs --help` 能显示所有子命令和核心选项。
- `docs build` 默认生成 HTML。
- `docs build --format html/pdf/all` 分别生成预期产物。
- `docs serve` 可启动 MkDocs 预览流程，测试中使用 mock 避免阻塞。
- `docs clean` 只清理 CLI 管理的输出目录。
- `docs archive --format zip` 生成可解压 zip。
- Windows、macOS、Linux CI 至少覆盖 Python 3.13。
- `docs --help` 在 PowerShell、CMD、POSIX shell 均可识别。

## 验收标准

- 每个功能文档均包含目标、接口/行为、实现步骤、影响范围、测试用例、验收标准和风险。
- `docs/summary.md` 包含“开发计划”导航，并能通过 `poetry run mkdocs build --strict`。
- 后续开发可以按文档顺序分支实施，不需要重新决定 CLI 语义。

## 风险与注意事项

- 裸 `docs` 命令与当前 `package-mode = false` 存在实现冲突，后续功能实现需切换 `package-mode = true` 并通过 `[project.scripts]` 暴露 console script；保留 `[project]` 元数据，但不引入 `publish`/`twine` 等上传流程。
- PDF 构建依赖 `mkdocs-with-pdf` 和底层渲染依赖，跨平台失败率高于 HTML。
- `clean` 是潜在破坏性命令，必须先实现严格路径保护。

<!-- END: auto-generated -->
