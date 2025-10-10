#!/bin/bash

echo "============================================================"
echo "Starting Tongue Detection Meme Display..."
echo "============================================================"
echo ""

# Function to check Python version
check_python_version() {
    local python_cmd=$1
    local version=$($python_cmd --version 2>&1 | grep -oE '3\.[0-9]+')
    echo "$version"
}

# Check if main.py exists
if [ ! -f "main.py" ]; then
    echo "[ERROR] main.py not found in current directory!"
    echo "Make sure you are running this from the project folder."
    echo ""
    exit 1
fi

# Check for image files and warn if missing
if [ ! -f "apple.png" ]; then
    echo "[WARNING] apple.png not found!"
    echo "You need to add apple.png to the current directory."
    echo "This image is displayed when tongue is NOT out."
    echo ""
fi

if [ ! -f "appletongue.png" ]; then
    echo "[WARNING] appletongue.png not found!"
    echo "You need to add appletongue.png to the current directory."
    echo "This image is displayed when tongue IS out."
    echo ""
fi

# Determine which Python to use
PYTHON_CMD=""

if command -v python3.11 &> /dev/null; then
    PYTHON_CMD="python3.11"
    echo "[OK] Python 3.11 detected:"
    python3.11 --version
elif command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(check_python_version python3)
    if [[ "$PYTHON_VERSION" == "3.11" ]]; then
        PYTHON_CMD="python3"
        echo "[OK] Python 3.11 detected:"
        python3 --version
    else
        echo "[WARNING] Python 3.11 not found."
        echo "Found Python $PYTHON_VERSION instead."
        echo "This may cause compatibility issues."
        echo ""
        read -p "Continue anyway? (y/n) " -n 1 -r
        echo ""
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            PYTHON_CMD="python3"
        else
            echo "[ERROR] Exiting. Please install Python 3.11."
            echo ""
            echo "Installation instructions:"
            echo "  macOS (Homebrew): brew install python@3.11"
            echo "  Ubuntu/Debian: sudo apt install python3.11"
            echo "  Fedora: sudo dnf install python3.11"
            exit 1
        fi
    fi
else
    echo "[ERROR] Python 3 not found!"
    echo "Please install Python 3.11."
    echo ""
    echo "Installation instructions:"
    echo "  macOS (Homebrew): brew install python@3.11"
    echo "  Ubuntu/Debian: sudo apt install python3.11"
    echo "  Fedora: sudo dnf install python3.11"
    exit 1
fi

echo ""
echo "Starting application..."
echo "Press Ctrl+C to stop or 'q' in the application window to quit."
echo ""

# Run the application
$PYTHON_CMD main.py

echo ""
echo "[OK] Application closed."
echo ""

