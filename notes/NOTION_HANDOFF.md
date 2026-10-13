# 余光所及｜Notion ↔ 本地仓库交接协议

本文件只记录连接、交接和产物边界；“余光所及”的写作、视觉、生图和视频创意机制正文永远在 Notion 现行页面，不在仓库缓存或兜底。

## 入口

- 工作台：<https://app.notion.com/p/3f727110f8d5813e9b22dbeff5ebdd9c>
- 写作机制：<https://app.notion.com/p/3d727110f8d5816dbed0f5360d37014b>
- 创意视频机制：<https://app.notion.com/p/3f727110f8d5812da32dd21d59e30131>
- 有解贴图生成器：<https://app.notion.com/p/3f627110f8d581918bf3de93e837a339>
- 生图运行协议 v4.0：<https://app.notion.com/p/3da27110f8d5819b835ac3154cec5e3a>

所有入口和依赖页面只通过 Notion MCP fetch；Notion MCP 不可用、页面不可读或依赖缺失时返回 `blocked`，不使用本地旧 Prompt、缓存机制或模型记忆继续。

## 贴图 Fast Lane

贴图、图片消息、小绿书式轻图文、双格卡和冷启动验证可以直接进入有解贴图生成器，不强制先做完整长文母稿。输入有四类：

1. 明确主题、困惑或一句话；
2. lite-try 已验证题；
3. 今日探索（从选题库筛选建议形式含“贴图”的候选，不足时生成轻量候选）；
4. 工作台选题库的一条选题，保留其 `认知转折`、`读者带走` 和 `测试假设`。

运行时先在产物库创建记录，再按 Notion 贴图 Skill 和生图运行协议执行。产物页至少记录工作标题、类型、平台、关联选题、测试假设/变量和正文中的卡片核心表达；Prompt 只保存在 Notion 03 / 04，不在仓库复制。

贴图仓库产物需要时才返回 `sticker_manifest`，并带：

```json
{
  "source": "notion-yuguang-sticker-skill",
  "notion_skill_url": "https://app.notion.com/p/3f627110f8d581918bf3de93e837a339",
  "notion_output_url": "",
  "content_unit": "two-panel-insight-card",
  "topic": "",
  "test_hypothesis": "",
  "card_count": 0,
  "mode": "image|prompt-only",
  "title_candidates": [],
  "caption": "",
  "ai_content_disclosure_checked": true,
  "status": "ready|prompt_ready|blocked"
}
```

仓库保存到 `outputs/stickers/YYYY-MM-DD/<slug>/`，只放 manifest、标题、配文、Prompt 和实际取得的图片，不镜像 Notion 机制。发布数据和读者原话回填 Notion 产物页。

## 通用产物交接

`yuguang-handoff` 接收一个产物页 URL 后：

1. fetch 产物页正文、属性中的 `仓库交接`、`状态` 和关联选题；
2. 按 `类型` / `平台` / `仓库交接` 选择本地执行器，并实时读取对应 Notion 机制；
3. 把结果保存到 `productions/<YYYY-MM-DD-slug>/`，生产 manifest 必须包含 `content_line` 和 `notion_output_url`；
4. 通过 Notion MCP 回填产物库真实字段 `发布链接`（“链接”的实际字段名）和 `状态=待发布`；不写数据字段，不自动发布；
5. 回读刚更新的产物页，确认属性写入成功后再报告完成。

没有 `仓库交接`、没有明确关联产物或对应机制无法读取时，停止并返回 `blocked`。

## 当前数据库事实

- 产物库：`collection://b10d972d-cdda-4b95-98ab-a6d4354a7439`
- 真实交接字段：`仓库交接`、`状态`、`发布链接`；不要假设存在名为 `链接` 的字段。
- 想法库、选题库和 03 / 04 / 07 数据库的 schema 必须在首次使用时重新读取，按真实字段和选项写入。
