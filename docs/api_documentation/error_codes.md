# 错误代码

<!-- BEGIN: auto-generated -->

当前没有统一错误代码。建议后续定义稳定的错误类型：

| 错误代码 | 说明 | 触发条件 |
| --- | --- | --- |
| `SOURCE_NOT_FOUND` | 输入目录不存在 | 用户传入不存在的 Markdown 源目录。 |
| `NO_MARKDOWN_FILES` | 未发现 Markdown 文件 | 输入目录没有 `.md` 文件。 |
| `CONFIG_INVALID` | MkDocs 配置无效 | 配置生成或加载失败。 |
| `BUILD_FAILED` | 构建失败 | MkDocs 或 PDF 渲染器返回失败。 |
| `ASSET_MISSING` | 资源缺失 | Markdown 引用的图片或资源不存在。 |

<!-- TODO: 实现异常类型后，补充退出码和用户提示。 -->

<!-- END: auto-generated -->
