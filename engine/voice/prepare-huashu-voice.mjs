import crypto from 'node:crypto';
import fs from 'node:fs';
import path from 'node:path';
import { execFileSync } from 'node:child_process';

const audioDir = path.resolve(process.argv[2]);
const voiceRef = process.argv[3] || 'zh_male_liufei_uranus_bigtts';
const model = process.argv[4] || 'seed-tts-2.0';

function probe(file) {
  return JSON.parse(execFileSync('ffprobe', [
    '-v', 'error', '-show_entries', 'stream=codec_name,sample_rate,channels:format=duration', '-of', 'json', file,
  ]));
}

for (const name of fs.readdirSync(audioDir).filter((n) => n.endsWith('.wav') && !n.endsWith('.tmp.wav'))) {
  const file = path.join(audioDir, name);
  const temp = file.replace(/\.wav$/, '.tmp.wav');
  const before = probe(file);
  const stream = before.streams.find((s) => s.codec_name);
  if (stream?.sample_rate !== '48000' || stream?.channels !== 1) {
    execFileSync('ffmpeg', ['-y', '-v', 'error', '-i', file, '-ar', '48000', '-ac', '1', temp]);
    fs.rmSync(file, { force: true });
    fs.renameSync(temp, file);
  }
  const after = probe(file);
  const bytes = fs.readFileSync(file);
  const receipt = {
    path: name,
    provider: 'volcengine',
    mode: 'official_tts',
    generated: true,
    requested_model: model,
    voice_ref: voiceRef,
    duration: Number(after.format.duration),
    codec_name: after.streams[0].codec_name,
    sample_rate: Number(after.streams[0].sample_rate),
    channels: Number(after.streams[0].channels),
    sha256: crypto.createHash('sha256').update(bytes).digest('hex'),
    credential: 'VOLC_TTS_API_KEY supplied transiently; value not stored',
  };
  fs.writeFileSync(file.replace(/\.wav$/, '.voice.json'), JSON.stringify(receipt, null, 2) + '\n', 'utf8');

  const timingFile = file.replace(/\.wav$/, '.json');
  if (fs.existsSync(timingFile)) {
    const timing = JSON.parse(fs.readFileSync(timingFile, 'utf8'));
    timing.duration = receipt.duration;
    fs.writeFileSync(timingFile, JSON.stringify(timing, null, 1) + '\n', 'utf8');
  }
  console.log(`${name}: ${receipt.duration.toFixed(2)}s / ${receipt.sample_rate}Hz / ${receipt.channels}ch / ${receipt.sha256.slice(0, 12)}`);
}
