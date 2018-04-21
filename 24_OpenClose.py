# http://blog.csdn.net/gangzhucoll/article/details/78927295
# 闭操作：
#  1、图像形态学的重要操作之一，基于膨胀与腐蚀操作组合形成的
#  2、主要是应用在二值图像分析中，灰度图像也可以
#  3、闭操作=膨胀+腐蚀，输入图像+结构元素
# 开操作：
#  1、图像形态学的重要操作之一，基于膨胀与腐蚀操作组合形成的
#  2、主要是应用在二值图像分析中，灰度图像也可以
#  3、开操作=腐蚀+膨胀，输入图像+结构元素
# 开操作与闭操作的区别是：膨胀与腐蚀的顺序
# 开操作作用：消除图像中小的干扰区域
# 闭操作作用：填充小的封闭区域
import cv2 as cv


def open(img):
    gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
    # 形态学操作
    # 第二个参数：要执行的形态学操作类型，这里是开操作
    binary = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel)
    cv.imshow("open", binary)


def close(img):
    gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
    # 形态学操作
    # 第二个参数：要执行的形态学操作类型，这里是开操作
    binary = cv.morphologyEx(binary, cv.MORPH_CLOSE, kernel)
    cv.imshow("close", binary)


src = cv.imread('ErodeDilate.jpg')
cv.imshow('def', src)
open(src)
close(src)
cv.waitKey(0)
cv.destroyAllWindows()
