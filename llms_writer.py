import os
import yaml

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

def generate_llms_txt(config_path, output_path, seo_mode=False):
    with open(config_path, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)

    lines = []

    if seo_mode:
        lines.append('[ENTITY]')
        lines.append(config.get('client_name', 'Unknown'))

        # Properly format the address dict
        address = config.get('address', {})
        if isinstance(address, dict):
            addr_line = f"{address.get('street', '')}, {address.get('city', '')}, {address.get('state', '')} {address.get('zip', '')}, {address.get('country', '')}"
            lines.append(addr_line.strip())
        else:
            lines.append(str(address))

        lines.append(config.get('website', ''))

        lines.append('\n[CATEGORY]')
        lines.append(config.get('category', ''))

        lines.append('\n[SERVICES]')
        lines.extend([f'- {s}' for s in config.get('services', [])])

        lines.append('\n[LOCATIONS SERVED]')
        lines.extend([f'- {c}' for c in config.get('target_cities', [])])

        lines.append('\n[TOP CONTENT LINKS]')
        lines.extend(config.get('top_pages', []))

        lines.append('\n[FAQ PROMPTS]')
        lines.extend(config.get('faq_prompts', []))

        lines.append('\n[SEO TOPICS]')
        lines.extend(config.get('keywords', []))

        lines.append('\n[RELATED ENTITIES]')
        for rel in config.get('citations', []):
            if isinstance(rel, dict):
                lines.append(f"{rel.get('name', 'Unknown')} | {rel.get('url', '')}")
            else:
                lines.append(str(rel))

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        for line in lines:
            if isinstance(line, str):
                f.write(line.strip() + "\n")
            elif isinstance(line, (dict, list)):
                f.write(str(line) + "\n")
            elif line is None:
                f.write("\n")
            else:
                f.write(str(line).strip() + "\n")

    print(f"✅ llms.txt written to: {output_path}")
