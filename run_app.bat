@echo off
REM Ensure the script stops if any command fails
setlocal enabledelayedexpansion
set err=0

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Python is not installed. Please install it from https://www.python.org/ and try again.
    set err=1
)

REM Install dependencies
if !err!==0 (
    echo Installing dependencies...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo Failed to install dependencies.
        set err=1
    )
)

REM Run the application
if !err!==0 (
    echo Running the application...
    start /B pythonw main.py
)

REM Exit the script
exit
