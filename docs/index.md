# docsbuildtool

`docsbuildtool` 是一个跨平台 CLI 工具，使用 MkDocs 生态将结构化 Markdown 文档构建为静态 HTML 和 PDF。

## 快速开始

```powershell
poetry install --with dev-group --no-root
pip install -e .
docs build
```

## CLI 命令

| 命令 | 说明 |
|------|------|
| `docs build` | 构建 HTML（默认），`--format pdf` 或 `--format all` |
| `docs serve` | 启动本地 MkDocs 预览服务器 |
| `docs clean` | 安全删除生成的构建文件 |
| `docs archive --format zip` | 将构建输出打包为 ZIP |

## 当前状态

项目已实现 12 个开发阶段：

- **Phase 01**: Typer 命令行入口
- **Phase 02**: 源目录解析与 MkDocs 配置生成
- **Phase 03**: HTML 构建
- **Phase 04**: PDF 构建（mkdocs-with-pdf）
- **Phase 05**: 全量构建与输出布局
- **Phase 06**: 本地预览服务器
- **Phase 07**: 安全清理
- **Phase 08**: ZIP 归档
- **Phase 09**: 跨平台行为统一
- **Phase 10**: 测试套件与 CI（35 个测试）
- **Phase 11**: 用户文档
- **Phase 12**: 审查与治理

## 项目信息

- 项目名：`docsbuildtool`
- 源码目录：`src/docsbuildtool/`
- 测试目录：`tests/`
- Poetry 模式：非打包（仅依赖管理）
- 开发状态：Pre-Alpha
