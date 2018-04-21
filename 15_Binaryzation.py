import cv2 as cv
import numpy as np


def threshold(image):
    """图像二值化：全局阈值"""
    # 图像灰度化
    gray = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
    # 变为二值图像
    # gary：灰度图像
    # 0：阈值，如果选定了阈值方法，则这里不起作用
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_TRIANGLE)
    print(ret)
    cv.imshow("binary", binary)


def local_threshold(image):
    """局部阈值"""
    # 图像灰度化
    gray = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
    # 变为二值图像
    binary = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 25, 10)
    cv.imshow("local_threshold", binary)


def custom_threshold(image):
    """局部阈值"""
    # 图像灰度化
    gray = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
    h, w = gray.shape[:2]
    m = np.reshape(gray, [1, w * h])
    mean = m.sum() / (w * h)
    # 变为二值图像
    binary = cv.threshold(gray, mean, 255, cv.THRESH_BINARY)
    cv.imshow("custom_threshold", binary)


def big_img_binary(img):
    # 定义分割块的大小
    cw = 256
    ch = 256
    h, w = img.shape[:2]
    # 将图片转化为灰度图片
    gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
    for row in range(0, h, ch):
        for col in range(0, w, cw):
            roi = gray[row:row + ch, col:col + cw]
            dst = cv.adaptiveThreshold(roi, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 127, 20)
            gray[row:row + ch, col:col + cw] = dst
    cv.imwrite('Binaryzation.png', gray)


src = cv.imread('DEMO.jpg')
# threshold(src)
# local_threshold(src)
# custom_threshold(src)
# big_img_binary(src)
cv.waitKey(0)
cv.destroyAllWindows()
