import requests
from urllib.parse import urljoin

def discover_sitemap_from_robots(base_url):
    try:
        robots_url = urljoin(base_url, '/robots.txt')
        response = requests.get(robots_url, timeout=10)
        if response.status_code == 200:
            for line in response.text.splitlines():
                if line.lower().startswith('sitemap:'):
                    return line.split(':', 1)[1].strip()
    except Exception:
        pass
    return None

def validate_url_and_sitemap(base_url):
    try:
        response = requests.head(base_url, timeout=10)
        response.raise_for_status()
    except Exception as e:
        raise ValueError(f"Site not reachable: {e}")

    sitemap_url = discover_sitemap_from_robots(base_url)
    if not sitemap_url:
        sitemap_url = urljoin(base_url, '/sitemap.xml')

    try:
        response = requests.head(sitemap_url, timeout=10)
        response.raise_for_status()
        return sitemap_url
    except Exception as e:
        raise ValueError(f"Sitemap not found at {sitemap_url}: {e}")