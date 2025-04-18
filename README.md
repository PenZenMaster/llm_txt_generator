# LLM Text Generator & Site Scanner

A Python-based tool for generating LLM-ready training text from websites using sitemaps, HTML scrapers, and content filters. Includes both a Flask web UI and command-line interface (CLI), as well as a complete Pytest-based test suite.

## 🚀 Features
- ✅ Hierarchical sitemap discovery (`sitemap_index.xml` supported)
- ✅ Robust HTML content extraction (skips non-HTML safely)
- ✅ CLI mode and Flask web interface
- ✅ Full test suite located in `tests/`
- ✅ Auto-generated output (`llms.txt`, `llms-full.txt`)
- ✅ Download links from UI, or script output via CLI

## 📁 Directory Structure

```
llm_txt_generator/
├── main.py
├── html_cleaner.py
├── sitemap_parser.py
├── llms_writer.py
├── check_site.py
├── run_tests.py
├── requirements.txt
├── flask_ui/
│   ├── app.py
│   ├── templates/
│   └── static/
└── tests/
    ├── test_check_site.py
    ├── test_html_cleaner.py
    ├── test_llms_writer.py
    ├── test_sitemap_parser.py
    ├── test_sitemap_nested.py
    └── __init__.py
```

## ⚙️ How to Run (Dev)

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the Flask UI
```bash
python flask_ui/app.py
```

### 3. Run tests
```bash
python run_tests.py
```

### 4. Run CLI
```bash
python main.py --url=https://example.com --maxUrls=10 --showFullText --markdown
```

## 🧪 Notes
- Output files (`llms.txt`, `llms-full.txt`) are generated in the working directory.
- Non-HTML pages are gracefully skipped during scraping.