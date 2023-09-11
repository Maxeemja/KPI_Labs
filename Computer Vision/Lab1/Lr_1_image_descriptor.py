'''
Приклади реалізації конвеєру задач виявлення / ідентифікації об'єктів  за особливими точками:
1. Детектор кутів Харріса;
2. Дескриптор SIFT для заданих функцій на основі виявлення кутів Харріса;
3. sift - співставлення ознак: дескрипторів двох зображень

Package            Version
------------------ -----------
numpy              1.24.1
opencv-python      3.4.18.65

'''

import numpy as np
import cv2 as cv

'''
Детектор кутів Харріса
https://docs.opencv.org/3.4/dc/d0d/tutorial_py_features_harris.html

'''

def Harris_Corner_Detector (filename):

    img = cv.imread(filename)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    gray = np.float32(gray)
    dst = cv.cornerHarris(gray, 2, 3, 0.04)

    # result is dilated for marking the corners, not important
    dst = cv.dilate(dst, None)

    # Threshold for an optimal value, it may vary depending on the image.
    img[dst > 0.01 * dst.max()] = [0, 0, 255]
    cv.imshow('Harris_Corner_Detector', img)
    if cv.waitKey(0) & 0xff == 27:
        cv.destroyAllWindows()

    return

'''
Дескриптор SIFT для заданих функцій на основі виявлення кутів Харріса
'''

def SIFT_descriptors_on_Harris (filename):

    def harris(img):
        gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        gray_img = np.float32(gray_img)
        dst = cv.cornerHarris(gray_img, 2, 3, 0.04)
        result_img = img.copy()  # deep copy image
        # Threshold for an optimal value, it may vary depending on the image.
        # draws the Harris corner key-points on the image (RGB [0, 0, 255] -> blue)
        result_img[dst > 0.01 * dst.max()] = [0, 0, 255]
        # for each dst larger than threshold, make a keypoint out of it
        keypoints = np.argwhere(dst > 0.01 * dst.max())
        keypoints = [cv.KeyPoint(float(x[1]), float(x[0]), 13) for x in keypoints]

        return (keypoints, result_img)

    img = cv.imread(filename)
    # Calculate the Harris Corner features and transform them to keypoints
    kp, img = harris(img)
    # compute the SIFT descriptors from the Harris Corner keypoints
    sift = cv.SIFT_create()
    sift.compute(img, kp)
    img = cv.drawKeypoints(img, kp, img)
    cv.imshow('SIFT', img)
    if cv.waitKey(0) & 0xff == 27:
        cv.destroyAllWindows()

    return

'''
sift - співставлення ознак: дескрипторів двох зображень
https://docs.opencv.org/4.x/dc/dc3/tutorial_py_matcher.html

'''

def sift_feature_matching (filename_1, filename_2):

    img1 = cv.imread(filename_1, cv.IMREAD_GRAYSCALE)  # queryImage
    img2 = cv.imread(filename_2, cv.IMREAD_GRAYSCALE)  # trainImage

    # Initiate SIFT detector
    sift = cv.SIFT_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = sift.detectAndCompute(img1, None)
    kp2, des2 = sift.detectAndCompute(img2, None)

    # FLANN parameters
    FLANN_INDEX_KDTREE = 1
    index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
    search_params = dict(checks=50)  # or pass empty dictionary
    flann = cv.FlannBasedMatcher(index_params, search_params)
    matches = flann.knnMatch(des1, des2, k=2)

    # Need to draw only good matches, so create a mask
    matchesMask = [[0, 0] for i in range(len(matches))]

    # ratio test as per Lowe's paper
    for i, (m, n) in enumerate(matches):
        if m.distance < 0.7 * n.distance:
            matchesMask[i] = [1, 0]

    draw_params = dict(matchColor=(0, 255, 0),
                       singlePointColor=(255, 0, 0),
                       matchesMask=matchesMask,
                       flags=cv.DrawMatchesFlags_DEFAULT)

    img3 = cv.drawMatchesKnn(img1, kp1, img2, kp2, matches, None, **draw_params)

    cv.imshow('sift_feature_matching', img3)
    if cv.waitKey(0) & 0xff == 27:
        cv.destroyAllWindows()

    return

# -------------------------- Головні виклики -----------------------------------

if __name__ == '__main__':

    # 1: ------- Детектор кутів Харріса ---------------
    Harris_Corner_Detector('3D.jpg')
    Harris_Corner_Detector('Malevic.jpg')
    Harris_Corner_Detector('KPI_1.jpg')
    Harris_Corner_Detector('KPI_2.jpg')

    # 2:-- дескриптори SIFT для кутів Харріса ---------
    SIFT_descriptors_on_Harris('KPI_1.jpg')
    SIFT_descriptors_on_Harris('KPI_2.jpg')
    
    # 3: ---- sift - співставлення ознак --------------
    sift_feature_matching('KPI_1.jpg', 'KPI_2.jpg')

