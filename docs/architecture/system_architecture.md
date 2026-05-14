# 系统架构

<!-- BEGIN: auto-generated -->

## 当前状态

当前源码只有 `src/docsbuildtool/__init__.py`，尚未形成实际模块依赖。根据项目目标，系统应围绕“输入 Markdown 目录 -> 构建配置 -> HTML/PDF 输出”的流水线组织。

## 推荐架构

```text
CLI
 |
 v
Build Service
 |--------- Markdown Source Scanner
 |--------- MkDocs Config Builder
 |--------- HTML Builder Adapter
 |--------- PDF Builder Adapter
 |
 v
Output Artifacts
```

## 层职责

| 层 | 职责 | 说明 |
| --- | --- | --- |
| CLI 层 | 参数解析、错误展示、命令退出码 | 可使用 `typer` 实现。 |
| 应用服务层 | 组织 HTML/PDF 构建流程 | 不直接处理终端展示细节。 |
| 文档发现层 | 扫描 Markdown 文件和资源 | 应支持稳定排序和严格模式。 |
| 配置生成层 | 生成确定性的 MkDocs 配置 | 输出可复现，便于测试。 |
| 构建适配层 | 调用 MkDocs 或 PDF 渲染器 | 隔离第三方工具差异。 |

<!-- TODO: 实现源码模块后，补充真实模块图和调用关系。 -->

<!-- END: auto-generated -->
