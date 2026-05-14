# 开发计划：测试、CI 与质量门禁

<!-- BEGIN: auto-generated -->

## 目标

建立覆盖 CLI、构建流程、配置解析、跨平台行为和文档构建的测试体系，并让 CI 自动执行。

## 接口/行为

质量命令：

```powershell
poetry check --lock
poetry run black --check .
poetry run isort --check-only .
poetry run ruff check .
poetry run mypy
poetry run pytest
poetry run mkdocs build --strict
```

CI 要求：

- lint workflow 运行格式、lint、类型检查、文档构建。
- tests workflow 运行 pytest。
- 后续加入三平台矩阵。

## 实现步骤

1. 建立 `tests/fixtures/`，包含最小 Markdown、嵌套文档、资源文件、断链文档。
2. 使用 Typer CliRunner 测试命令帮助和参数解析。
3. 使用临时目录测试 build/clean/archive。
4. 对 MkDocs 调用建立可替换边界，便于 mock serve 和失败场景。
5. 扩展 GitHub Actions 为 Python 3.13 三平台矩阵。
6. 增加覆盖率报告，但不在第一版强制覆盖率阈值。

## 影响范围

- 需要为功能代码设计可测试边界。
- CI 时间随 PDF 和三平台测试增加。
- 文档构建 strict 模式会要求导航和链接保持干净。

## 测试用例

- Typer help 和参数解析测试。
- HTML/PDF/all 构建集成测试。
- source 有/无 `summary.md`、有/无 `mkdocs.yml` 的配置解析测试。
- serve mock 测试。
- clean 高风险路径测试。
- archive zip 内容测试。
- CI 三平台 smoke 测试。
- MkDocs strict build 测试。

## 验收标准

- 本地质量命令全部通过。
- CI 在 pull_request 和 push 上运行。
- 每个功能至少有成功路径和失败路径测试。
- 测试不依赖本机绝对路径。

## 风险与注意事项

- PDF 集成测试可能慢且不稳定，应区分 smoke test 和完整集成测试。
- 过早设置覆盖率阈值可能阻碍初期开发，第一版只报告覆盖率。
- mock 过多会掩盖真实 MkDocs 行为，关键路径必须保留集成测试。

<!-- END: auto-generated -->
