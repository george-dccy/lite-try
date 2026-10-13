# 世界机制故事引擎 · World Mechanism Story Engine

> 借助模型加深人的思考与对世界的理解，再把这种理解编译成孩子和朋友愿意看、愿意读、愿意继续想的作品。

这个项目不是“一句话生成视频”的流水线。人的问题意识、文化位置、判断与设计在上；模型的研究、推演、写作和生产能力在下。

## 核心链路

问题 / 母题  
→ 必要时 Research Pass A  
→ Mechanism Explorer ↔ Creative Exploration  
→ Editorial Gate（KEEP / HOLD / REJECT）  
→ Creative Blueprint  
→ Research Pass B / Evidence Pack  
→ Content Master  
→ **Expression Concept（如 Video Concept）**  
→ **Director Proposal**  
→ **Production Manifest**  
→ **art-motion Routing**  
→ **Motion Plan / Keyframe / Prototype**  
→ Codex Production / Rough Cut  
→ QA + Revision  
→ Release Candidate / Human Release Gate  
→ Retrospective

**KEEP 之后的创意不再默认停在文案或方案阶段。**

如果媒介选择视频，`wm-video-producer` 与 Production Orchestrator 会把已确认的创意继续编译为可恢复的视频生产状态。

## 当前核心 Skills

- `wm-mechanism-explorer`
- `wm-research-agent`
- `wm-creative-director`
- `wm-video-producer`

Creative Director 当前优先级：

> **Cognitive Surprise > Truth Surprise > Gimmick Surprise**

以及：

> **Wish Fulfillment Stress Test**：不急着反驳读者的愿望，先真正满足它，再观察解决方案自己产生什么新问题。

Video Producer 当前优先级：

> **Codex-first > deterministic code/compositing > bounded generated assets > end-to-end generative video**

## Authorial Voice

项目保护：

> **让读者经历机制，而不是听作者宣布机制。**

### S01
“我不要推荐算法”  
→ 不断更换注意力分配机制  
→ 问题从“算法好不好”升级为“谁筛、为什么筛、能否切换”。

### F01
“同一时刻世界有无数生活，我为什么只能经历这一份？”  
→ 同时体验全部 → 逐个回放 → AI总结 → 只选最精彩  
→ 最终从“覆盖更多世界”转向“世界并行，人生串行”。

F01 v0.4 明确：

> **时间在这里首先不是‘重复赋予小事意义’，而是让第一人称经验只能从这一刻进入下一刻。**

因此别处正在发生的完整生活，不是“我这里缺掉的一块”。

## Video Concept Layer

视频不再只是“文章 + 配画面”。

Video Concept 先定义：
- Core Cognitive Turn；
- Visual Argument；
- Temporal Device；
- Sound Argument；
- Beat Map；
- Must Preserve。

F01 的核心 Visual Proof：

1. 分屏越分越多，直到所有生活都难以真正观看；
2. 逐个回放形成几乎没有尽头的长卷；
3. AI摘要让信息更完整，却让空间与关系消失；
4. 最精彩的片段仍然只是互不连续的片段；
5. 最后所有视觉系统撤走，只剩一个人物从 `08:00:00` 连续走进 `08:00:01`。

## Director Proposal Layer

Director Proposal 不重写机制，而把 Video Concept 转成可生产的导演决策：
- 固定人物策略；
- Visual / Sound Grammar；
- Sequence Map；
- Asset Strategy；
- Production Risks；
- Locked / Flexible。

F01 v0.4 已删除“杯子固定放在左手边”的重复赋义路线，不再用额外生活故事证明时间。

## Production Manifest

每个正式视频 production 建立：

`productions/<id>/production.yaml`

它记录：
- 上游创意与锁定项；
- 当前生产 stage；
- art-motion 风格 / 动画语法选择；
- 资产来源；
- Codex 当前目标与 `next_actions`；
- prototypes / rough cuts / release candidates；
- QA / blocker。

目的只有一个：

> **聊天可以结束，生产不能失忆。**

新的 Codex 会话先读 manifest，就能继续执行，而不是重新追问“我们上次做到哪了”。

## Art Motion Renderer

首个正式生产 Renderer：`renderers/art-motion/`。

底层锁定并完整接入 MIT 项目 `alchaincyf/huashu-art-motion`：
- 35 种艺术风格；
- 9 种动画/解说语法；
- 参数化片段；
- 长卷；
- 角色合成；
- 转场、音乐与 QA。

本项目在其上增加 **Cognitive Motion Routing**：

> 不按“哪种画风最漂亮”路由，而按“这一段要让观众经历什么认知动作”路由。

### 风格数量不是 KPI

每支片都先评估 art-motion 的完整能力库，但最后可以：
- 全片只用 **1 个风格**；
- 少量章节分别用不同风格；
- 不同并行世界使用不同风格；
- 只在一个短段快速跨风格；
- 代码世界 + 生成人物 / sprite 资产混合。

每一次换风格都必须有叙事、认知、空间或时间上的理由。

## Codex-first Production

后续视频生产以 Codex / coding agent 为主。

Codex 负责：
- 场景与动画代码；
- camera / timeline；
- transition；
- typography / UI / diagram；
- split-screen / long-scroll；
- 人物与生成图像合成；
- audio cue / FFmpeg / Playwright；
- deterministic render；
- QA / regression。

图片生成主要作为人物、sprite、纹理、背景 plate 等资产来源。

**MiniMax H3 等生成式视频模型不是默认整片生产引擎。**

只有某个特殊镜头的有机运动确实明显更适合 text/image-to-video 时，才把它作为有明确入/出点、可替换、记录来源的局部资产，然后重新纳入代码/剪辑管线。

## F01 First Production

F01 的第一支 production 采用：

> **Real → Many Worlds → Information → Highlights → Real**

多风格承担“世界并行”的论证，最终越接近结论，视觉反而越简单。

当前生产状态保存在：

`productions/F01-world-second/production.yaml`

Codex 下一步已经写入 manifest：
- A/B/C 三方向 lookdev；
- S2 多世界打开原型；
- S4 long-scroll 原型；
- S7 `08:00:00 → 08:00:01` 原型。

## Golden / Candidate / Retired

- A08：Golden Case
- S01：Golden Case
- F01：Golden Candidate v0.4 / first production case
- H01：Retired Case

## 不变边界

1. 理解世界是输入端，媒介只是输出端。
2. 第一联想只当 baseline。
3. Cognitive Surprise 优先于冷知识。
4. 中国视角不是地名换皮。
5. 固定爆款模板不是默认叙事结构。
6. AI 可以提出候选，但关键创作取舍保留给人。
7. F / I / H / R 必须分层。
8. 一个题可以被正式 Retire；沉没成本不是继续做的理由。
9. Renderer 不能把 Content Master 降格成“旁白配图”。
10. Video Concept 与 Director Proposal 的锁定项不能为了“更电影感”或“更多画风”被生产层改写。
11. 多风格必须承担叙事/认知功能，不能把作品变成能力 showreel。
12. 创意 KEEP 后应形成可续跑的 Production Manifest；会话结束不是生产结束。
13. 生成式视频模型是可选资产工具，不是默认创作架构。
