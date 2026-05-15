# 分支策略

<!-- BEGIN: auto-generated -->

## 分支命名格式

所有带计数器的分支遵循统一格式：

```
<prefix>/<TAG>-<NNNNNN>-<yyyyMMdd>-<short-description>
```

| 组成部分 | 说明 | 示例 |
|----------|------|------|
| `<prefix>` | 分支类别路径 | `develop/feature/` |
| `<TAG>` | 类型缩写 | `PROJ` |
| `<NNNNNN>` | 6 位零填充序号，按类别独立计数 | `000001` |
| `<yyyyMMdd>` | 创建日期 | `20260515` |
| `<short-description>` | kebab-case 简短描述（2-5 词） | `oauth-google-login` |

示例完整分支名：`develop/feature/PROJ-000042-20260512-oauth-google-login`

## 分支类型速查

### 特殊分支（无计数器）

| 分支名 | 说明 |
|--------|------|
| `main` | 生产稳定分支 |
| `init/project-scaffold` | 项目初始化 |
| `develop/main` | 主开发线 |

### 开发分支（带计数器）

| 分支前缀 | TAG | 用途 | 分支来源 | 合并目标 |
|----------|-----|------|---------|---------|
| `develop/feature/` | `PROJ` | 新功能开发 | `develop/main` | `develop/main` |
| `develop/debug/` | `DBG` | 调试/问题排查 | `develop/main` | `develop/main` |
| `develop/refactor/` | `REF` | 代码重构 | `develop/main` | `develop/main` |
| `develop/test/` | `TST` | 测试编写 | `develop/main` | `develop/main` |
| `develop/docs/` | `DOC` | 文档编写/更新 | `develop/main` | `develop/main` |
| `develop/fix/` | `FIX` | 非紧急 Bug 修复 | `develop/main` | `develop/main` |
| `develop/audit/` | `SEC` | 安全审计 | `develop/main` | `develop/main` |

### 发布与热修复分支

| 分支前缀 | TAG | 用途 | 分支来源 | 合并目标 |
|----------|-----|------|---------|---------|
| `release/` | `RC` | 发布候选 | `develop/main` | `release/vX.Y.Z` + `main` |
| `release/` | `vX.Y.Z` | 正式发布标签 | `release/RC-*`（或 `main`） | `main` |
| `hotfix/` | `HOT` | 紧急生产修复 | `main` | `main` **和** `develop/main` |

> **重要**：hotfix 必须双合并（同时合入 `main` 和 `develop/main`），否则修复将在下一发布周期丢失。

## 计数器管理

每个 TAG 类型有独立的 6 位序号计数器，从 `000001` 开始。查找下一个可用计数器：

```bash
git fetch --all --prune
git branch -a | grep -oP '<TAG>-\K\d{6}' | sort -n | tail -1
```

若无结果，从 `000001` 开始；否则取最大值 +1。

### 分支类型判定规则

当需求描述在两种类型间模糊时：

| 场景 | 判定 |
|------|------|
| **fix vs debug** | `fix` 用于已知 Bug（有明确复现步骤），`debug` 用于未知根因的调查 |
| **refactor vs feature** | `refactor` 改变结构但不变行为，行为变更则属 `feature` |
| **hotfix vs fix** | `hotfix` 用于需立即部署的线上紧急问题，`fix` 用于正常开发周期中的计划修复 |

## 分支生命周期

1. **创建** — 从正确的基础分支切出（见合并流程表）
2. **开发** — 遵循 Conventional Commits 提交
3. **推送** — 定期推送避免丢失工作
4. **合并** — 通过 PR 合并到目标分支
5. **删除** — 合并后删除本地和远程分支：
   ```bash
   git branch -d <branch-name>
   git push origin --delete <branch-name>
   ```

## 当前分支状态

| 分支 | 类型 | 状态 |
|------|------|------|
| `main` | 特殊分支 | 稳定 |
| `dev/mian` | `develop/main` | 12 阶段开发完成 |
| `init/project-scaffold` | 特殊分支 | 已合并 |
| `dev/docs/DOC-000001-20260515-rebuild-all-docs` | 文档分支 | 当前工作中 |

<!-- END: auto-generated -->
