import cv2
from cvzone import HandTrackingModule

cap = cv2.VideoCapture(0)
detector = HandTrackingModule.HandDetector()

while (True):
    success,img=cap.read()
    detector.findHands(img)
    cv2.imshow('HandDector',img)
    cv2.waitKey(1)