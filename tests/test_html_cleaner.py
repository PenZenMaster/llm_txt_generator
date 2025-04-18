from html_cleaner import extract_text_from_url

def test_extract_text_returns_list():
    sections = extract_text_from_url("https://rankrocket.co/llms-sitemap.xml")
    assert isinstance(sections, list)

    # Filter out invalid entries
    cleaned = [s for s in sections if isinstance(s, str) and s.strip()]
    
    # Must have at least one usable string
    assert len(cleaned) > 0