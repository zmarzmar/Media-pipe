# macOS Setup Guide

Complete guide for setting up the Tongue Detection Meme Display on macOS.

## System Requirements

- **macOS:** 10.14 (Mojave) or newer
- **Python:** 3.11
- **Webcam:** Built-in FaceTime camera or USB webcam
- **RAM:** 4GB minimum, 8GB recommended
- **Disk Space:** ~500MB for dependencies

## Installation

### Method 1: Using Homebrew (Recommended)

#### Step 1: Install Homebrew (if not already installed)

Open Terminal and run:
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

#### Step 2: Install Python 3.11

```bash
brew install python@3.11
```

#### Step 3: Verify Installation

```bash
python3.11 --version
```

You should see: `Python 3.11.x`

#### Step 4: Clone or Download the Project

```bash
git clone https://github.com/aaronhubhachen/simple-mediapipe-project.git
cd simple-mediapipe-project
```

#### Step 5: Install Python Dependencies

```bash
python3.11 -m pip install -r requirements.txt
```

If you encounter issues, try:
```bash
brew install cmake
python3.11 -m pip install --upgrade pip
python3.11 -m pip install -r requirements.txt
```

#### Step 6: Add Your Images

Place `apple.png` and `appletongue.png` in the project directory.
See [IMAGE_GUIDE.md](IMAGE_GUIDE.md) for help finding images.

#### Step 7: Make Shell Script Executable

```bash
chmod +x run.sh
```

#### Step 8: Run the Application

```bash
./run.sh
```

Or:
```bash
python3.11 main.py
```

### Method 2: Using python.org Installer

If you don't want to use Homebrew:

1. Download Python 3.11 from [python.org](https://www.python.org/downloads/macos/)
2. Run the installer (`.pkg` file)
3. Open Terminal
4. Verify: `python3.11 --version`
5. Follow steps 4-8 from Method 1

## Camera Permissions

macOS requires explicit permission for apps to use the camera.

### First Time Running

When you first run the app, macOS will show a permission dialog:

**"Terminal" would like to access the camera.**

Click **OK** to allow.

### If You Accidentally Denied Permission

1. Open **System Preferences**
2. Go to **Security & Privacy**
3. Click the **Privacy** tab
4. Select **Camera** from the left sidebar
5. Check the box next to **Terminal** (or your IDE like VS Code, iTerm2, etc.)
6. Restart Terminal
7. Run the app again

### Still Not Working?

Try running from a fresh Terminal window:
```bash
cd /path/to/simple-mediapipe-project
./run.sh
```

## Common Issues on macOS

### Issue 1: "python3.11: command not found"

**Solution 1 - Find Python:**
```bash
# Check what Python versions you have
ls /usr/local/bin/python*
# or
ls /opt/homebrew/bin/python*

# Try these commands
python3 --version
python --version
```

**Solution 2 - Create alias (temporary):**
```bash
# If you have python3 but it's 3.11.x
alias python3.11=python3
python3.11 --version
```

**Solution 3 - Add to PATH:**
```bash
# For Homebrew Python
echo 'export PATH="/opt/homebrew/opt/python@3.11/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

### Issue 2: "Permission denied" when running run.sh

**Solution:**
```bash
chmod +x run.sh
./run.sh
```

### Issue 3: OpenCV or MediaPipe Installation Fails

**Solution 1 - Install build tools:**
```bash
xcode-select --install
brew install cmake
```

**Solution 2 - Update pip:**
```bash
python3.11 -m pip install --upgrade pip setuptools wheel
```

**Solution 3 - Install one by one:**
```bash
python3.11 -m pip install numpy
python3.11 -m pip install opencv-python
python3.11 -m pip install mediapipe
```

### Issue 4: Camera Not Working

Checklist:
- Camera permissions granted (see Camera Permissions section above)
- No other app is using the camera (close Zoom, FaceTime, Photo Booth)
- Camera works in other apps (test with Photo Booth)
- Try restarting Terminal

Try different camera index by editing `main.py`, line ~142:
```python
cap = cv2.VideoCapture(0)  # Change 0 to 1
```

### Issue 5: Window Doesn't Appear

macOS may place windows on a different desktop/space.

1. Look at Mission Control (swipe up with 3-4 fingers or press F3)
2. Check if windows appeared on another desktop
3. Or try running in full screen Terminal

### Issue 6: "SSL: CERTIFICATE_VERIFY_FAILED" During Install

```bash
# For Homebrew Python
/Applications/Python\ 3.11/Install\ Certificates.command

# Or install certificates package
python3.11 -m pip install --upgrade certifi
```

### Issue 7: NumPy Compatibility Warning

This is usually just a warning and won't affect functionality. To fix:
```bash
python3.11 -m pip install numpy --upgrade
```

## Performance Tips for macOS

For better performance:

1. Close other apps using the camera or CPU
2. Reduce window size - edit `main.py`:
   ```python
   WINDOW_WIDTH = 640
   WINDOW_HEIGHT = 480
   ```
3. Lower MediaPipe complexity - edit `main.py`:
   ```python
   face_mesh = mp_face_mesh.FaceMesh(
       model_complexity=0,  # 0=fastest
       min_detection_confidence=0.5,
       min_tracking_confidence=0.5
   )
   ```

For MacBook users:

- Plug in power adapter (app may throttle on battery)
- Close browser tabs and other apps
- Use Activity Monitor to check CPU usage

## Uninstalling

To remove the project and dependencies:

```bash
# Remove project directory
cd ..
rm -rf simple-mediapipe-project

# Uninstall Python packages (optional)
python3.11 -m pip uninstall mediapipe opencv-python numpy

# Uninstall Python 3.11 via Homebrew (optional)
brew uninstall python@3.11
```

## Apple Silicon (M1/M2/M3) Notes

The project works on Apple Silicon Macs! The dependencies should automatically install ARM64 versions.

If you encounter issues:

```bash
# Make sure you're using ARM Homebrew
which brew
# Should show: /opt/homebrew/bin/brew

# Use Rosetta 2 as last resort (not recommended)
arch -x86_64 python3.11 -m pip install -r requirements.txt
```

## Getting Help

If you're still stuck:

1. Check the main [README.md](README.md)
2. Read [QUICKSTART.md](QUICKSTART.md)
3. Review error messages carefully
4. Check Python version: `python3.11 --version`
5. Check pip version: `python3.11 -m pip --version`
6. List installed packages: `python3.11 -m pip list`

## Useful Terminal Commands

```bash
# Navigate to project
cd ~/Downloads/simple-mediapipe-project  # or wherever you saved it

# Run the app
./run.sh

# See what's running
ps aux | grep python

# Kill if frozen
killall python3.11

# Check camera devices
system_profiler SPCameraDataType
```

## macOS Versions

Tested on:
- macOS Sonoma (14.x)
- macOS Ventura (13.x)
- macOS Monterey (12.x)
- macOS Big Sur (11.x)
- macOS Catalina (10.15)
- macOS Mojave (10.14) - should work but not extensively tested

## Next Steps

Once everything is working:

1. Try the [TUTORIAL.md](TUTORIAL.md) to understand the code
2. Read [IMAGE_GUIDE.md](IMAGE_GUIDE.md) for image ideas
3. Customize the detection threshold
4. Add new features!

Happy coding on macOS!

