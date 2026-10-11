---
name: yuguang-sticker-bridge
description: 为 lite-try 的关系与处世内容生成公众号贴图、图片消息或小绿书式轻图文。每次通过 Notion MCP 实时读取“余光所及｜有解贴图生成器”及其现行上游机制；仓库只提供关系主题和测试目的，不复制视觉规则。
---

# 余光所及关系贴图桥接器

先读 `notes/BRAND_POSITIONING.md` 与 `notes/NOTION_YUGUANG_STICKER_BRIDGE.md`。

## 何时使用

用户要求“贴图”“公众号图片消息”“小绿书”“关系场景图片组”“用余光所及做这个关系题”“今天发几条轻图文”或明确要用图片做冷启动/选题验证时，优先使用本 Skill。

这条路径是 `relationship-content` 的 Fast Lane，不要求先完成长文章、完整母稿或常规正式选题卡。某条贴图被验证值得放大后，再回常规内容生产线。

## 强制入口

1. 通过已连接的 Notion MCP fetch：
   `https://app.notion.com/p/3f627110f8d581918bf3de93e837a339`
2. 把本轮的关系主题、具体瞬间、核心困惑、可选测试假设和用户指定的平台/数量作为输入交给该 Notion Skill。
3. 完全按 Skill 页面执行。该页会继续要求实时读取当前“余光所及”Agent 运行协议及现行权威页面。
4. 所有 `app.notion.com` 内容只通过 Notion MCP 访问。

如果 Notion MCP 不可用、页面读取失败或上游协议阻断，立即返回 `blocked` 并说明具体缺口。**不得**使用仓库缓存、旧 Prompt、历史成图或模型记忆模拟“余光所及”机制。

## 项目注入边界

仓库只决定“为什么做、要测试什么关系问题”；视觉实现由 Notion 当前机制决定。

允许传入的内容层信息：

- 目标人群
- 关系瞬间
- 一句话困惑
- 真实材料或演绎标记
- 本轮测试假设
- 平台、数量与是否成图

不要把关系主题强行变成知识卡、心理学海报或文字密集型轮播。最终图片首先必须是一组成立的“余光所及”作品。

## 输出

优先接收 Notion Skill 返回的 `sticker_manifest`。若当前环境具备生图能力，保存最终成图；若只有 Prompt，则明确标记 `prompt_ready`，不冒充成图完成。

推荐目录：

`outputs/stickers/YYYY-MM-DD/<slug>/`

至少保存：

- `manifest.json`
- `caption.txt`
- `titles.txt`
- 最终图片或最终逐图 Prompt

只保存本轮产物、必要元数据和来源页面 URL，不把 Notion 机制正文同步到仓库。

## 完成检查

- 本轮确实实时 fetch 了 Notion Skill；
- Notion Skill 内部依赖按当前协议执行，没有改用本地旧规则；
- 关系题只作为项目目的注入，没有覆盖“余光所及”视觉判断；
- `sticker_manifest` 状态与真实完成情况一致；
- 生成内容包含 AI 内容声明检查字段；
- 不自动公开发布。
