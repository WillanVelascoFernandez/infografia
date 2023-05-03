import cv2
import mediapipe as mp
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

while cap.isOpened():
    succes, img = cap.read()
    if not succes:
        print("empty frame")
        continue

    cv2.imshow("mediapipe face detection", img)

    if cv2.waitKey(5) & 0XFF == 27:
        break

cap.release()
