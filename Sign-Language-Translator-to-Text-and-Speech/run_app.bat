@echo off
REM Sign Language Translator - Easy Launch Script
REM This script runs the application with proper error handling

cd /d "%~dp0"

echo.
echo ========================================
echo  Sign Language Translator v1.0
echo ========================================
echo.
echo Starting application...
echo.

REM Check if model file exists
if not exist cnn8grps_rad1_model.h5 (
    echo ERROR: Model file not found!
    echo Please ensure cnn8grps_rad1_model.h5 is in this directory
    pause
    exit /b 1
)

REM Run the application
python final_pred.py

if errorlevel 1 (
    echo.
    echo Application closed with error code: %errorlevel%
    pause
) else (
    echo.
    echo Application closed successfully
)
