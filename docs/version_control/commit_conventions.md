# 提交规范

<!-- BEGIN: auto-generated -->

## Conventional Commits

项目遵循 [Conventional Commits](https://www.conventionalcommits.org/) 规范。

### 提交格式

```
<type>(<optional-scope>): <description>
```

- `type` — 变更类型（必填）
- `scope` — 受影响模块/组件/阶段（可选）
- `description` — 简短描述，一般现在时，小写

### 类型速查

| 类型 | 用途 | 示例 |
|------|------|------|
| `feat` | 新功能 | `feat(cli): add Typer-based CLI entrypoint` |
| `fix` | Bug 修复 | `fix(config): _merge_exclude_docs returns multi-line string` |
| `docs` | 文档变更 | `docs(phase-11): user documentation complete` |
| `style` | 格式化（无逻辑变更） | `style: apply black formatting` |
| `refactor` | 代码重构（无功能变更） | `refactor(db): extract connection pool to shared module` |
| `test` | 添加或更新测试 | `test(ci): test fixtures in place, CI workflows ready` |
| `chore` | 维护、依赖、构建任务 | `chore(governance): PR template established` |
| `perf` | 性能优化 | `perf(build): cache mkdocs config generation` |
| `security` | 安全相关 | `security(cross-platform): audit path usage` |
| `ci` | CI/CD 变更 | `ci: add GitHub Actions lint workflow` |
| `build` | 构建系统或外部依赖变更 | `build(deps): bump mkdocs to 1.6.1` |

### Scope 规则

- 使用模块、组件或功能区域作为 scope
- 若变更跨多个区域，考虑省略 scope 或拆分为多个提交
- 本项目常用 scope：`cli`, `config`, `builder`, `clean`, `archive`, `serve`, `errors`, `phase-NN`, `governance`, `cross-platform`

### 提交要求

- 每个提交聚焦单一可审查变更
- 描述使用一般现在时、小写、简洁
- 不跳过 pre-commit hook

## 近期提交示例（最新 5 条）

| Hash | 消息 |
|------|------|
| `6427237` | `update .gitignore` |
| `f79a218` | `docs: update README and project docs to reflect implemented CLI features` |
| `cdd2ea9` | `docs(phase-12): governance framework complete` |
| `1573ba3` | `fix(governance): no fixes required` |
| `f9e8315` | `security(governance): audit review process — no issues` |

<!-- END: auto-generated -->
