# 🧠 LLMs Text Generator

## Overview
This tool converts structured YAML files into SEO-optimized `llms.txt` files designed to help Large Language Models (LLMs) like ChatGPT, Bing AI, and Perplexity understand the semantic footprint of your website.

---

## 🔧 Key Components

- `generate_llms.py` – CLI launcher that accepts a YAML config and produces `llms.txt`
- `llms_writer.py` – Core logic for formatting structured YAML content
- `run_llm_txt_generator.bat` – Desktop batch launcher for non-terminal users
- `launch_llm_txt_generator.ps1` – Activates virtual environment and runs generator
- Output is saved to `output/llms.txt` or to the root directory of a WordPress site

---

## 🧩 Inputs

### Example YAML
```yaml
client_name: Slick Willy
address:
  street: 6869 wine
  city: Anytown
  state: WY
  zip: 999999
  country: US
website: https://me.me
category: Slicker
services:
  - service
target_cities: []
top_pages: []
faq_prompts: []
keywords: []
citations:
  - name: Google
    url: https://google.com
```

---

## ✅ Usage
```bash
python generate_llms.py --config path/to/client.yaml --output output/llms.txt --seo-mode
```

---

## 🚀 Next Steps
- [ ] Integrate with Skippy YAML Builder for one-click generation
- [ ] Return `llms.txt` content directly to YAML Builder UI
- [ ] Upload `llms.txt` to root of WordPress site for LLM indexing
- [ ] Optionally create a hidden WordPress page for `llms.txt` via Push It Real Good

