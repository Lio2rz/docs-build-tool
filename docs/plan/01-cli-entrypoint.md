# 开发计划：跨平台 CLI 入口

<!-- BEGIN: auto-generated -->

## 目标

实现跨平台 `docs` 命令，作为所有文档构建操作的统一入口。CLI 使用 Typer，支持 Windows、macOS、Linux。

## 接口/行为

命令：

```powershell
docs --help
docs build
docs serve
docs clean
docs archive
```

要求：

- `docs --help` 显示全局帮助、子命令和简短描述。
- CLI 退出码稳定：`0` 成功；`1` 构建/运行失败；`2` 用户输入错误（沿用 Typer/Click 默认）；`3` 依赖或环境缺失。
- `docs --version` 输出包版本，行为与 `docs --help` 一致退出 `0`。
- 支持 `python -m docsbuildtool` 作为等价入口，覆盖未安装 console script 的场景。
- 错误信息使用用户可读文本，不输出未处理 traceback；`--verbose`/`--debug` 全局开关可打开完整 traceback。
- 输出使用 `rich` 渲染（已在主依赖中）。
- 为支持裸 `docs` 命令，后续实现需要恢复本地可安装 console script；项目仍不上传 PyPI。

## 实施决策

- 包模式：将 `pyproject.toml` 的 `[tool.poetry]` 改为 `package-mode = true`，让 `poetry install` 默认安装本项目（src 布局）。
- 命令入口：通过 PEP 621 的 `[project.scripts]` 暴露：
  ```toml
  [project.scripts]
  docs = "docsbuildtool.cli:app"
  ```
- 备用入口：在 `src/docsbuildtool/__main__.py` 中调用 `cli.app()`，支持 `python -m docsbuildtool`。
- 不引入 `publish`/`twine` 流程；保留现有 `[project]` 元数据用于本地安装与工具识别。

## 实现步骤

1. 新增 `docsbuildtool.cli` 模块，定义 Typer app。
2. 在 CLI 中注册 `build`、`serve`、`clean`、`archive` 子命令。
3. 建立统一异常处理，将内部异常映射为退出码（0/1/2/3）和错误消息。
4. 增加全局 `--verbose/--debug` 选项控制 traceback 输出；增加 `--version` 选项。
5. 在 `pyproject.toml` 中切换 `package-mode = true` 并增加 `[project.scripts]` 入口。
6. 新增 `src/docsbuildtool/__main__.py` 以支持 `python -m docsbuildtool`。
7. 更新 README 和 CLI 使用文档。

## 影响范围

- `pyproject.toml`：切换 `package-mode = true` 并新增 `[project.scripts]`；不增加发布相关配置。
- `src/docsbuildtool/`：新增 CLI 模块、`__main__.py` 与错误类型。
- `.github/workflows/`：CI 需要验证 `docs --help` 与 `python -m docsbuildtool --help`。
- 文档：需要说明裸 `docs` 命令的本地安装方式与备用 `python -m` 入口。

## 测试用例

- 调用 `docs --help`，断言包含 `build`、`serve`、`clean`、`archive`。
- 调用 `docs --version`，断言输出版本号且退出码 `0`。
- 调用未知命令，断言退出码 `2` 且提示可读。
- 调用 `docs build --help`，断言包含 `--format`、`--source`、`--output`。
- 在 Windows、macOS、Linux CI 中执行 `docs --help` 与 `python -m docsbuildtool --help`。
- 模拟内部异常，断言默认输出简短错误且退出码 `1`；加 `--debug` 后输出完整 traceback。

## 验收标准

- 在三类操作系统中，`docs --help` 与 `python -m docsbuildtool --help` 均可直接执行。
- 所有子命令出现在帮助信息中。
- CLI 命令不依赖 shell 专有语法。
- `pyproject.toml` 没有 `publish` / `twine` 等上传配置，但允许保留 `[project]` 元数据。

## 风险与注意事项

- 当前项目设置为 `package-mode = false`，裸命令需要重新设计本地安装方式。
- `docs` 名称较通用，可能与用户系统已有命令冲突；文档需说明如何确认命令来源。
- Typer/Click 在不同 shell 下对路径引号的表现可能不同，测试需覆盖含空格路径。

<!-- END: auto-generated -->
