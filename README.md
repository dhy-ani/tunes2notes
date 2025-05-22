# 🎼 Tunes2Notes

Convert any audio file into clean sheet music (PDF) using Spleeter, Magenta, and LilyPond — all in a Streamlit UI.

## How it works
1. Upload audio (mp3, wav, etc.)
2. Piano is isolated using Spleeter
3. Converted to MIDI with Magenta
4. Rendered into sheet music PDF via music21 + LilyPond

## Run Locally
```bash
docker build -t tunes2notes .
docker run -p 8501:8501 tunes2notes
