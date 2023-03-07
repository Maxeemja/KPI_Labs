import cv2 as cv
import numpy as np
from func import draw_lines

def process_image(frame):
    kernel_size = 5
    grayscale = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
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
        (0, frame.shape[0]), (450,310),
        (490, 310), (frame.shape[1], frame.shape[0])
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
    try:    
      draw_lines(frame, lines)
    except:
      pass



video_capture = cv.VideoCapture('./road.mp4')

while video_capture.isOpened():
    ret, frame = video_capture.read()
    if ret:
        process_image(frame)
        cv.imshow('framee', frame)

        if cv.waitKey(1) & 0xFF == ord('q'):
            break
        
    else:
      break

video_capture.release()
cv.destroyAllWindows()

