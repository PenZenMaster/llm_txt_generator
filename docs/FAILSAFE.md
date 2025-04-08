# 🛡️ LLMs.txt Generator – FAILSAFE

## Purpose
This file serves as your emergency manual in case things go sideways.

---

## 💥 If It Fails to Run
1. Ensure all required packages are installed:
   ```
   pip install -r docs/requirements.txt
   ```

2. Run the CLI:
   ```
   python llm_txt_generator/main.py --url https://example.com --maxUrls 10 --showFullText
   ```

3. Validate:
   - The URL must be reachable
   - `https://example.com/sitemap.xml` must exist

---

## 🧪 Run Unit Tests
```
python -m unittest discover -s llm_txt_generator/tests
```

---

## 🛠️ Modify or Extend
- Add functionality in modules inside `llm_txt_generator/`
- Use `summarize()` in `llms_writer.py` to tweak LLM summary behavior
- Extend HTML cleaning logic in `html_cleaner.py` for better output

---

## 🔒 Fail-Safe Principles
- Keep everything modular
- Validate before crawling
- Fail gracefully with informative errors
- Keep `llms.txt` short, `llms-full.txt` detailed
