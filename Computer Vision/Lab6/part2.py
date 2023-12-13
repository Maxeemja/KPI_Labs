import numpy as np
import imutils
import time
import cv2

p_model = "dataset2/MobileNetSSD_deploy.caffemodel"
p_prototxt = "dataset2/MobileNetSSD_deploy.prototxt.txt"
p_video = "dataset2/road.mp4"

p_confidence = 0.71

CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
 "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
 "dog", "horse", "motorbike", "person", "train", "tvmonitor"]

COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))

print("[INFO] loading model...")
net = cv2.dnn.readNetFromCaffe(p_prototxt, p_model)

cap = cv2.VideoCapture(p_video)

while True:

     _, frame = cap.read()
     frame = imutils.resize(frame, width=900)

     (h, w) = frame.shape[:2]
     blob = cv2.dnn.blobFromImage(cv2.resize(frame, (400, 400)),
     0.007843, (400, 400), 127.5)

     net.setInput(blob)
     detections = net.forward()
     time.sleep(0.1)

     for i in np.arange(0, detections.shape[2]):

         confidence = detections[0, 0, i, 2]

         if confidence > p_confidence:

             idx = int(detections[0, 0, i, 1])
             box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
             (startX, startY, endX, endY) = box.astype("int")
             # Контур виявленого обєкту
             label = "{}: {:.2f}%".format(CLASSES[idx],
             confidence * 100)
             cv2.rectangle(frame, (startX, startY), (endX, endY),
             COLORS[idx], 2)
             y = startY - 15 if startY - 15 > 15 else startY + 15
             cv2.putText(frame, label, (startX, y),
             cv2.FONT_HERSHEY_SIMPLEX, 0.4, COLORS[idx], 2)
     # Відображення вихідного кадру з розпізнаним обєктом
     cv2.imshow("Window", frame)
     key = cv2.waitKey(1) & 0xFF

     if key == ord("q"):
        break
# Закриття графічного вікна
cv2.destroyAllWindows()
cap.release()
