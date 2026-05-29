# Accessibility & Inclusive Learning — Text-to-Speech Assistant

A small Flask app that converts user-provided text or uploaded PDFs into spoken audio. Built for accessibility with a simple, keyboard-friendly UI and options for online/offline TTS.

**Project folder:** `accessibility-learning-system`

**Live locally:** http://127.0.0.1:5000

## Quick Start (Windows PowerShell)

1. Open PowerShell and change to the project folder:

```powershell
cd accessibility-learning-system
```

2. (Optional) Activate the virtual environment:

```powershell
. .venv/Scripts/Activate.ps1
```

3. Install dependencies:

```powershell
e:/inclusive_learning/.venv/Scripts/python.exe -m pip install -r requirements.txt
# or if venv is activated: python -m pip install -r requirements.txt
```

4. Run the app:

```powershell
e:/inclusive_learning/.venv/Scripts/python.exe app.py
# or: python app.py
```

Open your browser at http://127.0.0.1:5000.

## How to use

- Go to the home page, paste or type text, or upload a PDF file.
- Click Convert to generate audio — playback and download links appear on the result page.

## Troubleshooting

- If the server stops, restart with:

```powershell
cd accessibility-learning-system
e:/inclusive_learning/.venv/Scripts/python.exe app.py
```
- If PDF text extraction fails for scanned/image PDFs, try OCR before uploading (not included).

## Files to know

- `accessibility-learning-system/app.py` — main Flask app
- `accessibility-learning-system/utils/pdf_reader.py` — PDF text extraction
- `accessibility-learning-system/utils/tts_engine.py` — TTS wrapper used to produce MP3 files

---

Created from accessibility-learning-system/README.md
