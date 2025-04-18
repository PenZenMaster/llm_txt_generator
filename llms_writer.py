import os

def write_llms_files(data, use_markdown=False, include_full_text=False):
    llms_path = os.path.join(os.getcwd(), 'llms.txt')
    full_path = os.path.join(os.getcwd(), 'llms-full.txt')

    with open(llms_path, 'w', encoding='utf-8') as f:
        for url, sections in data.items():
            f.write(f"# {url}\n\n" if use_markdown else f"{url}\n")
            f.write(f"{sections}\n\n")

    if include_full_text:
        with open(full_path, 'w', encoding='utf-8') as f:
            for url, sections in data.items():
                f.write(f"# {url}\n\n{sections}\n\n")