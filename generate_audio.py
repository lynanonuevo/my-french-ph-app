#!/usr/bin/env python3
from pathlib import Path
import json, wave, sys
try:
    from piper import PiperVoice
except Exception as e:
    print("Piper is not available in this Python environment.")
    print("Activate it first: source ~/french-voice/bin/activate")
    raise
ROOT=Path(__file__).resolve().parent
MODEL_CANDIDATES=[Path.cwd()/"fr_FR-siwis-medium.onnx", Path.home()/"fr_FR-siwis-medium.onnx", ROOT/"fr_FR-siwis-medium.onnx"]
model=next((p for p in MODEL_CANDIDATES if p.exists()),None)
if model is None:
    # Search home shallowly because the voice was downloaded from Terminal's working directory
    hits=list(Path.home().glob("**/fr_FR-siwis-medium.onnx"))
    model=hits[0] if hits else None
if model is None:
    print("Could not find fr_FR-siwis-medium.onnx on your Mac.")
    print("Run: python -m piper.download_voices fr_FR-siwis-medium")
    sys.exit(1)
print(f"Using voice: {model}")
voice=PiperVoice.load(str(model))
manifest=json.loads((ROOT/"audio_manifest.json").read_text(encoding="utf-8"))
out=ROOT/"audio"; out.mkdir(exist_ok=True)
items=list(manifest.items())
for n,(text,fn) in enumerate(items,1):
    dest=out/fn
    if dest.exists() and dest.stat().st_size>1000:
        continue
    print(f"[{n}/{len(items)}] {text}")
    with wave.open(str(dest),"wb") as wav:
        # Compatible with the Piper package installed earlier
        if hasattr(voice,"synthesize_wav"):
            voice.synthesize_wav(text,wav)
        else:
            voice.synthesize(text,wav)
print(f"Done. Generated {len(items)} fixed French recordings in: {out}")
print("You can now upload this whole folder's contents to GitHub.")
