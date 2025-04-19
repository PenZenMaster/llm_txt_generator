"""
Module/Script Name: llms_validator.py

Description:
Validates an llms.txt file to ensure it meets SEO-ready, LLM-readable format:
- Contains all required sections
- Contains only ASCII characters
- Includes at least one valid URL

Author(s):
Skippy the Magnificent with an eensy weensy bit of help from that filthy monkey, Big G

Created Date: 2025-04-18
Last Modified Date: 2025-04-18

Comments:
- v1.00: Initial validator release for LLM-SEO content
"""

import re
import sys

REQUIRED_SECTIONS = [
    "[ENTITY]",
    "[CATEGORY]",
    "[MISSION STATEMENT]",
    "[SERVICES]",
    "[LOCATIONS SERVED]",
    "[TOP CONTENT LINKS]",
    "[FAQ PROMPTS]",
    "[SEO TOPICS]",
    "[RELATED ENTITIES]",
]

URL_REGEX = re.compile(r"https?://[\w./%-]+")


def is_ascii(text):
    return all(ord(c) < 128 for c in text)


def validate_llms_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    text = "".join(lines)
    missing_sections = [s for s in REQUIRED_SECTIONS if s not in text]
    non_ascii_lines = [
        (i + 1, line.strip()) for i, line in enumerate(lines) if not is_ascii(line)
    ]
    urls = URL_REGEX.findall(text)

    print(f"\n🔍 Validating: {filepath}")

    if missing_sections:
        print(f"❌ Missing sections:")
        for s in missing_sections:
            print(f"  - {s}")
    else:
        print("✅ All required sections present.")

    if non_ascii_lines:
        print(f"❌ Non-ASCII characters found:")
        for lineno, line in non_ascii_lines[:5]:
            print(f"  Line {lineno}: {line}")
    else:
        print("✅ No Unicode characters found.")

    if urls:
        print(f"✅ Found {len(urls)} URLs.")
    else:
        print("❌ No URLs found in file.")

    if not missing_sections and not non_ascii_lines and urls:
        print("\n🎉 llms.txt passes all validation checks! Ready for upload.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python llms_validator.py <path-to-llms.txt>")
        sys.exit(1)

    validate_llms_file(sys.argv[1])
