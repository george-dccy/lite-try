param(
  [Parameter(Mandatory = $true)]
  [string]$ProjectDir,
  [Parameter(Mandatory = $true)]
  [string]$AudioDir
)

$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.Speech

New-Item -ItemType Directory -Force -Path $AudioDir | Out-Null
$scriptPath = Join-Path $ProjectDir 'scenes\script.json'
$scenes = Get-Content -Raw -LiteralPath $scriptPath | ConvertFrom-Json
$utf8NoBom = New-Object System.Text.UTF8Encoding($false)

function Get-NormCount([string]$Text) {
  return @([regex]::Matches($Text, '[\p{L}\p{N}]')).Count
}

function Get-Units([string]$Text) {
  return @([regex]::Matches($Text, '[\p{L}\p{N}]|[，。？！；：、]') | ForEach-Object { $_.Value })
}

foreach ($scene in $scenes) {
  $segments = @($scene.segments)
  $text = ($segments -join '')
  $wavPath = Join-Path $AudioDir "$($scene.name).wav"
  $jsonPath = Join-Path $AudioDir "$($scene.name).json"

  $synth = New-Object System.Speech.Synthesis.SpeechSynthesizer
  $voice = $synth.GetInstalledVoices() | Where-Object { $_.VoiceInfo.Name -eq 'Microsoft Huihui Desktop' } | Select-Object -First 1
  if ($voice) { $synth.SelectVoice($voice.VoiceInfo.Name) }
  $synth.Rate = 2
  $synth.Volume = 100
  $synth.SetOutputToWaveFile($wavPath)
  $synth.Speak($text)
  $synth.SetOutputToNull()
  $synth.Dispose()

  $durationText = (& ffprobe -v quiet -show_entries format=duration -of csv=p=0 -- $wavPath).Trim()
  $duration = [double]::Parse($durationText, [Globalization.CultureInfo]::InvariantCulture)
  $units = @(Get-Units $text)
  $unitCount = [Math]::Max(1, $units.Count)
  $wordList = @()
  for ($i = 0; $i -lt $units.Count; $i++) {
    $start = $duration * $i / $unitCount
    $end = $duration * ($i + 1) / $unitCount
    $wordList += [pscustomobject]@{
      w = $units[$i]
      s = [Math]::Round($start, 3)
      e = [Math]::Round($end, 3)
    }
  }

  $segmentStarts = @()
  $prefix = ''
  foreach ($segment in $segments) {
    $segmentStarts += [Math]::Round($duration * (Get-NormCount $prefix) / [Math]::Max(1, (Get-NormCount $text)), 3)
    $prefix += $segment
  }
  if ($segmentStarts.Count -gt 0) { $segmentStarts[0] = 0 }

  $payload = [ordered]@{
    name = $scene.name
    duration = [Math]::Round($duration, 3)
    segmentStarts = @($segmentStarts)
    segments = @($segments)
    voice = 'Microsoft Huihui Desktop'
    words = $wordList.Count
    normChars = Get-NormCount $text
    wordList = @($wordList)
  }
  [IO.File]::WriteAllText($jsonPath, ($payload | ConvertTo-Json -Depth 8), $utf8NoBom)
  Write-Output "$($scene.name): $([Math]::Round($duration, 1))s  starts=$($segmentStarts -join ',')  words=$($wordList.Count)"
}
