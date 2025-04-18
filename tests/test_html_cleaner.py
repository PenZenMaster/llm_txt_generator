from html_cleaner import extract_text_from_url

def test_extract_text_returns_list():
    sections = extract_text_from_url("https://rankrocket.co/contact-rank-rocket/")
    assert isinstance(sections, list)

    cleaned = [s for s in sections if isinstance(s, str) and s.strip()]
    assert len(cleaned) > 0