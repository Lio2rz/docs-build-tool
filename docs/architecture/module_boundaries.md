# 模块划分

<!-- BEGIN: auto-generated -->

## 当前模块

| 模块/路径 | 当前内容 | 责任 |
| --- | --- | --- |
| `src/docsbuildtool/__init__.py` | 空包入口 | 保留包命名空间。 |
| `tests/__init__.py` | 空测试包入口 | 保留测试目录。 |

## 建议模块边界

| 建议模块 | 责任 | 不应承担的责任 |
| --- | --- | --- |
| `docsbuildtool.cli` | 命令定义、参数解析、输出摘要 | 不直接实现构建细节。 |
| `docsbuildtool.sources` | Markdown 文件发现、导航排序、资源识别 | 不调用 MkDocs。 |
| `docsbuildtool.config` | MkDocs 配置生成和读取 | 不执行构建命令。 |
| `docsbuildtool.builders.html` | HTML 构建适配 | 不处理 PDF 专有逻辑。 |
| `docsbuildtool.builders.pdf` | PDF 构建适配 | 不修改源 Markdown。 |
| `docsbuildtool.errors` | 统一异常类型和错误消息 | 不包含业务流程。 |

<!-- TODO: 模块实现后，将建议模块表更新为实际模块表。 -->

<!-- END: auto-generated -->
