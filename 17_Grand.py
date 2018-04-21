import cv2 as cv


def sobel(img):
    """索贝尔算子"""
    grad_x = cv.Sobel(img, cv.CV_32F, 1, 0)
    grad_y = cv.Sobel(img, cv.CV_32F, 0, 1)
    gradx = cv.convertScaleAbs(grad_x)
    grady = cv.convertScaleAbs(grad_y)
    cv.imshow("x", gradx)
    cv.imshow("y", grady)

    gradxy = cv.addWeighted(gradx, 0.5, grady, 0.5, 0)
    cv.imshow("grad", gradxy)


def scharr(img):
    """某些边缘差异很小的情况下使用"""
    grad_x = cv.Scharr(img, cv.CV_32F, 1, 0)
    grad_y = cv.Scharr(img, cv.CV_32F, 0, 1)
    gradx = cv.convertScaleAbs(grad_x)
    grady = cv.convertScaleAbs(grad_y)
    cv.imshow("x", gradx)
    cv.imshow("y", grady)

    gradxy = cv.addWeighted(gradx, 0.5, grady, 0.5, 0)
    cv.imshow("grad", gradxy)


def lapalian(img):
    """拉普拉斯算子"""
    dst = cv.Laplacian(img, cv.CV_32F)
    lpls = cv.convertScaleAbs(dst)
    cv.imshow("lpls", lpls)


src = cv.imread('testwli.jpg')
#sobel(src)
scharr(src)
# lapalian(src)
cv.waitKey(0)
cv.destroyAllWindows()
