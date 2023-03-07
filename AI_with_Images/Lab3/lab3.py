import cv2 as cv
import numpy as np
from func import draw_lines

img = cv.imread('./road2.jpg')
kernel_size = 5
grayscale = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(
  grayscale,
  (kernel_size,kernel_size),
  0
)
low_t = 50
high_t = 150
edges = cv.Canny(blur, low_t, high_t)

verticles = np.array(
  [
    [
    (0, img.shape[0]), (450,310),
    (490, 310), (img.shape[1], img.shape[0])
    ]
  ],
  dtype=np.int32
)
mask = np.zeros_like(edges)
ignore_mask_color = 255
cv.fillPoly(mask, verticles, ignore_mask_color)
masked_edges = cv.bitwise_and(edges, mask)
rho = 3 
theta = np.pi / 180
threshold = 15
min_line_len = 150
max_line_gap = 60

lines = cv.HoughLinesP(
    masked_edges, rho, theta, threshold,
    np.array([]),
    minLineLength=min_line_len,
    maxLineGap=max_line_gap
)

draw_lines(img, lines)



cv.imshow('Input img', img)

cv.waitKey(0)
cv.destroyAllWindows()