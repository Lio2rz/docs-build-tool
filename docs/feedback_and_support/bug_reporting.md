# 错误报告

<!-- BEGIN: auto-generated -->

## 收集诊断信息

报告 bug 前请收集：

```powershell
python --version
poetry --version
poetry run docs --version
poetry run pip list | grep -E "mkdocs|typer|rich|yaml"
```

## 需要提供的信息

- Python 和 Poetry 版本
- 执行的完整命令（含参数）
- 输入 Markdown 目录结构（`tree docs/`）
- 期望输出与实际输出
- 完整错误消息和 traceback（使用 `--debug` 标志）
- 是否能通过最小示例复现

## 提交渠道

通过 GitHub Issues 提交（参见 [支持渠道](support_channels.md)）。

## Phase 12 审查流程中的 Bug 处理

在 Phase 12 治理框架中，每个阶段的 bug 按：发现 -> 修复 -> 安全审计 -> 回归测试 流程处理。

<!-- END: auto-generated -->
