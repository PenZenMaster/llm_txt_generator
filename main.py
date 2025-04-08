# Author: Skippy the Magnificent & George Penzenik
# Version: 1.02
# Date Modified: 04/07/2025 15:12
# Comment: CLI entry point for LLMs.txt Generator

import argparse
from check_site import validate_url_and_sitemap
from sitemap_parser import get_all_urls_from_sitemap
from html_cleaner import extract_text_from_url
from llms_writer import write_llms_files

def main():
    parser = argparse.ArgumentParser(description="""LLMs.txt Generator by Skippy

How It Works:
- Crawls the provided website's sitemap and extracts up to --maxUrls pages
- Cleans and groups page content into logical sections (H2/H3 headers)
- Writes output to:
  * llms.txt - concise summaries
  * llms-full.txt - full raw cleaned content (if --showFullText is used)
  * Optional Markdown formatting with --markdown

Example:
  python main.py --url https://example.com --showFullText --markdown
""")
    parser.add_argument('--url', required=True, help='Root URL of the site')
    parser.add_argument('--maxUrls', type=int, default=10, help='Max pages to crawl (default: 10)')
    parser.add_argument('--showFullText', action='store_true', help='Generate llms-full.txt')
    parser.add_argument('--markdown', action='store_true', help='Output llms.txt in Markdown format')

    import sys
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()

    root_url = args.url
    max_urls = min(max(args.maxUrls, 1), 100)

    print(f"🔍 Validating {root_url}...")
    sitemap_url = validate_url_and_sitemap(root_url)

    print("🌐 Crawling sitemap(s)...")
    urls = get_all_urls_from_sitemap(sitemap_url, max_urls)

    content_data = []
    for url in urls:
        print(f"📄 Extracting from: {url}")
        text = extract_text_from_url(url)
        if text:
            content_data.append((url, text))

    print("📝 Writing output files...")
    write_llms_files(content_data, generate_full=args.showFullText, markdown=args.markdown)

    print("✅ Done! Files saved to current directory.")

if __name__ == "__main__":
    main()
