# 仓库独有执行细节

本文件只记录 Notion 无法替代的本地执行事实，不承载“余光所及”的写作、视觉或生图机制正文。

## 公众号排版与视觉调用

- 公众号 HTML 使用 `.agents/skills/gzh-design/`；成品校验命令为：

  ```powershell
  python .agents/skills/gzh-design/scripts/validate_gzh_html.py <生成的.html 的实际路径>
  ```

- 校验目标：ERROR 清零；重点检查内联样式、禁止标签/属性、`span leaf` 文字节点、图片尺寸和微信粘贴兼容性。具体主题组件从 `references/theme-index.md` 读取，不凭记忆重写 HTML。
- 公众号封面使用 `.agents/skills/guizang-social-card-skill/` 的 Editorial 路线；2.35:1 和 1:1 必须独立构图。需要自动检查时，在任务目录运行：

  ```powershell
  node validate-social-deck.mjs <task-dir>
  ```

- 正文插画使用 `.agents/skills/jiejie-illustrations/`；固定角色参考图为 `research/visual-ip/explainer-boy-v1.png`，生成前实际查看，去掉旧参考图中的发夹，不覆盖既有资产。封面不由该技能承担。

## 配音

- Huashu 当前绑定配置记录在 `notes/huashu-voice-config.json` 和 `notes/VOICE_INTEGRATION.md`；默认复刻音色是配置中的现行值，不在技能或脚本里写入凭证。
- API key 只在当前命令进程的临时环境变量中注入；音频生成后用 `engine/voice/prepare-huashu-voice.mjs` 统一格式并保留回执。

## 研究、平台样本与对标

- 互联网、GitHub、社交平台、公众号样本和参考视频研究，先运行当前环境的 `agent-reach doctor --json`，再按 `C:\Users\georg\.agents\skills\agent-reach\SKILL.md` 的当前 references 路由；不把搜索摘要当原文，不绕过验证码、登录、权限、付费墙或 DRM。
- 来源台账至少保留原始链接、访问日期、作者/平台、数据口径和“未获取”状态；没有互动数据不估算，不把单篇高赞称为稳定爆款。
- 对标筛选只迁移结构和机制，不复制原句、人物、镜头顺序、视觉指纹或未经核实的数据；互动分布、广告露出、承接意图和公开成交证据分开记录。
- 写作前存在可访问的同赛道样本时，至少拆开头、节奏、口播、画面和结尾；拆解结果作为 Notion 产物页的研究输入，不在仓库重建选题机制。

## 上游与许可

- `notes/REPOSITORY_ADOPTION_20261011.md` 保存已安装技能的来源、提交和许可证据。
- 安装工具管理的上游技能不直接修改；项目派生技能要保留来源与许可说明。
- `world-mechanism/` 内的 `wm-*` 技能和 `renderers/art-motion/` 属于合并进来的项目自有能力，顶层入口只做发现，不复制正文。
