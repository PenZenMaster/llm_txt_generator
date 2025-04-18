from flask import (
    Flask,
    render_template,
    request,
    send_from_directory,
    url_for,
    redirect,
    flash,
)
import subprocess
import os

# Create Flask app
app = Flask(__name__, static_folder="static", template_folder="templates")
app.secret_key = "shades-of-white-skippy-key"  # Needed for flashing messages

# Expected output files from the generator
OUTPUT_FILES = ["llms.txt", "llms-full.txt"]


@app.route("/", methods=["GET"])
def index():
    """Render the main form."""
    return render_template("index.html")


@app.route("/generate", methods=["GET", "POST"])
def generate():
    if request.method == "GET":
        return redirect(url_for("index"))

    # Gather form inputs
    url = request.form.get("url")
    max_urls = request.form.get("maxUrls") or "10"
    show_full = "showFullText" in request.form
    markdown = "markdown" in request.form

    # Build command to run the existing CLI tool (adjust path to main.py)
    main_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "main.py")
    )
    venv_python = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "venv", "Scripts", "python.exe")
    )
    cmd = [venv_python, main_path, f"--url={url}", f"--maxUrls={max_urls}"]

    if show_full:
        cmd.append("--showFullText")
    if markdown:
        cmd.append("--markdown")

    # Remove any prior output files
    for fname in OUTPUT_FILES:
        if os.path.exists(fname):
            os.remove(fname)

    try:
        # Execute the CLI generator
        process = subprocess.run(
            cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )
    except Exception as e:
        flash(f"Error executing generator: {str(e)}", "error")
        return redirect(url_for("index"))

    # Determine which files were created
    available = [f for f in OUTPUT_FILES if os.path.exists(f)]

    # Check for missing module error
    if "ModuleNotFoundError" in process.stderr:
        flash(
            " Python module not found. Please make sure all required packages are installed (e.g., beautifulsoup4).",
            "error",
        )

    # Render the template with execution logs and download links
    return render_template(
        "index.html", stdout=process.stdout, stderr=process.stderr, files=available
    )


@app.route("/download/<path:filename>")
def download_file(filename):
    """Serve generated files for download."""
    return send_from_directory(os.getcwd(), filename, as_attachment=True)


if __name__ == "__main__":
    # Run in debug mode for development
    app.run(debug=True, host="0.0.0.0", port=5000)
