# 编码标准

<!-- BEGIN: auto-generated -->

## Python 标准

- 目标 Python 版本为 `py313`。
- 使用 `pathlib.Path` 处理路径。
- 避免硬编码平台路径分隔符。
- 构建逻辑和 CLI 展示逻辑分离。
- 行宽遵循 `.editorconfig`、Black、isort 和 Ruff 的统一配置：120。

## 格式化和类型检查工具

| 工具 | 用途 | 关键配置 |
| --- | --- | --- |
| Black | Python 格式化 | `line-length = 120`，`target-version = ["py313"]` |
| isort | import 排序 | `profile = "black"`，`line_length = 120` |
| mypy | 静态类型检查 | Python 3.13，检查 `src` 和 `tests` |
| Ruff | lint | `line-length = 120`，`target-version = "py313"` |

## Ruff 规则

当前启用：

- `B`：flake8-bugbear
- `E`：pycodestyle errors
- `F`：Pyflakes
- `I`：导入排序
- `UP`：pyupgrade

## 命名建议

- 模块名使用小写加下划线。
- 函数和变量使用 `snake_case`。
- 类名使用 `PascalCase`。
- 常量使用 `UPPER_SNAKE_CASE`。

<!-- END: auto-generated -->
