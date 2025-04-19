import os
import re

EXCLUDE_DIRS = {"venv", ".venv", "__pycache__", "site-packages"}


def nuke_unicode_safe(root_dir):
    for subdir, dirs, files in os.walk(root_dir):
        # Skip excluded folders
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        for file in files:
            if file.endswith(".py"):
                path = os.path.join(subdir, file)
                try:
                    with open(path, "r", encoding="utf-8") as f:
                        content = f.read()
                    cleaned = re.sub(r"[^\x00-\x7F]+", "", content)
                    if content != cleaned:
                        with open(path, "w", encoding="utf-8") as f:
                            f.write(cleaned)
                        print(f" Cleaned: {path}")
                except Exception as e:
                    print(f" Error on {path}: {e}")


#  Your actual project path here
nuke_unicode_safe(r"E:\projects\llm_txt_generator")
