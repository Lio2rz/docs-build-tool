# 开发依赖

<!-- BEGIN: auto-generated -->

## `dev-group`

`dev-group` 是本项目推荐的本地开发依赖组，包含文档构建、测试和所有 lint 工具。

| 包或包含项 | 类型 | 用途 |
| --- | --- | --- |
| `{include-group = "doc-group"}` | 组引用 | 引入全部文档构建依赖（8 个包）。 |
| `{include-group = "test-group"}` | 组引用 | 引入 pytest + pytest-cov。 |
| `black` | 直接依赖（>=26.0,<27.0） | Python 代码格式化，配置 line-length=120, target-version=py313。 |
| `isort` | 直接依赖（>=8.0,<9.0） | Python import 排序，profile=black, line_length=120。 |
| `mypy` | 直接依赖（>=2.1.0,<3.0） | 静态类型检查，disallow_untyped_defs=true, check_untyped_defs=true, no_implicit_optional=true。 |
| `ruff` | 直接依赖（>=0.9,<1.0） | 代码检查与自动修复，select=B/E/F/I/UP, line-length=120, target-version=py313。 |

安装命令：

```bash
poetry install --with dev-group --no-root
```

## 常用验证命令

```bash
poetry check --lock           # 验证 pyproject.toml 与锁文件一致性
poetry run black --check .    # 检查代码格式
poetry run isort --check-only .  # 检查 import 排序
poetry run ruff check .       # 运行 lint 检查
poetry run ruff check --fix . # 自动修复可修复的 lint 问题
poetry run mypy               # 运行静态类型检查
```

<!-- END: auto-generated -->
