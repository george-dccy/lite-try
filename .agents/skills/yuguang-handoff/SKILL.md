---
name: yuguang-handoff
description: 接收一个“余光所及”Notion产物页 URL，把已确认的文字、Brief、Prompt或节拍表交接为本地排版、渲染、配音或发布包，并把结果链接和待发布状态回填产物库。
---

# 余光所及｜产物页到本地执行交接

在项目根目录执行。先读 `AGENTS.md`、`notes/BRAND_POSITIONING.md` 和 `notes/NOTION_HANDOFF.md`，再通过 Notion MCP fetch 用户提供的产物页 URL。Notion 是机制和内容真源；本技能不在仓库补写正文、Prompt 或视觉规则。

## 输入

输入必须是一个 Notion 工作台产物页 URL，适用于贴图、公众号长文和视频的本地执行交接。想象瞬间图静态生图不走本技能，直接进入 Notion v4.0，并记录在 07 发布包；只有明确要求代码视频版时才另行交接。读取并确认：

- 产物页正文；
- 属性 `仓库交接`、`状态`、`类型`、`平台`、`选题`、`生成任务`；
- 关联选题的 `内容线`、`认知转折`、`机制一句话`、`读者带走` 和 `测试假设`；
- 本轮需要读取的 Notion 机制页和执行范围。

首次访问数据库时先 fetch 真实 schema。贴图、长文和视频的真实交接字段在产物库，当前为 `仓库交接`、`状态`、`发布链接`；用户口中的“链接”按 `发布链接` 写入，不创建或假设名为 `链接` 的字段。07 发布包是想象瞬间图的唯一内容记录，不复制成产物库记录。

若产物页没有 `仓库交接`、没有可读正文、关联关系缺失或对应机制页不可读，立即返回 `blocked`，说明具体缺口。

## 执行路由

- **贴图组 / 公众号贴图**：输入应来自已完成 03/04、且已在产物库关联 03 的记录；按 `yuguang-sticker-bridge` 和 Notion 有解贴图生成器执行，只保存 Notion 已确认的图片、Prompt、标题、配文和 manifest，不重新设计双格机制。
- **公众号文章 / 长文**：正文必须已经在产物页；只用 `gzh-design` 排版和校验，按交接要求调用 Guizang 封面与 Jiejie 正文图。不要在本地补写文章。
- **视频**：读取 Notion 创意视频机制和产物页的 Brief、节拍表、`cues.json`、口播与 Prompt；简单片用 `engine/video-kit`，复杂片用 `world-mechanism/renderers/art-motion`。按关键帧 → 运动 → 声音 → 渲染 → §8 检查 → 独立评审执行。
- **世界机制故事**：保留 Notion S2–S3 的选题判断；深度制作按 `world-mechanism` 的 Content Master → Video Concept → Director Proposal → production manifest 路由。
- **想象瞬间**：静态生图仍在 Notion v4.0 完成；只有交接明确要求代码视频版时，才进入代码视频路由。

## 产物目录

新任务统一写入：

```text
productions/<YYYY-MM-DD-slug>/
```

生产目录沿用 `world-mechanism/engine/production-orchestrator/template-production.yaml`，并在 `production.yaml` 顶层增加：

```yaml
content_line: "有解｜关系与处世 | 世界机制 | 想象瞬间｜Edge of Sight"
notion_output_url: "<输入的产物页 URL>"
```

旧 `episodes/` 只读保留，不作为新产物目录。历史文件不覆盖；版本使用新的 slug 或候选目录。

## 回填协议

完成本地执行并通过相关检查后：

1. 将最终本地结果的绝对路径或可访问链接写入回填值；
2. 通过 Notion MCP 更新产物库真实字段 `发布链接`；
3. 将 `状态` 更新为 `待发布`；
4. 不填写阅读、播放、点赞、收藏、评论、新增关注或其他数据字段；
5. 回读刚更新的产物页，确认 `发布链接` 和 `状态` 已生效；
6. 返回产物 URL、本地生产目录、结果路径、验证结论和任何未解决问题。

不要自动公开发布。用户没有要求时，不改发布数据、不改关联选题、不修改 Notion 机制页。

## 阻断条件

- Notion MCP、产物页或依赖机制页不可读；
- `仓库交接` 未说明输入、执行范围或输出位置；
- 正文、Brief、节拍表或 Prompt 缺失，且补写会改变内容判断；
- 本地凭证、字体、素材或渲染依赖缺失；
- 需要删除历史文件、修改安装工具管理的上游技能，或遇到 Notion 也无法裁决的规则冲突。

遇到阻断返回 `blocked`，说明已读取的页面、已完成的检查和下一步所需输入，不用缓存规则绕过。
