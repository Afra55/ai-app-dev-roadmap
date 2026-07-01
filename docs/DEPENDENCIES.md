# 依赖安装说明（统一入口）

本仓库**推荐只使用一种安装方式**，避免各周 `requirements.txt` 与根目录依赖不一致。

## 推荐方式（全仓库）

```bash
# 在仓库根目录执行一次即可
pip install -e ".[dev]"
```

这会安装 Phase 1 / Phase 2 所需的 Python 依赖，以及 pytest 等开发工具。

## 各周 `requirements.txt` 的角色

| 文件 | 用途 |
|------|------|
| `pyproject.toml` | **权威依赖清单**（CI 与推荐安装源） |
| `phase1/weekN/requirements.txt` | 历史参考 / 最小子集，**新环境不必单独 pip install** |
| `phase2/*/requirements.txt` | 同上，仅作查阅 |

## API Key

```bash
cp .env.example phase1/week1/.env
# 编辑 DEEPSEEK_API_KEY（可选，无 Key 可走 Mock / 离线模式）
```

## 验证安装

```bash
bash scripts/check_portfolio.sh
```

## 何时仍需单独 venv？

- 你想隔离本仓库与其他项目时：在根目录 `python -m venv .venv` 后 `pip install -e ".[dev]"`
- **不需要**每周进入 `weekN/` 再建一个 venv

## Android 构建（额外）

- 需要 JDK 17+ 与 Android SDK
- 见各项目 `android-app/README.md` 或 `local.properties.example`
