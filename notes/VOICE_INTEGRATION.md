# 语音接入记录

## 本次采用

- Provider：Volcengine。
- API：新式 `VOLC_TTS_API_KEY`，只在当前命令进程中注入，不写入项目文件。
- Model：`seed-icl-2.0`（Huashu 复刻 2.0 路由）。
- Voice：`S_iGgUZmh22`，作为项目默认复刻音色。
- 字幕：火山返回的逐字时间戳，写入白板渲染所需的 `audio/*.json`。
- Huashu 兼容验收：`engine/voice/prepare-huashu-voice.mjs` 将音频统一到 48kHz 单声道，并生成相邻 `.voice.json` 回执，记录时长、编码、SHA256、模型和音色引用。

## 当前状态

Huashu 用户配置已绑定 `narrator → S_iGgUZmh22`，并将默认 voice mode 设为 `clone`。项目只保存 speaker ID，不保存 API Key。

如果更换音色，只需更新 Huashu 用户配置和项目 `config.json` 的 voice/resourceId；不要把 API Key 或参考音频写进项目公开配置。
