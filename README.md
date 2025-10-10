# 👅 Tongue Detection Meme Display

A fun Python application using MediaPipe and OpenCV that detects when your tongue is out and displays different meme images in real-time!

**GitHub:** [https://github.com/aaronhubhachen/simple-mediapipe-project](https://github.com/aaronhubhachen/simple-mediapipe-project)

Perfect for learning about:
- MediaPipe Face Mesh detection
- Real-time video processing with OpenCV
- Facial landmark analysis
- Computer vision basics

**🚀 New to this project?** Start with the [Quick Start Guide](QUICKSTART.md) to get running in 5 minutes!

**📚 Want to understand how it works?** Check out the [Tutorial](TUTORIAL.md) for detailed explanations!

**🍎 macOS user?** See the [macOS Setup Guide](SETUP_MACOS.md) for platform-specific instructions!

## Features

- 🎥 Real-time webcam face detection using MediaPipe Face Mesh
- 👅 Tongue-out detection algorithm
- 🖼️ Dual window display: Camera input and Meme output
- 📺 Large window sizes (960x720) for clear visibility
- 🔄 Real-time switching between normal and tongue-out meme images

## Requirements

- **Python 3.11** (specifically 3.11, not 3.13 or other versions)
- Webcam (built-in or USB)
- Two meme images: `apple.png` and `appletongue.png`
- **Operating System:** Windows 10/11, macOS 10.14+, or Linux

## Installation

### For All Operating Systems:

1. **Install Python dependencies (using Python 3.11):**
   
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

2. **Add your meme images:**
   
   You need to provide two PNG images:
   - `apple.png` - Displayed when tongue is NOT out
   - `appletongue.png` - Displayed when tongue IS out
   
   **How to get images:**
   - Find any meme images you like online
   - Create your own custom images
   - Use any PNG images (they will be automatically resized to 960x720)
   - Recommended: Use images with transparent backgrounds or high contrast
   
   **Example ideas:**
   - Apple emoji + Apple with tongue out emoji
   - Happy face + Silly face
   - Normal pet + Derpy pet
   - Any before/after style meme format

## Usage

### Windows:

**Option 1: Double-click the batch file (easiest):**
- Simply double-click `run.bat` in File Explorer

**Option 2: Run from PowerShell:**
```powershell
.\run.bat
```

**Option 3: Run from Command Prompt (cmd):**
```cmd
run.bat
```

**Option 4: Run directly with Python:**
```bash
python3.11 main.py
```

### macOS/Linux:

**Option 1: Run with shell script (easiest):**
```bash
chmod +x run.sh  # Only needed once to make script executable
./run.sh
```

**Option 2: Run directly with Python:**
```bash
python3.11 main.py
# or
python3 main.py
```

### Controls
- Press **'q'** to quit the application

### How it works

1. The application opens two windows:
   - **Camera Input**: Shows your live webcam feed with detection status
   - **Meme Output**: Displays the appropriate meme image

2. When your face is detected:
   - If your tongue is **NOT out** → displays `apple.png`
   - If your tongue **IS out** → displays `appletongue.png`

3. Status indicators appear on the camera input window:
   - "TONGUE OUT!" (green) - Tongue detected
   - "No tongue detected" (yellow) - Face detected but no tongue
   - "No face detected" (red) - No face in view

## Troubleshooting

### Tongue detection not working properly

The tongue detection threshold can be adjusted in `main.py`. Look for this line:

```python
TONGUE_OUT_THRESHOLD = 0.03  # Adjust this value based on your needs
```

- **Increase the value** (e.g., 0.05) if it's too sensitive (detects tongue when it's not out)
- **Decrease the value** (e.g., 0.02) if it's not sensitive enough (doesn't detect tongue when it is out)

### Webcam not opening

- Make sure no other application is using the webcam
- Try changing the camera index in `main.py`: `cap = cv2.VideoCapture(0)` to `cap = cv2.VideoCapture(1)`
- **macOS users:** Grant camera permissions in System Preferences → Security & Privacy → Camera
- **Linux users:** Ensure your user is in the `video` group: `sudo usermod -a -G video $USER`

### Images not loading

- Ensure `apple.png` and `appletongue.png` are in the same directory as `main.py`
- Check that the image files are valid PNG format

## Installation Quick Start

```bash
# Clone the repository
git clone https://github.com/aaronhubhachen/simple-mediapipe-project.git
cd simple-mediapipe-project

# Install dependencies (Python 3.11)
python3.11 -m pip install -r requirements.txt

# Add your meme images (apple.png and appletongue.png)

# Run the app
# Windows (PowerShell): .\run.bat
# Windows (Command Prompt): run.bat
# Windows (Double-click): Just double-click run.bat
# macOS/Linux: ./run.sh
```

See the [Quick Start Guide](QUICKSTART.md) for detailed instructions.

## Project Structure

```
simple-mediapipe-project/
├── main.py              # Main application script (well-commented for learning)
├── requirements.txt     # Python dependencies
├── run.bat              # Windows batch file to run with Python 3.11
├── run.sh               # macOS/Linux shell script to run with Python 3.11
├── README.md            # This file - project overview and documentation
├── QUICKSTART.md        # Quick 5-minute setup guide
├── TUTORIAL.md          # Detailed tutorial on how the code works
├── IMAGE_GUIDE.md       # Guide for finding and preparing images
├── SETUP_MACOS.md       # macOS-specific setup guide
├── CONTRIBUTING.md      # Guide for contributors
├── LICENSE              # MIT License
├── .gitignore           # Git ignore file
├── apple.png            # Meme image (normal state) - YOU NEED TO ADD THIS
└── appletongue.png      # Meme image (tongue out) - YOU NEED TO ADD THIS
```

## Technical Details

- **Face Detection**: Uses MediaPipe Face Mesh for real-time facial landmark detection
- **Tongue Detection**: Analyzes mouth landmark distances to determine if tongue is extended
- **Window Size**: 960x720 pixels (approximately half of a 1920x1080 monitor)
- **Frame Processing**: Mirror effect applied for natural interaction

## Dependencies

- `mediapipe==0.10.7` - Face mesh detection and tracking
- `opencv-python==4.8.1.78` - Video capture and display
- `numpy==1.24.3` - Numerical operations

## Customization Ideas 🎨

Want to make this project your own? Try these modifications:

1. **Different gestures**: Modify the detection logic to detect smiles, winks, or eyebrow raises
2. **More images**: Add multiple states (happy, sad, surprised) instead of just two
3. **Sound effects**: Play sounds when tongue is detected
4. **Record mode**: Save funny moments to video files
5. **Filters/Effects**: Add Instagram-style filters to the camera feed
6. **Hand gestures**: Combine with MediaPipe Hands for hand gesture detection
7. **Green screen**: Replace the background instead of showing meme images

## Troubleshooting Common Issues

### "No module named 'cv2'"
- Make sure you installed the requirements with Python 3.11
- Run: `python3.11 -m pip install -r requirements.txt`

### Webcam shows black screen
- Check if another application is using the webcam
- Try allowing webcam permissions in Windows Settings

### Detection is laggy
- Close other applications using the webcam
- Lower the camera resolution in `main.py`
- Ensure your computer meets minimum requirements

## Contributing

We welcome contributions! Whether you're fixing bugs, adding features, or improving documentation, your help is appreciated.

**Want to contribute?** Check out our [Contributing Guide](CONTRIBUTING.md) for:
- How to get started
- Code style guidelines
- Pull request process
- Feature ideas for all skill levels

Some quick ideas:
- Improve tongue detection algorithm
- Add support for multiple faces (smile, wink, etc.)
- Create a GUI for adjusting sensitivity
- Add gesture recording/playback
- Optimize performance
- Improve cross-platform compatibility

## Platform Support

This project is fully cross-platform:

| Platform | Status | Instructions |
|----------|--------|--------------|
| 🪟 Windows 10/11 | ✅ Fully Supported | Use `run.bat` or see [Quick Start](QUICKSTART.md) |
| 🍎 macOS 10.14+ | ✅ Fully Supported | See [macOS Setup Guide](SETUP_MACOS.md) |
| 🐧 Linux | ✅ Supported | Use `run.sh` or see [Quick Start](QUICKSTART.md) |

## Credits

Built with:
- [MediaPipe](https://google.github.io/mediapipe/) by Google
- [OpenCV](https://opencv.org/)
- [NumPy](https://numpy.org/)
- Python 3.11

## License

MIT License - Feel free to use and modify as needed. See LICENSE file for details.

