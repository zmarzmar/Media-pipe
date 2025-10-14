# Quick Start Guide

Get up and running in 5 minutes.

## Prerequisites

- **Operating System:** Windows 10/11, macOS 10.14+, or Linux
- **Python 3.11** installed
- **Webcam** (built-in or USB)
- **Two meme images** (see step 4)

## Setup

### 1. Download the Project

```bash
git clone https://github.com/aaronhubhachen/simple-mediapipe-project.git
cd simple-mediapipe-project
```

### 2. Verify Python 3.11

**Windows:**
```bash
python3.11 --version
```

**macOS/Linux:**
```bash
python3.11 --version
# or try:
python3 --version
```

You should see: `Python 3.11.x`

Don't have Python 3.11? Download from [python.org](https://www.python.org/downloads/)
- macOS with Homebrew: `brew install python@3.11`
- Linux (Ubuntu/Debian): `sudo apt install python3.11`
- Linux (Fedora): `sudo dnf install python3.11`

### 3. Install Dependencies

**Windows:**
```bash
python3.11 -m pip install -r requirements.txt
```

**macOS/Linux:**
```bash
python3.11 -m pip install -r requirements.txt
# or if python3.11 command doesn't exist:
pip3 install -r requirements.txt
```

This will install:
- MediaPipe (face detection)
- OpenCV (camera and image processing)
- NumPy (numerical operations)

Note for macOS users: You may need to install cmake if you get errors:
```bash
brew install cmake
```

### 4. Add Your Meme Images

You need two PNG images named:
- `apple.png` - Shown when tongue is NOT out
- `appletongue.png` - Shown when tongue IS out

Where to find images:
- Google Images (search for "apple emoji png", "tongue emoji png")
- Emoji websites (emojipedia.org)
- Create your own in Paint/Photoshop
- Use any fun before/after images

Place both PNG files in the same directory as `main.py`

### 5. Run the Application

**Windows:**
- Double-click `run.bat` in File Explorer, or:
```powershell
.\run.bat
```
Or run directly:
```bash
python3.11 main.py
```

**macOS/Linux:**
```bash
chmod +x run.sh  # Only needed the first time
./run.sh
```
Or run directly:
```bash
python3.11 main.py
```

### 6. Use the App

Two windows will open:
1. **Camera Input** - Shows your face with detection status
2. **Meme Output** - Shows the meme that changes when you stick your tongue out

Controls:
- Stick your tongue out → meme changes to `appletongue.png`
- Close your mouth → meme changes back to `apple.png`
- Press 'q' → quit

## Troubleshooting

### "python3.11 not found"

**Windows:**
Try:
```bash
python --version
```

If you have Python 3.11 but the command doesn't work:
```bash
python -m pip install -r requirements.txt
python main.py
```

**macOS/Linux:**
Try:
```bash
python3 --version
```

If it shows 3.11.x, use `python3` instead:
```bash
python3 -m pip install -r requirements.txt
python3 main.py
```

Note: Make sure it's Python 3.11, not 3.13 or other versions.

### "Could not open webcam"

All platforms:
1. Close any other apps using the webcam (Zoom, Teams, Skype, etc.)
2. Try unplugging and replugging your USB webcam (if external)

Windows:
- Check webcam permissions: Settings → Privacy → Camera
- Allow desktop apps to access camera

macOS:
- Check permissions: System Preferences → Security & Privacy → Camera
- Allow Terminal or your IDE to access the camera
- You may need to restart Terminal after granting permission

Linux:
- Check if your user is in the video group: `groups $USER`
- If not, add yourself: `sudo usermod -a -G video $USER` (then log out and back in)
- Check camera device: `ls /dev/video*`

### Images not found

Make sure:
1. Files are named exactly `apple.png` and `appletongue.png` (lowercase, .png extension)
2. Files are in the same folder as `main.py`
3. Files are valid PNG images (not corrupted)

### Tongue detection too sensitive / not sensitive enough

Edit `main.py` and change line 27:

```python
TONGUE_OUT_THRESHOLD = 0.03  # Change this value
```

- **Too sensitive?** Increase to 0.04 or 0.05
- **Not sensitive enough?** Decrease to 0.02 or 0.015

## What's Next?

Got it working? Great! Now try:

1. **Experiment with different images** - Try funny faces, pets, memes
2. **Adjust the threshold** - Find the perfect sensitivity for you
3. **Read the tutorial** - Learn how the code works: `TUTORIAL.md`
4. **Customize it** - Add new gestures, sounds, filters!

## Need Help?

- Check the main `README.md` for detailed documentation
- Read `TUTORIAL.md` to understand how the code works
- Look at the troubleshooting sections

## Tips for Best Results

**Position yourself well:**
- Face the camera directly
- Ensure good lighting
- Stay 1-2 feet from the camera

**For better detection:**
- Open your mouth wider when sticking tongue out
- Make exaggerated expressions
- Avoid backlighting (light behind you)

**Performance tips:**
- Close other camera applications
- Run on a decent computer (webcam processing requires CPU)

Have fun!

