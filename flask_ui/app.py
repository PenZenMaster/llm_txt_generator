from flask import Flask, render_template, request, send_from_directory, url_for
import subprocess
import os

# Create Flask app
app = Flask(__name__, static_folder="static", template_folder="templates")

# Expected output files from the generator
OUTPUT_FILES = ["llms.txt", "llms-full.txt"]


@app.route("/", methods=["GET"])
def index():
    """Render the main form."""
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    """Handle form submission, invoke the CLI generator, and return results."""
    # Gather form inputs
    url = request.form.get("url")
    max_urls = request.form.get("maxUrls") or "10"
    show_full = "showFullText" in request.form
    markdown = "markdown" in request.form

    # Build command to run the existing CLI tool
    cmd = ["python", "main.py", f"--url={url}", f"--maxUrls={max_urls}"]
    if show_full:
        cmd.append("--showFullText")
    if markdown:
        cmd.append("--markdown")

    # Remove any prior output files
    for fname in OUTPUT_FILES:
        if os.path.exists(fname):
            os.remove(fname)

    # Execute the CLI generator
    process = subprocess.run(
        cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    )

    # Determine which files were created
    available = [f for f in OUTPUT_FILES if os.path.exists(f)]

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
