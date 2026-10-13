# Changelog

## v0.7 — 2026-10-07
- 新增根目录 `AGENTS.md`，把项目级生产规约直接交给 Codex：默认 `understand → design → compile → code → render → inspect → revise`，而不是整片 prompt-to-video。
- 新增 `wm-video-producer`：当 Creative Gate 为 KEEP 且媒介包含视频时，从 Content Master / Video Concept 继续推进到 Production Manifest、art-motion Routing、Motion Plan、Keyframe/Prototype、Timing、Rough Cut、QA 和 Release Candidate。
- 新增 Production Orchestrator 与 `productions/<id>/production.yaml` 状态机，保存上游锁定项、当前 stage、风格/语法路由、资产来源、Codex `next_actions`、render 与 QA，使新的 Codex 会话可直接续跑。
- 新增 `video-production.schema.json` 与 CI validator，正式把 Production Manifest 纳入可测试系统资产。
- 全局视频生产策略升级为 **Codex-first**：代码负责场景、相机、节奏、转场、UI、分屏、长卷、合成、音频 cue、渲染与 QA；图片生成主要作为人物/sprite/纹理等资产来源。
- MiniMax H3 等生成式视频模型降级为**可选、可替换的特殊镜头资产**，不作为默认整片生产引擎；若使用必须记录理由、来源、设置与替换边界。
- art-motion 成为默认视频生产底座，但风格数量不设配额：每支片先评估完整风格/语法库，最后可以只用一个风格，也可以按章节、并行世界或短 speedrun 使用多个风格；每次风格变化必须有认知/空间/时间功能。
- F01 新增正式 `production.yaml`，当前 stage 为 `motion_plan_ready`，下一步锁定为 A/B/C lookdev 与 S2/S4/S7 三个最小运动原型。

## v0.6 — 2026-10-07
- F01 升级为 v0.4：删除“杯子固定放在左手边 → 酒店摸空 → 重复赋义”的支线，不再额外证明“普通事物因重复获得意义”。
- F01 核心重新收束为：**世界并行，人生串行；时间让第一人称经验只能从这一刻进入下一刻。**
- Video Concept / Director Proposal 升级为 approved v0.2，最终 Visual Proof 改为 `08:00:00 → 08:00:01`，不依赖象征性道具。
- 以 Git submodule 完整接入 `alchaincyf/huashu-art-motion`，锁定 2026-10-06 的 `26dba25b2b495c2138848c29a2c90df356a20325`，保留 MIT 归属与第三方声明。
- 新增 `renderers/art-motion/`，吸收 35 种艺术风格、9 种动画/解说语法、长卷、角色合成、转场与 QA 能力。
- 在上游能力之上新增 **Cognitive Motion Routing**：按每一段的认知任务选择动画语法，而不是按“哪种画风漂亮”选风格。
- 新增 F01 Production Design：首选 `Real → Many Worlds → Information → Highlights → Real`，多风格承担“世界并行”的论证，越接近结论视觉越简单。
- F01 正式进入首支视频 production：先做三方向 Keyframe，再做 S2 多世界 / S4 长卷 / S7 时间推进三个 Motion Prototype，之后进入旁白时间戳与 rough cut。

## v0.5 — 2026-10-01
- H01 正式 Retire，不再继续围绕标准时间 / 北京时间优化。
- 新建 F01《你连世界的一秒都活不完》Seed、Mechanism Run、Blueprint、Content Master 和完整文章 v0.1。
- F01 使用 Wish Fulfillment Stress Test：同时体验全部 → 逐个补看 → AI总结 → 只选最精彩。
- 作者写作基准升级为：**Cognitive Surprise > Knowledge / Truth Surprise**。
- wm-creative-director 升级 v0.2，加入 Wish Fulfillment、Cognitive Surprise、Strawman 防护。
- Golden 基线新增 F01 Candidate；H01 移入 Retired Cases。

## v0.4 — 2026-10-01
- 项目默认文化视角升级为 China-first, World-second。
- S01 获人工明确认可，升级为 Golden Case。
- 新增 wm-creative-director v0.1。

## v0.3 — 2026-10-01
- H01 放弃美国电报少年并尝试现代车票入口。
- S01 编译出第一份 Content Master 与文章试写。

## v0.2 — 2026-10-01
- H01 / S01 完成第一轮真实运行。
- Research 拆为 Pass A / Pass B。
- 建立 wm-research-agent。

## v0.1 — 2026-09-30
- 项目从科学视频工厂升维为世界机制故事引擎。
