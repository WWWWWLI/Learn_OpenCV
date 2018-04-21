import cv2 as cv
import numpy as np


def line_detection(img):
    """方法一"""
    gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
    edges = cv.Canny(gray, 50, 150, apertureSize=3)
    lines = cv.HoughLines(edges, 1, np.pi / 180, 200)
    # 以下为标准做法
    for line in lines:
        rho, theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * a)
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * a)
        cv.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
    cv.imshow("img lines", img)


def line_detect_possible(img):
    """方法二"""
    gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
    edges = cv.Canny(gray, 50, 150, apertureSize=3)
    # minLineLength：线段最大长度
    # maxLineGap:点和线段之间允许的间隔大小
    lines = cv.HoughLinesP(edges, 1, np.pi / 180, 200, minLineLength=50, maxLineGap=10)
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
    cv.imshow("img lines", img)


src = cv.imread('templatematch.jpg')
cv.imshow('def', src)
line_detect_possible(src)
cv.waitKey(0)
cv.destroyAllWindows()
