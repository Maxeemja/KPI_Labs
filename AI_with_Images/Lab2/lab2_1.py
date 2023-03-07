import cv2 as cv
import numpy as np

hog = cv.HOGDescriptor()
hog.setSVMDetector(cv.HOGDescriptor_getDefaultPeopleDetector())
cv.startWindowThread()

capt = cv.VideoCapture('./vids/vid.mp4')

while True:
  ret, frame = capt.read()

  frame = cv.resize(frame, (800, 560))
  gray_filter = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
  boxes, weights = hog.detectMultiScale(frame, winStride=(8,8))
  boxes = np.array([[x, y, x + w, y + h] for (x, y, w, h) in boxes])

  for (xa, ya, xb, yb) in boxes:
    cv.rectangle(frame, (xa, ya), (xb, yb), (0, 255, 255), 1)

  cv.imshow('Video', frame)

  if(cv.waitKey(1) & 0XFF==ord('g')):
    break

capt.release()
cv.destroyAllWindows()
