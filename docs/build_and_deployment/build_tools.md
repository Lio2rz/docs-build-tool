# 构建工具

<!-- BEGIN: auto-generated -->

## 构建与验证工具总览

| 工具 | 用途 | CLI 入口 / 使用方式 |
| --- | --- | --- |
| Poetry | 依赖管理、脚本入口注册 | `poetry install`、`poetry lock`、`poetry run` |
| MkDocs | 生成静态 HTML 文档站点 | `poetry run mkdocs build` / `mkdocs serve` |
| `mkdocs-material` | Material 主题（中文） | MkDocs 插件，通过 `mkdocs.yml` 配置 |
| `mkdocs-literate-nav` | 基于 summary.md 的导航 | MkDocs 插件，`nav_file: summary.md` |
| `mkdocs-section-index` | 章节索引页自动生成 | MkDocs 插件 |
| `mkdocs-with-pdf` | 从 MkDocs 站点生成 PDF | MkDocs 插件，`docs build --format pdf` 时启用 |
| Black | Python 代码格式化 | `poetry run black --check .` / `black .` |
| isort | Python import 排序 | `poetry run isort --check-only .` / `isort .` |
| mypy | 静态类型检查 | `poetry run mypy` |
| Ruff | 代码检查与自动修复 | `poetry run ruff check .` / `ruff check --fix .` |
| pytest | 测试运行器 | `poetry run pytest` |
| pytest-cov | 测试覆盖率 | `poetry run pytest --cov=docsbuildtool` |

## 常用命令

```bash
# 依赖管理
poetry check --lock                  # 验证锁文件一致性
poetry install --with dev-group --no-root  # 安装全部开发依赖

# 代码质量
poetry run black --check .           # 格式检查
poetry run isort --check-only .      # import 排序检查
poetry run ruff check .              # Lint 检查
poetry run ruff check --fix .        # 自动修复
poetry run mypy                      # 类型检查

# 测试
poetry run pytest                    # 运行全部测试
poetry run pytest --cov=docsbuildtool --cov-report=term-missing  # 带覆盖率

# 文档构建
poetry run mkdocs build --strict     # 构建 HTML（严格模式）
poetry run mkdocs serve              # 启动开发预览
```

<!-- END: auto-generated -->
