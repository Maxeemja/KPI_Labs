import cv2
import numpy as np
from matplotlib import pyplot as plt
# зчитування та відображення зображення
def image_read(FileIm):
     img = cv2.imread(FileIm)
     img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
     plt.imshow(img)
     plt.show()
     return img
# опрацювання зображення
def image_processing(img):
     # розмиття гауса
     img = cv2.GaussianBlur(img,(5,5),3)
     # перехід до HSV
     hsv_img = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
     # нижній кордон зеленого кольору
     lower_range = (40, 100, 20)
     # верхній кордон зеленого кольору
     upper_range = (120, 255, 255)
     # маска частин зображення що задовольняють потреби
     mask = cv2.inRange(hsv_img, lower_range, upper_range)
     plt.imshow(mask)
     plt.show()

     # для наочності змінюємо колір частин зображення що задовольняють потреби
     img[mask>0] = (0,128,0)
     # підрахунок зелених насаджень у кадрі
     res = img.shape
     green = np.sum(mask == 255)
     print(f"Зелені насадження займають = {(green/(res[0]*res[1])*100):.2f}% кадру")
     # відображення
     plt.imshow(img)
     plt.show()
     return
# головна частина скрипту
if __name__ == '__main__':
 # зчитування високоточного зображення
 image_entrance = image_read("input1.jpg")
 # його опрацювання
 image_processing(image_entrance)
 # зчитування оперативного зображення
 image_entrance = image_read("input2.jpg")
 # його опрацювання
 image_processing(image_entrance)
