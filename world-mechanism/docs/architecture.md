# Architecture v0.2

## 1. 总原则
> **理解层独立于表达层，表达层独立于生产工具；生产工具必须可替换，但生产状态必须可继续。**

不能让“今天哪个模型最强”“某种画风正火”反向决定我们思考什么、怎么理解、讲什么。

同样，也不能让一个好创意在进入生产时丢失上下文，只能依赖某次聊天继续。

## 2. 核心不是直线，而是双入口回路

### Route A — Question-first
真实困惑 → Mechanism Explorer → Creative Exploration

### Route B — Spark-first
有生命力的母题 → Creative Exploration → Mechanism Explorer

两条路线都必须经过：
**Mechanism ↔ Creative Exploration → Editorial Gate → Creative Blueprint**

为什么这样设计：
- 好问题需要创意把机制变成可感受的世界；
- 好母题也需要机制探索避免沦为漂亮空壳；
- 不把“母题先于机制”和“理解世界是核心”做成二选一。

## 3. 七层架构

### Layer A — Capture
输入可能是：
- 真实问题；
- 观察；
- 新闻；
- 历史细节；
- 知识点；
- 一个突然出现的世界规则或关系母题。

产物：`Question Seed` 或 `Creative Seed`。

### Layer B — Mechanism
拆 actors、forces、constraints、incentives、flows、feedback loops、thresholds、time scale、information asymmetry、path dependence。

产物：`Mechanism Map`。

### Layer C — Creative Exploration
发散母题、反事实和人物行为，检查同一规则是否能持续产生状态变化。

产物：`Creative Candidates`。

### Layer D — Editorial + Blueprint
总编辑负责淘汰与保真；Creative Blueprint 把问题、机制、规则、人物任务、知识载荷与 Must Preserve 锁为跨媒介接口。

产物：`Creative Blueprint`。

### Layer E — Research + Content Master
查事实、原始资料、历史脉络与争议边界，把 Fact / Interpretation / Hypothesis / Fictional Rule 分开，再形成媒介无关的故事或内容母版。

产物：`Evidence Pack` + `Content Master`。

### Layer F — Expression
判断媒介如何承担认知任务。

视频进一步拆为：
- `Video Concept`：画面/运动/声音如何完成 Visual Proof；
- `Director Proposal`：人物、镜头、声音、Sequence、资产和风险。

表达层不能被具体生成模型反向决定。

### Layer G — Production Orchestrator + Renderer
把已确认表达继续编译为真正可运行、可恢复的生产工程。

视频默认：

> `wm-video-producer` → `Production Manifest` → `art-motion routing` → `Codex production` → `QA / revision`

产物：
- `production.yaml`；
- Motion Plan；
- lookdev / keyframes；
- prototypes；
- narration timing；
- runnable code；
- rough cuts；
- QA logs；
- Release Candidate；
- Retrospective。

## 4. Production Manifest 是生产阶段的核心中间语言

Creative Blueprint 是跨媒介稳定接口。

进入视频以后，`productions/<id>/production.yaml` 是生产状态稳定接口。

它记录：
- 上游 source artifacts；
- Must Preserve；
- 当前 stage；
- art-motion 风格与语法路由；
- Codex 当前任务与下一步；
- 资产来源；
- 原型结果；
- render candidates；
- QA 状态；
- blocker。

因此：

> **聊天可以结束，生产不能失忆。**

新的 Codex 会话必须能从 manifest 继续，而不是重新发明创意。

## 5. 默认视频生产技术栈

### 主体：Codex / code-driven production

默认负责：
- Canvas / SVG / DOM / JS / Python；
- camera / timeline；
- transition；
- typography；
- diagrams / UI；
- split screen；
- long scroll；
- sprite / generated-image compositing；
- audio cues；
- Playwright / FFmpeg render；
- deterministic QA。

### 默认 Renderer：art-motion

`renderers/art-motion/` 在 `third_party/huashu-art-motion` 的完整能力之上增加认知路由。

每一支片都先评估它的：
- 艺术风格库；
- 解说/动画语法；
- camera / transition；
- long-scroll；
- compositing；
- QA。

但可以最终只选择一个风格。

风格数量是创作变量，不是 KPI。

### 图片生成：资产工具

适合人物 keyframe、sprite、复杂有机物、纹理与背景 plate。

由代码接管位置、镜头、节奏、材质和连续性。

### 生成式视频：例外性资产工具

MiniMax H3 等 text/image-to-video 模型不承担默认整片生产图。

只有特定镜头明显更适合生成式有机运动时才使用，而且必须：
- 有明确入/出点；
- 可替换；
- 记录模型/参数/来源；
- 通过代码/剪辑管线统一整合；
- 不得让随机生成结果反向改写上游创意。

## 6. 人工 Gate

1. **Question / Mechanism Gate**：这真是我想弄明白的问题吗？
2. **Creative Gate**：哪个候选 KEEP / HOLD / REJECT？
3. **Blueprint Gate**：核心机制和 Must Preserve 是否确认？
4. **Direction Gate**：若视觉方向存在实质分歧，选哪条？
5. **Prototype Gate**：关键新运动机制是否值得扩展到整片？
6. **Release Gate**：最终作品是否忠于上游且值得发布？

生产层可以高度自动化，Routine engineering decision 不默认升级成人工 Gate。

## 7. Notion 与 GitHub

### GitHub：系统真源 + 生产真源
保存稳定、可版本化、可测试、可续跑的能力和生产状态：
- engine；
- schemas；
- skills；
- renderer contracts；
- golden cases；
- regression checks；
- architecture decisions；
- Production Manifest；
- runnable production code；
- QA logs。

### Notion：创作者驾驶舱
保存活的、尚在形成中的内容：
- 问题火花；
- 阅读与观察；
- 选题池；
- 项目状态；
- 临时研究材料；
- Blueprint 工作稿；
- 作品链接；
- 个人复盘。

原则：**Notion 不复制全部规则；GitHub 不吞掉人的思考轨迹。**

## 8. 两个稳定接口

### Creative Blueprint
保证：Renderer / 媒介变化时，创作核心不丢。

### Production Manifest
保证：Codex / 会话 / 生产工具变化时，生产进度不丢。

这两个接口共同把项目从“好 Prompt”变成“可持续创作系统”。
