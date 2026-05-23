# Sign Language Translator - PowerShell Launch Script
# Run with: powershell -ExecutionPolicy Bypass -File run_app.ps1

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Sign Language Translator v1.0" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Get script directory
$scriptPath = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $scriptPath

# Check model file
if (-not (Test-Path "cnn8grps_rad1_model.h5")) {
    Write-Host "ERROR: Model file not found!" -ForegroundColor Red
    Write-Host "Please ensure cnn8grps_rad1_model.h5 is in this directory"
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host "Starting application..." -ForegroundColor Green
Write-Host ""

# Run the application
& python final_pred.py

if ($LASTEXITCODE -ne 0) {
    Write-Host ""
    Write-Host "Application closed with error code: $LASTEXITCODE" -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
}
