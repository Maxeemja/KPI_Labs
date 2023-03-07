import cv2 as cv

face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
smile_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_smile.xml')
eye_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_eye.xml')


scaling_factor = 0.5
frame = cv.imread('./pics/6290ff28f099c4001956aa3c.webp');

gray_filter = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)



face_rects = face_cascade.detectMultiScale(gray_filter, 1.2, 5)
print(f"Found {len(face_rects)} faces!")


for(x, y, w, h) in face_rects:
  cv.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)
  roi_gray = gray_filter[y:y+h, x:x+w]
  roi_color = frame[y:y+h, x:x+w]
  smile = smile_cascade.detectMultiScale(roi_gray)
  eye = eye_cascade.detectMultiScale(roi_gray)

  for(sx, sy, sw, sh) in smile:
    cv.rectangle(roi_color, (sx,sy), (sx+sw, sy+sh), (0,255,0), 1)

  for(ex, ey, ew, eh) in eye:
    cv.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0,0,255), 1)

cv.imshow('Example', frame)
cv.waitKey()