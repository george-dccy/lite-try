# 余光所及｜有解：公众号视觉、配图与排版规范

## 当前执行规则（用户最新决定，优先于下方历史方案）

- IP 保留原参考图的年轻化漫画比例与面貌，不做成人化。深蓝头发、蓝橙服装保持；去掉发夹。橙色括号口袋标只是建议方案，待样张确认，不当作已批准标志。
- 正文图默认使用项目派生技能 `.agents/skills/jiejie-illustrations/SKILL.md`。上游 `.agents/skills/ian-xiaohei-illustrations/` 保留供追溯，不直接用于本品牌生图，避免重新生成小黑。
- 正文图白底、手绘线条，解解头发深蓝实色、衣服少量蓝橙平涂；表情有生活感，不套空表情或强制怪诞。按转折配图，不按章节均匀配图。
- 公众号封面使用 `guizang-social-card-skill` 的 Editorial 路线，沿用本项目蓝橙品牌色；不用 Punk。生成横版与方版独立构图，标题由 HTML 排，人物素材与正文同源；读取上游平台、模板、标题压缩和质检参考后执行。
- 公众号正文排版仍用 gzh-design 的项目适配，视觉样张未确认前不宣称已锁定完整主题。新图必须实际嵌入文章，不能只有 assets 文件。
- 旧参考图、成稿和已生成图片不覆盖。新版 IP 参考图尚未生成。

## 以下为历史方案（仅供追溯，不覆盖当前规则）

> 2026-10-11 审阅状态：本文件为首轮尝试，用户未认可其排版与配图，不作为已验收固定风格。新版推荐及问题证据见 `notes/WECHAT_VISUAL_DIRECTION_V2.md`，待样张确认后再替换正式规范。下文“经过严格平台合规校验”等旧描述不代表微信实机验收；Punk 当前商业许可尚未确认，不作为生产依赖。

更新日期：2026-10-11
归属规范：notes/BRAND_POSITIONING.md & notes/ARTICLE_EDITORIAL_WORKFLOW.md
吸收来源：
- 封面图：吸收 Punk-Skill 的多平台比例、视觉隐喻与大字排版冲击力；
- 正文配图：吸收 Ian Xiaohei Illustrations 的“16:9 纯白底手绘线稿 + IP 深度参与认知动作 + 橙蓝手写批注”；
- 页面排版：融合 gzh-design 的“留白禅意风”与“橄榄手记风（品牌暖纸）”。

---

## 一、 整体视觉资产与品牌色彩基调

- **品牌核心定位**：“孩子懂相处，大人看见人”；
- **视觉 IP**：“解解”（青年观察者，深蓝短发、橙色括号发夹、深蓝外套、橙色内搭、米白长裤）；
- **核心色彩系统**：
  - **纸感底色**：纯白 `#FFFFFF` 或 米白纸感底 `#FDFDF8`
  - **墨色/正文**：深墨黑 `#1E1F23`、深炭灰 `#2B2B2B`、中深灰 `#4D4F46`
  - **品牌点睛橙**：`#ED7B2F`（橙色括号发夹、重点关键词下划线、手写批注框、高亮标签）
  - **沉稳黛蓝**：`#253746`（解解外套、次要结构边框、冷静批注）
  - **橄榄灰/极细线**：`#BFC1B7` / `#E8E8E8`（1px 分割线、留白边框）

---

## 二、 封面图体系（Cover Artwork System）

参考 Punk-Skill 的平台比例与视觉张力：

1. **规格与尺寸**：
   - **微信公众号头条封面**：标准比例 `2.35:1`（实际推荐设计尺寸 `900 x 383` 或 `21:9` 兼容）；
   - **次条/小红书备用**：`1:1`（500x500）或 `3:4`。
2. **构图法则**：
   - **黄金分割三段式**：
     - 左侧或居中上方：主标题大字（加粗非衬线，极强识别度，字号占视觉重心 30% 以上）；
     - 副标题/金句：小一号浅色文字或药丸标签；
     - 画面右侧或下半部：**核心场景隐喻手绘/插画**（如：一扇虚掩透光的门、一盒系着橙色丝带的伴手礼、两个并排望向远方的背影剪影）。
3. **生图 Prompt 配方模板**：
   ```text
   Clean editorial cover illustration for WeChat article, 2.35:1 ratio (or 16:9), warm cream paper texture background (#fdfdf8). Minimalist clean hand-drawn line art style, featuring young observer boy 'JieJie' with dark blue hair and an iconic bright orange bracket hairpin. Symbolic scene representing [文章核心场景，如：standing in front of a half-open door holding a small gift]. Bold artistic composition, generous whitespace, accent colors of vivid warm orange (#ed7b2f) and deep navy blue (#1e1f23). Modern, thoughtful, warm humanistic atmosphere, no cluttered details.
   ```

---

## 三、 正文配图体系（In-Article Cognitive Illustrations）

深度融合 Ian Xiaohei 的认知动作理念，升级为**“解解认知手绘图”**：

1. **核心原则**：
   - **“不只是为了好看配图，而是把文章的一个关键认知动作画出来”**；
   - 每一张图都是读者阅读长文时的“视觉休息站”和“记忆锚点”；
   - 一篇文章标配 **3 ~ 5 张正文配图**，均匀分布在各核心小节末尾或转折处。
2. **画面规格与样式特征**：
   - **画幅比例**：统一 `16:9` 横版（在手机端滑动时视觉体验最平稳，不压迫版面）；
   - **底色**：纯白 `#ffffff` 或 极浅暖灰 `#fdfdf8`，无复杂渐变；
   - **线条**：黑色手绘细线条，轻微手工抖动感，透气质朴；
   - **主体占比**：主体人物与道具占画面 40%~60%，四周保持大留白；
   - **手写批注**：每张图带 1~2 处用橙色（`#ed7b2f`）或黛蓝（`#253746`）圈注的中文手写标签或括号框，直接点破该图的认知逻辑。
3. **IP“解解”的角色行为规范**：
   - 解解不是死板站在角落的贴纸或吉祥物，而是**正在现场参与认知动作**：
     - 在纠结时：站在虚线台阶前踌躇；
     - 在叙旧时：和老友面对面坐在路边小凳上，头顶漂浮当年的回忆气泡；
     - 在避免尴尬时：把标有“查户口盘问”的椅子轻轻推开，递上一杯冒热气的清茶；
     - 在并排走时：跟在跑跳的孩子身后，视线望向前方风景；
     - 在散场时：手机屏幕亮起具体小事的对话气泡。
4. **生图 Prompt 配方模板**：
   ```text
   16:9 horizontal editorial illustration, pure white background, generous whitespace. Minimalist clean black hand-drawn sketch style with subtle organic line wobble. Featuring young observer boy 'JieJie' (dark blue hair, orange bracket hairpin, navy casual jacket). JieJie is performing a specific conceptual action: [具体认知动作描述]. Handwritten-style conceptual diagram elements, annotated with small orange arrow and bracket frame. Simple, witty, philosophical yet warm, intellectual comic style like Sempé meets modern conceptual illustration.
   ```

---

## 四、 排版样式体系（Typographic Layout Themes）

提供两套经过严格平台合规校验的固定主题：

### 样式 A：留白禅意风（Zen Whitespace）
- **调性**：极简超大留白、衬线字体金句、1px 极细线、低饱和墨绿（`#4A5D52`）点缀、书卷气与呼吸感最强；
- **适用**：深度生活随笔、内心独白、关于岁月与关系的散文。

### 样式 B：橄榄内刊手记（Olive Journal · 品牌定制版）
- **调性**：米白纸感底（`#fdfdf8`）+ 墨黑（`#1e1f23`）+ 边框（`#bfc1b7`）+ 品牌点睛橙（`#ed7b2f`）；
- **组件特色**：内刊头图卡（Hero Banner）、01/02 PART 分节徽章、橙色下划线、极简对照卡片、内刊尾部存档签名；
- **适用**：观察者手记、关系问题复盘、处世方法解法分析。
