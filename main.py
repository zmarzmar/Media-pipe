"""
Tongue Detection Meme Display
A MediaPipe + OpenCV application that auto-switches images when your tongue is out
or your index finger is near your face — no keyboard toggle needed.
"""

import cv2
import mediapipe as mp
import numpy as np
import os
from collections import deque

# ============================================================================
# CONFIGURATION SETTINGS
# ============================================================================

WINDOW_WIDTH = 960
WINDOW_HEIGHT = 720

# Tongue detection sensitivity (lip gap in normalized coords)
TONGUE_OUT_THRESHOLD = 0.03

# Finger-near-face sensitivity (normalized margin around face bbox)
# Increase to trigger easier (wider halo), decrease for stricter.
FINGER_FACE_MARGIN = 0.06

# Optional: simple smoothing so the image doesn't flicker rapidly
# A state is applied only if it was seen at least this many consecutive frames.
STABILITY_FRAMES = 3  # 0 = no smoothing

# ============================================================================
# MEDIAPIPE INITIALIZATION
# ============================================================================

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5,
    max_num_faces=1
)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

# ============================================================================
# DETECTION FUNCTIONS
# ============================================================================

def is_tongue_out(face_landmarks):
    upper_lip = face_landmarks.landmark[13]
    lower_lip = face_landmarks.landmark[14]
    mouth_opening = abs(upper_lip.y - lower_lip.y)
    return mouth_opening > TONGUE_OUT_THRESHOLD

def _compute_face_bbox_norm(face_landmarks):
    xs = [lm.x for lm in face_landmarks.landmark]
    ys = [lm.y for lm in face_landmarks.landmark]
    return min(xs), min(ys), max(xs), max(ys)

def is_index_finger_near_face(face_landmarks, hands_result, margin=FINGER_FACE_MARGIN):
    if not hands_result or not hands_result.multi_hand_landmarks:
        return False

    xmin, ymin, xmax, ymax = _compute_face_bbox_norm(face_landmarks)
    xmin -= margin; ymin -= margin; xmax += margin; ymax += margin
    xmin = max(0.0, xmin); ymin = max(0.0, ymin)
    xmax = min(1.0, xmax); ymax = min(1.0, ymax)

    for hand_lms in hands_result.multi_hand_landmarks:
        tip = hand_lms.landmark[8]  # index fingertip
        if xmin <= tip.x <= xmax and ymin <= tip.y <= ymax:
            return True
    return False

def _draw_face_box_and_index_tip(frame, face_landmarks, hands_result):
    xmin, ymin, xmax, ymax = _compute_face_bbox_norm(face_landmarks)
    x1, y1 = int(xmin * WINDOW_WIDTH), int(ymin * WINDOW_HEIGHT)
    x2, y2 = int(xmax * WINDOW_WIDTH), int(ymax * WINDOW_HEIGHT)
    cv2.rectangle(frame, (x1, y1), (x2, y2), (200, 200, 200), 2)

    if hands_result and hands_result.multi_hand_landmarks:
        for hlm in hands_result.multi_hand_landmarks:
            tip = hlm.landmark[8]
            cx, cy = int(tip.x * WINDOW_WIDTH), int(tip.y * WINDOW_HEIGHT)
            cv2.circle(frame, (cx, cy), 6, (0, 255, 255), -1)

# ============================================================================
# MAIN LOOP
# ============================================================================

def main():
    print("=" * 60)
    print("Tongue Detection Meme Display (Auto Mode)")
    print("=" * 60)

    # ------------------------------------------------------------------------
    # STEP 1: Load Images
    # ------------------------------------------------------------------------
    required_files = ["base.png", "tongue.png", "finger.png"]
    for f in required_files:
        if not os.path.exists(f):
            print(f"\n[ERROR] {f} not found! Please add it to the project directory.")
            return

    base_img   = cv2.imread("base.png")
    tongue_img = cv2.imread("tongue.png")
    finger_img = cv2.imread("finger.png")

    if base_img is None or tongue_img is None or finger_img is None:
        print("\n[ERROR] Could not load meme images. Check file validity.")
        return

    base_img   = cv2.resize(base_img,   (WINDOW_WIDTH, WINDOW_HEIGHT))
    tongue_img = cv2.resize(tongue_img, (WINDOW_WIDTH, WINDOW_HEIGHT))
    finger_img = cv2.resize(finger_img, (WINDOW_WIDTH, WINDOW_HEIGHT))

    print("[OK] Meme images loaded successfully!")

    # ------------------------------------------------------------------------
    # STEP 2: Webcam Setup
    # ------------------------------------------------------------------------
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("\n[ERROR] Could not open webcam.")
        return

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, WINDOW_WIDTH)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, WINDOW_HEIGHT)

    cv2.namedWindow('Camera Input', cv2.WINDOW_NORMAL)
    cv2.namedWindow('Meme Output',  cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Camera Input', WINDOW_WIDTH, WINDOW_HEIGHT)
    cv2.resizeWindow('Meme Output',  WINDOW_WIDTH, WINDOW_HEIGHT)

    print("\n[OK] Webcam initialized successfully!")
    print("[INFO] Auto mode: priority = TONGUE > FINGER > BASE | Press 'q' to quit")

    current_meme = base_img.copy()

    # Simple stability buffer for states to reduce flicker
    # states: "tongue", "finger", "base"
    recent_states = deque(maxlen=max(1, STABILITY_FRAMES))
    applied_state = "base"

    # ------------------------------------------------------------------------
    # STEP 3: Detection Loop
    # ------------------------------------------------------------------------
    while True:
        ret, frame = cap.read()
        if not ret:
            print("[ERROR] Failed to read frame.")
            break

        frame = cv2.flip(frame, 1)
        frame = cv2.resize(frame, (WINDOW_WIDTH, WINDOW_HEIGHT))
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = face_mesh.process(rgb_frame)
        hands_results = hands.process(rgb_frame)  # always process (no manual toggle)

        detected_state = "base"

        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                # Priority: tongue > finger > base
                tongue_out = is_tongue_out(face_landmarks)
                if tongue_out:
                    detected_state = "tongue"
                    cv2.putText(frame, "TONGUE OUT!", (10, 50),
                                cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3)
                else:
                    finger_near = is_index_finger_near_face(face_landmarks, hands_results, FINGER_FACE_MARGIN)
                    if finger_near:
                        detected_state = "finger"
                        cv2.putText(frame, "FINGER NEAR FACE!", (10, 50),
                                    cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 3)
                    else:
                        cv2.putText(frame, "Neutral", (10, 50),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 255), 2)

                # Debug visuals (optional)
                _draw_face_box_and_index_tip(frame, face_landmarks, hands_results)
                break  # we track max_num_faces=1
        else:
            detected_state = "base"
            cv2.putText(frame, "No face detected", (10, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        # ----- Apply simple stability to avoid flicker -----
        recent_states.append(detected_state)
        if STABILITY_FRAMES <= 1 or len(recent_states) < STABILITY_FRAMES:
            stable = detected_state
        else:
            # if all recent states agree, apply; else keep previous
            stable = detected_state if len(set(recent_states)) == 1 else applied_state

        if stable != applied_state:
            applied_state = stable
            if applied_state == "tongue":
                current_meme = tongue_img.copy()
            elif applied_state == "finger":
                current_meme = finger_img.copy()
            else:
                current_meme = base_img.copy()

        # ---------------------------------------------------
        cv2.imshow('Camera Input', frame)
        cv2.imshow('Meme Output', current_meme)

        if (cv2.waitKey(1) & 0xFF) == ord('q'):
            print("[QUIT] Exiting...")
            break

    cap.release()
    cv2.destroyAllWindows()
    face_mesh.close()
    hands.close()
    print("[OK] Application closed successfully.")

if __name__ == "__main__":
    main()