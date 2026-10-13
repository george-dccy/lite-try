# 用法：python3 audio.py  → audio.wav（48 kHz 立体声）
# 配乐和音效全部用代码合成；时间点读 cues.json（与画面同一份），音效强弱读 motion.json（画面导出的速度曲线）
import json, wave, numpy as np
C = json.load(open('cues.json')); E = C['ev']; SR = 48000; DUR = C['duration']
N = int(SR * DUR); L = np.zeros(N); R = np.zeros(N); rs = np.random.default_rng(7)   # 种子固定，每次结果一致
t_all = np.arange(N) / SR
def add(sig, at, gain_db=0.0, pan=0.0):
    i = int(at * SR); sig = sig[: max(0, N - i)] * 10 ** (gain_db / 20)
    L[i:i + len(sig)] += sig * np.sqrt((1 - pan) / 2) * 1.414; R[i:i + len(sig)] += sig * np.sqrt((1 + pan) / 2) * 1.414
def env(n, a=0.005, d=0.3):                       # 起音 + 指数衰减
    t = np.arange(n) / SR; return np.minimum(1, t / max(a, 1e-4)) * np.exp(-t / d)
def lowpass(x, fc):                               # 一阶低通（fc 可为逐采样数组）
    fc = np.broadcast_to(fc, x.shape); a = np.exp(-2 * np.pi * fc / SR); y = np.zeros_like(x); s = 0.0
    for i in range(len(x)): s = (1 - a[i]) * x[i] + a[i] * s; y[i] = s
    return y
def midi(n): return 440 * 2 ** ((n - 69) / 12)
# ---------- 音乐：120 BPM 节拍网格（60 fps 时一拍 = 30 帧），冲击后才进鼓 ----------
beat = 60 / C['bpm']
chords = [[57, 60, 64], [53, 57, 60], [55, 59, 62], [52, 55, 59]]          # Am F G Em
for bar in range(int(DUR / (beat * 4)) + 1):
    t0 = bar * beat * 4; n = int(beat * 4 * SR); tt = np.arange(n) / SR
    pad = sum(np.sin(2 * np.pi * midi(m) * tt + np.sin(2 * np.pi * 0.3 * tt)) for m in chords[bar % 4]) / 3
    pad *= np.minimum(1, tt / 0.6) * np.minimum(1, (beat * 4 - tt) / 0.3).clip(0)
    add(pad * 0.18, t0, -6)
k = 0
while k * beat < DUR:
    tb = k * beat
    if tb >= E['impact'] - 1e-6:                                             # 鼓从冲击那一拍开始
        n = int(0.35 * SR); tt = np.arange(n) / SR
        f = 45 + 75 * np.exp(-tt / 0.03); kick = np.sin(2 * np.pi * np.cumsum(f) / SR) * env(n, 0.001, 0.12)
        add(kick, tb, -4)
        hat = rs.standard_normal(int(0.05 * SR)); hat = (hat - lowpass(hat, 6000)) * env(len(hat), 0.001, 0.015)
        add(hat, tb + beat / 2 + 0.004 * ((k % 2) * 2 - 1), -16, 0.3)       # 微偏移 ±4 ms，避免机械感
    k += 1
# ---------- 音效：从运动里长出来 ----------
M = json.load(open('motion.json')); mt = np.array([m['t'] for m in M]); sp = np.array([m['speed'] for m in M])
speed = np.interp(t_all, mt, sp); sn = speed / (speed.max() + 1e-9)
whoosh = lowpass(rs.standard_normal(N), 300 + 5000 * sn) * sn ** 1.5        # 速度 → 风声的音量和亮度
L += whoosh * 0.5; R += whoosh * 0.5
def impact(at, strength=1.0):                                                # 冲量 → 冲击声：低频 thump + 噪声 click
    n = int(0.6 * SR); tt = np.arange(n) / SR
    thump = np.sin(2 * np.pi * (60 + 90 * np.exp(-tt / 0.02)) * tt) * env(n, 0.001, 0.18)
    click = rs.standard_normal(n) * env(n, 0.0005, 0.008)
    add((thump + 0.4 * click) * strength, at, -2)
impact(E['impact'], 1.0)
for i in range(1, len(sp) - 1):                                               # 之后的小弹跳：速度曲线里的“折返点”
    if mt[i] > E['impact'] + 0.05 and sp[i] > 200 and sp[i] >= sp[i - 1] and sp[i] > sp[i + 1] and M[i]['y'] > M[i - 1]['y'] - 1:
        impact(mt[i], min(1, sp[i] / sp.max()) * 0.8)
def chime(at, note, gain=-10, pan=0):
    n = int(1.2 * SR); tt = np.arange(n) / SR; f = midi(note)
    s = (np.sin(2 * np.pi * f * tt) + 0.3 * np.sin(2 * np.pi * 2.01 * f * tt) + 0.1 * np.sin(2 * np.pi * 3.0 * f * tt)) * env(n, 0.002, 0.35)
    add(s, at, gain, pan)
for i in range(7): chime(E['label'] + i * 3 / C['fps'], 76 + [0, 2, 4, 7, 9, 12, 14][i], -18, -0.5 + i / 6)   # 字入场：逐字错峰小音
chime(E['hero'], 81, -8); chime(E['hero'] + 0.02, 88, -14)                   # 英雄时刻
# ---------- 输出（母带响度交给 master.py 做两遍 loudnorm）----------
mx = np.stack([L, R], 1); mx /= max(1e-9, np.abs(mx).max()) / 0.7
fade = np.minimum(1, (DUR - t_all) / 0.25)[:, None]; mx *= fade
with wave.open('audio.wav', 'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((mx * 32767).astype('<i2').tobytes())
print('audio.wav', DUR, 's')
