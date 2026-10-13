# Renderers

Renderer 是“表达编译器”，不是选题引擎。

## 当前 Renderer

### art-motion

位置：`renderers/art-motion/`

完整吸收并锁定 `alchaincyf/huashu-art-motion` 作为底层动画生产引擎：

- 35种艺术风格配方；
- 9种解说/动画语法；
- 参数化片段；
- 长卷；
- 角色帧合成；
- 节奏、转场与 QA。

本项目在其上增加 **Cognitive Motion Routing**：不是按“哪种画风好看”选风格，而是按每一段的 cognitive job 选择动画语法与风格。

F01 是首个正式 production case。

## 其他候选
- story-film
- minimal-line / stickman
- whiteboard
- archive-collage
- documentary / evidence-mg
- article
- comic
- talk
- hybrid

其中 whiteboard / archive-collage / 部分 MG 能力已可优先通过 `art-motion` 的语法层实现，不再急于各造一套独立引擎。

## Renderer Contract
输入：
- 已确认 Blueprint
- 已确认 Content Master
- 已确认 Expression Concept / Video Concept
- 已确认 Director Proposal
- factual constraints
- must_preserve
- target audience
- target medium

输出：
- medium-specific Motion / Layout Plan
- storyboard / shot plan
- asset plan
- renderable scene specs
- picture track / clips
- audio timeline
- QA checklist
- production package

## 重要边界
- Renderer 可以改变节奏、镜头、版式、措辞长度。
- Renderer 不得改变核心问题、机制、世界规则和已确认事实。
- “当前模型擅长什么”只能影响表达策略，不能反向改写内容。
- 多风格必须服务认知结构；Renderer 不得为了展示能力把作品变成 showreel。
- Video Concept 与 Director Proposal 的 Locked 项优先于风格配方。

未来仍可吸收 stickman-video-director 的角色/clip contract，以及 Simon Skills 的素材覆盖、时间预算、来源台账与 QA 思想；这些能力应通过统一 Renderer Contract 进入，而不是各自接管上游创作逻辑。
