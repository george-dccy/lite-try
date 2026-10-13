# lite-try 重构盘点与迁移决策（2026-10-12）

## 盘点范围与结论

本报告记录重构开始前的只读盘点。现行机制以 Notion 为准；本地仓库只保留可版本化的执行规则、运行时、历史产物和交接协议，不复制 Notion 的机制正文。

已通过 Notion MCP 读取的运行入口：

- 导航页：<https://app.notion.com/p/3d527110f8d581b3b3c2f53574559f94>（人看的地图，不作为运行规则）
- 工作台：<https://app.notion.com/p/3f727110f8d5813e9b22dbeff5ebdd9c>（S1–S5 总入口）
- 写作机制：<https://app.notion.com/p/3d727110f8d5816dbed0f5360d37014b>
- 创意视频机制：<https://app.notion.com/p/3f727110f8d5812da32dd21d59e30131>
- 视频附录脚手架：<https://app.notion.com/p/3f727110f8d581409fc6efb83e348eb0>
- 有解贴图适配入口：<https://app.notion.com/p/3f627110f8d581918bf3de93e837a339>
- 生图运行协议 v4.0：<https://app.notion.com/p/3da27110f8d5819b835ac3154cec5e3a>

明确不读取 Notion 历史归档页：<https://app.notion.com/p/3f727110f8d5810599c1e0fa6aedc761>。导航页已明确该页不是运行入口。

实时读取到的数据库事实：

- 想法库：`collection://2172cbcb-6c94-4836-a266-5601ef730bbe`
- 选题库：`collection://5049912e-16d6-4754-af52-05622859c116`
- 产物库：`collection://b10d972d-cdda-4b95-98ab-a6d4354a7439`
- 产物库真实交接字段为 `仓库交接`、`状态`、`发布链接`。后续文档中的“回填链接”均按实际 schema 写 `发布链接`，不假设不存在的 `链接` 属性。
- 03 / 04 / 07 的当前数据库也已读取；它们分别是 03 生成任务库、04 逐图 Prompt / Shot Plan、07 内容任务与发布包库。

## 与现行 Notion 的冲突

| 现有仓库规则或资产 | 冲突 | 处理 |
| --- | --- | --- |
| `relationship-content` 宽泛请求先在仓库形成候选卡 | 工作台要求 S1–S3 在 Notion 落想法、选题，并在 S3 停在 KEEP / HOLD / REJECT | 技能改为 Notion 工作台路由；仓库不再写本地候选卡 |
| `TOPIC_SELECTION_SYSTEM.md`、`ARTICLE_EDITORIAL_WORKFLOW.md`、`AUTHOR_VOICE_GUIDELINES.md` 等本地方法正文 | 写作机制 v1.0 已合并这些内容，Notion 是唯一文字机制 | 归档，原位保留短指针；只留下仓库独有执行细节 |
| `MULTIFORMAT_CONTENT_SYSTEM.md` 与旧视频路线 | 工作台规定成品文字、Prompt 和视频 Brief 在 Notion 完成，仓库只渲染、排版、整理和回填 | 归档方法正文；执行路由写入根规则和 `notes/NOTION_HANDOFF.md` |
| `WECHAT_VISUAL_*`、`BRACKET_NARRATIVE_FORMAT.md` | 写作机制 §5、§7 已定义关系叙事、封面、正文图和公众号排版边界 | 归档机制正文；保留 gzh-design、guizang、jiejie 的调用和验证细节 |
| `yuguang-sticker-bridge` 的本地 Fast Lane 约定 | Notion 贴图生成器已经内置双格版式和当前输入/输出契约 | 同步为实时 Notion MCP 入口；不复制视觉规则 |
| lite-try 当前以 Huashu 为主路线 | 创意视频机制规定代码画面、代码声音、同一 `cues.json`、关键帧 → 运动 → 声音 → 渲染 | Huashu 保留为配音/参考能力；简单代码片从 `engine/video-kit` 起步，复杂片走 art-motion |
| 当前 `episodes/` 作为新产物目录 | 新项目要求统一采用 `productions/<YYYY-MM-DD-slug>/production.yaml` | `episodes/` 只保留历史，不迁移；新内容不再写入 |
| `STYLE_SELECTION.md` 的 AI 眼镜/旧视频实验说明 | Notion 当前内容主线和视频入口已改为三条内容线与代码视频机制 | 归档为历史记录，不作为新任务规则 |

## lite-try 文件与目录处理表

| 路径 | 决策 | 理由 / 后续动作 |
| --- | --- | --- |
| `AGENTS.md` | 重写 | 升级为“余光所及”三内容线本地执行仓库规则，声明 Notion 真源、人工 Gate、路由、生产目录和边界 |
| `.gitignore` | 保留并按需补充 | 现有 build、依赖、环境变量忽略规则仍适用；不忽略新 `productions/`，因为生产 manifest 和执行状态需入库 |
| `skills-lock.json` | 保留，不加入 wm 技能 | 它只记录安装工具管理的上游技能；项目自有和合并进来的 `wm-*` 不进入锁文件 |
| `notes/BRAND_POSITIONING.md` | 保留并对齐 | 保留“有解”关系线、解解与材料边界；新增世界机制故事、想象瞬间两条内容线，并把 Notion 现行机制置于上层 |
| `notes/ARTICLE_EDITORIAL_WORKFLOW.md` | 归档 + 原位指针 | 方法正文已并入写作机制；gzh-design 等仓库执行细节转入执行说明 |
| `notes/AUTHOR_VOICE_GUIDELINES.md` | 归档 + 原位指针 | 作者表达指纹已在写作机制 §3 原样保留 |
| `notes/TOPIC_SELECTION_SYSTEM.md` | 归档 + 原位指针 | S1–S3 和 KEEP / HOLD / REJECT 以 Notion 工作台为准 |
| `notes/MULTIFORMAT_CONTENT_SYSTEM.md` | 归档 + 原位指针 | 一题多出口和 S4 交付以工作台、写作机制、视频机制为准 |
| `notes/WECHAT_VISUAL_STYLE_SYSTEM.md` | 归档 + 原位指针 | 视觉方法正文以 Notion 写作机制 §7 与生图协议为准；保留仓库调用边界 |
| `notes/WECHAT_VISUAL_DIRECTION_V2.md` | 归档 + 原位指针 | 属于旧样张/审阅记录，不能继续充当新视觉真源 |
| `notes/BRACKET_NARRATIVE_FORMAT.md` | 归档 + 原位指针 | 括号叙事已进入写作机制关系长文骨架；不在仓库维护第二份正文 |
| `notes/CREATOR_BUDDY_ADAPTER.md` | 拆分 | 写作、标题和视频方法部分归档；Agent Reach 路由、对标筛选口径等仓库执行细节保留 |
| `notes/NOTION_YUGUANG_STICKER_BRIDGE.md` | 合并为 `notes/NOTION_HANDOFF.md`，原位改指针 | 统一贴图和产物页交接协议；保留旧路径兼容指针，不删除历史文件 |
| `notes/METHODOLOGY_FUSION.md` | 归档 + 原位指针 | 旧的多技能视频融合方案被 Notion 视频机制和新根路由替代 |
| `notes/STYLE_SELECTION.md` | 归档 + 原位指针 | 旧期风格选择和 AI 眼镜实验不再作为新任务规则 |
| `notes/VISUAL_IP_AND_ACCOUNT_NAME.md` | 保留并校准 | 账号名、解解参考图路径和仓库资产边界是项目执行信息；去除与 Notion v4.0 冲突的固定生图规则 |
| `notes/VOICE_INTEGRATION.md` | 保留 | Huashu 当前绑定配置、临时凭证边界和音频回执是仓库独有执行细节 |
| `notes/REPOSITORY_ADOPTION_20261011.md` | 保留 | 记录上游安装来源、提交和许可，属于仓库治理证据 |
| `notes/huashu-voice-config.json` | 保留 | 只含当前绑定配置，不写入凭证；供配音执行读取 |
| `research/` | 保留 | 事实来源、视觉参考和历史研究是执行证据；不把 Notion 机制正文复制到这里 |
| `episodes/` | 保留为历史 | 已完成/停止实验的样片和历史制作记录不迁移、不覆盖；新产物统一进入根 `productions/` |
| `build/` | 保留 | 渲染中间产物，可清理，不作为发布交付 |
| `outputs/` | 保留 | 历史发布包继续可追溯；新导出仍保留版本，不覆盖旧文件 |
| `engine/voice/` | 保留 | Huashu 配音执行器是仓库独有能力 |
| `engine/whiteboard-video/` | 保留为参考/兼容执行器 | 根路由不再将其作为视频主路线，但历史样片和手绘执行仍可复现 |
| `.agents/skills/relationship-content/` | 修改 | 宽泛请求改走 Notion S1–S3；“做这个”从产物页交接开始；保留关系内容线的本地执行路由 |
| `.agents/skills/yuguang-sticker-bridge/` | 修改 | 输入、先落产物库、实时读取 Notion、生图/Prompt-only 状态和 `sticker_manifest` 与新交接协议同步 |
| `.agents/skills/jiejie-illustrations/` | 保留并修正指针 | 作为公众号正文图执行技能保留；方法依据 Notion，保留 `research/visual-ip/explainer-boy-v1.png` 路径和不覆盖旧资产的细节 |
| `.agents/skills/ian-xiaohei-illustrations/` 及其他已安装技能 | 保留 | 上游安装内容不改；只在根路由中声明主次关系 |
| `engine/video-kit/` | 新增 | 从 Notion 视频附录同步 6 个可运行文件，作为简单代码视频的最小执行器 |
| `productions/` | 新增 | 采用 world-mechanism 的 `production.yaml` 生产状态契约，增加 `content_line`、`notion_output_url` |

## world-mechanism-story-engine 文件与目录处理表

| 路径 | 决策 | 理由 / 后续动作 |
| --- | --- | --- |
| `AGENTS.md` | 合并后保留并加顶部指针 | 子目录继续维护世界机制生产约定；顶部声明上层根规则和 Notion 现行机制优先 |
| `PROJECT.md` | 保留 | 说明世界机制引擎的目标、文化视角和内容边界，是世界机制内容线的项目背景 |
| `docs/` | 保留 | 记录世界机制的架构、研究、文化视角、工作流、风格路由和测试；不取代 Notion 的内容创意机制 |
| `engine/` | 保留 | 机制探索、研究、创意蓝图、表达路由、质量和生产编排是可版本化执行能力 |
| `schemas/` | 保留 | Blueprint、Evidence Pack、Video Concept、Director Proposal、Production 的结构校验契约 |
| `skills/wm-*` | 保留 | 四个项目自有世界机制技能及 references/evals 需保留原位，供子项目测试和追溯 |
| `.agents/skills/wm-*` | 新增入口 | 在顶层建立发现入口，指向 `world-mechanism/skills/wm-*`；不复制进 `skills-lock.json` |
| `renderers/art-motion/` | 保留原位 | 子仓库已有相对路径、上游锁和生产说明；作为全仓共用 renderer 时由根 `AGENTS.md` 统一指向此处，避免移动造成无价值的路径改写 |
| `third_party/huashu-art-motion` | 保留子模块关系 | art-motion 的上游依赖和锁定来源继续由子目录约定管理；测试不因上层路由改写 |
| `content-masters/` | 保留 | 世界机制内容母版是深度制作输入；新选题前端仍在 Notion S2–S3 |
| `productions/` | 保留为子目录历史/示例 | 原有 F01 生产状态、模板和素材保持历史可回放；跨内容线新任务写根 `productions/` |
| `runs/` | 保留 | 研究、创意和编辑运行记录属于世界机制历史证据 |
| `tests/` | 保留并运行 | golden cases、retired cases 和技能回归保护迁移完整性；无关旧失败只记录 |
| `scripts/` | 保留 | schema/skill 校验脚本是本地执行能力 |
| `requirements-dev.txt` | 保留 | 合并后按它安装 Python 测试依赖并运行 pytest |
| `CHANGELOG.md`、`README.md`、`THIRD_PARTY_NOTICES.md`、`.gitmodules` | 保留 | 版本历史、使用说明、许可和子模块声明需要随提交历史进入子目录 |

## 执行顺序与成功标准

1. 在当前干净分支 `restructure/yuguang-v4` 上用 `git subtree add --prefix=world-mechanism ... main` 合并，并保留 world-mechanism 历史。
2. 只做必要的规则指针、技能入口、`video-kit` 和交接协议修改；不改原仓库，不改安装工具管理的上游技能，不删除历史文件。
3. 验证：world-mechanism 测试通过或明确记录无关失败；`engine/video-kit/run.sh` 产出 4.000 秒成片并检查响度/真峰；路径引用检查通过；Notion 当前入口和数据库 URL 可读。
4. 每个阶段小步提交，commit message 使用英文，不 push。

