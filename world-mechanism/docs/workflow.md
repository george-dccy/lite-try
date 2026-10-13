# Human–AI Workflow v0.3

## Stage 0 — Capture
记录一个真正让人想追问的东西，或者一个突然出现的有生命力母题。

### 问题型输入
- 我看到了什么？
- 哪里让我觉得奇怪？
- 我为什么会在意？
- 我现在最想知道什么？

### 母题型输入
- 这个怪事 / 关系 / 规则为什么本身就让我想看后来？
- 它最先改变人的哪个动作？
- 不解释意义，它还能继续长吗？

## Stage 1 — Choose Entry Route

### Route A：Question-first
先进入 Mechanism Explorer，再进入 Creative Exploration。

### Route B：Spark-first
先保护母题，在创意室做繁殖测试，再回 Mechanism Explorer 检验它照亮了什么现实机制。

两条路线可以往返，不强制一次完成。

## Stage 2 — Operationalize + Research Pass A

对于历史、科学、技术、社会等事实依赖题，创意前先做一次轻量前置研究。

只回答：
- 关键术语到底指什么？
- 核心前提是否真实？
- 时间、地点、人群、制度范围是什么？
- 哪些说法是 F / I / H / R？
- 有没有一个事实错误会让整个创意失效？

对于社会反事实，额外写清：
- 拿走什么；
- 保留什么；
- 允许哪些替代机制。

Pass A 不是完整调研，不堆材料。

## Stage 3 — Mechanism Exploration

目标不是出内容，而是让问题变深。

AI 可以：
- 提出不同层级追问；
- 给 2–4 个机制候选；
- 区分 Core mechanism / Supporting pressures / System consequences；
- 指出反例和边界；
- 建议证据缺口；
- 做反事实推演。

人要做：
- 选择真正值得继续的问题；
- 标记“虽然对但没意思”的解释；
- 加入自己的生活经验；
- 决定何时停止拆解。

## Stage 4 — Creative Exploration

根据任务选择模式。

### Discovery Mode
适合从零选题。可以广泛产生 10–20 个母题，再筛选。

### Focused Mode
适合已经有强问题或 Mechanism Map。只生成 3–5 个结构差异明显的 Creative Hypothesis，不为数量而数量。

Focused Mode 重点检查：
- 这个机制可以变成哪几种不同表达？
- 是否必须故事化？
- 哪种表达最能暴露机制，而不是最容易生产？

## Stage 5 — Counterfactual Design

低不确定、规则清晰时可以使用 consequence ladder：
- first order；
- second order；
- third order。

高不确定社会系统优先使用：
- branching scenarios；
- replacement mechanism matrix；
- conditional consequences。

不要把“可能”写成一条确定的 Day 1 → Day 3 → Day 7 预测。

## Stage 6 — Editorial Gate

总编辑负责淘汰，而不是把平庸创意修漂亮。

### Story / Fable
检查：
- 外部任务；
- 重复动作改义（仅在该作品确实需要时，不作为固定模板）；
- 状态变化；
- 人物自主性；
- 去寓意后是否仍值得看。

### Essay / Explainer
检查：
- 是否有真正的认知冲突，而不是结论先行；
- 是否保留 competing mechanisms / trade-offs；
- 每一节是否改变读者对问题的模型；
- 是否把价值判断留给读者，而不是伪装成事实。

### Investigation / Documentary
检查：
- 事实链；
- 证据强度；
- 反方解释；
- 结论是否超过证据。

输出：`KEEP / HOLD / REJECT`。

**只有 KEEP 才进入持续生产链。**

## Stage 7 — Creative Blueprint

把问题、机制、规则、人/系统、任务或阅读推进、知识载荷、开放问题和 Must Preserve 统一到媒介无关对象。

**没有 Blueprint，不进入正式生产。**

Blueprint 可以没有 story 字段，前提是它明确自己的 primary mode。

## Stage 8 — Research Pass B

Blueprint 形成后再做完整 Evidence Pack（若事实依赖题需要）：

- claim ledger；
- 原始来源；
- 争议解释；
- 时代 / 地域 / 人群边界；
- 人物和制度细节；
- 可视化事实；
- 素材来源；
- 不得强化的说法。

Research Pass B 可以修正 Blueprint 的事实层，但不能偷偷重写已确认的创作核心。

## Stage 9 — Content Master

形成媒介无关的内容母版，锁定：
- 核心认知转折；
- 结构；
- 必须保留的句子 / 情节 / 事实；
- 不希望作品滑向的解释；
- 可压缩、可改写与不可改写部分。

这里不是最终脚本，也不是镜头表。

## Stage 10 — Expression Routing

根据内容判断媒介，而不是根据“当前最强模型”判断。

如果选择视频，继续生成：

1. `Video Concept`：画面、运动和声音怎样亲自完成论证；
2. `Director Proposal`：人物、镜头、声音、Sequence、资产和风险；
3. 初始化 `Production Manifest`。

**视频表达一旦确定，不应停在创意文档等待下一次人工重新启动。**

## Stage 11 — Video Production Continuation

视频项目默认由 `wm-video-producer` + `Production Orchestrator` 接管。

状态链：

```text
KEEP
→ Blueprint
→ Content Master
→ Video Concept
→ Director Proposal
→ Production Manifest
→ art-motion Routing
→ Motion Plan
→ Keyframe Gate
→ Prototype Gate
→ Narration / Timing
→ Rough Cut
→ QA / Revision
→ Release Candidate
```

除真正需要作者判断的 Gate 外，完成一个阶段后应继续生成下一个可机械推导的产物，不以“创意已经给出”作为结束条件。

## Stage 12 — art-motion Routing + Codex Production

### 默认视频底座

所有新视频首先评估：

`renderers/art-motion/` + `third_party/huashu-art-motion`

不是要求把所有风格都用一遍，而是从完整能力库中做选择。

可选策略：
- `single_style`：全片一个风格；
- `sectional_styles`：少量风格对应不同章节；
- `parallel_world_styles`：不同世界/视角并存不同风格；
- `speedrun_styles`：短段快速跨风格；
- `hybrid_assets`：代码世界 + 生成人物/图像资产。

每个风格必须能回答：
> 它在这里承担什么认知、空间、时间或情绪功能？

不能只因为“好看”而换风格。

### 默认生产者：Codex

Codex / coding agent 负责主生产图：
- 场景代码；
- 相机；
- 动画；
- 转场；
- 排版；
- 分屏 / 长卷 / 图表 / UI；
- 角色与图片资产合成；
- 音频 cue；
- FFmpeg / Playwright 渲染；
- QA 与回归。

图片生成是资产来源。

MiniMax H3 等生成式视频模型只作为**可替换的特殊镜头资产**，不作为整支片默认主引擎。只有代码 + 图像/sprite 明显不适合某个有机运动镜头时才使用，并记录原因、模型、参数和替换边界。

## Stage 13 — Production Gates

### Direction Gate
视觉方向真正开放时，先做 2–3 个同一代表时刻的 keyframe / lookdev，再选方向。

### Prototype Gate
先验证 1–3 个最难、最关键的运动机制，再做整片。

### Rough-cut Gate
先形成端到端 rough cut，检查逻辑、节奏、视觉论证、声音论证和连续性，再做高成本精修。

### Release Gate
最终 Release Candidate 必须由人确认。

Routine engineering decision 不新增人工 Gate。

## Stage 14 — QA + Revision Loop

验收维度：
- Mechanism QA；
- Motion QA；
- Style QA；
- Camera / framing QA；
- Audio QA；
- Continuity QA；
- Subtitle safe-zone；
- Independent Review。

问题统一记录：

> timecode → symptom → root cause → change → recheck

同类问题两种修法仍失败时，向上判断是 asset / renderer / motion plan / director / concept / content 哪一层出错，不在下游无限抛光。

## Stage 15 — Release + Retrospective

1. 做之前怎么理解？
2. Pass A / Pass B 分别纠正了什么？
3. 哪个机制真正改变了我的看法？
4. 为了好看牺牲了什么？
5. 哪个观众反应暴露了新问题？
6. 哪个机制值得进入机制库？
7. 哪条生产能力值得回流 art-motion adapter / engine？
8. 哪条规则只是这个案例特例，不应泛化？

## Resume Rule

任何新的 Codex / Agent 会话处理已有视频项目时，先读：

1. `productions/<id>/production.yaml`
2. Content Master
3. Video Concept
4. Director Proposal
5. Motion Plan
6. 最新 QA log

然后直接执行 manifest 中的 `codex.next_actions`。

**不要因为聊天上下文消失而重做创意阶段。**
