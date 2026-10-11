# 新赛道技能接入记录

检查日期：2026-10-11。通过 Agent Reach 的 GitHub CLI 路由克隆、读取仓库技能和许可证，安装使用 skill-installer，按固定提交下载。上游未修改。

| 仓库 | 检查提交 | 本地位置 | 决策 |
| --- | --- | --- | --- |
| [归藏社交卡片](https://github.com/op7418/guizang-social-card-skill) | cf4b810fac1c73fb65a2bb31d8c9278d82cbc4c5 | .agents/skills/guizang-social-card-skill | 文字卡片、公众号封面，优先杂志系统 |
| [CY 图文轮播](https://github.com/chengyi-ai/cy-carousel-skill) | be1a9f1d35cf87b92fe34d172851060b1a4a35b1 | .agents/skills/cy-carousel | 安装为备选；AI 科技体裁不套进关系账号 |
| [Creator Buddy](https://github.com/SpaceZephyr/creator-buddy) | edf46c567ff54b72ee2157d06f3a02dbd67aaa9c | .agents/skills/creator-buddy | 已安装版本相同，复用写作、样本、标题和平台改编 |
| [微信图文变现](https://github.com/chenjin-cmd/wechat-graphic-monetization) | c50a3fda154ca38bf4167486503e0ddbc90793a6 | .agents/skills/wechat-graphic-monetization | 商业化阶段参考，非默认内容引擎 |
| [甲木公众号排版](https://github.com/isjiamu/gzh-design-skill) | fa4b78fb9471db33fe4538f04e88c62e38f54250 | .agents/skills/gzh-design | Markdown 到公众号 HTML、复制预览、确定性校验 |
| [手绘画风](https://github.com/threerocks/hand-drawn-styles) | 4132988b8596bfa36321c970a4472d4e3bb25d96 | .agents/skills/hand-drawn | 插画提示词与一致性协议，图片另用生图工具 |

归藏与甲木许可证为 AGPL-3.0 类；CY、手绘、微信变现为 MIT。安装包保留上游许可证。此处记录软件许可，不代表所有参考图均可用于公开发布。

## 验证状态

- 五个新增技能由安装器成功安装；Creator Buddy 上游提交与现有接入记录一致。
- relationship-content 是本项目自有总控，quick_validate 通过。
- 手绘 check_skill 扫描 21 套配方、108 个别名、21 项完整调用，但整体失败：3.1、13、19、20 的四张参考图下载失败。对应正式生产不可标为就绪；其余调用的检查结果不代表实际生图验收。
- 公众号排版、卡片截图、平台适配和 Huashu 新题成片尚未端到端验证。本次没有选定新题，没有生成成稿或媒体，不冒称流程已跑通。
- Agent Reach v1.5.0，检查无新版。
- 当前目录没有 Git 仓库元数据，不能提供 Git diff；按实际文件检查本次改动。

## 自动化状态

已完成项目内 Agent 编排：简短启动 → 候选卡 → 用户拍板 → 共享简报/母稿 → 各形式独立改编 → 渲染与验收 → 发布包。

未创建无人值守定时任务、后台服务或自动发布。选题后的第一套内容是端到端验证对象，执行时检查各子技能依赖，不把装包当成运行成功。
