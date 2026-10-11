---
name: relationship-content
description: 在 lite_try 项目中把关系与处世创意编排为公众号文章、文字配图卡片、Huashu 视频或图片故事。用于今天做什么、新关系创意、一题多种内容或整套生产；先形成候选卡，选题确认后生产指定形式。
---

# 关系与处世内容总控

在项目根目录执行。先读 notes/BRAND_POSITIONING.md、notes/TOPIC_SELECTION_SYSTEM.md 和 notes/MULTIFORMAT_CONTENT_SYSTEM.md。当前品牌主要面向成人，IP 代表 Devin，妻子贡献经验与判断但不冒称已参与审阅。

## 入口

宽泛请求研究后给三张候选卡。每卡说明具体读者、场景、一个困惑、单一交付、材料与可迁移样本机制。用户选择后再写长稿和生成媒体；明确“做这个”视为已选择。整套输出四种形式；单一形式请求只制作该形式。

## 执行

1. 保存内容简报，区分真实材料、个人观点和演绎场景。平台研究走 Agent Reach 当前路由，样本拆解按 Creator Buddy 接入文档。
2. Gemini 直接生成初稿；主 Agent 核对材料，按需收集妻子的具体判断，再执行 deai-promax。吸引力看场景、冲突和推进，不用检测分数替代审稿。
3. 为每种目标形式独立改编，沿用同一核心判断。按 MULTIFORMAT_CONTENT_SYSTEM.md 的路由读取被选子技能及所需 references；不默认加载全部技能。
4. 视频以 huashu-art-motion 为主，先镜头表和检查，再 Visual Master Sheet 与单镜头包，按声音实际时长对齐。语音读取当前 Huashu narrator 绑定，不写死旧 ID。H3 使用真实动态片段。
5. 各形式按上游检查及实际目检验收，产物保存至 episodes/、build/，通过后导出 outputs/ 的新版本。

## 路由要点

文章写作与配文用已安装 Creator Buddy 子技能；公众号排版用 gzh-design；公众号封面与文字卡片用 guizang-social-card-skill；正文插画默认用项目派生 jiejie-illustrations，再交内置生图工具。hand-drawn 仅用于明确指定的其他画风。解解保留年轻化漫画比例，去掉发夹，不做成人化；识别符号按 BRAND_POSITIONING.md 的确认状态执行。cy-carousel 只在适合其 AI 科技笔记体裁时使用。微信图文变现技能仅在明确提出商业化任务时调用。

用户已要求自动化，常规尺寸、主题推荐和目录选择自行处理；创意拍板保留。上游固定科技配色、强制模板页数和与项目冲突的工作区路径不覆盖品牌及用户意图。

关系图文读取 notes/BRACKET_NARRATIVE_FORMAT.md。把归藏 Editorial 当作布局参考，内容采用原话、可能的理解、回应与关系变化的原创叙事语法；不复制快乐的小小我上下双格模板或他人固定角色。对标账号分别核实常态互动、内容结构、商业入口和成交证据；单篇高赞与商品露出不等于稳定变现。

交付可审阅文件与简短状态。不得凭 Skill 安装宣称成片生产已经跑通；不自动公开发布，不替用户妻子编造资历或审稿结果。
