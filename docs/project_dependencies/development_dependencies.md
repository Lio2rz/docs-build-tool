# 开发依赖

<!-- BEGIN: auto-generated -->

## `dev-group`

`dev-group` 是本项目推荐的本地开发依赖组，包含文档构建、测试和 lint 工具。

| 包或包含项 | 用途 |
| --- | --- |
| `{include-group = "doc-group"}` | 引入文档构建依赖。 |
| `{include-group = "test-group"}` | 引入测试依赖。 |
| `black` | Python 代码格式检查和格式化。 |
| `isort` | Python import 排序检查和格式化。 |
| `mypy` | Python 静态类型检查。 |
| `ruff` | 代码检查和导入排序检查。 |

安装命令：

```powershell
poetry install --with dev-group
```

常用验证命令：

```powershell
poetry run black --check .
poetry run isort --check-only .
poetry run ruff check .
poetry run mypy
```

<!-- END: auto-generated -->
