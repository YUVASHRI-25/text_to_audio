# Accessibility & Inclusive Learning – Text-to-Speech Learning Assistant

A web-based accessibility tool that converts educational text and PDF materials into speech to support visually impaired students.

## Features

- **Text-to-Speech**: Enter text and convert it to spoken audio
- **PDF Processing**: Upload PDF documents and extract text automatically
- **Dual Engine Support**: Online (gTTS) and offline (pyttsx3) speech engines
- **Accessible UI**: High-contrast colors, large fonts, keyboard navigation, skip links, ARIA labels
- **Audio Playback & Download**: Listen in-browser or download the MP3 file

## Project Structure

```
accessibility-learning-system/
├── app.py                  # Flask backend
├── requirements.txt        # Python dependencies
├── README.md
├── templates/
│   ├── index.html          # Home page
│   └── result.html         # Audio result page
├── static/
│   ├── style.css           # Styles (high-contrast, accessible)
│   └── script.js           # Frontend interactivity
├── uploads/                # Temporary PDF uploads
├── audio/                  # Generated speech files
└── utils/
    ├── __init__.py
    ├── pdf_reader.py        # PDF text extraction (PyPDF2)
    └── tts_engine.py        # TTS engine wrapper (gTTS / pyttsx3)
```

## Installation

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application**:
   ```bash
   python app.py
   ```

3. **Open in browser**: Visit `http://127.0.0.1:5000`

## Usage

1. Open the website
2. Enter text in the text box **or** upload a PDF file
3. Choose a speech engine (online or offline)
4. Click **Convert to Speech**
5. Listen to the audio or download the MP3 file

## Technology Stack

| Component          | Technology     |
|--------------------|----------------|
| Frontend           | HTML, CSS, JS  |
| Backend            | Flask          |
| Text-to-Speech     | gTTS           |
| Offline TTS        | pyttsx3        |
| PDF Processing     | PyPDF2         |
| Language           | Python         |

## Accessibility Features

- Skip-to-content link for keyboard users
- ARIA roles and labels throughout
- High-contrast dark theme
- Large, readable fonts (18px base)
- Visible focus indicators
- Audio autoplay on result page
- Responsive design for all screen sizes
