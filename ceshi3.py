import cv2
import numpy as np
def defect_B(img_path):
    image = cv2.imread(img_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    #image = cv2.circle(image, (644, 503), 293, 0, -1)
    image1 = cv2.resize(image, (512, 512))
    # cv2.imshow('image2', image2)
    #cv2.imshow('image1', image1)
    # cv2.waitKey(0)
    x = 256
    y = 256
    r = 150
    mask = np.zeros(image1.shape[:2], dtype=np.uint8)
    mask = cv2.circle(mask, (x, y), r, (255, 255, 255), -1)
    ret,mask_1=cv2.threshold(mask, 50, 255, cv2.THRESH_BINARY_INV)
    im_gauss = cv2.GaussianBlur(image1, (3, 3), 0)
    image = cv2.add(im_gauss, np.zeros(np.shape(im_gauss), dtype=np.uint8), mask=mask_1)
    ret, im = cv2.threshold(image, 90, 255, 0)
    #im = cv2.adaptiveThreshold(im_gauss,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
    #cv2.imshow("o", im)
    ret,im_1=cv2.threshold(im, 127, 255, cv2.THRESH_BINARY_INV)
    im_2=cv2.add(im_1, np.zeros(np.shape(im_gauss), dtype=np.uint8), mask=mask_1)
    #cv2.imshow("im_2",im_2)

    contours, hierarchy = cv2.findContours(im_2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    image1 = cv2.cvtColor(image1, cv2.COLOR_GRAY2BGR)
    cv2.drawContours(image1, contours, -1, (255, 0, 0), 1)
    text="defect-b"
    add_im=image1.copy()
    cv2.putText(add_im,text,(50,50),cv2.FONT_HERSHEY_COMPLEX, 2.0, (100, 200, 200), 5)

    # cv2.imshow("Keypoints", add_im)
    # cv2.waitKey(0)
    return add_im