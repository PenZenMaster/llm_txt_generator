
import argparse
import os
from check_site import validate_url_and_get_sitemap
from sitemap_parser import get_all_urls_from_sitemap
from html_cleaner import extract_text_from_url
from llms_writer import write_llms_files

def main():
    parser = argparse.ArgumentParser(description='LLMs.txt Generator')
    parser.add_argument('--url', required=True, help='The root URL of the site to process')
    parser.add_argument('--maxUrls', type=int, default=10, help='Max number of URLs to fetch')
    parser.add_argument('--showFullText', action='store_true', help='Include full cleaned text output')
    parser.add_argument('--markdown', action='store_true', help='Format llms.txt using Markdown')

    args = parser.parse_args()
    root_url = args.url
    max_urls = args.maxUrls

    print(f"[*] Validating {root_url}...")
    sitemap_url = validate_url_and_get_sitemap(root_url)
    if not sitemap_url:
        print("[WARN] Sitemap not found or site could not be validated.")
        return

    print(f"[✓] Sitemap found: {sitemap_url}")
    urls = get_all_urls_from_sitemap(sitemap_url, max_urls)

    if not urls:
        print("[WARN] No URLs found in sitemap.")
        return

    print(f"[✓] Found {len(urls)} URLs to process.")

    page_texts = {}
    for i, url in enumerate(urls):
        print(f"[*] ({i+1}/{len(urls)}) Extracting: {url}")
        cleaned_text = extract_text_from_url(url)
        if cleaned_text:
            page_texts[url] = cleaned_text

    print(f"[✓] Writing output to llms.txt{' and llms-full.txt' if args.showFullText else ''}...")
    write_llms_files(page_texts, use_markdown=args.markdown, include_full_text=args.showFullText)

    print("[✓] All done.")

if __name__ == '__main__':
    main()
