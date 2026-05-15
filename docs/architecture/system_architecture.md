# 系统架构

<!-- BEGIN: auto-generated -->

## 当前状态

项目版本 0.1.0，已形成 7 模块架构：`cli.py`、`config.py`、`builder.py`、`serve.py`、`clean.py`、`archive.py`、`errors.py`。系统围绕”输入 Markdown 目录 -> 配置生成 -> MkDocs 子进程构建 -> HTML/PDF 输出”的流水线组织。

## 系统架构

```text
┌─────────────────────────────────────────────────┐
│                    CLI (cli.py)                  │
│    4 命令: build / serve / clean / archive       │
│    Typer + Rich 终端输出                         │
└─────────────────┬───────────────────────────────┘
                  │
    ┌─────────────┼────────────────┐
    │             │                │
    v             v                v
┌────────┐  ┌──────────┐  ┌──────────────┐
│ config │  │ builder  │  │    errors     │
│  .py   │  │  .py     │  │     .py       │
│        │  │          │  │              │
│ resolve│  │build_html│  │ ExitCode(4)  │
│ _source│  │build_pdf │  │ DocsError    │
│ resolve│  │build_all │  │ ConfigError  │
│ _output│  │          │  │ BuildError   │
│ generat│  │ 子进程    │  │ EnvMissing   │
│ e_mkd  │  │ mkdocs   │  │ Error        │
│ ocs_c  │  │ build    │  │              │
│ onfig  │  │          │  └──────────────┘
│ generat│  └──────────┘
│ e_pdf_ │
│ config │
│ valida │
│ te_pa  │
│ ths    │
└────────┘

  辅助模块:
  ┌───────────┐  ┌───────────┐
  │ serve.py  │  │ clean.py  │
  │           │  │           │
  │ mkdocs    │  │ 删除      │
  │ serve     │  │ html/     │
  │ (阻塞)    │  │ pdf/      │
  └───────────┘  │ archive/  │
                 │ 及临时    │
  ┌───────────┐  │ 工作目录  │
  │ archive   │  └───────────┘
  │  .py      │
  │           │
  │ ZIP 打包  │
  │ html/ +   │
  │ pdf/      │
  └───────────┘
```

## 数据流

```text
1. CLI 解析参数 (cli.py)
       │
       v
2. 路径解析与配置生成 (config.py)
   resolve_source() → resolve_output() → generate_mkdocs_config()
   或 generate_pdf_config() → validate_paths()
   → 产出 ResolvedConfig(source, output, config_path, summary_path, work_dir)
       │
       v
3. 构建编排 (builder.py)
   根据 BuildFormat(html/pdf/all) 分支:
   - HTML: 子进程 mkdocs build → site/html/
   - PDF:  子进程 mkdocs build（含 with-pdf）→ site/pdf/docs.pdf
   - ALL:  先 HTML 后 PDF，PDF 失败非致命
       │
       v
4. 输出产物
   site/html/           ← 静态站点
   site/pdf/docs.pdf    ← PDF 文件
   site/archive/docs.zip ← ZIP 归档（需执行 archive 命令）
```

## 层职责

| 层 | 对应模块 | 职责 |
| --- | --- | --- |
| CLI 层 | `cli.py` | 参数解析、Rich 风格化输出、退出码控制 |
| 配置层 | `config.py` | 路径解析（默认值、自定义）、mkdocs.yml 生成、SUMMARY.md 生成、路径保护校验 |
| 构建层 | `builder.py` | HTML/PDF 构建编排、子进程管理、BuildFormat 枚举 |
| 服务层 | `serve.py` | 本地预览服务器（阻塞式 mkdocs serve） |
| 清理层 | `clean.py` | 构建产物和临时工作目录清理 |
| 归档层 | `archive.py` | ZIP 打包（zipfile.ZIP_DEFLATED） |
| 错误层 | `errors.py` | ExitCode 枚举、DocsError 异常层次 |

## 关键技术决策

- **子进程调用**：不直接使用 MkDocs Python API，而是通过 `subprocess.run` 调用 mkdocs 命令行。这保持了与 mkdocs 版本的解耦。
- **临时工作目录**：每次构建在输出目录下创建 `docsbuildtool-*` 临时目录存放生成的 mkdocs.yml 等中间文件。
- **PDF 非致命**：`build_all()` 中 PDF 构建失败不阻塞整体流程，HTML 产出任然保留。
- **路径保护**：`_is_path_protected()` 防止误覆盖项目根目录、文件系统根目录、HOME 和 WINDIR。

<!-- END: auto-generated -->
