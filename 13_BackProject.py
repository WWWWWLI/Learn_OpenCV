# http://blog.csdn.net/gangzhucoll/article/details/78736768
import cv2 as cv
from matplotlib import pyplot as plt


def hist2d(image):
    """2d 直方图计算和显示"""
    # 转换为hsv色彩空间
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    # [180,256] bins 越多对每个像素细分的越厉害，会导致反响直方图的碎片化
    # [0,180,0,256]:hsv色彩空间中 h和s的取值范围，值是固定的
    hist = cv.calcHist([image], [0, 1], None, [180, 256], [0, 180, 0, 256])
    # interpolation:插值方式
    plt.imshow(hist, interpolation='nearest')
    # 直方图名字
    plt.title("2D hist")
    # 图一
    plt.show()


def backProjection():
    """直方图反向投影"""
    # 样本图片
    sample = cv.imread('wlihand.jpg')
    # 目标片图片
    target = cv.imread('cwwhand.jpg')
    sample_hsv = cv.cvtColor(sample, cv.COLOR_BGR2HSV)
    target_hsv = cv.cvtColor(target, cv.COLOR_BGR2HSV)

    # 图二
    cv.imshow("sample", sample)
    # 图三
    cv.imshow("target", target)

    # 获得样本图片直方图
    # [0,1]:用于计算直方图的通道，这里使用hsv计算直方图，所以就直接使用第一h和第二通道，即h和s通道；
    # None:是否使用mask，None 否
    # [32,32] bins 越多对每个像素细分的越厉害，会导致反响直方图的碎片化
    # [0,180,0,256]:hsv色彩空间中 h和s的取值范围，是固定的
    sample_hist = cv.calcHist([sample_hsv], [0, 1], None, [32, 32], [0, 180, 0, 256])

    # 规划样本图片直方图
    # sample_hist:输入的矩阵
    # sample_hist：归一化后的矩阵
    # 0:归一化后的矩阵的最小值
    # 255：归一化后的矩阵的最大值
    # cv.NORM_MINMAX:数组的数值被平移或缩放到一个指定的范围，线性归一化，一般较常用
    cv.normalize(sample_hist, sample_hist, 0, 255, cv.NORM_MINMAX)

    # 生成反向投影
    # target_hsv:目标图像hsv矩阵
    # [0,1]:用于计算直方图反射投影的通道，这里使用hsv计算直方图，所以就直接使用第一h和第二通道，即h和s通道；
    # [0,180,0,256]:hsv色彩空间中 h和s的取值范围，是固定的
    # 1:是否缩放大小，1不需要，0需要
    dst = cv.calcBackProject([target_hsv], [0, 1], sample_hist, [0, 180, 0, 256], 1)
    # 图四
    cv.imshow("BackProject", dst)


src = cv.imread('wlihand.jpg')

hist2d(src);
backProjection()

# 等待用户操作
cv.waitKey(0)
# 释放所有窗口
cv.destroyAllWindows()
