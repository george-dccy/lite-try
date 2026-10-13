#!/bin/sh
# 依赖：Node 18+ 与 playwright（npm i playwright && npx playwright install chromium）、Python 3 + numpy、ffmpeg
# 已有 Chromium 时可指定：CHROME=/path/to/chromium sh run.sh
set -e
node render.cjs --stills 0.5,1.0,1.1,2.0,2.6,3.8   # 1) 关键帧先看（stills/）
node render.cjs --mb 4                             # 2) 全片逐帧，4 个子帧做运动模糊（frames/ + motion.json）
python3 audio.py                                   # 3) 代码合成配乐与音效（audio.wav）
python3 master.py                                  # 4) 两遍响度归一 + 合成 video.mp4 + 规格检查 + contact.png
