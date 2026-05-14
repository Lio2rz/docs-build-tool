# 依赖管理

<!-- BEGIN: auto-generated -->

## 包管理器

项目使用 Poetry 管理依赖和构建，构建后端为：

```toml
[build-system]
requires = ["poetry-core>=2.0.0,<3.0.0"]
build-backend = "poetry.core.masonry.api"
```

## 常用命令

```powershell
poetry lock
poetry install --with dev-group --no-root
poetry check --lock
```

## 策略

- 修改依赖后必须刷新 `poetry.lock`。
- 不手工编辑 `poetry.lock`。
- 文档构建依赖放入 `doc-group`。
- 测试依赖放入 `test-group`。
- 开发聚合依赖放入 `dev-group`。
- 当前项目使用 `package-mode = false`，Poetry 只负责依赖管理，不打包、不上传到 PyPI。
- 只有项目脚本运行时真正需要的依赖才放入 `project.dependencies`。

<!-- END: auto-generated -->
