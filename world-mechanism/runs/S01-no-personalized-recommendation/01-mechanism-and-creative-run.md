# S01 实跑记录 v0.2 — 如果个性化推荐消失七天

> 目的：验证当代社会技术题能否保持多方视角、避免价值预设，并允许最终形式不是剧情故事。

## 1. Starting Point

原始问法：

> 如果推荐算法消失七天，互联网会不会更真实？

实跑第一步就发现：**这个问题不能直接回答。**

“算法消失”太含糊：
- 时间排序也是算法；
- 搜索结果有排序；
- 热门榜有统计与排序；
- 订阅流也需要规则决定如何呈现。

所以必须先 operationalize。

### 实验规则 v0.2
七天内：
- **禁止**根据个人历史、预测兴趣或相似用户行为，对首页内容进行个性化预测排序；
- **允许**用户主动订阅后的时间顺序流；
- **允许**明确查询触发的搜索与非个性化相关性排序；
- **允许**分类目录；
- **允许**清楚标注的人工编辑精选；
- 基线场景**不提供自动热门榜**，热门榜作为独立分支测试。

因此题目真正变成：

> **拿走个性化预测排序以后，注意力分配权和寻找成本会转移到哪里？**

---

## 2. Research Pass A｜前置轻研究

### F — 已核事实
- Netflix 把 Personalization、Recommendations、Search 描述为核心内容发现能力，并明确目标之一是减少 browsing / searching 时间。
- Google Drive 的 Quick Access 个性化推荐在该具体产品场景里，把用户寻找文件的时间约减半。
- Google Research 2024 的 recommender ecosystem 研究明确指出，现代推荐系统会耦合 users、content providers、advertisers 等多个参与者，单纯优化单用户短期推荐可能忽略长期生态效用。
- 推荐系统研究并不只优化 accuracy；Google 2021 的研究同时讨论 diversity、novelty、serendipity。
- cold-start 是推荐系统中的真实问题：新内容因为缺少历史交互，可能更难被有效分发，因此系统常引入 exploration 或其他内容特征。

### Sources
- Netflix Research — Recommendations  
  https://research.netflix.com/research-area/recommendations
- Google Research — Improving Recommendation Quality at Google Drive  
  https://research.google/pubs/improving-recommendation-quality-at-google-drive/
- Google Research — Modeling Recommender Ecosystems  
  https://research.google/pubs/modeling-recommender-ecosystems-research-challenges-at-the-intersection-of-mechanism-design-reinforcement-learning-and-generative-models/
- Google Research — Values of Exploration in Recommender Systems  
  https://research.google/pubs/values-of-exploration-in-recommender-systems/
- Google Research — Cold-start Recommendations  
  https://research.google/pubs/expediting-exploration-by-attribute-to-feature-mapping-for-cold-start-recommendations/

---

## 3. Question Ladder

1. 真正稀缺的是内容，还是用户时间、首页位置和第一次曝光机会？
2. “我自己选”具体意味着什么？订阅、搜索、按时间排，分别把选择成本放到谁身上？
3. 个性化推荐解决的是兴趣匹配，还是更底层的搜索成本？
4. 如果首页不预测兴趣，谁最先受益：强订阅关系的老创作者、会搜索的用户，还是编辑精选？
5. 谁最吃亏：新用户、新内容、长尾创作者，还是不愿主动搜索的人？
6. 没有个性化推荐后，创作者会不会改变发布时间、标题、外部社群经营？——这是 H，不是 F。
7. 人工编辑真的比算法“更没有偏见”吗？它只是把偏好变得更可见吗？
8. 热门榜如果回归，它会不会用集体行为替代个人行为，形成另一种反馈回路？
9. 我们真正想讨论的是算法有无，还是**谁替我筛、按什么目标筛、我能不能看见和控制这套筛法**？

---

## 4. Competing Mechanism Candidates

### Candidate A｜Search-cost Mechanism
个性化推荐降低用户在巨大内容库中的寻找成本。

**解释力**：能解释为什么平台和用户都需要推荐。  
**不足**：解释不了推荐如何改变创作者行为和生态。

### Candidate B｜Attention-allocation Mechanism — Core
当供给远超注意力时，首页和第一次曝光机会是稀缺资源，必须由某种规则分配。

**解释力**：能容纳个性化、时间排序、订阅、搜索、热门榜、人工编辑等所有替代机制。

### Candidate C｜Feedback / Ecosystem Mechanism
被展示会产生互动数据，互动又影响后续展示；创作者也会适应规则。

**解释力**：解释“推荐不仅预测偏好，也改变生态”。  
**风险**：容易滑向“算法操控一切”的过度叙事。

### 结论
B 为主机制；A 是用户侧成本；C 是长期系统后果。

### One-sentence Model

> **内容越过剩，排序越不可避免；取消个性化推荐不会消除中介，只会让别的中介接管首页，并重新分配寻找成本、曝光机会和控制权。**

---

## 5. Counterfactual：由时间线改为分支树

原计划是：
**Day 1 → Day 3 → Day 7**

实跑后发现这会产生一个问题：

> 模型很容易把“可能的适应行为”写成“必然发生的剧情”。

因此 S01 改用 **Replacement Branches**。

### Branch A｜Chronology
按发布时间排列。

可能后果 H：
- 高频发布者占据更多可见位置；
- 发布时间变成竞争变量；
- 用户需要自己维护关注关系。

### Branch B｜Subscription
只看主动关注对象。

可能后果 H：
- 已建立关系的创作者更稳定；
- 新内容 / 新创作者缺少第一次触达机会；
- 用户的旧选择更容易延续。

### Branch C｜Search
用户必须明确说出自己要找什么。

可能后果 H：
- 已知需求更高效；
- 未知兴趣、偶遇和“我不知道该搜什么”的发现更困难；
- 标题语言、关键词和搜索优化获得更大权重。

### Branch D｜Human Curation
编辑人工选择首页。

可能后果 H：
- 筛选标准更可解释；
- 编辑资源有限；
- 权力从模型团队转向编辑团队，并没有消失。

### Branch E｜Popularity / Trending
集体行为决定排序。

可能后果 H：
- 个人画像减少；
- 既有热度与反馈回路可能更强；
- “大家都在看”成为新的中介。

### 核心发现

> **“无推荐”不是一个系统状态。每删掉一种分配规则，下一步必须明确：谁接管了排序。**

---

## 6. Creative Exploration｜四种表达母题

### A｜《七天无推荐实验日志》
每天展示一种替代机制如何浮上来。

**优点**：有连续性。  
**问题**：极易把假设写成确定预测，必须改成“分支实验”而非新闻纪实口吻。

### B｜《首页只有十把椅子》
白板 / minimal-line：一百万条内容站在屏幕后，但首页第一屏只有十个位置。

每次拿走一种分配方式，就必须让另一种方式决定谁坐下。

**优点**：儿童也能理解稀缺与排序。  
**问题**：如果只有比喻，会缺少真实系统复杂度。

### C｜《你来设计一个没有推荐的首页》
互动文章 / 网页。

读者依次选择：
- 时间顺序；
- 只看关注；
- 搜索；
- 编辑精选；
- 热门榜。

每选一次，都出现一个新的成本与受益者。

**优点**：真正把价值判断交还给人；非常符合项目哲学。  
**问题**：首版制作复杂，可先编译成文章中的选择题结构。

### D｜《谁坐上了推荐算法空出来的椅子？》
思辨公众号文章，以“中介不会消失，只会换人”为主轴，逐个拆替代机制。

**优点**：最适合当前 Blueprint；能保留复杂度。  
**问题**：标题如果写得太结论化，会提前泄底。

---

## 7. Editorial Gate

### 主形态：D + C 的轻互动结构
先做一篇 **可选择的思辨文章 / explainer**，不是剧情故事。

核心阅读动作：

> 读者每一节都要自己选“那你希望首页按什么排？”然后马上看到这条规则把什么成本转移给了谁。

这比虚构一个“被算法困住的孩子”更适合 S01，因为后者会立刻带入预设立场。

### 非故事也要有推进
推进不是“人物越来越惨”，而是**概念状态不断变化**：

1. 我以为关掉推荐就回到“自己选择”；
2. 发现时间顺序也是规则；
3. 只看订阅会冻结过去的选择；
4. 搜索要求我先知道自己想找什么；
5. 人工编辑让偏好更可见，但权力仍在；
6. 热门榜又把集体行为变成排序器；
7. 最后问题从“要不要算法”升级为“我要哪种中介、什么目标、多少控制权”。

### 去观点图解测试
不能从第一段就告诉读者“中介不会消失”。要让读者自己经历几次替换失败后得出这一层。

---

## 8. Editorial Result

**进入 Blueprint 待人工确认。**

### Must Preserve
- 明确实验只取消“个性化预测排序”，不是所有算法；
- 不把 chronology / search / curation 写成中性基准；
- 至少保留 user / creator / platform 三方；
- 所有七天行为变化必须标 H，不伪装成事实；
- 不给“算法更好 / 更坏”的总裁决；
- 首选文章 / explainer，视频只是后续编译目标。

### Engine Learning
S01 证明两条需要回写引擎：
1. 反事实首先要 **operationalize rule scope**；
2. 高不确定性的社会系统优先使用 **branching counterfactual**，而不是确定性时间线。
