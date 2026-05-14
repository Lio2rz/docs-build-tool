# 开发计划：源目录与 MkDocs 配置解析

<!-- BEGIN: auto-generated -->

## 目标

实现 `--source`、`--output`、临时 MkDocs 配置生成与合并逻辑，为 build、serve、archive 等命令提供统一输入模型。

## 接口/行为

参数：

```powershell
docs build --source <directory> --output <directory>
docs serve --source <directory>
```

规则：

- 默认源目录为 `docs`。
- 默认输出根目录为 `site`。
- 如果源目录包含 `mkdocs.yml`，优先读取并合并用户配置。
- 如果源目录不包含 `mkdocs.yml`，使用项目 `mkdocs.yml` 作为模板。
- 如果源目录包含 `summary.md`，作为 literate-nav 导航源。
- 如果源目录缺少 `summary.md`，生成临时导航文件，不修改源目录。
- 临时配置和临时导航应写入临时目录或输出工作目录，不能污染源目录。

## 实现步骤

1. 定义源配置解析数据结构，包含 source、output、config_path、summary_path、work_dir。
2. 校验 source 是否存在且为目录。
3. 校验 output 不等于 source、不等于项目根、不等于磁盘根、不等于 `Path.home()`、不在 `$env:WINDIR` 或 `/` 等系统路径下。
4. 实现 MkDocs 配置加载：源目录配置优先，项目模板兜底。
5. 实现配置合并：覆盖 `docs_dir`、`site_dir` 与必要插件配置；对 `exclude_docs` 采用**追加**策略——在用户已有 `exclude_docs` 文本后追加 `/summary.md` 与临时导航文件路径，绝不覆盖用户原值；对 `plugins` 采用合并策略，保留用户插件并补齐 `literate-nav`、`section-index`。
6. 实现临时 `summary.md` 生成逻辑，按 Markdown 文件稳定排序。
7. 为后续构建命令返回可直接传给 MkDocs 的配置文件路径。

## 影响范围

- 构建命令、预览命令、清理命令都依赖该解析结果。
- `mkdocs.yml` 的模板字段会成为后续配置兼容边界。
- 测试需要创建多种临时源目录夹具。

## 测试用例

- source 不存在时报错。
- source 是文件时报错。
- source 含 `mkdocs.yml` 和 `summary.md` 时优先使用用户文件。
- source 仅含 Markdown 文件时生成临时 `summary.md`。
- output 与 source 相同时拒绝。
- output 等于项目根、磁盘根、`Path.home()` 或 `$env:WINDIR` / `/` 等系统路径时拒绝。
- output 含空格和非 ASCII 路径时解析成功。
- 合并后的配置包含 `literate-nav`、`section-index` 和正确 `docs_dir`，并保留用户原有 `exclude_docs` 与插件配置。

## 验收标准

- 不修改源目录中的任何文件。
- 所有 build/serve 命令共享同一套解析逻辑。
- 临时配置可被 `mkdocs build -f <config>` 成功读取。
- 错误消息明确指出无效路径或缺失文件。

## 风险与注意事项

- MkDocs 插件配置合并需要保留用户自定义插件，不能粗暴覆盖。
- 自动生成导航会影响页面顺序，需要在文档中说明排序规则。
- Windows 路径分隔符必须通过 `pathlib` 处理，配置中输出 POSIX 风格相对路径。

<!-- END: auto-generated -->
