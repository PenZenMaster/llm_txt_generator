import requests
import xml.etree.ElementTree as ET

def get_all_urls_from_sitemap(sitemap_url, max_urls=10):
    urls = []
    try:
        response = requests.get(sitemap_url, timeout=10)
        response.raise_for_status()
        root = ET.fromstring(response.content)

        ns = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}

        if root.tag.endswith('sitemapindex'):
            for sitemap in root.findall('ns:sitemap/ns:loc', ns):
                nested = get_all_urls_from_sitemap(sitemap.text, max_urls)
                urls.extend(nested)
                if len(urls) >= max_urls:
                    break
        else:
            for url in root.findall('ns:url/ns:loc', ns):
                urls.append(url.text)
                if len(urls) >= max_urls:
                    break

    except Exception as e:
        print(f" Failed to parse sitemap {sitemap_url}: {e}")
    
    return urls[:max_urls]
