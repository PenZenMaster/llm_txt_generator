import os

def find_unicode_offenders(root_path, extensions=(".py",)):
    print(f" Scanning for non-ASCII characters in: {root_path}\n")
    for dirpath, _, filenames in os.walk(root_path):
        for filename in filenames:
            if filename.endswith(extensions):
                filepath = os.path.join(dirpath, filename)
                try:
                    with open(filepath, "r", encoding="utf-8") as f:
                        for i, line in enumerate(f, 1):
                            if any(ord(char) > 127 for char in line):
                                print(f"  {filepath}:{i}: {line.strip()}")
                except Exception as e:
                    print(f" Failed to read {filepath}: {e}")

if __name__ == '__main__':
    import sys
    target = sys.argv[1] if len(sys.argv) > 1 else "."
    find_unicode_offenders(target)