import cv2
import mediapipe as mp
import time
from controller import Controller

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

prev_time = 0

while True:
    success, img = cap.read()
    if not success:
        print("Camera error — frame not read")
        break

    img = cv2.flip(img, 1)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    # FPS counter
    curr_time = time.time()
    fps = int(1 / (curr_time - prev_time + 1e-9))
    prev_time = curr_time
    cv2.putText(img, f'FPS: {fps}', (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    if results.multi_hand_landmarks:
        Controller.hand_Landmarks = results.multi_hand_landmarks[0]
        mpDraw.draw_landmarks(img, Controller.hand_Landmarks, mpHands.HAND_CONNECTIONS)

        Controller.update_fingers_status()
        Controller.cursor_moving()
        Controller.detect_scrolling()
        Controller.detect_zoomming()
        Controller.detect_clicking()
        Controller.detect_dragging()
        Controller.detect_screenshot()
        Controller.detect_volume()
        Controller.detect_brightness()

        # Gesture label
        label = Controller.get_gesture_label()
        cv2.putText(img, label, (10, 70),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 0), 2)

    cv2.imshow('Hand Tracker', img)
    if cv2.waitKey(5) & 0xff == 27:  # ESC to quit
        break

# Cleanup
hands.close()
cap.release()
cv2.destroyAllWindows()

# Supported gestures:
# Move cursor      — move hand naturally
# Freeze cursor    — all fingers up, thumb down
# Left click       — index into thumb
# Right click      — middle into thumb
# Double click     — ring into thumb
# Drag             — all fingers down
# Scroll up        — little finger up only
# Scroll down      — index finger up only
# Zoom in/out      — index + middle up (spread/pinch)
# Screenshot       — little finger up, thumb down
# Volume control   — index + thumb up, move hand up/down
# Brightness       — index + middle up, thumb down, move up/down
# DragDrop
