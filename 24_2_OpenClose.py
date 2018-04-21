# http://blog.csdn.net/gangzhucoll/article/details/78956799
# 一、顶帽
#     原图像与开操作之间的差值图像
# 二、黑帽
#     闭操作图像与原图像的差值图像
# 三、形态学梯度
#     1、基本梯度：膨胀后的图像减去腐蚀后的图像得到的差值图像
#     2、内部梯度：原图像减去腐蚀之后的图像得到的差值图像
#     3、外部梯度：图像膨胀之后减去原图像得到的差值图像
import cv2 as cv


def hat(img):
    """顶帽/黑帽梯度"""
    gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
    dst = cv.morphologyEx(gray, cv.MORPH_TOPHAT, kernel)
    cv.imshow("topHat", dst)

    dst = cv.morphologyEx(gray, cv.MORPH_BLACKHAT, kernel)
    cv.imshow("blackHat", dst)


def base(img):
    """基本梯度"""
    gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
    dst = cv.morphologyEx(gray, cv.MORPH_GRADIENT, kernel)
    cv.imshow("base", dst)


def i_e(img):
    """内/外梯度"""
    kerenl = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
    dm = cv.dilate(img, kerenl)
    em = cv.erode(img, kerenl)
    # 内梯度
    dst1 = cv.subtract(img, em)
    # 外梯度
    dst2 = cv.subtract(img, dm)
    cv.imshow("intrenal", dst1)
    cv.imshow("external", dst2)


src = cv.imread('ErodeDilate.jpg')
cv.imshow('def', src)
hat(src)
base(src)
i_e(src)
cv.waitKey(0)
cv.destroyAllWindows()
