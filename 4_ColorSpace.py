# http://blog.csdn.net/gangzhucoll/article/details/78574856
import cv2 as cv
import numpy as np


def ColorSpace(image):
    """
    色彩空间转化
    RGB转换为其他色彩空间
    """
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    cv.imshow("gray", gray)
    hsv = cv.cvtColor(image, cv.COLOR_RGB2HSV)
    cv.imshow("hsv", hsv)
    yuv = cv.cvtColor(image, cv.COLOR_RGB2YUV)
    cv.imshow("yuv", yuv)
    ycrcb = cv.cvtColor(image, cv.COLOR_RGB2YCrCb)
    cv.imshow("ycrcb", ycrcb)


# 以下代码是标注出图像中的黑色部分，黑色部分将以白色显示，其他颜色部分将以黑色显示
# 如果想标注其他的颜色部分，需要将HSV的最大最小范围进行调整
# 颜色标注OpenCV 提供了一个方法，inRange()
capture = cv.VideoCapture(0)
while (True):
    ret, frame = capture.read()
    frame = cv.flip(frame, 1)
    if ret == False:
        break;
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    lower_hsv = np.array([156, 43, 46])
    upperb_hsv = np.array([180, 255, 255])
    # 方法提供三个参数，
    # 第一个参数是图像色彩空间即hsv值，
    # 第二个参数是hsv的最小查找范围，
    # 第三个参数是hsv的最大查找范围。
    # 代码运行后，将会标注出图像的黑色部分。
    mask = cv.inRange(hsv, lowerb=lower_hsv, upperb=upperb_hsv)
    cv.imshow("video_mask", mask)
    cv.imshow("video", frame)
    c = cv.waitKey(40)
    if c == 27:
        break;
