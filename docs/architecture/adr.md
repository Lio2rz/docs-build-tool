# 架构决策记录

<!-- BEGIN: auto-generated -->

## 已记录决策

| 日期 | 决策 | 来源 | 状态 |
| --- | --- | --- | --- |
| 2026-05-14 | 使用 `AGENTS.md` 和 `.agents/` 作为 agent 指令根目录 | Git 提交 `db634a8`、`c8791c0` | 已采用 |
| 2026-05-14 | 使用 Poetry 和 `src/` 布局初始化 Python 包 | Git 提交 `2545f5c`、`pyproject.toml` | 已采用 |
| 2026-05-14 | 依赖按 `dev-group`、`doc-group`、`test-group` 分组 | Git 提交 `5afde33`、`pyproject.toml` | 已采用 |
| 2026-05-14 | 使用 MkDocs 生态生成 HTML，PDF 通过插件支持 | `AGENTS.md`、`.agents/project.md` | 已采用 |
| 2026-05-14 | 采用 Typer + Rich 构建 CLI（非 argparse/click） | `pyproject.toml`、`cli.py` | 已采用 |
| 2026-05-14 | 通过子进程调用 `mkdocs build/serve`（非直接使用 Python API） | `builder.py`、`serve.py` | 已采用 |
| 2026-05-14 | PDF 构建失败为非致命错误，`build_all()` 中不阻塞 HTML 输出 | `builder.py` → `build_all()` | 已采用 |
| 2026-05-14 | 使用结构化异常层次（`DocsError` → `ConfigError`/`BuildError`/`EnvMissingError`）实现统一错误处理 | `errors.py` | 已采用 |
| 2026-05-14 | 路径保护机制防止误覆盖关键目录（项目根、文件系统根、HOME、WINDIR） | `config.py` → `_is_path_protected()` | 已采用 |
| 2026-05-14 | 使用 mkdocs-material 作为默认主题，literate-nav + section-index 管理导航 | `config.py` → `generate_mkdocs_config()` | 已采用 |
| 2026-05-14 | `package-mode=false`，项目不作为 pip 包发布，仅用于开发环境 | `pyproject.toml` | 已采用 |
| 2026-05-14 | 使用 `tmp_path` fixture 进行所有文件系统相关测试，不依赖本机绝对路径 | `tests/conftest.py`、各测试文件 | 已采用 |
| 2026-05-14 | 代码质量：black 行宽 120，mypy strict 模式，ruff B/E/F/I/UP 规则 | `pyproject.toml` | 已采用 |

## ADR 模板

```markdown
## ADR-YYYYMMDD-标题

- 日期：
- 状态：提议中 / 已采用 / 已废弃
- 背景：
- 决策：
- 影响：
- 替代方案：
```

<!-- END: auto-generated -->
