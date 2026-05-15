# 安全最佳实践

<!-- BEGIN: auto-generated -->

## 路径安全（已实现）

`clean` 命令使用 `_is_path_protected()`（`config.py`）防止删除受保护路径：

```python
def _is_path_protected(path: Path) -> bool:
    # 保护：项目根目录、文件系统根、用户主目录、Windows 系统目录
```

`validate_paths()` 确保输出目录不等于源目录，且不在受保护路径上。

## Subprocess 安全（已实现）

所有子进程调用使用 **list 参数** 而非 shell 字符串：

```python
subprocess.run(["mkdocs", "build", "-f", str(config), "-d", str(output)], ...)
```

禁止 `shell=True`，防止命令注入。

## YAML 安全（已实现）

配置解析使用 `yaml.safe_load()` 和 `yaml.safe_dump()`，禁止任意 Python 对象反序列化：

```python
yaml.safe_load(content)   # 仅反序列化安全类型
yaml.safe_dump(merged, f) # 安全序列化
```

输入中如含 `!!python/name:` 标签会预先剥离。

## 无密钥/无配置文件中的敏感信息

项目不使用 API 密钥、数据库密码或其他凭据。`pyproject.toml` 仅包含公开的元数据和依赖声明。

<!-- END: auto-generated -->
