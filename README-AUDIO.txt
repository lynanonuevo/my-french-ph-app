FRENCH POCKET — STATIC SIWIS AUDIO

This package contains 890 unique French utterances.

ON YOUR MAC:
1. Extract this ZIP.
2. Open Terminal.
3. Activate Piper:
   source ~/french-voice/bin/activate
4. Go into the extracted folder. Easiest: type "cd " (with a space), drag the extracted folder from Finder into Terminal, then press Return.
5. Run:
   python generate_audio.py
6. Wait until it says Done.
7. Open index.html through your GitHub Pages deployment after uploading ALL files AND the audio folder.

The generator uses fr_FR-siwis-medium, the voice you approved. It loads the model once, then generates all clips. Existing clips are skipped, so rerunning is safe.
