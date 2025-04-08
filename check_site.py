import requests
from urllib.parse import urljoin

def validate_url_and_sitemap(base_url):
    try:
        response = requests.head(base_url, timeout=10)
        response.raise_for_status()
    except Exception as e:
        raise ValueError(f"Site not reachable: {e}")

    sitemap_url = urljoin(base_url, '/sitemap.xml')
    try:
        response = requests.head(sitemap_url, timeout=10)
        response.raise_for_status()
    except Exception as e:
        raise ValueError(f"Sitemap not found at {sitemap_url}: {e}")

    return sitemap_url
