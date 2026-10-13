# Art Motion Renderer

`art-motion` 是 World Mechanism Story Engine 的动画表达编译器。

它不负责决定“作品要说什么”，只负责把已经确认的 **Content Master → Video Concept → Director Proposal** 编译成可以实际渲染、混音、验收的视频生产包。

## 上游引擎

完整生产能力来自：

- upstream: `alchaincyf/huashu-art-motion`
- pinned commit: `26dba25b2b495c2138848c29a2c90df356a20325`
- local path: `third_party/huashu-art-motion`
- license: MIT

克隆本仓库时使用：

```bash
git clone --recurse-submodules <repo>
```

已有工作区：

```bash
git submodule update --init --recursive
```

## 为什么不是“多画风素材库”

吸收 huashu-art-motion 的重点是它的生产方法，而不只是 35 种风格：

1. **先设计一帧，再让它动。**
2. **世界画布 + 相机**，而不是把静态图片放大缩小。
3. **一段一个主动画语法**，避免同一段内部语法打架。
4. **每幕都有主动作与持续运动**，不是 PPT 式切图。
5. **风格签名转场**承担叙事连接。
6. **角色与环境分工**：复杂人物可由生成帧提供，代码负责位置、换帧、材质与镜头。
7. **确定性渲染 + 数字 QA + 独立审片**。

## 我们增加的一层：Cognitive Motion Routing

本项目不按“哪种风格漂亮”选 renderer，而按这一段的 **cognitive job** 选动画语言。

| Cognitive job | 首选动画语言 | 用法 |
|---|---|---|
| 让观众进入一个具体生活 | continuous scene / documentary-like observation | 固定人物、连续空间、具体环境声 |
| 展示多个世界同时成立 | multi-window + multi-style worlds | 不同窗口可用不同风格，但共享同一参考时间 |
| 证明“全部同时拥有”会失效 | window multiplication + sound overload | 画面和声音共同过载 |
| 展示无法穷尽的逐个回放 | long-scroll / endless queue | 世界持续向前滑，主体自己的时间也继续 |
| 展示“知道”与“经历”的差异 | keynote UI / kinetic type / abstract summary | 信息变得干净但失去空间与关系 |
| 展示被筛选的高光 | short style-speedrun | 允许快速换风格，但必须服务“筛选”这件事 |
| 回到个人时间线 | single world + continuous camera | 视觉复杂度骤降，恢复具体声场与单一方向 |

### 硬规则

- 风格变化必须有认知理由，不能为了炫技而换。
- 同一 beat 内原则上只使用一种主语法；多窗口本身是唯一例外，每个窗口内部仍保持单一语法。
- Renderer 不得改写 Content Master 的核心机制、事实、价值判断和 Must Preserve。
- Visual Proof 已经成立时，旁白不得再解释一遍。
- F01 不再把“重复动作获得意义”作为核心证明；动画层也不得重新偷偷加回这个命题。

## 编译链

```text
Content Master
  ↓
Video Concept
  ↓
Director Proposal
  ↓
Motion Plan
  ├─ scene / beat timing
  ├─ cognitive job
  ├─ animation grammar
  ├─ art style / renderer
  ├─ camera path
  ├─ transition
  ├─ audio cue
  └─ subtitle safe zone
  ↓
huashu-art-motion engine
  ↓
Picture Track / Motion Clips
  ↓
Voice + Foley + Music + Subtitle
  ↓
QA + independent review
```

## 推荐生产目录

```text
productions/<id>/
├── 00-source/
├── 01-motion-plan.yaml
├── 02-storyboard/
├── 03-assets/
│   ├── characters/
│   ├── generated-frames/
│   └── audio/
├── 04-code/
├── 05-renders/
│   ├── stills/
│   ├── clips/
│   └── candidates/
├── 06-final/
└── retrospective.md
```

## 上游命令

进入 `third_party/huashu-art-motion` 后，可直接复用其渲染和 QA：

```bash
uv run --with playwright python scripts/engine/render.py --spec <spec.json> --out <clip.mp4>
uv run scripts/qa.py --project scripts/engine --out <qa-dir>
```

F01 的第一支正式 production 设计见：

`renderers/art-motion/F01-production-design.md`
