# http://blog.csdn.net/gangzhucoll/article/details/78824590
# Canny边缘提取
# canny 算法五步骤
#         高斯模糊
#         灰度转换
#         计算梯度
#         非最大信号抑制
#         高低阈值输出二值图像
import cv2 as cv


def edge(img):
    # 高斯模糊,降低噪声
    blurred = cv.GaussianBlur(img, (3, 3), 0)
    # 灰度图像
    gray = cv.cvtColor(blurred, cv.COLOR_RGB2GRAY)
    # 图像梯度
    xgrad = cv.Sobel(gray, cv.CV_16SC1, 1, 0)
    ygrad = cv.Sobel(gray, cv.CV_16SC1, 0, 1)
    # 计算边缘
    # 50和150参数必须符合1：3或者1：2
    edge_output = cv.Canny(xgrad, ygrad, 25, 75)
    # 图一
    cv.imshow("edge", edge_output)

    dst = cv.bitwise_and(img, img, mask=edge_output)
    # 图二（彩色）
    cv.imshow('cedge', dst)


src = cv.imread('DEMO.jpg')
# 图三（原图）
cv.imshow('def', src)
edge(src)
cv.waitKey(0)
cv.destroyAllWindows()
