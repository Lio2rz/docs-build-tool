# 开发计划：跨平台 CLI 入口

<!-- BEGIN: auto-generated -->

## 目标

实现跨平台 `docs` 命令，作为所有文档构建操作的统一入口。CLI 使用 Typer，支持 Windows、macOS、Linux。

## 接口/行为

命令：

```powershell
docs --help
docs build
docs serve
docs clean
docs archive
```

要求：

- `docs --help` 显示全局帮助、子命令和简短描述。
- CLI 退出码稳定：成功为 `0`，用户输入错误为非零，构建失败为非零。
- 错误信息使用用户可读文本，不输出未处理 traceback，除非开启调试模式。
- 为支持裸 `docs` 命令，后续实现需要恢复本地可安装 console script；项目仍不上传 PyPI。

## 实现步骤

1. 新增 `docsbuildtool.cli` 模块，定义 Typer app。
2. 在 CLI 中注册 `build`、`serve`、`clean`、`archive` 子命令。
3. 建立统一异常处理，将内部异常映射为退出码和错误消息。
4. 在 `pyproject.toml` 中恢复本地 CLI 安装入口，例如 `docs = "docsbuildtool.cli:app"`。
5. 调整 Poetry 配置，使本地开发安装可暴露 console script，但不增加发布配置或上传流程。
6. 更新 README 和 CLI 使用文档。

## 影响范围

- `pyproject.toml`：需要增加 scripts 入口并支持本地安装。
- `src/docsbuildtool/`：新增 CLI 模块和错误类型。
- `.github/workflows/`：CI 需要验证 `docs --help`。
- 文档：需要说明裸 `docs` 命令的本地安装方式。

## 测试用例

- 调用 `docs --help`，断言包含 `build`、`serve`、`clean`、`archive`。
- 调用未知命令，断言退出码非零且提示可读。
- 调用 `docs build --help`，断言包含 `--format`、`--source`、`--output`。
- 在 Windows、macOS、Linux CI 中执行 `docs --help`。
- 模拟内部异常，断言 CLI 返回非零并展示简短错误。

## 验收标准

- 在三类操作系统中，`docs --help` 均可直接执行。
- 所有子命令出现在帮助信息中。
- CLI 命令不依赖 shell 专有语法。
- 项目没有 PyPI 发布配置或发布流程。

## 风险与注意事项

- 当前项目设置为 `package-mode = false`，裸命令需要重新设计本地安装方式。
- `docs` 名称较通用，可能与用户系统已有命令冲突；文档需说明如何确认命令来源。
- Typer/Click 在不同 shell 下对路径引号的表现可能不同，测试需覆盖含空格路径。

<!-- END: auto-generated -->
