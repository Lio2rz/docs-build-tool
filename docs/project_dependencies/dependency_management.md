# 依赖管理

<!-- BEGIN: auto-generated -->

## 包管理器

项目使用 Poetry 管理依赖，构建后端配置：

```toml
[build-system]
requires = ["poetry-core>=2.0.0,<3.0.0"]
build-backend = "poetry.core.masonry.api"
```

项目设置 `package-mode = false`，Poetry 仅负责依赖管理与脚本入口，不构建和发布 Python 包。

## 常用命令

```bash
poetry lock                          # 解析并锁定依赖版本
poetry install --with dev-group --no-root  # 安装全部开发依赖
poetry check --lock                  # 验证 pyproject.toml 与 poetry.lock 一致性
poetry add <package> --group dev-group    # 添加开发依赖
poetry update <package>              # 更新指定依赖
```

## 策略

- 修改 `pyproject.toml` 依赖声明后必须运行 `poetry lock` 刷新锁文件。
- 禁止手工编辑 `poetry.lock`。
- 文档构建依赖放入 `doc-group`。
- 测试依赖放入 `test-group`。
- 开发聚合依赖放入 `dev-group`（通过 `include-group` 引用 doc-group 和 test-group）。
- 项目使用 `package-mode = false`，不上传到 PyPI，不作为 Python 包分发。
- 只有 CLI 运行时真正需要的依赖才放入 `project.dependencies`（目前为 rich + typer）。
- Poetry 通过 `[tool.poetry.scripts]` 注册 CLI 入口：`docs = docsbuildtool.cli:app`。

<!-- END: auto-generated -->
