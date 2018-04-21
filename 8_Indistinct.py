# http://blog.csdn.net/gangzhucoll/article/details/78660422
import cv2 as cv
import numpy as np


def blur(image):
    """
    均值模糊
    """
    # 参数（5，5）：表示高斯矩阵的长与宽都是5
    dst = cv.blur(image, (5, 5))
    # 图二为均值模糊图
    cv.imshow("blur", dst)


def median(image):
    """
    中值模糊
    """
    # 第二个参数是孔径的尺寸，一个大于1的奇数。
    # 比如这里是5，中值滤波器就会使用5×5的范围来计算。
    # 即对像素的中心值及其5×5邻域组成了一个数值集，对其进行处理计算，当前像素被其中值替换掉。
    # 参考自：http://blog.csdn.net/sunny2038/article/details/9155893
    dst = cv.medianBlur(image, 5)
    # 图三为中值模糊
    cv.imshow("median", dst)


def custom(image):
    """
    自定义模糊
    """
    # 定义一个5*5的卷积核
    kernel = np.ones([5, 5], np.float32) / 25
    dst = cv.filter2D(image, -1, kernel=kernel)
    # 图四为效果图
    cv.imshow("custom", dst)


# 读入图片文件
src = cv.imread('DEMO.jpg')
# 图一为原图
cv.imshow('image 1', src)

blur(src)
median(src)
custom(src)
# 等待用户操作
cv.waitKey(0)
# 释放所有窗口
cv.destroyAllWindows()
