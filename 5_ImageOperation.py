# http://blog.csdn.net/gangzhucoll/article/details/78598238
import cv2 as cv
import numpy as np

# 算数运算
def add(image1, image2):
    """图片相加"""
    dst = cv.add(image1, image2)
    cv.imshow("add image", dst)


def subtract(image1, image2):
    """图片相减"""
    dst = cv.subtract(image1, image2)
    cv.imshow("subtract image", dst)


def divide(image1, image2):
    """图片相除"""
    dst = cv.divide(image1, image2)
    cv.imshow("divide image", dst)


def multiply(image1, image2):
    """图片相乘"""
    dst = cv.multiply(image1, image2)
    cv.imshow("multiply image", dst)


# 逻辑运算
def logic(image1, image2):
    """逻辑运算"""
    # 与操作
    dst = cv.bitwise_and(image1, image2)
    cv.imshow("logic", dst)
    # 或操作(与相加操作类似)
    dst = cv.bitwise_or(image1, image2)
    cv.imshow("logic", dst)
    # 非操作(像素取反)
    dst = cv.bitwise_not(image1)
    cv.imshow("logic", dst)


# 其他运算
def others(image1, image2):
    # 计算每个通道的平均值
    m1 = cv.mean(image1)
    m2 = cv.mean(image2)
    # 计算每个通道的平均值和方差
    m1, dev1 = cv.meanStdDev(image1)
    m2, dev2 = cv.meanStdDev(image2)
    print(m1, dev1)
    print(m2, dev2)

def contrast_brightness(image,c,b):
    """
    修改亮度和对比度
    c：对比度
    b：亮度
    """
   #获取图片的高、宽和通道数
    h,w,ch=image.shape
    #创建一个全黑色的图片
    blank=np.zeros([h,w,ch],image.dtype)
    #调整亮度和对比度
    dst=cv.addWeighted(image,c,blank,1-c,b)
    cv.imshow("con-bri",dst)

src = cv.imread('DEMO.jpg')
cv.imshow('DEMO.jpg',src)#显示原图
contrast_brightness(src,1,1)
# 等待用户操作
cv.waitKey(0)
# 释放所有窗口
cv.destroyAllWindows()

