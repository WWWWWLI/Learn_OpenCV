import cv2 as cv


def contours(img):
    dst = cv.GaussianBlur(img, (3, 3), 0)
    # 转换为灰度图像
    gray = cv.cvtColor(dst, cv.COLOR_RGB2GRAY)
    # 转换为二值图像
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    cv.imshow("bi", binary)

    cloneImg, contours, heriachy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    for i, contour in enumerate(contours):
        cv.drawContours(img, contours, i, (0, 0, 255), 2)
    cv.imshow("contpurs", img)

    print(contours)


src = cv.imread('cwwhand.jpg')
cv.imshow('def', src)
contours(src)
cv.waitKey(0)
cv.destroyAllWindows()
