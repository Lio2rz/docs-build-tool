# 版本控制

<!-- BEGIN: auto-generated -->

项目使用 Git 进行版本控制，共 67 次提交。遵循结构化的分支命名规范和 Conventional Commits。

## 当前分支

| 分支 | 类型 | 说明 |
|------|------|------|
| `main` | 特殊分支 | 生产稳定分支 |
| `develop/main` | 特殊分支 | 主开发线（当前 `dev/mian`） |
| `init/project-scaffold` | 特殊分支 | 项目初始化（已完成合并） |
| `dev/docs/DOC-000001-20260515-rebuild-all-docs` | 文档分支 | 文档重建工作分支 |

## 分支命名格式

所有带计数器的分支遵循统一格式：

```
<prefix>/<TAG>-<NNNNNN>-<yyyyMMdd>-<short-description>
```

- `<prefix>` — 分支类别路径（如 `develop/feature/`）
- `<TAG>` — 类型缩写（PROJ、DBG、REF、TST、DOC、FIX、SEC、HOT、RC）
- `<NNNNNN>` — 6 位零填充序号，**每个类别独立计数**，从 `000001` 开始
- `<yyyyMMdd>` — 创建日期
- `<short-description>` — kebab-case 简短描述（2-5 词）

每个分支类型有独立计数器，例如第 1 个 feature 为 `PROJ-000001`，第 1 个 hotfix 为 `HOT-000001`。

## 子文档

- [分支策略](branching_strategy.md) — 完整分支类型、命名规范与合并流程
- [提交规范](commit_conventions.md) — Conventional Commits 规范
- [代码审查流程](code_review_process.md) — CI 工作流与审查清单

<!-- END: auto-generated -->
