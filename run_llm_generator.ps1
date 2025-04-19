# run_llm_generator.ps1
Set-Location "E:\projects\llm_txt_generator"

# Activate the virtual environment
& ".\.venv\Scripts\Activate.ps1"

# Ensure required Python packages are installed
pip install -r requirements.txt

# Create output folder if it doesn't exist
if (-not (Test-Path "output")) {
    New-Item -ItemType Directory -Path "output"
}

# Run the main script (update to match your entry point)
python main.py --config input\example_client.yaml --output output\llms.txt --seo-mode

# Open the output folder
if (Test-Path "output") {
    Start-Process "output"
}
