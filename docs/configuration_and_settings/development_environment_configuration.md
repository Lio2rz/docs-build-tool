# 开发环境配置

<!-- BEGIN: auto-generated -->

## Poetry 依赖组

开发环境安装 `dev-group`，包含文档构建、测试及所有 lint 工具：

```bash
poetry install --with dev-group --no-root
```

`dev-group` 由以下组成：

| 组件 | 类型 | 包含内容 |
| --- | --- | --- |
| `doc-group` | include-group | markdown、mkdocs、mkdocs-material、mkdocs-literate-nav、mkdocs-section-index、mkdocs-with-pdf、pymdown-extensions、pyyaml |
| `test-group` | include-group | pytest（>=9.0.3）、pytest-cov（>=6.0） |
| `black` | 直接依赖 | 代码格式化（>=26.0,<27.0） |
| `isort` | 直接依赖 | import 排序（>=8.0,<9.0） |
| `mypy` | 直接依赖 | 静态类型检查（>=2.1.0,<3.0） |
| `ruff` | 直接依赖 | 代码检查（>=0.9,<1.0） |

## Lint 工具配置（均在 pyproject.toml 中）

| 工具 | 配置项 | 值 |
| --- | --- | --- |
| Black | `line-length` | 120 |
| Black | `target-version` | py313 |
| isort | `profile` | black |
| isort | `line_length` | 120 |
| isort | `src_paths` | src, tests |
| mypy | `python_version` | 3.13 |
| mypy | `files` | src, tests |
| mypy | `disallow_untyped_defs` | true |
| mypy | `check_untyped_defs` | true |
| mypy | `no_implicit_optional` | true |
| Ruff | `line-length` | 120 |
| Ruff | `target-version` | py313 |
| Ruff | `lint.select` | B, E, F, I, UP |

## 本地缓存

Poetry、pytest、mypy 和 Ruff 会在本地创建缓存目录（`.mypy_cache/`、`.ruff_cache/`、`.pytest_cache/`）。这些目录已在 `.gitignore` 中排除，属于开发环境产物，不应纳入版本控制。

<!-- END: auto-generated -->
