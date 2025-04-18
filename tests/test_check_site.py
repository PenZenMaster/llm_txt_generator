import pytest
from check_site import validate_url_and_sitemap

def test_valid_url():
    sitemap = validate_url_and_sitemap("https://rankrocket.co")
    assert "sitemap" in sitemap.lower()

def test_invalid_url():
    with pytest.raises(ValueError):
        validate_url_and_sitemap("https://invalid.domain.zzz")