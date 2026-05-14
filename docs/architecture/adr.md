# 架构决策记录

<!-- BEGIN: auto-generated -->

## 已识别决策

| 日期 | 决策 | 来源 | 状态 |
| --- | --- | --- | --- |
| 2026-05-14 | 使用 `AGENTS.md` 和 `.agents/` 作为 agent 指令根目录 | Git 提交 `db634a8`、`c8791c0` 和相关文件 | 已采用 |
| 2026-05-14 | 使用 Poetry 和 `src/` 布局初始化 Python 包 | Git 提交 `2545f5c`、`pyproject.toml` | 已采用 |
| 2026-05-14 | 依赖按 `dev-group`、`doc-group`、`test-group` 分组 | Git 提交 `5afde33`、`pyproject.toml` | 已采用 |
| 2026-05-14 | 使用 MkDocs 生态生成 HTML，PDF 通过插件或适配器支持 | `AGENTS.md`、`.agents/project.md` | 已采用 |

## ADR 模板

<!-- TODO: 后续新增重要架构变更时，将模板复制为独立 ADR 条目。 -->

```markdown
## ADR-YYYYMMDD-标题

- 日期：
- 状态：提议中 / 已采用 / 已废弃
- 背景：
- 决策：
- 影响：
- 替代方案：
```

<!-- END: auto-generated -->
