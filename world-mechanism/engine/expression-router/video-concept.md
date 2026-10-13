# Video Concept Layer

Video Concept 是 Creative Blueprint / Content Master 与具体导演、生产之间的一层。

它不是 Storyboard，也不是生图 Prompt。

它回答：

> **这个认知机制，如何通过时间、画面、运动、声音和剪辑让观众“亲自看懂”？**

## Why this layer exists

很多视频只是：
> 旁白说观点 + 画面负责好看。

世界机制故事引擎需要进一步做到：

> **画面和声音本身承担论证。**

例如 F01：
- 分屏越分越多，直到每个生活都缩成不可持续观看的小格；
- 这不是装饰，而是在视觉上证明“覆盖全部 ≠ 真正体验”；
- 逐个回放变成近乎没有尽头的长卷；
- AI摘要更完整，却失去具体空间声；
- 精彩片段仍然只是互不连续的片段；
- 最终所有复杂系统退去，一个人物从 `08:00:00` 继续走进 `08:00:01`。

这种结构不能等到 Renderer 临时决定。

## Video Concept Contract

每个 Video Concept 至少包含：

### Core Cognitive Turn
观众看完以后，理解发生什么变化？

### Visual Argument
不用旁白，仅靠画面、运动和剪辑能证明哪一层？

### Temporal Device
时间如何被使用：
- 同时；
- 重复；
- 回放；
- 加速；
- 延迟；
- 分屏；
- 单镜连续；
- 时间戳；
- 跳切。

### Recurring Motif
必要时使用可重复、改义或建立连续性的视觉元素：
- 窗；
- 秒钟；
- 路口；
- 同一个动作；
- 同一个时间戳。

Recurring Motif 不是强制模板。不要为了“有一个象征物”硬造日常行为。

### Sound Argument
声音是否也承担机制：
- 多路声音叠加成噪声；
- 突然只保留一个人的环境声；
- AI摘要阶段变成干净信息播报；
- 回到生活后恢复空间感和呼吸。

### Beat Map
每一段必须写：
- Visual State
- Audio State
- Cognitive Function
- Transition

### Must Preserve
Renderer 不得为了“更电影感”、更方便生成或更多画风破坏核心认知结构。

## Good Video Concept

不是：
> “这里放日出延时，那里放城市夜景。”

而是：
> “画面数量从1变2、4、16、64，直到每个生活都无法持续观看；随后尝试逐个回放、摘要与高光筛选，最终所有系统撤走，只剩一条生活从这一秒进入下一秒。”

这叫 **Visual Proof**。

## Handoff is continuation, not a stop

Video Concept 之后：

1. Director Proposal；
2. 初始化 Production Manifest；
3. `wm-video-producer` / Production Orchestrator 接管；
4. art-motion 风格与动画语法路由；
5. Motion Plan；
6. keyframe / lookdev；
7. motion prototypes；
8. narration / word timing（若需要）；
9. rough cut；
10. QA / revision；
11. Release Candidate。

如果下一层可以机械推导，不应以“Video Concept 已完成”作为会话结束点。

## Production boundary

Video Concept 决定“画面和声音要证明什么”。

art-motion / Codex 决定“如何可靠地实现”。

MiniMax H3 等生成式视频模型若被使用，只能是 Production 层的可替换局部资产，不能反向成为 Video Concept 的出发点。
