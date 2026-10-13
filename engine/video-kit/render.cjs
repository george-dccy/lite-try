// 用法：node render.cjs [--stills 0.5,1.0,2.6] [--mb 4] [--scale 0.5]
// 逐帧调用 window.renderAt(t) → 截图 → frames/00000.png；同时记录 window.probe(t) → motion.json（给声音用）
const fs = require('fs'), path = require('path');
const { chromium } = require('playwright');
const arg = (k, d) => { const i = process.argv.indexOf('--' + k); return i > 0 ? process.argv[i + 1] : d; };
(async () => {
  const C = JSON.parse(fs.readFileSync('cues.json', 'utf8'));
  const scale = +arg('scale', 1), mb = +arg('mb', 1), stills = arg('stills', null);
  const browser = await chromium.launch({ executablePath: process.env.CHROME || undefined, args: ['--no-sandbox', '--font-render-hinting=none'] });
  const page = await browser.newPage({ viewport: { width: C.width, height: C.height }, deviceScaleFactor: scale });
  await page.addInitScript(`window.CUES = ${JSON.stringify(C)};`);
  await page.goto('file://' + path.resolve('scene.html'));
  await page.waitForFunction('window.__ready === true', null, { timeout: 30000 });
  const times = stills ? stills.split(',').map(Number) : [...Array(Math.round(C.duration * C.fps)).keys()].map(f => f / C.fps);
  const dir = stills ? 'stills' : 'frames'; fs.rmSync(dir, { recursive: true, force: true }); fs.mkdirSync(dir);
  const motion = [];
  for (let i = 0; i < times.length; i++) {
    const t = times[i];
    await page.evaluate(([t, mb]) => window.renderAt(t, mb), [t, mb]);
    const name = stills ? `t${t.toFixed(2)}.png` : `${String(i).padStart(5, '0')}.png`;
    await page.locator('canvas').screenshot({ path: path.join(dir, name) });
    if (!stills) motion.push({ t, ...(await page.evaluate(t => window.probe ? window.probe(t) : {}, t)) });
  }
  if (!stills) fs.writeFileSync('motion.json', JSON.stringify(motion));
  await page.close(); await browser.close();
  console.log(`rendered ${times.length} ${dir}`); process.exit(0);
})().catch(e => { console.error(e); process.exit(1); });
