import os

def write_llms_files(data, generate_full=False, markdown=False):
    llms_path = os.path.join(os.getcwd(), 'llms.txt')
    full_path = os.path.join(os.getcwd(), 'llms-full.txt')

    with open(llms_path, 'w', encoding='utf-8') as f:
        for url, sections in data:
            if markdown:
                f.write(f"# {get_page_title(sections)}\n")
                f.write(f"## URL: {url}\n")
            else:
                f.write(f"{url}\n")

            for section in sections:
                header = section['header'].strip()
                summary = summarize(section['body'])
                if markdown:
                    f.write(f"### {header}\n{summary}\n\n")
                else:
                    f.write(f"{header}: {summary}\n")
            f.write("\n")

    if generate_full:
        with open(full_path, 'w', encoding='utf-8') as f:
            for url, sections in data:
                f.write(f"URL: {url}\n---\n")
                for section in sections:
                    f.write(f"{section['header']}\n{section['body'].strip()}\n\n")

def summarize(text, max_sentences=2):
    sentences = text.split('. ')
    return '. '.join(sentences[:max_sentences]).strip() + ('...' if len(sentences) > max_sentences else '')

def get_page_title(sections):
    return sections[0]['header'] if sections else "Untitled Page"
