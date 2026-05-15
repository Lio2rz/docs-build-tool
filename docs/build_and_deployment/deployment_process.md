# 部署流程

<!-- BEGIN: auto-generated -->

项目不作为 Python 包发布到 PyPI（`package-mode = false`），但提供 CLI 入口和本地可安装的脚本。

## CLI 入口

Poetry 脚本注册：

```toml
[tool.poetry.scripts]
docs = "docsbuildtool.cli:app"
```

安装后可通过 `docs` 命令使用所有功能：

```bash
# 以可编辑模式安装（开发用）
pip install -e .

# 或通过 Poetry
poetry install

# 使用 CLI
docs build --source docs --output site --format html
docs serve --source docs
docs clean --output site
docs archive --format zip --output dist
```

## 构建产物

| 产物 | 格式 | 生成方式 | 输出位置 |
| --- | --- | --- | --- |
| HTML 文档站点 | 静态文件目录 | `docs build --format html` | `<output>/html/` |
| PDF 文档 | 单个 .pdf 文件 | `docs build --format pdf` | `<output>/pdf/docs.pdf` |
| 归档包 | .zip 文件 | `docs archive --format zip` | `<output>/archive/docs.zip` |

## 发布方式

- HTML 站点：可直接部署到任意静态文件服务器、GitHub Pages 或内部文档平台。
- PDF 文档：作为构建产物交付或上传到发布资产。
- 项目本身不上传到 PyPI，不构建 wheel 或 sdist 分发包。

## 环境要求

- Python >= 3.13
- Poetry（依赖管理）
- 文档构建需安装 `doc-group`，测试需安装 `test-group`，开发需安装 `dev-group`

<!-- END: auto-generated -->
