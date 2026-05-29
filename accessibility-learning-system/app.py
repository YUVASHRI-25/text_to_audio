import os

import uuid

from flask import Flask, render_template, request, send_file, redirect, url_for, flash

from werkzeug.utils import secure_filename

from utils.pdf_reader import extract_text_from_pdf

from utils.tts_engine import text_to_speech



app = Flask(__name__)

app.secret_key = os.urandom(24)



UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), "uploads")

AUDIO_FOLDER = os.path.join(os.path.dirname(__file__), "audio")

ALLOWED_EXTENSIONS = {"pdf"}



app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

app.config["AUDIO_FOLDER"] = AUDIO_FOLDER

app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024  # 16 MB max upload



os.makedirs(UPLOAD_FOLDER, exist_ok=True)

os.makedirs(AUDIO_FOLDER, exist_ok=True)





def allowed_file(filename):

    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS





@app.route("/")

def index():

    """Render the home page."""

    return render_template("index.html")





@app.route("/convert", methods=["POST"])

def convert():

    """Convert text or PDF to speech."""

    text = request.form.get("text", "").strip()

    pdf_file = request.files.get("pdf")



    # Extract text from PDF if uploaded

    if pdf_file and pdf_file.filename and allowed_file(pdf_file.filename):

        try:

            extracted = extract_text_from_pdf(pdf_file.stream)

            if extracted.strip():

                text = extracted

            else:

                flash("Could not extract text from PDF. The PDF may contain images only.")

                return redirect(url_for("index"))

        except Exception:

            flash("Failed to read the PDF file. Please try a different file.")

            return redirect(url_for("index"))

    elif pdf_file and pdf_file.filename and not allowed_file(pdf_file.filename):

        flash("Only PDF files are allowed.")

        return redirect(url_for("index"))



    if not text:

        flash("Please enter text or upload a PDF file.")

        return redirect(url_for("index"))



    # Generate unique audio filename

    audio_filename = f"speech_{uuid.uuid4().hex[:8]}.mp3"

    audio_path = os.path.join(app.config["AUDIO_FOLDER"], audio_filename)



    try:

        text_to_speech(text, audio_path)

    except Exception as e:

        flash(f"Speech generation failed: {str(e)}")

        return redirect(url_for("index"))



    return render_template("result.html", audio_file=audio_filename, text=text)





@app.route("/audio/<filename>")

def serve_audio(filename):

    """Serve a generated audio file."""

    safe_name = secure_filename(filename)

    audio_path = os.path.join(app.config["AUDIO_FOLDER"], safe_name)

    if not os.path.exists(audio_path):

        flash("Audio file not found.")

        return redirect(url_for("index"))

    return send_file(audio_path, mimetype="audio/mpeg")





@app.route("/download/<filename>")

def download(filename):

    """Download a generated audio file."""

    safe_name = secure_filename(filename)

    audio_path = os.path.join(app.config["AUDIO_FOLDER"], safe_name)

    if not os.path.exists(audio_path):

        flash("Audio file not found.")

        return redirect(url_for("index"))

    return send_file(audio_path, mimetype="audio/mpeg", as_attachment=True, download_name=safe_name)





if __name__ == "__main__":

    app.run(debug=True, port=5000)

