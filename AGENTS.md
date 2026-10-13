# 余光所及｜本地执行仓库约定

Devin 是一名热爱技术的银行人，使用 Codex 做产品开发和知识管理。这里的工作目标不是把 Notion 的内容机制复制到本地，而是把已经在 Notion 确认的内容交接为可复现的渲染、配音、排版、整理和发布包。

## 项目定位

本仓库是“余光所及”的本地执行仓库，服务三条内容线：

- **有解｜关系与处世**：朋友、家庭、职场、亲子、人与自己和世界相处中的具体难题；
- **世界机制故事**：科学、技术、历史、社会和经济中的机制，用故事或其他合适形式让理解发生变化；
- **想象瞬间｜Edge of Sight**：用生图记录只改一条世界规则的空间与瞬间。

Notion 是所有内容机制的唯一真源：想法、选题、写作、视频方法、贴图和生图都在 Notion 完成；仓库只接手必须用本地工具完成的执行环节，并把结果回填对应产物页。

## 真源层级

冲突时严格按以下顺序处理：

1. 用户明确反馈；
2. Notion 现行机制页；
3. Notion 产物页中的 Brief、节拍表、全文和 Prompt；
4. 本仓库执行规则；
5. 上游技能；
6. 工具上的便利。

Notion 当前入口：

- 导航：<https://app.notion.com/p/3d527110f8d581b3b3c2f53574559f94>（给人看的地图，不作为运行规则页）；
- 工作台：<https://app.notion.com/p/3f727110f8d5813e9b22dbeff5ebdd9c>（S1–S5 总入口）；
- 写作机制：<https://app.notion.com/p/3d727110f8d5816dbed0f5360d37014b>；
- 创意视频机制：<https://app.notion.com/p/3f727110f8d5812da32dd21d59e30131>；
- 有解贴图入口：<https://app.notion.com/p/3f627110f8d581918bf3de93e837a339>；
- 生图运行协议 v4.0：<https://app.notion.com/p/3da27110f8d5819b835ac3154cec5e3a>；
- 视频最小脚手架附录：<https://app.notion.com/p/3f727110f8d581409fc6efb83e348eb0>。

所有 Notion 内容必须通过 Notion MCP 读取或写回。Notion 不可用、页面不可读或依赖缺失时，返回 `blocked`，不用仓库缓存、旧 Prompt 或模型记忆顶替。历史归档页不作为运行输入。

## 工作边界

- 先读取 Notion 产物页，再执行本地工作；不要在仓库重新写作或重建机制。
- 真实经历、匿名改编和演绎场景分开标注；不编造人物、数据、引语、研究和发布结果。
- 不自动公开发布，不执行 `git push`，不提交密钥、token、密码或参考音频。
- 新任务先确认 Notion 产物页的 `仓库交接`；没有明确交接内容就不擅自开始制作。
- 每次只运行与改动相关的验证；无关失败单独记录，不为“全绿”扩大修复范围。
- `build/` 是可清理的中间产物；发布交付放 `outputs/` 或产物目录约定的位置，旧版本不覆盖。

## 目录职责

- `.agents/skills/`：项目自有技能入口与已安装上游技能。安装工具管理的技能不直接改上游内容；`wm-*` 入口指向 `world-mechanism/skills/`，不进入 `skills-lock.json`。
- `engine/`：本仓库独有执行器，包括 `video-kit/`、`voice/` 和历史兼容的 `whiteboard-video/`。
- `world-mechanism/`：合并保留的世界机制故事引擎；其子目录 `AGENTS.md` 继续有效，但受本文件和 Notion 现行机制约束。
- `world-mechanism/renderers/art-motion/`：全仓共用的代码动效渲染器。保留在子目录原位，是为了保留上游相对路径、锁定文件和测试；新生产通过这个路径引用，不再复制一份到根目录。
- `research/`：事实来源台账、视觉参考和研究证据；不存 Notion 机制正文副本。
- `productions/<YYYY-MM-DD-slug>/`：新内容的统一生产目录。沿用 world-mechanism 的 `production.yaml`，额外要求 `content_line` 和 `notion_output_url` 两个字段。
- `episodes/`：历史期目和旧实验，仅保留，不迁移到新的生产目录。
- `build/`：渲染中间产物，可清理。
- `outputs/`：验收后的成片、字幕、封面、贴图和发布包；`outputs/stickers/` 保存贴图发布包，不镜像 Notion 机制。
- `notes/archive/2026-10-12/`：已由 Notion 接管的方法正文归档；原路径保留短指针，方便旧链接回溯。

## Notion 工作台路由

宽泛请求改走 Notion 工作台 S1–S3：想法库 → 选题库 → KEEP / HOLD / REJECT。仓库不再生成本地候选卡。用户明确“做这个”时，从对应选题和产物页读取交接；没有拍板的候选不进入本地生产。

人工关口对应关系：

- Creative Gate：选题库里的 `KEEP / HOLD / REJECT`；
- Direction Gate：视频机制要求的三个差异化方案；
- Prototype Gate：关键帧和小样；
- Release Gate：用户审阅成片。

## 具体生产路由

### 贴图 / 双格观察卡

走 `.agents/skills/yuguang-sticker-bridge/SKILL.md`，再通过 Notion MCP 读取有解贴图生成器。先在产物库落一条记录；标题和配文按写作机制 §8.1。Notion Skill 负责当前视觉、双格版式和生图规则；仓库只保存本轮输入、结果文件和 `sticker_manifest`。manifest 需要带 `notion_output_url`，并准确区分 `ready`、`prompt_ready` 和 `blocked`。

### 公众号长文

正文在 Notion 产物页按写作机制完成。仓库只做本地排版和素材装配：

- `gzh-design`：16px 正文、约 1.85 行高、单列、内联样式、`span leaf` 节点和平台兼容校验；
- `guizang-social-card-skill`：2.35:1 与 1:1 分开构图，并另起封面短标题；
- `jiejie-illustrations`：正文约 3 张图，按转折而不是按章节平均分配；角色参考图路径见 `notes/VISUAL_IP_AND_ACCOUNT_NAME.md`；
- 需要起草时可以调用本机 Gemini CLI，但方法、口吻和质检仍按 Notion 写作机制，成稿必须写回产物页。

### 代码视频

读取 Notion 创意视频机制，并读取产物页中的 Brief、节拍表和 `cues.json`。执行顺序固定为：关键帧 → 运动 → 声音 → 渲染 → 视频机制 §8 检查 → 另开会话独立评审 → 回填产物页。简单片从 `engine/video-kit/` 起步；复杂风格使用 `world-mechanism/renderers/art-motion/`。`huashu-art-motion`、`whiteboard-video` 和 `space-video-*` 只作参考，不再是默认主路线。配音继续使用 Huashu 当前绑定配置，凭证只通过临时环境变量注入。

### 世界机制故事

选题和创意前端先走 Notion 工作台 S2–S3；进入深度制作后，沿用 `world-mechanism` 的 Content Master → Video Concept → Director Proposal → `production.yaml` → art-motion → QA 流程。不要把世界机制子目录的 F / I / H / R、文化视角、生产状态和 golden case 规则复制到根 notes。

### 想象瞬间 / Edge of Sight

静态生图不在本仓库执行，走 Notion 生图运行协议 v4.0。本仓库只在产物页明确要求代码视频版时接手，按代码视频路由执行；不保存生图机制正文。

## 生产 manifest

每个新的 `productions/<YYYY-MM-DD-slug>/production.yaml` 至少包含：

```yaml
content_line: "有解｜关系与处世 | 世界机制 | 想象瞬间｜Edge of Sight"
notion_output_url: "<产物页 URL>"
```

其余字段沿用 `world-mechanism/engine/production-orchestrator/template-production.yaml`，包括来源、Must Preserve、当前阶段、renderer、资产、原型、QA、阻塞和 `codex.next_actions`。仓库完成后，通过 Notion MCP 回填产物库的 `发布链接`（逻辑上的“链接”字段）和 `状态=待发布`；不填写猜测数据。

## 技能与上游边界

- `relationship-content` 是三条内容线之外的关系线总控入口，负责把 Notion 交接转成本地执行。
- `yuguang-sticker-bridge` 只保存贴图桥接协议，不保存 Notion 视觉机制。
- `yuguang-handoff` 接收一个产物页 URL，读取 `仓库交接`、关联选题和对应机制，执行本地生产并回填 `发布链接` / `状态`。
- `jiejie-illustrations` 是项目派生技能；`ian-xiaohei-illustrations` 保留供追溯，不改安装工具管理的上游技能。
- 四个 `wm-*` 技能的完整真源在 `world-mechanism/skills/`，顶层入口只负责发现和指向。

## 验证

改动相关时运行：

- 世界机制：在 `world-mechanism/` 执行 `python -m pip install -r requirements-dev.txt pytest`，再运行 `.github/workflows/validate.yml` 中的 6 个校验脚本；
- video-kit：在 `engine/video-kit/` 执行 `sh run.sh`，检查 4.000 s、响度 `−14 ±1 LUFS`、真峰 `≤ −1 dBTP`；
- 路径：运行仓库路径检查脚本，确认所有项目自有 `SKILL.md`、`AGENTS.md` 和交接文档引用的本地路径存在；
- Notion：所有当前入口 URL 和实际数据库 URL 通过 Notion MCP 重新读取后，才报告可读。

Git commit message 使用简洁英文。只在用户明确要求时 push；部署走项目自己的命令，不用 push 代替部署。
