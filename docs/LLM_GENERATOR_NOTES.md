# LLMs.txt Generator Overview

How It Works
The LLMs.txt Generator:

Crawls the provided website URL and its linked pages

Extracts clean, meaningful text content
Generates two formats:
llms.txt: Concise summaries and key information
llms-full.txt: Complete text content with more detail
Simply provide a URL, and Skippy magic will crawl the site and generate both llms.txt and llms-full.txt files that can be used for training or analysis with any LLM.
Has the ability to handle nested sitemaps and HTML parsing

Sanity checks 
1. verifies that provided URL is reachable
2. verifies that an XML sitemap is available at the URL (root of domain)

​Key Parameters:

url: The website URL to generate LLMs.txt files from
maxUrls (Optional): Maximum number of pages to crawl (1-100, default: 10)
showFullText (Optional): Generate llms-full.txt in addition to llms.txt (default: false)

CLI version - runable from a terminal and will deposit files in the directory where the python is run from
More Coolio UI version - Sexy interface 

Version 1.01
Add command line help for CLI version
When HELP is requested:
1. You need to provide the URL to scan to create the LLMx.txt files
2. Set the number of URLs to scan (default is 10) and reccomended for initial runs
3. Set the showFullText to true or false (default is false)