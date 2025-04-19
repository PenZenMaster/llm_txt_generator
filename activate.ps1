$env:VIRTUAL_ENV = "$PSScriptRoot\.venv"
& "$PSScriptRoot\.venv\Scripts\Activate.ps1"
Write-Host "🧠 Activated venv for $PWD"