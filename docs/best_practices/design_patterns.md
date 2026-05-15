# 设计模式

<!-- BEGIN: auto-generated -->

## 已采用的设计模式

| 模式 | 使用位置 | 说明 |
| --- | --- | --- |
| StrEnum | `builder.py` — `BuildFormat` | 使用 Python 3.11+ `StrEnum` 定义构建格式枚举（html, pdf, all） |
| Strategy | `builder.py` — `build_html`/`build_pdf`/`build_all` | 三种构建策略，通过 `--format` CLI 选项选择 |
| Adapter | `config.py` — `generate_pdf_config` | 在标准 MkDocs 配置基础上适配 `mkdocs-with-pdf` 插件 |

## 详细说明

### StrEnum — 构建格式枚举

```python
class BuildFormat(StrEnum):
    html = "html"
    pdf = "pdf"
    all = "all"
```

### Strategy — 构建策略

- `build_html(source, output)` — HTML 构建策略
- `build_pdf(source, output)` — PDF 构建策略
- `build_all(source, output)` — 全量构建策略（HTML + PDF，PDF 失败不中断）

### Adapter — PDF 配置适配

`generate_pdf_config` 在标准配置基础上添加 `mkdocs-with-pdf` 插件，复用 `generate_mkdocs_config` 的核心逻辑。

### 其他模式

| 模式 | 位置 | 说明 |
| --- | --- | --- |
| Dataclass | `config.py` — `ResolvedConfig` | 封装配置解析结果（source, output, config_path 等） |
| IntEnum | `errors.py` — `ExitCode` | 退出码枚举（SUCCESS=0, FAILURE=1, USER_ERROR=2, ENV_MISSING=3） |
| Facade | `cli.py` — Typer app | CLI 作为统一入口，隐藏内部模块细节 |

<!-- END: auto-generated -->
