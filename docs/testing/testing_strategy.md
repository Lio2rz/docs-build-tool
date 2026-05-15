# 测试策略

<!-- BEGIN: auto-generated -->

## 目标

- 确保 CLI 命令入口正确：`--help`、`--version` 及子命令帮助输出准确。
- 确保配置解析确定性：`resolve_source()`、`resolve_output()` 默认值与覆盖行为稳定。
- 确保构建流程可靠：`mkdocs build` 子进程调用正确，HTML/PDF 输出可验证。
- 确保 PDF 失败非致命：PDF 构建失败不影响 HTML 构建结果（`build_all` 容错）。
- 确保清理与归档安全：路径保护机制防止误删关键目录。
- 确保子进程错误能正确映射到 ExitCode。

## 测试层次

| 层次 | 说明 | 对应文件 |
| --- | --- | --- |
| CLI 入口测试 | 使用 Typer `CliRunner` 测试命令解析、帮助输出、全局选项。 | `test_cli.py` |
| 单元测试 | 测试纯函数：配置解析、路径保护、MkDocs 配置生成、退出码枚举。 | `test_config.py`、部分 `test_cli.py` |
| 集成测试 | 使用 `tmp_path` fixture 在临时目录中构建最小文档结构，调用构建/清理/归档函数。 | `test_builder.py`、`test_clean.py`、`test_archive.py` |
| 元数据测试 | 验证包版本号与 `pyproject.toml` 一致。 | `test_package.py` |

## 测试方法

- **Typer CliRunner**：所有 CLI 命令测试通过 `CliRunner().invoke(app, args)` 执行，无需启动真实进程。
- **tmp_path fixture**：使用 pytest 内置的 `tmp_path` 创建隔离的临时文件系统，避免污染项目目录。
- **子进程 Mock**：构建测试中通过控制 `mkdocs` 子进程的可用性来模拟成功和失败场景。
- **路径保护验证**：测试覆盖对项目根目录、文件系统根目录、`$HOME`、`%WINDIR%` 的保护拒绝。

<!-- END: auto-generated -->
