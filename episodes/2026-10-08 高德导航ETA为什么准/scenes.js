const path = require('path');
const { Scene, C, CX, build } = require(path.join(__dirname, '../../engine/whiteboard-video/lib/scene-dsl')).use(__dirname);

const scenes = [];

function heading(s, title, sub = '') {
  s.text(110, 52, title, { size: 76, color: C.brand });
  s.line([[110, 155], [1810, 155]], { stroke: C.gray, strokeWidth: 2 });
  if (sub) s.text(110, 178, sub, { size: 30, color: C.gray });
}

function card(s, x, y, w, h, title, body, fill = C.fBlue, color = C.ink) {
  s.rect(x, y, w, h, { round: true, fill, fillStyle: 'solid', stroke: color, strokeWidth: 3 });
  s.text(x + w / 2, y + 28, title, { size: 46, align: 'center', color });
  if (body) s.text(x + w / 2, y + 98, body, { size: 32, align: 'center', color });
}

function road(s, x, y, labels, colors = [C.blue, C.brand, C.orange, C.purple]) {
  const w = 1500 / labels.length;
  labels.forEach((label, i) => {
    const left = x + i * w;
    s.rect(left, y, w - 14, 120, { round: true, fill: i % 2 ? C.fGray : '#ffffff', fillStyle: 'solid', stroke: colors[i % colors.length], strokeWidth: 5 });
    s.text(left + (w - 14) / 2, y + 30, label, { size: 34, align: 'center', color: colors[i % colors.length] });
    if (i < labels.length - 1) s.arrow([[left + w - 6, y + 60], [left + w + 28, y + 60]], { stroke: C.gray, strokeWidth: 3 });
  });
}

function car(s, x, y, color = C.blue, label = '') {
  s.rect(x, y, 92, 44, { round: true, fill: color, fillStyle: 'solid', stroke: C.ink, strokeWidth: 3 });
  s.ellipse(x + 16, y + 32, 18, 18, { fill: C.ink, fillStyle: 'solid', stroke: C.ink });
  s.ellipse(x + 58, y + 32, 18, 18, { fill: C.ink, fillStyle: 'solid', stroke: C.ink });
  if (label) s.text(x + 46, y - 44, label, { size: 28, align: 'center', color });
}

function clock(s, x, y, value, color = C.brand) {
  s.ellipse(x, y, 180, 180, { fill: C.fYellow, fillStyle: 'solid', stroke: color, strokeWidth: 5 });
  s.line([[x + 90, y + 90], [x + 90, y + 45]], { stroke: color, strokeWidth: 5 });
  s.line([[x + 90, y + 90], [x + 130, y + 115]], { stroke: color, strokeWidth: 5 });
  s.text(x + 90, y + 200, value, { size: 46, align: 'center', color });
}

// 01：先把终点时间拆出问题
{
  const s = new Scene('01-hook', '你开导航时，它会先给一个预计到达时间。奇怪的是，这个时间往往和你实际到达的时刻很接近。|它不是在猜你今天会开多快。|它在算另一件事：等你开到前面每一段路时，那段路大概会堵成什么样。');
  s.nextBeat();
  heading(s, '预计到达，不是猜的');
  s.rect(1390, 220, 420, 690, { round: true, fill: '#ffffff', fillStyle: 'solid', stroke: C.gray, strokeWidth: 3 });
  s.imageFile(1600, 240, path.join(__dirname, 'assets', 'amap-eta-1.png'), { w: 380, align: 'center' });
  s.text(1600, 885, 'AMAP ETA 界面示例', { size: 26, align: 'center', color: C.gray });
  s.text(250, 300, '终点', { size: 48, color: C.gray });
  s.ellipse(205, 385, 90, 90, { fill: C.fGreen, fillStyle: 'solid', stroke: C.brand, strokeWidth: 4 });
  s.text(250, 405, '出发', { size: 28, align: 'center', color: C.brand });
  s.arrow([[330, 430], [1430, 430]], { stroke: C.gray, strokeWidth: 8 });
  s.text(800, 370, '一条路线', { size: 44, align: 'center', color: C.gray });

  s.nextBeat();
  s.text(260, 650, '不是：', { size: 56, color: C.red });
  s.text(500, 650, '全程距离 ÷ 一个平均车速', { size: 58, color: C.red });
  s.line([[500, 740], [1420, 740]], { stroke: C.red, strokeWidth: 8 });
  s.text(900, 815, '前方的路，未来还会变化', { size: 46, align: 'center', color: C.gray });

  s.nextBeat();
  s.text(180, 760, '更接近：', { size: 48, color: C.brand });
  road(s, 260, 820, ['路段 1', '路段 2', '路段 3', '路段 4']);
  scenes.push(s);
}

// 02：历史速度与实时路况
{
  const s = new Scene('02-inputs', '高德不会把整条路线当成一根直线。它会先把路线切成一段一段的道路，每一段就是一个 link。|每段路有两类信息：过去相同时段通常有多快，也就是 SP；现在通行要花多久，AutoLR 每分钟更新。|前一类看规律，后一类看眼下。两类信息放在一起，才知道这一段接下来可能需要多少时间。');
  s.nextBeat();
  heading(s, '先看“路段”，不是整条路', '来源：高德技术公开文章 / 高德开放平台文档');
  road(s, 210, 260, ['Link 1', 'Link 2', 'Link 3', 'Link 4']);
  s.text(960, 455, '路线 = 一串路段（trace）', { size: 44, align: 'center', color: C.gray });

  s.nextBeat();
  card(s, 220, 590, 620, 220, 'SP · 历史速度画像', '同一时段，过去通常多快', C.fYellow, C.ink);
  card(s, 1080, 590, 620, 220, 'AutoLR · 实时路况', '当前通行耗时，分钟级更新', C.fGreen, C.ink);
  s.arrow([[840, 700], [1060, 700]], { stroke: C.gray, strokeWidth: 4 });

  s.nextBeat();
  s.text(280, 900, '通常怎样', { size: 42, color: C.orange });
  s.text(820, 870, '+', { size: 60, color: C.gray, align: 'center' });
  s.text(1040, 900, '现在怎样', { size: 42, color: C.brand });
  s.text(1500, 900, '→ 这一段未来可能要多久', { size: 40, color: C.ink });
  scenes.push(s);
}

// 03：未来流量与复杂路况预测
{
  const s = new Scene('03-future', '只看现在还不够。你出发时前面很顺，等你开到那里，可能已经进入高峰。|所以遇到复杂拥堵，系统还要估计：堵车会不会往前传，什么时候传到哪一段。|正在导航、已经出发的车辆，会被匿名汇总成一份“未来车流”估计。');
  s.nextBeat();
  heading(s, '复杂拥堵，需要预测未来', '公开文章描述：未来交通流量');
  s.text(180, 230, '现在', { size: 48, color: C.brand });
  s.text(1500, 230, '未来', { size: 48, color: C.red });
  s.line([[260, 430], [1680, 430]], { stroke: C.gray, strokeWidth: 6 });
  s.line([[560, 430], [800, 330], [1080, 510], [1380, 350], [1680, 430]], { stroke: C.blue, strokeWidth: 7, round: true });
  [[560, 430], [800, 330], [1080, 510], [1380, 350], [1680, 430]].forEach(([x, y], i) => s.ellipse(x - 22, y - 22, 44, 44, { fill: i > 2 ? C.fRed : C.fBlue, fillStyle: 'solid', stroke: i > 2 ? C.red : C.blue, strokeWidth: 3 }));
  car(s, 340, 370, C.blue, '已经出发');
  car(s, 700, 270, C.green, '计划中的车流');

  s.nextBeat();
  card(s, 260, 650, 520, 170, '路段关系', '上游变化会传到下游', C.fBlue, C.blue);
  card(s, 860, 650, 520, 170, '时间变化', '高峰会向前推进', C.fYellow, C.orange);
  s.rect(1435, 605, 390, 310, { round: true, fill: '#ffffff', fillStyle: 'solid', stroke: C.brand, strokeWidth: 3 });
  s.imageFile(1630, 620, path.join(__dirname, 'assets', 'amap-eta-3.png'), { w: 350, align: 'center' });
  s.text(1630, 875, 'AMAP ETA 模型示意', { size: 24, align: 'center', color: C.gray });

  s.nextBeat();
  s.arrow([[300, 900], [1600, 900]], { stroke: C.brand, strokeWidth: 5 });
  s.text(950, 840, '不是等堵了才看见，而是提前估计车流会在哪里出现', { size: 40, align: 'center', color: C.ink });
  scenes.push(s);
}

// 04：按进入时刻逐段推演
{
  const s = new Scene('04-propagation', '接下来，系统沿着路线往前推。它关心的是：你什么时候会进入下一段路。|高德技术文章用了一个例子：第一段预计 11 分钟。这个数字只用来说明推演过程，不是某条真实路线的测量结果。|系统把 11 分钟后的时刻带给第二段，算出第二段的耗时，再把新的进入时刻带给第三段。一路推到终点，才得到整条 ETA。');
  s.nextBeat();
  heading(s, '整条路线，是这样算出来的', '公开机制示例：第一段 11 分钟（非实测）');
  s.text(210, 230, '出发时刻 t0', { size: 46, color: C.brand });
  road(s, 210, 360, ['Link 1', 'Link 2', 'Link 3', '终点'], [C.brand, C.blue, C.orange, C.purple]);
  clock(s, 260, 620, 't0');
  s.arrow([[450, 710], [650, 710]], { stroke: C.gray, strokeWidth: 4 });
  s.text(700, 670, '+ 11 分钟', { size: 44, color: C.brand });

  s.nextBeat();
  s.text(160, 820, '进入 Link 2：t0 + 11 分钟', { size: 46, color: C.blue });
  s.arrow([[800, 845], [1010, 845]], { stroke: C.gray, strokeWidth: 4 });
  s.text(1050, 805, '再用 Link 2 在那个时刻的预测', { size: 42, color: C.ink });

  s.nextBeat();
  s.text(240, 890, '路段预测', { size: 40, color: C.gray });
  s.arrow([[520, 925], [790, 925]], { stroke: C.brand, strokeWidth: 4 });
  s.text(850, 890, '进入时刻', { size: 40, color: C.gray });
  s.arrow([[1120, 925], [1390, 925]], { stroke: C.brand, strokeWidth: 4 });
  s.text(1440, 890, '终点 ETA', { size: 40, color: C.brand });
  scenes.push(s);
}

// 05：真实轨迹反馈闭环
{
  const s = new Scene('05-feedback', '这套方法好不好，不能只看屏幕上的终点数字。|系统会把车辆实际走过的时间，拿回来和每一段、整条路线的预测对照。|预测、实走、误差，再回到模型里。公开资料至少说明了：高德会用这套评估方法检查预测质量。');
  s.nextBeat();
  heading(s, '预测、实走、再校准', '公开资料：link 级 / trace 级评估');
  card(s, 230, 330, 420, 190, '行前预测', 'Link 1：11 分钟', C.fBlue, C.blue);
  card(s, 750, 330, 420, 190, '实际轨迹', '真实走了多久？', C.fYellow, C.orange);
  card(s, 1270, 330, 420, 190, '误差', '差多少？', C.fRed, C.red);
  s.arrow([[650, 425], [730, 425]], { stroke: C.gray, strokeWidth: 4 });
  s.arrow([[1170, 425], [1250, 425]], { stroke: C.gray, strokeWidth: 4 });

  s.nextBeat();
  s.arrow([[1480, 560], [1030, 710], [560, 560]], { stroke: C.brand, strokeWidth: 5, round: true });
  s.text(1030, 680, '回到下一轮预测', { size: 44, align: 'center', color: C.brand });

  s.nextBeat();
  s.text(280, 820, 'link 级评估', { size: 44, color: C.blue });
  s.text(880, 820, 'trace 级评估', { size: 44, color: C.orange });
  s.text(1480, 820, '不是只看终点', { size: 44, color: C.red, align: 'center' });
  s.line([[260, 900], [1650, 900]], { stroke: C.gray, strokeWidth: 3, strokeStyle: 'dashed' });
  s.text(950, 910, '预测质量要拿真实行程回放验证', { size: 40, align: 'center', color: C.gray });
  scenes.push(s);
}

// 06：边界与收束
{
  const s = new Scene('06-boundary', '当然，它也不是水晶球。事故、封路、突发天气，都可能让路况突然改写。|公开资料能说明路段怎么预测、路线怎么推演、结果怎么评估；至于每次到底差几分钟，以及当前线上模型的全部细节，没有公开。|所以，预计到达时间要当成动态估计，不是承诺。下次看导航，除了看终点，也看看哪一段路的时间正在变化。');
  s.nextBeat();
  heading(s, '准，不等于全知', '已公开机制 ≠ 已公开全部线上模型');
  card(s, 220, 290, 700, 250, '公开资料能说明', '路段预测 · 未来推演 · 实走评估', C.fGreen, C.brand);
  card(s, 1000, 290, 700, 250, '公开资料不能说明', '所有场景的具体误差与完整线上模型', C.fRed, C.red);

  s.nextBeat();
  s.text(220, 680, '事故', { size: 52, color: C.red });
  s.text(620, 680, '封路', { size: 52, color: C.red });
  s.text(1020, 680, '极端天气', { size: 52, color: C.red });
  s.text(1450, 680, '都会改变未来', { size: 52, color: C.orange });
  s.line([[260, 780], [1620, 780]], { stroke: C.red, strokeWidth: 5, strokeStyle: 'dashed' });

  s.nextBeat();
  s.rect(260, 835, 1400, 92, { round: true, fill: C.fYellow, fillStyle: 'solid', stroke: C.brand, strokeWidth: 4 });
  s.text(CX, 854, 'ETA = 基于当下信息，对未来路段耗时的动态估计', { size: 48, align: 'center', color: C.ink });
  scenes.push(s);
}

const cover = (s, ratio) => s.coverLayout({
  ratio,
  title: '预计到达\n不是猜的',
  sub: '高德导航 ETA 的路段级预测机制',
  tag: '机制拆解 · 第 1 期',
});

build(__dirname, scenes, { cover });
