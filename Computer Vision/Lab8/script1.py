import cv2 as cv
from matplotlib import pyplot as plt

img1 = cv.imread('view3.png', cv.IMREAD_GRAYSCALE)
img2 = cv.imread('view4.png', cv.IMREAD_GRAYSCALE)
img3 = cv.imread('view5.png', cv.IMREAD_GRAYSCALE)
img4 = cv.imread('view6.png', cv.IMREAD_GRAYSCALE)

stereoLR = cv.StereoBM_create(numDisparities=16, blockSize=15)
stereoUD = cv.StereoBM_create(numDisparities=16, blockSize=15)

disparityLR_1 = stereoLR.compute(img1, img2)
disparityLR_2 = stereoLR.compute(img3, img4)

disparityUD_1 = stereoUD.compute(img1, img3)
disparityUD_2 = stereoUD.compute(img2, img4)

plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.imshow(img1, cmap='gray')
plt.title('Image 1')

plt.subplot(2, 2, 2)
plt.imshow(img2, cmap='gray')
plt.title('Image 2')

plt.subplot(2, 2, 3)
plt.imshow(disparityLR_1, cmap='plasma')
plt.title('Disparity 1|2')

plt.subplot(2, 2, 4)
plt.imshow(disparityLR_2, cmap='plasma')
plt.title('Disparity 3|4')

plt.show()

plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.imshow(img1, cmap='gray')
plt.title('Image 1')

plt.subplot(2, 2, 2)
plt.imshow(img3, cmap='gray')
plt.title('Image 3')

plt.subplot(2, 2, 3)
plt.imshow(disparityUD_1, cmap='plasma')
plt.title('Disparity 1|3')

plt.subplot(2, 2, 4)
plt.imshow(disparityUD_2, cmap='plasma')
plt.title('Disparity 2|4')

plt.show()
