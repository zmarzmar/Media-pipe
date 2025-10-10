#!/bin/bash

echo "============================================================"
echo "Starting Tongue Detection Meme Display..."
echo "============================================================"
echo ""
echo "Make sure you have:"
echo "  - apple.png in the current directory"
echo "  - appletongue.png in the current directory"
echo ""

# Try to use python3.11 if available, otherwise fall back to python3
if command -v python3.11 &> /dev/null; then
    echo "Using Python 3.11..."
    python3.11 main.py
elif command -v python3 &> /dev/null; then
    # Check if python3 is version 3.11
    PYTHON_VERSION=$(python3 --version 2>&1 | grep -oP '3\.\d+')
    if [[ "$PYTHON_VERSION" == "3.11" ]]; then
        echo "Using Python 3.11..."
        python3 main.py
    else
        echo "Warning: Python 3.11 not found. Using $PYTHON_VERSION instead."
        echo "This may cause compatibility issues."
        echo ""
        read -p "Continue anyway? (y/n) " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            python3 main.py
        else
            echo "Exiting. Please install Python 3.11."
            exit 1
        fi
    fi
else
    echo "Error: Python 3 not found. Please install Python 3.11."
    exit 1
fi

