import cv2 as cv
from matplotlib import pyplot as plt


def plot(image):
    """简单的图像直方图"""
    plt.hist(image.ravel(), 256, [0, 256])
    plt.show("simplehis")


def image_his(image):
    """
    这里生成的直方图是opencv 对图片
    进行分割、图像检索等所需要的
    """
    color = ('blue', 'green', 'red')
    for i, color in enumerate(color):
        hist = cv.calcHist([image], [i], None, [256], [0, 256])
        plt.plot(hist, color=color)
        plt.xlim([0, 256])
    plt.show()


# 读入图片文件
src = cv.imread('DEMO.jpg')
cv.imshow('def', src)

# 图一
plot(src)
# 图二
image_his(src)

cv.waitKey(0)
cv.destroyAllWindows()
