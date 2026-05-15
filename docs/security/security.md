# 安全

<!-- BEGIN: auto-generated -->

`docsbuildtool` 是纯本地 CLI 工具，无网络服务、无认证授权、无密钥管理。安全重点为：

- **路径保护** — `clean` 命令的 `_is_path_protected` 防止误删系统目录
- **子进程安全** — subprocess 使用 list 参数（禁止 `shell=True`）
- **YAML 安全** — 使用 `safe_load`/`safe_dump` 防止任意代码执行
- **依赖安全** — Poetry 管理，lock 文件控制版本

不存在：网络攻击面、SQL 注入、XSS、CSRF、认证绕过等传统 web 安全问题。

## 子文档

- [安全最佳实践](security_best_practices.md) — 路径保护、子进程安全、YAML 安全

<!-- END: auto-generated -->
