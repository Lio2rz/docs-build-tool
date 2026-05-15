# 代码审查指南

<!-- BEGIN: auto-generated -->

## Phase 12 审查检查清单

Phase 12（治理框架）建立了标准化审查流程，每项变更需经过：

1. **安全检查** — 路径保护（`_is_path_protected`），subprocess 使用 list 参数（非 shell 字符串），YAML safe_load
2. **测试验证** — `poetry run pytest` 全部通过（当前 35 个测试）
3. **类型检查** — `poetry run mypy src/` 零错误
4. **代码风格** — `poetry run ruff check .` 零告警，Black/isort 自动格式化
5. **文档更新** — 相关 docs/ 文件同步更新

## 审查重点

- 路径处理是否使用 `pathlib`，是否跨平台安全
- 构建流程是否可测试（优先临时目录）
- 第三方工具调用是否通过 subprocess（list 参数，禁止 `shell=True`）
- 错误消息是否对用户可理解（使用 `DocsError` 层级）
- 是否避免修改源 Markdown 文件
- 是否避免提交生成产物（HTML/PDF/archive）
- YAML 操作是否使用 `safe_load`/`safe_dump`

## 治理框架工作流

PR 提交 -> CI（lint + tests）-> 安全审查 -> 修复（如有）-> 二次审查 -> 合并

<!-- END: auto-generated -->
