import requests
from bs4 import BeautifulSoup

def extract_text_from_url(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        # Skip non-HTML responses (e.g., plain text, images)
        content_type = response.headers.get('Content-Type', '')
        if 'text/html' not in content_type:
            print(f"[WARN] Skipping non-HTML content at {url}")
            return []

        soup = BeautifulSoup(response.content, 'lxml')

        content_root = soup.find('main') or soup.find('article') or soup.body
        if not content_root:
            print(f"[WARN] No usable content section found at {url}")
            return []

        for tag in content_root(['script', 'style', 'nav', 'footer', 'noscript']):
            tag.decompose()

        sections = [section.get_text(separator=' ', strip=True)
                    for section in content_root.find_all(['h1', 'h2', 'p', 'div'])]
        return [s for s in sections if s]

    except Exception as e:
        print(f" Error extracting text from {url}: {e}")
        return []