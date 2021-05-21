import cv2
import numpy as np
import tensorflow as tf


def defect_B(img_path):
    image = cv2.imread(img_path)
    image2 = cv2.resize(image, (800, 600))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    image = cv2.circle(image, (644, 503), 293, 0, -1)
    image1 = cv2.resize(image, (800, 600))
    # cv2.imshow('image2', image2)
    # cv2.imshow('image1', image1)
    # cv2.waitKey(0)

    im_gauss = cv2.GaussianBlur(image1, (3, 3), 0)
    ret, im = cv2.threshold(im_gauss, 40, 255, 0)
    # cv2.imshow("o", im)
    # canny = cv2.Canny(im, 125, 250)
    canny = cv2.Canny(im, 50, 1000)
    # cv2.imshow('Canny', canny)
    # cv2.waitKey(0)

    circles = cv2.HoughCircles(canny, cv2.HOUGH_GRADIENT, 1, 20, param1=100, param2=7, minRadius=6, maxRadius=1)
    circles = np.uint16(np.around(circles))  # 四舍五入，取整

    for i in circles[0, :]:
        cv2.circle(image2, (i[0], i[1]), i[2], (0, 0, 255), 2)  # 画圆
        # cv2.circle(image, (i[0], i[1]), 2, (255, 0, 255), 10)  # 画圆心
    text = "defect-b"
    add_im = image2.copy()
    cv2.putText(add_im, text, (100, 100), cv2.FONT_HERSHEY_COMPLEX, 2.0, (100, 200, 200), 5)
    # cv2.imshow("HoughCircle", add_im)
    # cv2.waitKey(0)
    return add_im
