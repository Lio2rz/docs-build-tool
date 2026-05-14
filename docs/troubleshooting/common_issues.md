# 常见问题与症状

<!-- BEGIN: auto-generated -->

| 症状 | 可能原因 | 处理方式 |
| --- | --- | --- |
| `poetry check` 提示 lock 过期 | 修改了依赖但未刷新锁文件 | 运行 `poetry lock`。 |
| `pytest` 报告 `no tests ran` | 当前没有测试用例 | 添加测试后重试。 |
| `mkdocs` 命令不可用 | 未安装 `doc-group` | 运行 `poetry install --with doc-group --no-root` 或 `poetry install --with dev-group --no-root`。 |
| PDF 构建失败 | PDF 插件或系统依赖问题 | 检查 `mkdocs-with-pdf` 和 WeasyPrint 相关依赖。 |

<!-- END: auto-generated -->
