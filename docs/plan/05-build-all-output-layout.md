# 开发计划：全量构建与输出目录布局

<!-- BEGIN: auto-generated -->

## 目标

实现 `docs build --format all`，按稳定顺序生成 HTML 和 PDF，并固定输出目录结构。

## 接口/行为

命令：

```powershell
docs build --format all
docs build --format all --source <directory> --output <directory>
```

输出结构：

```text
<output>/
├── html/
├── pdf/
│   └── docs.pdf
└── archive/
```

行为：

- 先构建 HTML，再构建 PDF。
- HTML 失败时不继续 PDF。
- PDF 失败时保留已成功生成的 HTML，并返回失败状态。
- `archive` 目录只作为归档输出位置，不在 build 阶段生成 zip。

## 实现步骤

1. 复用 HTML 构建服务和 PDF 构建服务。
2. 在 all 构建中创建输出根目录及必要子目录。
3. 实现顺序执行和结果聚合。
4. 输出每种格式的产物路径，通过 `rich` 渲染构建摘要。
5. 将部分成功状态记录到构建结果：PDF 失败时退出码为 `1`（构建失败），但终端消息中标注"部分成功：HTML 已生成，PDF 失败"，帮助用户区分全量成功和部分成功。
6. 与 `clean` 和 `archive` 共享输出布局常量。

## 影响范围

- 输出布局成为所有命令的共享约定。
- `archive` 默认读取 `<output>/html` 和 `<output>/pdf`。
- 测试夹具需要覆盖部分成功和失败场景。

## 测试用例

- all 构建生成 `<output>/html/index.html` 和 `<output>/pdf/docs.pdf`。
- HTML 构建失败时不调用 PDF 构建。
- PDF 构建失败时 HTML 仍存在，命令返回非零。
- 重复执行 all 构建输出结构保持稳定。
- 自定义 `--output` 目录下仍生成三个子目录。

## 验收标准

- 输出目录固定为 `html`、`pdf`、`archive` 三个子目录。
- all 构建的日志清楚展示每个阶段状态。
- 任何阶段失败都返回非零退出码。
- 成功构建后可立即执行 `docs archive --format zip`。

## 风险与注意事项

- 部分成功可能让用户误以为全量成功，终端摘要必须明确。
- 重复构建是否清理旧文件要与 `clean` 规则一致，避免陈旧产物混入归档。
- PDF 阶段较慢，all 构建不应成为默认。

<!-- END: auto-generated -->
