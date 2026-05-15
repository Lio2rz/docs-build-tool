# CI/CD

<!-- BEGIN: auto-generated -->

项目配置了 2 个 GitHub Actions 工作流，均在 push 和 pull_request 事件触发。

## 工作流 1：Lint（`.github/workflows/lint.yml`）

| 步骤 | 操作 | 说明 |
| --- | --- | --- |
| 1 | `actions/checkout@v4` | 检出仓库代码。 |
| 2 | `actions/setup-python@v5` | 安装 Python 3.13。 |
| 3 | `pipx install poetry` | 安装 Poetry 包管理器。 |
| 4 | `poetry install --with dev-group --no-root` | 安装全部开发依赖（含 doc-group、test-group、lint 工具）。 |
| 5 | `poetry check --lock` | 验证 `pyproject.toml` 与 `poetry.lock` 一致性。 |
| 6 | `poetry run black --check .` | 检查代码格式是否符合 Black 规范。 |
| 7 | `poetry run isort --check-only .` | 检查 import 排序是否符合 isort 规范。 |
| 8 | `poetry run ruff check .` | 运行 Ruff 代码检查（B/E/F/I/UP 规则）。 |
| 9 | `poetry run mypy` | 运行 mypy 静态类型检查。 |
| 10 | `poetry run mkdocs build --strict` | 构建 MkDocs 站点（严格模式，警告即失败）。 |

运行环境：`ubuntu-latest`，Python 3.13。

## 工作流 2：Tests（`.github/workflows/tests.yml`）

| 步骤 | 操作 | 说明 |
| --- | --- | --- |
| 1 | `actions/checkout@v4` | 检出仓库代码。 |
| 2 | `actions/setup-python@v5` | 安装 Python 3.13。 |
| 3 | `pipx install poetry` | 安装 Poetry 包管理器。 |
| 4 | `poetry install --with test-group --no-root` | 安装测试依赖（pytest + pytest-cov）。 |
| 5 | `poetry run pytest` | 运行全部 35 个测试用例。 |

运行环境：`ubuntu-latest`，Python 3.13。

## 触发条件

两个工作流均在 `push` 和 `pull_request` 事件时自动触发，覆盖所有分支。代码检查与测试独立运行，互不阻塞。

<!-- END: auto-generated -->
