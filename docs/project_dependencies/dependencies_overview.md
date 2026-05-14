# 项目依赖

<!-- BEGIN: auto-generated -->

本章节说明项目依赖分组、运行依赖、文档构建依赖、测试依赖和依赖管理规则。

## 依赖分组

| 分组 | 用途 |
| --- | --- |
| `project.dependencies` | 项目脚本运行期基础依赖；当前项目不作为 Python 包发布。 |
| `doc-group` | 文档构建依赖，包括 MkDocs、主题和 PDF 支持。 |
| `test-group` | 测试和覆盖率依赖。 |
| `dev-group` | 开发环境聚合组，包含 `doc-group`、`test-group`、Black、isort、mypy 和 Ruff。 |

## 子文档

- [依赖列表](dependencies_list.md)
- [开发依赖](development_dependencies.md)
- [测试依赖](testing_dependencies.md)
- [依赖管理](dependency_management.md)

<!-- END: auto-generated -->
