# video-kit

这是 Notion「创意视频机制｜用代码做视频」附录脚手架的可运行本地实现。机制正文和验收标准只在 Notion 维护；这里不复制机制，只保存 6 个可运行文件和仓库执行说明。

来源：https://app.notion.com/p/3f727110f8d581409fc6efb83e348eb0

运行：

```sh
sh run.sh
```

依赖：Node 18+、Playwright/Chromium、Python 3、numpy、ffmpeg。脚手架默认输出 video.mp4、contact.png 和中间目录。验证目标为精确 4.000 s、−14 ±1 LUFS、真峰 ≤ −1 dBTP；完整检查仍按 Notion 视频机制 §8 执行。

