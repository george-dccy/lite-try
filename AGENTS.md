# lite_try 项目约定

## 项目目标

这是“余光所及｜有解”的本地关系与处世内容生产项目：主要面向成人，从朋友、家庭、职场和亲子中的具体难题出发，形成文章、文字卡片、视频和图片故事。定位真源为 notes/BRAND_POSITIONING.md。
当前首期高德 ETA 只作为已停止的实验样片，不代表项目长期内容范围。

## 目录职责

- `.agents/skills/`：外部技能通过安装工具更新，不直接改上游内容；`relationship-content` 是本项目自有总控技能，`jiejie-illustrations` 是基于 Ian Xiaohei Illustrations 的项目派生技能，二者可按项目需求维护。Ian 原版单独保留，派生版保留来源与许可。
- `engine/`：从已安装技能复制出的本项目运行时；只为适配本项目目录和品牌配置而改，不反向修改 `.agents/skills/`。
- `research/`：事实链、来源台账和检索记录；原始来源与日期必须保留。
- `episodes/`：每期视频的口播、分镜、素材清单、代码工程和生成物。
- `build/`：渲染中间产物；可清理，不作为发布交付。
- `outputs/`：通过验收后导出的成片、字幕、封面和发布包；旧版本不覆盖。
- `notes/`：本项目方法论融合、决策和待确认事项。
- `notes/BRAND_POSITIONING.md`：品牌定位、内容母题、三类内容、IP 和新任务启动契约；属于本项目上层约束。
- `notes/TOPIC_SELECTION_SYSTEM.md`：项目级选题机制与选题卡真源；所有新题先经过这里的入口、材料和读者价值门禁。
- `notes/CREATOR_BUDDY_ADAPTER.md`：Creator Buddy 选题、爆款拆解、标题、口播和 B-roll 能力在本项目的接入规则。
- `notes/MULTIFORMAT_CONTENT_SYSTEM.md`：一题多种内容的流程、技能路由与交付标准；关系题材优先按此执行。

## 工作边界

- 先事实和口播，再视觉主表/镜头包，再渲染；动画只执行已确定的画面和运动，不替事实源发明内容。
- 外部来源、官方资料、截图和素材使用区间写入来源台账；未核实内容保留“待确认”，不当作事实。
- 不自动公开发布，不提交密钥，不执行 `git push`。
- 每次改动只运行与改动相关的检查；通过后停止，和本次无关的失败单独记录。
- 任何新内容先检查 `notes/BRAND_POSITIONING.md`，不要把单期题材当成账号定位。
- 任何新选题先检查 `notes/TOPIC_SELECTION_SYSTEM.md`；没有明确读者、单一交付和可核验材料时，不进入口播或制作。
- 写稿前，若存在可访问的同赛道样本，必须先按 `notes/CREATOR_BUDDY_ADAPTER.md` 完成开头、节奏、口播和画面拆解。

## 当前视频路线

- 当前内容主线为关系与处世；科技题材存档保留，不自动续做 AI 眼镜。使用 `relationship-content` 编排一题多种内容，视频以 Huashu 为主。

- 证据与流程借鉴 `investigation-video` / `video-common`。
- 机制解释和动态画面借鉴 `whiteboard-video` 与 `huashu-art-motion`，优先使用可复现的代码动画。
- 新选题先交给本机 Gemini CLI 生成初始口播；主 Agent 不先写一篇“研究说明”再让模型润色。
- 成稿面向自媒体观众：先讲一件值得看完的事，不在口播里解释搜索过程、模型过程或 Agent 的责任边界；事实核对放在台账和制作门禁里。
- 先定创意与 Visual Master Sheet，再按段选择 y2 Vox、t1 3B1B、y3 白板、真实图片/视频或 H3；H3 只执行确定的动作和时间，不重写故事、不生成文字。
- 语音默认走 Huashu 当前的 clone 配置和已绑定 speaker；凭证只走临时环境变量，不进项目文件。

## 新任务的简单启动

用户只需说“想一个关于 X 的视频”“今天做什么”或“来一个新创意”。Agent 先按 `notes/TOPIC_SELECTION_SYSTEM.md` 研究并形成候选选题卡：宽泛请求默认给 3 张，明确要求一张候选卡时给 1 张。用户拍板后才进入 Gemini 初始口播、事实核对、去 AI 味、Visual Master Sheet 和生产；不要在用户没拍板前擅自进入长稿、配音、H3 或渲染。
