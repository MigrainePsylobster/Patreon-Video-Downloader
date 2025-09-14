@echo off
echo Patreon Video Downloader - Setup Script
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH.
    echo Please install Python 3.8+ from https://python.org
    echo Make sure to check "Add Python to PATH" during installation.
    pause
    exit /b 1
)

echo Python found:
python --version
echo.

REM Check if virtual environment exists
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
    if errorlevel 1 (
        echo Error: Failed to create virtual environment.
        echo Make sure Python venv module is available.
        pause
        exit /b 1
    )
    echo Virtual environment created successfully.
    echo.
) else (
    echo Virtual environment already exists.
    echo.
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate
if errorlevel 1 (
    echo Error: Failed to activate virtual environment.
    pause
    exit /b 1
)

REM Check if requirements are already installed by looking for yt-dlp
python -c "import yt_dlp" 2>nul
if errorlevel 1 (
    echo Installing requirements...
    echo This may take a few minutes...
    pip install -r source\requirements.txt
    if errorlevel 1 (
        echo Error: Failed to install requirements.
        echo Make sure you have an internet connection.
        pause
        exit /b 1
    )
    echo.
    echo Requirements installed successfully!
    echo.
) else (
    echo Requirements already installed.
    echo Checking for updates...
    pip install -r source\requirements.txt --upgrade
    echo.
)

REM Verify installation
echo Verifying installation...
python -c "import tkinter; import yt_dlp; import requests; print('All dependencies verified successfully!')"
if errorlevel 1 (
    echo Error: Some dependencies are missing or corrupted.
    echo Try running this setup script again.
    pause
    exit /b 1
)

echo.
echo ========================================
echo Setup completed successfully!
echo ========================================
echo.
echo You can now run the application using:
echo   - Double-click "start.bat" 
echo   - Or run: python source\SH_downloader.py
echo.
echo Press any key to exit...
pause >nul
