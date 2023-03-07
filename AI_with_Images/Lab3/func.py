import cv2 as cv
import numpy as np

def draw_lines(img, lines, color=[255,0,0], thickness=7):
    x_bottom_pos = []
    x_upper_pos = []
    x_bottom_neg = []
    x_upper_neg = []


    y_bottom = 540
    y_upper = 315

    for line in lines:
      for x1,y1,x2,y2 in line:
        if((y2 - y1) / (x2 - x1)) > 0.5 and ((y2 - y1) / (x2 - x1)) < 0.8:
            slope = ((y2 - y1) / (x2 - x1))
            b = y1 - slope * x1

            x_bottom_pos.append((y_bottom - b) / slope)
            x_upper_pos.append((y_upper - b) / slope)

        elif ((y2 - y1) / (x2 - x1)) < -0.5 and ((y2 - y1) / (x2 - x1)) > -0.8:
          slope = ((y2 - y1) / (x2 - x1))
          b = y1 - slope * x1
          x_bottom_neg.append((y_bottom - b) / slope)
          x_upper_neg.append((y_upper - b) / slope)
    
    lines_mean = np.array(
       [[int(np.mean(x_bottom_pos)), int(np.mean(y_bottom)), int(np.mean(x_upper_pos)), int(np.mean(y_upper))],
         [int(np.mean(x_bottom_neg)), int(np.mean(y_bottom)), int(np.mean(x_upper_neg)), int(np.mean(y_upper))]])

    for i in range(len(lines_mean)):
      cv.line(img, (lines_mean[i, 0],lines_mean[i, 1]), (lines_mean[i, 2],lines_mean[i, 3]), color, thickness )