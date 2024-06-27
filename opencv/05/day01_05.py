import sys
import cv2

cap = cv2.VideoCapture()
if not cap.isOpened():
    print("check camera ")
    sys.exit()

w = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h =round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps  = cap.get(cv2.CAP_PROP_FPS)
fource = 