import os
from gtts import gTTS


def text_to_speech(text, output_path):
    """Convert text to speech using gTTS."""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    tts = gTTS(text=text, lang="en")
    tts.save(output_path)
    return output_path
