# Tutorial: Building a Tongue Detection App with MediaPipe

This tutorial will walk you through how this tongue detection application works and how you can customize it.

## Table of Contents
1. [Understanding the Code Structure](#understanding-the-code-structure)
2. [How MediaPipe Face Mesh Works](#how-mediapipe-face-mesh-works)
3. [The Tongue Detection Algorithm](#the-tongue-detection-algorithm)
4. [Customizing the Detection](#customizing-the-detection)
5. [Adding New Features](#adding-new-features)

## Understanding the Code Structure

The application is built with three main components:

### 1. MediaPipe Face Mesh Initialization
```python
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5,
    max_num_faces=1
)
```
This sets up the face detection model with:
- `min_detection_confidence`: How confident the model must be to detect a face (0.5 = 50%)
- `min_tracking_confidence`: How confident to keep tracking the face
- `max_num_faces`: Maximum faces to detect (we only need 1)

### 2. Webcam Capture Loop
The main loop continuously:
1. Captures frames from the webcam
2. Processes each frame with MediaPipe
3. Detects if tongue is out
4. Displays the appropriate meme image

### 3. Tongue Detection Function
The `is_tongue_out()` function analyzes facial landmarks to determine if the tongue is visible.

## How MediaPipe Face Mesh Works

MediaPipe Face Mesh detects **468 3D facial landmarks** in real-time. These landmarks are numbered points that track:
- Eyes and eyebrows
- Nose
- Mouth (lips, inner mouth)
- Face contour
- And more!

Each landmark has three coordinates:
- `x`: Horizontal position (0.0 to 1.0, normalized)
- `y`: Vertical position (0.0 to 1.0, normalized)
- `z`: Depth (relative distance from camera)

### Key Landmarks for Mouth Detection

For tongue detection, we focus on mouth landmarks:
- Landmark #13: Upper lip center
- Landmark #14: Lower lip center
- Landmark #0: Nose tip (used as reference)
- Landmark #17: Chin bottom

You can view all 468 landmarks here: [MediaPipe Face Mesh Landmarks](https://github.com/google/mediapipe/blob/master/mediapipe/modules/face_geometry/data/canonical_face_model_uv_visualization.png)

## The Tongue Detection Algorithm

### Current Implementation

```python
def is_tongue_out(face_landmarks):
    upper_lip = face_landmarks.landmark[13]
    lower_lip = face_landmarks.landmark[14]
    
    mouth_opening = abs(upper_lip.y - lower_lip.y)
    
    TONGUE_OUT_THRESHOLD = 0.03
    
    return mouth_opening > TONGUE_OUT_THRESHOLD
```

### How It Works

1. **Get lip positions**: Extracts the Y-coordinates of upper and lower lips
2. **Calculate mouth opening**: Measures vertical distance between lips
3. **Compare to threshold**: If opening exceeds 0.03 (3% of screen height), tongue is considered "out"

### Why This Works

When you stick your tongue out, your mouth naturally opens wider. The algorithm detects this increased mouth opening.

**Normalized coordinates**: Since MediaPipe uses 0.0-1.0 coordinates, the threshold 0.03 means "3% of the frame height"

## Customizing the Detection

### Adjusting Sensitivity

Make it **more sensitive** (detects smaller mouth openings):
```python
TONGUE_OUT_THRESHOLD = 0.02  # Detects with smaller opening
```

Make it **less sensitive** (requires bigger mouth opening):
```python
TONGUE_OUT_THRESHOLD = 0.05  # Requires wider opening
```

### Improving Accuracy

Add more landmark checks for better detection:

```python
def is_tongue_out(face_landmarks):
    # Upper and lower lips
    upper_lip = face_landmarks.landmark[13]
    lower_lip = face_landmarks.landmark[14]
    
    # Inner mouth landmarks (more precise)
    upper_inner = face_landmarks.landmark[12]
    lower_inner = face_landmarks.landmark[15]
    
    # Calculate both distances
    outer_opening = abs(upper_lip.y - lower_lip.y)
    inner_opening = abs(upper_inner.y - lower_inner.y)
    
    # Require both to exceed threshold
    return outer_opening > 0.03 and inner_opening > 0.025
```

### Detecting Tongue Position

Want to know if tongue is left, right, or center?

```python
def get_tongue_position(face_landmarks):
    # Get mouth corners
    left_corner = face_landmarks.landmark[61]
    right_corner = face_landmarks.landmark[291]
    mouth_center_x = (left_corner.x + right_corner.x) / 2
    
    # Get tongue position (approximate from lower lip)
    tongue_x = face_landmarks.landmark[14].x
    
    if tongue_x < mouth_center_x - 0.02:
        return "LEFT"
    elif tongue_x > mouth_center_x + 0.02:
        return "RIGHT"
    else:
        return "CENTER"
```

## Adding New Features

### Feature 1: Smile Detection

Add smile detection alongside tongue detection:

```python
def is_smiling(face_landmarks):
    # Mouth corners
    left_corner = face_landmarks.landmark[61]
    right_corner = face_landmarks.landmark[291]
    
    # Upper lip center
    upper_lip = face_landmarks.landmark[13]
    
    # Calculate if corners are higher than center (smile)
    avg_corner_y = (left_corner.y + right_corner.y) / 2
    
    return upper_lip.y > avg_corner_y + 0.01
```

Then in your main loop:
```python
if is_tongue_out(face_landmarks):
    current_meme = appletongue_img.copy()
elif is_smiling(face_landmarks):
    current_meme = smile_img.copy()
else:
    current_meme = apple_img.copy()
```

### Feature 2: Eye Wink Detection

```python
def is_winking(face_landmarks):
    # Left eye landmarks
    left_eye_top = face_landmarks.landmark[159]
    left_eye_bottom = face_landmarks.landmark[145]
    
    # Right eye landmarks
    right_eye_top = face_landmarks.landmark[386]
    right_eye_bottom = face_landmarks.landmark[374]
    
    left_eye_opening = abs(left_eye_top.y - left_eye_bottom.y)
    right_eye_opening = abs(right_eye_top.y - right_eye_bottom.y)
    
    # One eye closed, other open
    if left_eye_opening < 0.008 and right_eye_opening > 0.015:
        return "LEFT_WINK"
    elif right_eye_opening < 0.008 and left_eye_opening > 0.015:
        return "RIGHT_WINK"
    return None
```

### Feature 3: Add Sound Effects

Install pygame: `pip install pygame`

```python
import pygame

# Initialize sound
pygame.mixer.init()
tongue_sound = pygame.mixer.Sound("tongue_sound.wav")

# In your main loop
if is_tongue_out(face_landmarks):
    if not tongue_was_out:  # Only play once per tongue-out
        tongue_sound.play()
        tongue_was_out = True
    current_meme = appletongue_img.copy()
else:
    tongue_was_out = False
    current_meme = apple_img.copy()
```

### Feature 4: Record Funny Moments

```python
# Initialize video writer
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
recording = False
video_writer = None

# In your main loop
if is_tongue_out(face_landmarks) and not recording:
    # Start recording
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    video_writer = cv2.VideoWriter(
        f'tongue_moment_{timestamp}.mp4',
        fourcc, 20.0, (WINDOW_WIDTH, WINDOW_HEIGHT)
    )
    recording = True

if recording:
    video_writer.write(frame)
    # Stop after 3 seconds
    if frame_count > 60:  # 20 fps * 3 seconds
        video_writer.release()
        recording = False
        frame_count = 0
```

## Performance Tips

### 1. Reduce Processing Load
```python
# Process every N frames instead of every frame
frame_count = 0
process_every = 2  # Process every 2nd frame

if frame_count % process_every == 0:
    results = face_mesh.process(rgb_frame)
```

### 2. Lower Camera Resolution
```python
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
```

### 3. Adjust MediaPipe Model Complexity
```python
face_mesh = mp_face_mesh.FaceMesh(
    model_complexity=0,  # 0=fastest, 1=balanced, 2=most accurate
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)
```

## Debugging Tips

### Visualize Landmarks
Want to see where landmarks are? Add this to your main loop:

```python
if results.multi_face_landmarks:
    for face_landmarks in results.multi_face_landmarks:
        # Draw all landmarks
        for idx, landmark in enumerate(face_landmarks.landmark):
            x = int(landmark.x * WINDOW_WIDTH)
            y = int(landmark.y * WINDOW_HEIGHT)
            cv2.circle(frame, (x, y), 1, (0, 255, 0), -1)
            
            # Label specific landmarks
            if idx in [13, 14, 0, 17]:
                cv2.putText(frame, str(idx), (x, y), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.3, (255, 0, 0), 1)
```

### Print Landmark Distances
```python
mouth_opening = abs(upper_lip.y - lower_lip.y)
print(f"Mouth opening: {mouth_opening:.4f}")
```

This helps you find the right threshold value for your setup.

## What's Next?

Try building these advanced features:
1. Multiple gesture combinations: Detect "tongue out + winking"
2. Gesture sequences: Detect a series of gestures in order
3. Face filters: Add snapchat-style filters to your face
4. Background replacement: Replace your background with images
5. Multiplayer mode: Detect multiple faces and track each person

## Platform-Specific Notes

**Windows:**
- Use `run.bat` to launch the app quickly
- Python command may be `python` instead of `python3.11`
- Camera permissions: Settings → Privacy → Camera

**macOS:**
- Use `./run.sh` to launch (after `chmod +x run.sh`)
- You'll need to grant Terminal camera permissions
- System Preferences → Security & Privacy → Camera
- If opencv fails to install, you may need: `brew install cmake`
- Python command is usually `python3` or `python3.11`

**Linux:**
- Use `./run.sh` to launch (after `chmod +x run.sh`)
- Ensure user is in video group: `sudo usermod -a -G video $USER`
- Camera device usually at `/dev/video0`
- Python command is usually `python3` or `python3.11`

## Resources

- [MediaPipe Face Mesh Documentation](https://google.github.io/mediapipe/solutions/face_mesh.html)
- [OpenCV Python Tutorials](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html)
- [Face Mesh Landmark Map](https://github.com/google/mediapipe/blob/master/mediapipe/modules/face_geometry/data/canonical_face_model_uv_visualization.png)

## Questions?

If you get stuck:
1. Check the main README troubleshooting section
2. Print out landmark values to debug
3. Try adjusting threshold values
4. Draw landmarks on screen to visualize
5. Check platform-specific notes above

Happy coding!

