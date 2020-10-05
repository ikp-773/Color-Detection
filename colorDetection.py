import numpy as np
import cv2

cap = cv2.VideoCapture("test.mp4")

while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    low_red = np.array([161, 155, 84])
    high_red = np.array([179, 255, 255])
    red_mask = cv2.inRange(hsv_frame, low_red, high_red)
    red = cv2.bitwise_and(frame, frame, mask=red_mask)

    low_blue = np.array([94, 180, 2])
    high_blue = np.array([126, 255, 255])
    blue_mask=cv2.inRange(hsv_frame, low_blue, high_blue)
    blue=cv2.bitwise_and(frame, frame, mask=blue_mask)

    low_green = np.array([25, 52, 72])
    high_green = np.array([102, 255, 255])
    green_mask=cv2.inRange(hsv_frame, low_green, high_green)
    green=cv2.bitwise_and(frame, frame, mask=green_mask)

    cv2.imshow("Frame", frame)
    cv2.imshow("Red", red)
    cv2.imshow("Blue", blue)
    cv2.imshow("Green", green)

    key = cv2.waitKey(5)
    if key == 27:
        break