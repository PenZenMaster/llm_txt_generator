import requests
from bs4 import BeautifulSoup

def extract_text_from_url(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        for tag in soup(['script', 'style', 'header', 'footer', 'nav', 'noscript', 'form']):
            tag.decompose()

        text = soup.get_text(separator=' ', strip=True)
        return text

    except Exception as e:
        print(f"⚠️ Error extracting text from {url}: {e}")
        return None
