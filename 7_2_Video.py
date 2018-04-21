import cv2 as cv
import numpy as np


def fill_color_demo(image):
    copyImg = image.copy()
    h, w = image.shape[:2]
    mask = np.zeros([h + 2, w + 2], np.uint8)
    cv.floodFill(copyImg, mask, (250, 250), (0, 255, 255), (100, 100, 100), (50, 50, 50), cv.FLOODFILL_FIXED_RANGE)
    cv.imshow("fill color", copyImg)

capture = cv.VideoCapture(0)
while True:
    ret, frame = capture.read()
    frame = cv.flip(frame, 1)
    fill_color_demo(frame)

    c = cv.waitKey(40)
    if c == 27:
        break
