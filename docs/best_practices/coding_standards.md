# 编码标准

<!-- BEGIN: auto-generated -->

## Python 标准

- 目标 Python 版本 >= 3.13（`pyproject.toml` 中 `requires-python = ">=3.13"`）
- 统一使用 `pathlib.Path` 处理所有文件系统操作（禁止 `os.path`）
- 避免硬编码平台路径分隔符
- 构建逻辑与 CLI 展示逻辑分离
- 行宽统一为 120 字符

## 格式化和类型检查工具

| 工具 | 用途 | 关键配置 |
| --- | --- | --- |
| Black | Python 格式化 | `line-length = 120`，`target-version = ["py313"]` |
| isort | import 排序 | `profile = "black"`，`line_length = 120`，`src_paths = ["src", "tests"]` |
| mypy | 静态类型检查 | `python_version = "3.13"`，`disallow_untyped_defs = true`，`check_untyped_defs = true` |
| Ruff | lint | `line-length = 120`，`target-version = "py313"` |

mypy 启用了接近 strict 模式的规则：`disallow_untyped_defs`、`check_untyped_defs`、`warn_unused_configs`、`no_implicit_optional`。

## Ruff 规则

当前启用（`pyproject.toml` `[tool.ruff.lint]` select）：

- `B` — flake8-bugbear
- `E` — pycodestyle errors
- `F` — Pyflakes
- `I` — isort（导入排序）
- `UP` — pyupgrade

## 命名规范

- 模块名：`snake_case`（如 `docsbuildtool`）
- 函数/变量：`snake_case`（如 `build_html`, `resolve_source`）
- 类名：`PascalCase`（如 `BuildFormat`, `DocsError`, `ResolvedConfig`）
- 常量：`UPPER_SNAKE_CASE`（如 `DEFAULT_SOURCE`, `OUTPUT_HTML`）
- 私有函数：`_` 前缀（如 `_is_path_protected`, `_generate_summary`）

<!-- END: auto-generated -->
