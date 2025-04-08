import requests
from bs4 import BeautifulSoup

def extract_text_from_url(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # Prefer <main> or <article> content if available
        content_root = soup.find('main') or soup.find('article') or soup.body

        # Remove junk
        for tag in content_root(['script', 'style', 'footer', 'nav', 'noscript', 'form', 'header', 'aside', 'button', 'svg', 'img', 'input']):
            tag.decompose()

        # Extract text sections grouped by headers
        sections = []
        current_section = {"header": "Introduction", "body": ""}

        for element in content_root.descendants:
            if element.name in ['h2', 'h3']:
                if current_section["body"]:
                    sections.append(current_section)
                current_section = {"header": element.get_text(strip=True), "body": ""}
            elif element.name is None and isinstance(element, str):
                current_section["body"] += element.strip() + " "

        if current_section["body"]:
            sections.append(current_section)

        return sections

    except Exception as e:
        print(f"⚠️ Error extracting text from {url}: {e}")
        return []
