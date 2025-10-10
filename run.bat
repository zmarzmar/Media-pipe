@echo off
echo ============================================================
echo Starting Tongue Detection Meme Display...
echo ============================================================
echo.

REM Check if Python 3.11 is available
python3.11 --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python 3.11 not found!
    echo Please install Python 3.11 or update this script to use your Python version.
    echo.
    pause
    exit /b 1
)

echo Python 3.11 detected: 
python3.11 --version
echo.

REM Check if required files exist
if not exist "main.py" (
    echo ERROR: main.py not found in current directory!
    echo Make sure you are running this from the project folder.
    echo.
    pause
    exit /b 1
)

if not exist "apple.png" (
    echo WARNING: apple.png not found!
    echo You need to add apple.png to the current directory.
    echo This image is displayed when tongue is NOT out.
    echo.
)

if not exist "appletongue.png" (
    echo WARNING: appletongue.png not found!
    echo You need to add appletongue.png to the current directory.
    echo This image is displayed when tongue IS out.
    echo.
)

echo Starting application...
echo Press Ctrl+C to stop or 'q' in the application window to quit.
echo.

python3.11 main.py

echo.
echo Application closed.
pause

