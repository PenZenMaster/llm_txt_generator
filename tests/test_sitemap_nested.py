from sitemap_parser import get_all_urls_from_sitemap

def test_nested_sitemap_index():
    urls = get_all_urls_from_sitemap("https://rankrocket.co/sitemap_index.xml", max_urls=10)
    assert isinstance(urls, list)
    assert len(urls) > 0
    assert all(url.startswith("http") for url in urls)