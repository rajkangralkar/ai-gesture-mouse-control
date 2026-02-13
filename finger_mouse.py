import cv2
import mediapipe as mp
import pyautogui
import math
import time

# Init
cap = cv2.VideoCapture(0)
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.8)
mp_draw = mp.solutions.drawing_utils
screen_w, screen_h = pyautogui.size()

clicking = False
prev_click_time = 0

def get_distance(p1, p2, w, h):
    x1, y1 = int(p1.x * w), int(p1.y * h)
    x2, y2 = int(p2.x * w), int(p2.y * h)
    return math.hypot(x2 - x1, y2 - y1)

while True:
    success, frame = cap.read()
    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if result.multi_hand_landmarks:
        landmarks = result.multi_hand_landmarks[0].landmark

        index_finger = landmarks[8]
        thumb_finger = landmarks[4]
        middle_finger = landmarks[12]

        # Move mouse
        cx, cy = int(index_finger.x * screen_w), int(index_finger.y * screen_h)
        pyautogui.moveTo(cx, cy, duration=0.05)

        # Detect pinch
        pinch_dist = get_distance(index_finger, thumb_finger, w, h)
        scroll_dist = get_distance(index_finger, middle_finger, w, h)

        if pinch_dist < 40:
            if not clicking:
                pyautogui.mouseDown()
                clicking = True
        else:
            if clicking:
                pyautogui.mouseUp()
                clicking = False

        # Scroll
        if scroll_dist < 40:
            pyautogui.scroll(-20)

        mp_draw.draw_landmarks(frame, result.multi_hand_landmarks[0], mp_hands.HAND_CONNECTIONS)

    cv2.imshow("Finger Mouse", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
