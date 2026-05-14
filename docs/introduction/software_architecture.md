# 软件架构概览

<!-- BEGIN: auto-generated -->

当前项目仍处于骨架阶段，仓库中只有包入口文件和配置文件。根据 `AGENTS.md` 与 `.agents/project.md` 的约束，推荐架构应分为 CLI 编排、文档发现、MkDocs 配置生成、HTML 构建和 PDF 构建几个职责区。

## 当前仓库结构

```text
docsbuildtool/
├── src/docsbuildtool/
│   └── __init__.py
├── tests/
│   └── __init__.py
├── pyproject.toml
├── poetry.lock
├── AGENTS.md
└── .agents/
```

## 预期数据流

```text
Markdown 输入目录
    |
    v
目录扫描与导航生成
    |
    v
MkDocs 配置生成或读取
    |
    +--> MkDocs HTML 构建 --> 静态 HTML 输出目录
    |
    +--> PDF 插件或渲染器 --> PDF 输出文件
```

## 分层建议

- CLI 层：解析命令参数，处理终端输出和退出码。
- 应用层：编排 HTML/PDF 构建流程。
- 配置层：生成或加载 `mkdocs.yml`。
- 文件系统层：使用 `pathlib.Path` 处理输入、输出和资源路径。
- 渲染适配层：封装 MkDocs 和 PDF 渲染实现，避免业务逻辑直接绑定具体插件。

<!-- END: auto-generated -->
