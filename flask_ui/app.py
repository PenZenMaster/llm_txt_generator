import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from flask import Flask, render_template, request, send_file
from check_site import validate_url_and_sitemap
from sitemap_parser import get_all_urls_from_sitemap
from html_cleaner import extract_text_from_url
from llms_writer import write_llms_files
import os
import tempfile

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    output_files = None
    log = ""
    if request.method == "POST":
        url = request.form["url"]
        max_urls = int(request.form.get("maxUrls", 10))
        show_full = "showFullText" in request.form
        markdown = "markdown" in request.form

        try:
            sitemap_url = validate_url_and_sitemap(url)
            urls = get_all_urls_from_sitemap(sitemap_url, max_urls)

            data = []
            for u in urls:
                sections = extract_text_from_url(u)
                if sections:
                    data.append((u, sections))

            write_llms_files(data, generate_full=show_full, markdown=markdown)
            output_files = {
                "llms": "llms.txt",
                "full": "llms-full.txt" if show_full else None,
            }
            log = f"✅ Generated {len(data)} entries from sitemap."

        except Exception as e:
            log = f"❌ Error: {str(e)}"

    return render_template("index.html", output=output_files, log=log)


@app.route("/download/<filename>")
def download(filename):
    return send_file(filename, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
