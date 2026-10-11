const path = require('node:path');
const { pathToFileURL } = require('node:url');
const { chromium } = require('C:/AI/ai_opc/ai_videos/lite_try/engine/whiteboard-video/node_modules/playwright-core');

const root = __dirname;
const browserPath = 'C:/Program Files/Google/Chrome/Application/chrome.exe';

(async () => {
  const browser = await chromium.launch({ headless: true, executablePath: browserPath });
  const page = await browser.newPage({ viewport: { width: 1200, height: 1600 }, deviceScaleFactor: 1 });
  await page.goto(pathToFileURL(path.join(root, 'index.html')).href, { waitUntil: 'load' });
  await page.evaluate(() => document.fonts.ready);
  await page.locator('#xhs-01').screenshot({ path: path.join(root, 'output', '括号叙事-单页样张.png') });
  await browser.close();
})().catch(error => {
  console.error(error);
  process.exitCode = 1;
});
