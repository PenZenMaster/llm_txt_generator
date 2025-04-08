import os

def write_llms_files(data, generate_full=False):
    llms_path = os.path.join(os.getcwd(), 'llms.txt')
    full_path = os.path.join(os.getcwd(), 'llms-full.txt')

    with open(llms_path, 'w', encoding='utf-8') as f:
        for url, text in data:
            summary = summarize(text)
            f.write(f"{url}\nSummary: {summary}\n\n")

    if generate_full:
        with open(full_path, 'w', encoding='utf-8') as f:
            for url, text in data:
                f.write(f"URL: {url}\n---\n{text}\n\n")

def summarize(text, max_sentences=2):
    sentences = text.split('. ')
    return '. '.join(sentences[:max_sentences]).strip() + ('...' if len(sentences) > max_sentences else '')
