# 代码审查流程

<!-- BEGIN: auto-generated -->

## 合并流程

每种分支类型有定义的合并来源和目标：

| 分支类型 | 分支来源 | 合并目标 | 说明 |
|----------|---------|---------|------|
| `init/project-scaffold` | `main` | `develop/main` | 项目初始化 |
| `develop/main` | `init/project-scaffold` 或 `main` | `release/RC-*` | 主开发线 |
| `develop/feature/*` | `develop/main` | `develop/main` | 功能分支 |
| `develop/debug/*` | `develop/main` | `develop/main` | 调试分支 |
| `develop/refactor/*` | `develop/main` | `develop/main` | 重构分支 |
| `develop/test/*` | `develop/main` | `develop/main` | 测试分支 |
| `develop/docs/*` | `develop/main` | `develop/main` | 文档分支 |
| `develop/fix/*` | `develop/main` | `develop/main` | Bug 修复分支 |
| `develop/audit/*` | `develop/main` | `develop/main` | 安全审计分支 |
| `release/RC-*` | `develop/main` | `release/vX.Y.Z` + `main` | 发布候选 |
| `release/vX.Y.Z` | `release/RC-*`（或 `main`） | `main` | 正式发布 |
| `hotfix/*` | `main` | `main` **和** `develop/main` | 紧急修复 |

> **关键规则**：hotfix 必须双合并到 `main` 和 `develop/main`，避免修复被下一发布周期丢弃。

## CI 工作流

项目已配置 GitHub Actions CI（`.github/workflows/`）：

| 工作流 | 触发条件 | 检查项 |
|--------|---------|--------|
| `lint.yml` | push + pull_request | `poetry check --lock`, `black --check`, `isort --check-only`, `ruff check`, `mypy`, `mkdocs build --strict` |
| `tests.yml` | push + pull_request | `poetry install --with test-group --no-root`, `poetry run pytest`（35 个测试） |

## Phase 12 治理框架

Phase 12 引入了完整的治理框架，包括：

- **PR 模板**：标准化的 Pull Request 描述格式
- **审查检查清单**：覆盖安全性、测试覆盖、文档更新
- **每阶段审计流程**：每个开发阶段包含修复审查、安全审计、文档审查三步骤

## 审查检查清单

提交 PR 前确认以下项目：

1. 变更符合 `AGENTS.md` 和 `.agents/` 中的项目规则
2. 输入/输出路径可配置，使用 `pathlib` 而非 `os.path`
3. 未修改源 Markdown 文件（正常构建操作中）
4. 遵循分支命名规范（`<prefix>/<TAG>-<NNNNNN>-<yyyyMMdd>-<description>`）
5. 提交遵循 Conventional Commits 格式
6. 通过所有代码质量检查：
   ```powershell
   poetry run black --check .
   poetry run isort --check-only .
   poetry run ruff check .
   poetry run mypy src/
   poetry run mkdocs build --strict
   ```
7. 测试通过：`poetry run pytest`（35 passing）
8. 相关开发文档已更新

## PR 生命周期

1. 从正确的基础分支切出功能分支
2. 遵循 Conventional Commits 提交
3. 推送并创建 Pull Request
4. 通过 CI 检查（lint + tests）
5. 代码审查通过后合并到目标分支
6. 删除已合并的功能分支（本地和远程）

<!-- END: auto-generated -->
