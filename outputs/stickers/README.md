# Sticker outputs

这里保存通过 Notion「余光所及｜有解贴图生成器」产生并通过当前运行验收的贴图发布包。

目录约定：

`outputs/stickers/YYYY-MM-DD/<slug>/`

推荐文件：

- `manifest.json`：主题、关系瞬间、测试假设、Notion Skill URL、模式、状态、AI 内容声明检查等。
- `titles.txt`：公众号贴图标题候选。
- `caption.txt`：最终短配文。
- `prompts/`：若本轮保留逐图最终 Prompt。
- `images/`：当前运行环境能够取得并写入最终图片文件时保存。
- `notes.md`：必要的本轮说明或人工复盘。

本目录**不保存或镜像 Notion 的“余光所及”视觉机制正文**。需要重跑时必须按 `notes/NOTION_YUGUANG_STICKER_BRIDGE.md` 重新通过 Notion MCP 读取现行机制。
