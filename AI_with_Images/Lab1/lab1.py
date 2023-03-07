import cv2
import imutils
import numpy as np

image = np.zeros((200,500,3), np.uint8)
font = cv2.FONT_ITALIC
cv2.putText(
  image, 'OpenCv', (0, 100), font, 4, (255, 100, 255), 4, cv2.LINE_4
)


cv2.imshow('Text', image)
cv2.waitKey()
cv2.destroyAllWindows();


blurred = cv2.GaussianBlur()