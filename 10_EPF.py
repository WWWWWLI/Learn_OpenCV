# http://blog.csdn.net/gangzhucoll/article/details/78700989
# EPF 边缘保留滤波
import cv2 as cv


def bi(image):
    """
    色彩窗的半径
    图像将呈现类似于磨皮的效果
    """

    # image：输入图像，可以是Mat类型，
    #       图像必须是8位或浮点型单通道、三通道的图像
    # 0：表示在过滤过程中每个像素邻域的直径范围，一般为0
    # 后面两个数字：空间高斯函数标准差，灰度值相似性标准差
    dst = cv.bilateralFilter(image, 0, 60, 10);
    cv.imshow('bi', dst)


def shift(image):
    """
    均值迁移
    图像会呈现油画效果
    """

    # 10:空间窗的半径
    # 50:色彩窗的半径
    dst = cv.pyrMeanShiftFiltering(image, 10, 50);
    cv.imshow('shift', dst)


src = cv.imread('testcww.jpg')

# 图一（原图）
cv.imshow('def', src)
# 图二（色彩窗的半径）
bi(src)
# 图三（均值迁移）
shift(src)
cv.waitKey(0)

cv.destroyAllWindows()
