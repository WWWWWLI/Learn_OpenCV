# http://blog.csdn.net/gangzhucoll/article/details/78917011
# 什么是膨胀和腐蚀
#
#     膨胀就是求局部最大值的操作
#
#     腐蚀就是求局部最小值的操作
#
#     膨胀与腐蚀都支持任意形状的结构元素
import cv2 as cv


def erode(img):
    gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    # 获得结构元素
    # 第一个参数：结构元素形状，这里是矩形
    # 第二个参数：结构元素大小
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
    # 执行腐蚀
    dst = cv.erode(binary, kernel)
    cv.imshow("erode", dst)


def dilate(img):
    gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    # 获得结构元素
    # 第一个参数：结构元素形状，这里是矩形
    # 第二个参数：结构元素大小
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
    # 执行膨胀
    dst = cv.dilate(binary, kernel)
    cv.imshow("dilate", dst)


src = cv.imread('ErodeDilate.jpg')
cv.imshow('def', src)
erode(src)
dilate(src)
cv.waitKey(0)
cv.destroyAllWindows()
