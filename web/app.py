import os
import subprocess
import json
from flask import Flask, request, render_template

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHECKER_PATH = os.path.join(BASE_DIR, "checker", "checker.py")
UPLOAD_DIR = os.path.join(BASE_DIR, "uploads")

os.makedirs(UPLOAD_DIR, exist_ok=True)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("upload.html")

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]
    zip_path = os.path.join(UPLOAD_DIR, file.filename)
    file.save(zip_path)

    result = subprocess.run(
        ["python", CHECKER_PATH, zip_path],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    stdout = result.stdout.strip()
    first_line = stdout.splitlines()[0] if stdout else ""

    try:
        report = json.loads(first_line)
    except Exception as e:
        report = {
            "status": "ERROR",
            "output": stdout,
            "error": str(e)
        }

    return render_template("report.html", report=report)

if __name__ == "__main__":
    app.run(debug=True)
