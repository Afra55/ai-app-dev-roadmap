# GitHub 与个人作品集检查清单

投递前逐项勾选。

---

## GitHub 主页

- [ ] 头像与简介已填写（一句话：Android → AI 应用开发）
- [ ] **Pin** 本仓库 `ai-app-dev-roadmap`
- [ ] 联系邮箱可见（或 README 中提供）

---

## 本仓库

- [ ] 根 `README.md` 含学习路线与快速开始
- [ ] `bash scripts/check_portfolio.sh` 通过
- [ ] 无 `.env`、无 API Key、无大模型权重提交
- [ ] `phase3/` 演示脚本路径正确
- [ ] 主项目 README 有架构图与验收清单

---

## 演示材料

- [ ] 录屏或 GIF 链接已填入 README（可选但强烈推荐）
- [ ] Demo 命令在干净环境试过（`verify_setup.py`）
- [ ] 离线可演示部分已排练（无 Key 场景）

---

## 简历与仓库一致

- [ ] 简历项目名与仓库目录一致
- [ ] 技术栈描述与代码相符
- [ ] 无夸大（未做的训练/生产 K8s 不写）

---

## 安全自查

```bash
# 检查是否误提交密钥（应无输出或仅 .env.example）
git grep -i "sk-" -- ':!*.md' ':!*.example' ':!.env.example' || true
```

- [ ] 上述检查通过
- [ ] `.gitignore` 含 `data/`、`chroma_db/`、`.env`

---

## 作品集一页纸（面试可发）

建议包含：

1. 姓名 + 联系方式 + GitHub
2. 主项目 3 条 bullet（来自 week10）
3. 演示链接 / 二维码
4. 架构图截图（来自 `project-highlights.md`）

---

## 完成后

- [ ] 请朋友从 **clone 仓库** 开始跟 README 走一遍（30 分钟测试）
