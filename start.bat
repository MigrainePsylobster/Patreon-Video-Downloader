@echo off
echo Starting Patreon Video Downloader
echo.

REM Check if virtual environment exists
if not exist "venv" (
    echo Virtual environment not found!
    echo Please run "setup.bat" first to set up the application.
    pause
    exit /b 1
)

REM Activate virtual environment
call venv\Scripts\activate
if errorlevel 1 (
    echo Error: Failed to activate virtual environment.
    echo Please run "setup.bat" to fix the installation.
    pause
    exit /b 1
)

REM Start the application
python source\SH_downloader.py

REM Keep window open if there's an error
if errorlevel 1 (
    echo.
    echo Application exited with an error.
    pause
)
