@echo off
echo Cleaning project cruft...
if exist bad.txt del bad.txt
if exist not_ASCII.txt del not_ASCII.txt
if exist resuts.txt del resuts.txt
if exist llms_launcher_kit.zip del llms_launcher_kit.zip
if exist dir.txt del dir.txt
if exist tree.txt del tree.txt
if exist __init__.py del __init__.py
if exist __pycache__\ (rmdir /s /q __pycache__)
if exist .pytest_cache\ (rmdir /s /q .pytest_cache)
echo Done.