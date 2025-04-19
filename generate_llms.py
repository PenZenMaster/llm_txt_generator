"""
Module/Script Name: generate_llms.py

Description:
Runs the LLMs text file generator using YAML input to produce a clean llms.txt

Author(s):
Skippy the Magnificent with that filthy monkey, Big G

Created Date: 2025-04-19
Last Modified Date: 2025-04-19

Comments:
- v1.00: Standalone launcher for YAML → LLMs.txt generation
"""

import argparse
from llms_writer import generate_llms_txt

def main():
    parser = argparse.ArgumentParser(description="Generate llms.txt from YAML config")
    parser.add_argument("--config", required=True, help="Path to YAML config")
    parser.add_argument("--output", default="output/llms.txt", help="Output file path")
    parser.add_argument("--seo-mode", action="store_true", help="Enable SEO format")
    args = parser.parse_args()

    generate_llms_txt(args.config, args.output, args.seo_mode)

if __name__ == "__main__":
    main()
