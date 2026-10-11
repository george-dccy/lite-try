# Sticker outputs

这里保存通过 Notion「余光所及｜有解贴图生成器」产生并通过当前运行验收的双格观察卡 / 贴图发布包。

默认内容单位是 **3–6 张独立双格观察卡 / 双格洞察卡**：每张卡自身应能表达完整意思，上下两格之间有明确对照、转折、递进或互文；整组可以共享主题，但不要求是一条连续剧情。

目录约定：

`outputs/stickers/YYYY-MM-DD/<slug>/`

推荐文件：

- `manifest.json`：主题、测试假设、卡片数量、Notion Skill URL、模式、状态、AI 内容声明检查，以及可用时每张卡的上下格语义关系。
- `titles.txt`：公众号贴图标题候选。
- `caption.txt`：最终短配文。
- `prompts/`：若本轮保留逐卡最终 Prompt。
- `images/`：当前运行环境能够取得并写入最终双格卡图片文件时保存。
- `notes.md`：必要的本轮说明或人工复盘。

本目录**不保存或镜像 Notion 的“余光所及”视觉机制与完整版式语法正文**。需要重跑时必须按 `notes/NOTION_YUGUANG_STICKER_BRIDGE.md` 重新通过 Notion MCP 读取现行机制。

双格版式设计方法已经内置在 Notion Skill 中；运行时不需要、也不应再次访问 `yang0/handraw-style` 或其他外部模板仓库来补齐版式规则。
