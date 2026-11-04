# 维护指南

## 本地构建

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python scripts/build.py
```

构建结果位于 `dist/`。内容保存在 `docs/` 中，使用 MyST Markdown；主题为 Furo。公式由 MathJax 渲染，首次访问需要能连接其 CDN。

## 新增与修订

1. 从复用模板创建 `.md` 文件。
2. 在对应栏目页面的 `toctree` 中加入文件路径。
3. 在 `catalog.json` 中登记标题、路径、标签和摘要。
4. 执行构建并检查链接、公式和移动端布局。
5. 提交源码；项目里程碑的浏览器记录需手动同步回源文件。

## GitHub Pages

源码已提供 `.github/workflows/pages.yml`。将源码推送到你自己的 GitHub 仓库，在 Settings → Pages 中选择 GitHub Actions。工作流构建并上传 `dist/`。

当前站点通过 Sites 发布；尚未创建或绑定 GitHub 仓库。

## 目录结构

```text
docs/
  notes/       # 稳定知识
  projects/    # 项目与实验
  blog/        # 日期型记录
  _static/     # 样式与交互
catalog.json   # 分类、标签与检索目录
scripts/build.py
.github/workflows/pages.yml
```

## 技术文档

[Sphinx](https://www.sphinx-doc.org/) · [MyST 数学语法](https://myst-parser.readthedocs.io/en/latest/syntax/math.html) · [Furo 主题](https://furo.readthedocs.io/)
