# 文档指南

<!-- BEGIN: auto-generated -->

## 文档结构

- 开发文档放在 `docs/`，按功能域分子目录
- Agent 规则放在 `AGENTS.md`（入口）和 `.agents/`（详情）
- 面向用户的 README 链接到完整文档

## 自动生成标记

多数文档使用 `<!-- BEGIN: auto-generated -->` / `<!-- END: auto-generated -->` 标记区分自动生成区域与手写区域。更新文档时**仅替换标记之间的内容**，保留标记外的内容不变。

## 更新策略

- 阶段性更新：每个 Phase 完成后更新相关文档
- 全量重建：运行 `poetry run docs build` 生成最新 HTML 版本
- 增量修复：通过 `docs/audit/` 审计报告驱动针对性修复

## Markdown 约定

- 每个文档一个一级标题
- 使用相对链接引用同目录或邻近目录文件
- 命令示例使用 fenced code block，标注 `powershell`
- 表格用于依赖、配置、接口和错误码清单
- 未确认或待实现内容使用 `<!-- TODO: ... -->` 注释

## 文档工具链

- MkDocs 1.6.1 + Material 主题生成 HTML
- literate-nav + section-index 自动导航
- mkdocs-with-pdf 生成 PDF

<!-- END: auto-generated -->
