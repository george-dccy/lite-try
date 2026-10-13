# 用法：python3 master.py → video.mp4 + contact.png + 检查报告
import json, subprocess as sp, re
C = json.load(open('cues.json'))
def run(cmd): return sp.run(cmd, capture_output=True, text=True)
# 1) 两遍 loudnorm：先测，再按测量值精确归一到 −14 LUFS / 真峰 −1 dBTP
r = run(['ffmpeg', '-hide_banner', '-i', 'audio.wav', '-af', 'loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json', '-f', 'null', '-'])
m = json.loads(r.stderr[r.stderr.rfind('{'): r.stderr.rfind('}') + 1])
af = (f"loudnorm=I=-14:TP=-1.5:LRA=11:measured_I={m['input_i']}:measured_TP={m['input_tp']}:"
      f"measured_LRA={m['input_lra']}:measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true")
run(['ffmpeg', '-y', '-hide_banner', '-i', 'audio.wav', '-af', af, '-ar', '48000', 'audio_master.wav'])
# 2) 合成：PNG 序列 + 母带音频 → H.264 / AAC
run(['ffmpeg', '-y', '-hide_banner', '-framerate', str(C['fps']), '-i', 'frames/%05d.png', '-i', 'audio_master.wav',
     '-c:v', 'libx264', '-crf', '16', '-preset', 'slow', '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '256k', '-ar', '48000',
     '-t', str(C['duration']), '-movflags', '+faststart', 'video.mp4'])
# 3) 检查：时长 / 分辨率 / 帧率 / 响度 / 真峰 + 每 0.5 s 一格的 contact sheet
p = json.loads(run(['ffprobe', '-v', 'error', '-show_streams', '-show_format', '-of', 'json', 'video.mp4']).stdout)
v = [s for s in p['streams'] if s['codec_type'] == 'video'][0]
e = run(['ffmpeg', '-hide_banner', '-i', 'video.mp4', '-af', 'ebur128=peak=true', '-f', 'null', '-']).stderr
I = re.findall(r'I:\s+(-?[\d.]+) LUFS', e)[-1]; TP = re.findall(r'Peak:\s+(-?[\d.]+) dBFS', e)[-1]
cols = int(C['duration'] * 2 / 2)
run(['ffmpeg', '-y', '-hide_banner', '-i', 'video.mp4', '-vf', f'fps=2,scale=480:-1,tile={cols}x2', '-frames:v', '1', 'contact.png'])
print(f"duration {float(p['format']['duration']):.3f}s | {v['width']}x{v['height']} | {v['r_frame_rate']} fps | {I} LUFS | true peak {TP} dBTP")
