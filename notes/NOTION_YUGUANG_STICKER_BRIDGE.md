# 余光所及关系贴图｜Notion Bridge

更新日期：2026-10-11

## 定位

本文件只保存 `lite-try` 到 Notion「余光所及」关系贴图入口的**连接契约**。它不是视觉机制副本，也不保存人物、穿搭、镜头、光感、参考学习、Prompt Grammar、文案或 07 回写规则。

Notion 中的现行「余光所及」机制始终是视觉生产 Single Source of Truth。仓库不得把其正文复制回来做缓存或 fallback。

## 唯一入口

- Notion Skill：`余光所及｜有解贴图生成器｜lite-try 适配入口`
- URL：`https://app.notion.com/p/3f627110f8d581918bf3de93e837a339`
- 上游项目：`余光所及｜多账号内容生产系统与视觉连载试验`

## 调用要求

当请求属于公众号贴图、图片消息、小绿书式轻图文、关系场景图片组、贴图冷启动实验时：

1. 读取 `notes/BRAND_POSITIONING.md`，确认仍服务「余光所及｜有解」的关系与处世定位。
2. 加载 `.agents/skills/yuguang-sticker-bridge/SKILL.md`。
3. 通过已连接的 **Notion MCP** fetch 上述 Notion Skill 页面。
4. 完全按该页面执行；页面内部会要求实时读取当前「余光所及」Agent 运行协议及其现行权威页面。
5. 不先复制或重建 Notion 视觉规则，不拿仓库旧 Prompt、历史成图或模型记忆替代实时 fetch。
6. 如果 Notion MCP 不可用、Skill 页面不可读或上游协议依赖失败，停止并报告 `blocked`；不得静默降级为本地仿制机制。

所有 `app.notion.com` 内容只通过 Notion MCP 访问，不使用普通网页抓取。

## 输入层

仓库只向 Notion 注入本轮业务目的与内容输入，例如：

- 目标人群
- 具体关系瞬间
- 一句话核心困惑
- 可选的测试假设
- 可选的平台与数量要求

贴图 fast lane 不要求先完成长文章、完整母稿或常规 18 字段正式选题卡。若用户明确要求从既有正式选题派生，则复用已经确认的内容判断。

## 输出与落库

Notion Skill 应返回一个 `sticker_manifest`。仓库接收后，发布包保存到：

`outputs/stickers/YYYY-MM-DD/<slug>/`

建议包含：

- `manifest.json`
- `caption.txt`
- `titles.txt`
- `prompts/`（保留最终逐图 Prompt 时）
- `images/`（当前运行环境能够取得最终图片文件时）
- `notes.md`（仅记录本轮必要说明，不复制 Notion 机制正文）

manifest 至少保留：Notion Skill URL、主题、关系瞬间、测试假设、图片数量、执行模式、状态和 AI 内容声明检查结果。

## 从贴图升级成长内容

贴图首先用于低成本验证。某一关系题表现值得放大时，再回到 `relationship-content` 的常规路径，按 `TOPIC_SELECTION_SYSTEM.md` 与 `MULTIFORMAT_CONTENT_SYSTEM.md` 进入文章、卡片或视频生产。

贴图数据可以成为选题证据，但单次高阅读不自动等于长期结论。
