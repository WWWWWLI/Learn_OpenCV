import cv2 as cv


def backProjection():
    """直方图反向投影"""
    capture = cv.VideoCapture(0)
    # 样本图片
    sample = cv.imread('cwwhand.jpg')
    cv.imshow("sample", sample)
    sample_hsv = cv.cvtColor(sample, cv.COLOR_BGR2HSV)
    sample_hist = cv.calcHist([sample_hsv], [0, 1], None, [32, 32], [0, 180, 0, 256])
    cv.normalize(sample_hist, sample_hist, 0, 255, cv.NORM_MINMAX)
    while True:
        # 目标片图片
        ref, target = capture.read()
        target = cv.flip(target, 1)
        cv.imshow("target", target)
        target_hsv = cv.cvtColor(target, cv.COLOR_BGR2HSV)
        dst = cv.calcBackProject([target_hsv], [0, 1], sample_hist, [0, 180, 0, 256], 1)
        cv.imshow("BackProject", dst)
        c=cv.waitKey(50)
        if c==27:
            break

backProjection()