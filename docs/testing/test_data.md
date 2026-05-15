# 测试数据

<!-- BEGIN: auto-generated -->

## 测试 fixtures 目录

```
tests/fixtures/
└── minimal-docs/
    ├── index.md      # 最小首页内容（"# Home"）
    └── summary.md    # 导航定义（"* [Home](index.md)"）
```

`minimal-docs/` 提供最简 Markdown 文档树，用于测试配置解析和构建流程。测试中将其复制到 `tmp_path` 后作为 `--source` 参数传入。

## 测试数据生成方式

| 方式 | 说明 | 使用场景 |
| --- | --- | --- |
| `tmp_path` fixture | pytest 内置，自动创建临时目录，测试结束后自动删除。 | 绝大部分测试（构建输出、清理目标、归档路径）。 |
| `minimal-docs/` fixtures | 位于 `tests/fixtures/` 的静态测试数据。 | 需要真实 Markdown 文件的配置解析与构建测试。 |
| 内联数据 | 在测试函数中直接构造字符串或配置对象。 | 路径保护、退出码枚举等纯逻辑测试。 |

## 测试输出隔离

所有构建、清理和归档测试均在 `tmp_path` 隔离环境中运行，不修改项目 `docs/` 源目录和 `site/` 输出目录。测试使用 `mkdocs.yml` 的临时副本，确保不与项目真实配置冲突。

<!-- END: auto-generated -->
