# Skills Roadmap

## 已实现

### wm-mechanism-explorer — v0.2
认知层入口 Skill。

负责 operationalize、Question Ladder、competing mechanisms、F/I/H/R、Mechanism Map 和反事实。

### wm-research-agent — v0.1
证据层 Skill。

- Pass A｜Premise Check
- Pass B｜Evidence Pack

### wm-creative-director — v0.2
创意方向 Skill。

当前核心规则：
- China-first, World-second；
- First Association Test；
- **Cognitive Surprise > Truth Surprise > Gimmick Surprise**；
- **Wish Fulfillment Stress Test**；
- Audience Distance；
- Form Fit；
- Author Fit；
- KEEP / HOLD / REJECT。

S01 和 F01 共同证明：
> 很多有作者气质的内容，不是“找到一个更奇怪的事实”，而是先认真满足读者的直觉愿望，再让解决方案自己暴露隐藏机制。

### wm-video-producer — v0.1
视频持续生产 Skill。

解决“创意生成完以后流程断掉”的问题。

当候选进入 KEEP 且媒介包含视频时，它继续推进：

> Blueprint → Content Master → Video Concept → Director Proposal → Production Manifest → art-motion Routing → Motion Plan → Keyframe / Prototype → Timing → Rough Cut → QA → Release Candidate

默认：
- **Codex-first**；
- `renderers/art-motion/` 为默认视频生产底座；
- 每支片都评估完整风格/动画语法库，但可最终只使用一个风格；
- 多风格必须有认知/空间/时间功能，不为炫技；
- 图片生成作为人物/sprite/纹理等资产来源；
- MiniMax H3 等生成式视频模型只做有明确理由、可替换的特殊镜头，不做整片主引擎；
- 用 `productions/<id>/production.yaml` 记录生产状态和 Codex 下一步，支持跨会话续跑。

## 下一批

1. wm-story-builder
2. wm-expression-router
3. wm-reviewer

其中视频 production 已不再等待完整 `wm-expression-router` 才能继续；`wm-video-producer` 可以接管已明确的视频项目。

原则：
- 每个 Skill 有明确输入输出；
- 关键 Gate 不隐式通过；
- Routine engineering decision 不升级成不必要的人工作业；
- Skill 可替换，schema 和 Golden Cases 尽量稳定；
- 先让方法变好，再让流程变快；
- 创意通过后要形成可续跑生产状态，而不是停留在一次回答里。
