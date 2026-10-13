# 本地生产目录

新内容统一创建在 `productions/<YYYY-MM-DD-slug>/`，不要把新任务放进历史 `episodes/`。

每个生产目录至少包含 `production.yaml`。模板沿用：

`world-mechanism/engine/production-orchestrator/template-production.yaml`

并在顶层增加：

```yaml
content_line: "有解｜关系与处世 | 世界机制 | 想象瞬间｜Edge of Sight"
notion_output_url: "https://app.notion.com/..."
```

目录保存 Brief 交接、代码、素材、渲染候选、QA 和回填证据；成品发布包按根目录 `AGENTS.md` 的规则导出到 `outputs/`，不自动发布。
