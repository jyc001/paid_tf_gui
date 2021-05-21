import cv2
import numpy as np


def defect_A(img_path):
    im = cv2.imread(img_path)
    im_o = cv2.resize(im, (800, 600))
    im_gauss = cv2.cvtColor(im_o, cv2.COLOR_RGB2GRAY)
    im_gauss = cv2.GaussianBlur(im_gauss, (7, 7), 0)
    ret, im = cv2.threshold(im_gauss, 100, 255, 0)
    # cv2.imshow("o", im)
    params = cv2.SimpleBlobDetector_Params()

    params.minThreshold = 10
    params.maxThreshold = 200

    params.filterByArea = True

    params.minArea = 35

    params.filterByCircularity = True
    # 设置类圆性
    params.minCircularity = 0.3

    # Filter by Convexity
    params.filterByConvexity = True
    # 设置最小凸性
    params.minConvexity = 0.7  # 0.57

    # Filter by Inertia
    params.filterByInertia = True
    # 测量了一个形状有多长：对于一个圆，这个值是1，对于一个椭圆，它在0到1之间，对于一条直线，它是0
    params.minInertiaRatio = 0.01

    # Create a detector with the parameters
    ver = (cv2.__version__).split('.')
    if int(ver[0]) < 3:
        detector = cv2.SimpleBlobDetector(params)
    else:
        detector = cv2.SimpleBlobDetector_create(params)

    # Detect blobs.
    keypoints = detector.detect(im)

    # Draw detected blobs as red circles.
    # cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures
    # the size of the circle corresponds to the size of blob

    im_with_keypoints = cv2.drawKeypoints(im_o, keypoints, np.array([]), (0, 0, 255),
                                          cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    text = "defect-a"
    add_im = im_with_keypoints.copy()
    cv2.putText(add_im, text, (100, 100), cv2.FONT_HERSHEY_COMPLEX, 2.0, (100, 200, 200), 5)
    # Show blobs
    # cv2.imshow("Keypoints", add_im)
    # cv2.waitKey(0)
    return add_im
