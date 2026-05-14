# 开发环境配置

<!-- BEGIN: auto-generated -->

## Poetry 依赖组

开发环境建议安装 `dev-group`：

```powershell
poetry install --with dev-group
```

`dev-group` 包含：

- `doc-group`：文档构建依赖。
- `test-group`：测试依赖。
- `ruff`：代码检查工具。

## 本地缓存

Poetry、pytest 和 Ruff 会在本地创建缓存目录。这些目录属于开发环境产物，不应作为项目文档或源码的一部分。

<!-- TODO: 如后续引入 pre-commit、IDE 配置或本地示例数据，请在此补充。 -->

<!-- END: auto-generated -->
