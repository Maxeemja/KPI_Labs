import pickle
import cv2 as cv
from utils import face_encodings, nb_of_matches, face_rects


with open('encodings.pickle', 'rb') as f:
    name_encodings_dict = pickle.load(f)

image = cv.imread('./examples/14.jpg')

encodings = face_encodings(image)

names = []

for encoding in encodings:
    counts = {}

    for (name, encodings) in name_encodings_dict.items():
        counts[name] = nb_of_matches(encodings, encoding)

    if all(count == 0 for count in counts.values()):
        name = 'Unknown'

    else:
        name = max(counts, key=counts.get)

    names.append(name)


for rect, name in zip(face_rects(image), names):
    x1, y1, x2, y2 = rect.left(), rect.top(), rect.right(), rect.bottom()

    cv.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

    cv.putText(image, name, (x1, y1 - 10),
               cv.FONT_HERSHEY_COMPLEX, 0.75, (0, 255, 0), 2)


cv.imshow('img', image)
cv.waitKey(0)
