# http://blog.csdn.net/gangzhucoll/article/details/78682492
import cv2 as cv
import numpy as np


def clamp(pv):
    """防止颜色值超出颜色取值范围（0-255）"""
    if pv > 255:
        return 255
    if pv < 0:
        return 0
    else:
        return pv


def gaussian_noise(image):
    """高斯噪声"""
    h, w, c = image.shape

    for row in range(h):
        for col in range(w):
            # 获取三个高斯随机数
            # 第一个参数：概率分布的均值，对应着整个分布的中心
            # 第二个参数：概率分布的标准差，对应于分布的宽度
            # 第三个参数：生成高斯随机数数量
            s = np.random.normal(0, 20, 3)
            # 获取每个像素点的bgr值
            b = image[row, col, 0]
            g = image[row, col, 1]
            r = image[row, col, 2]
            # 给每个像素值设置新的bgr值
            image[row, col, 0] = clamp(b + s[0])
            image[row, col, 0] = clamp(g + s[1])
            image[row, col, 0] = clamp(r + s[2])

    cv.imshow("noise", image)


# 读入图片文件
src = cv.imread('DEMO.jpg')

gaussian_noise(src)
# 给图片创建毛玻璃特效
# 第二个参数：高斯核的宽和高（建议是奇数）
# 第三个参数：x和y轴的标准差
dst = cv.GaussianBlur(src, (5, 5), 15)
cv.imshow("gaussian", dst)

# 等待用户操作
cv.waitKey(0)
# 释放所有窗口
cv.destroyAllWindows()
