import cv2 as cv
import numpy as np

def pyramin(img):
    """高斯金字塔"""
    #图像金字塔层数
    level=3
    #复制图片
    tmp=img.copy()
    pyramin_img=[]
    for i in range(level):
        dst=cv.pyrDown(tmp)
        pyramin_img.append(dst)
        cv.imshow("pyramid_down_"+str(i),dst)
        tmp=dst.copy();
    return pyramin_img

def lapalian(img):
    """拉普拉斯金字塔"""
    pyramid_images=pyramin(img)
    level=len(pyramid_images)
    #从高到低进行循环
    for i in range(level-1,-1,-1):
        if (i-1)<0:
            #如果是第一幅图，则用原图进行计算
            exapand = cv.pyrUp(pyramid_images[i], dstsize=img.shape[:2])
            lpls = cv.subtract(img, exapand)
            cv.imshow("lpls_down_" + str(i), lpls)
        else:
            exapand=cv.pyrUp(pyramid_images[i],dstsize=pyramid_images[i-1].shape[:2])
            lpls=cv.subtract(pyramid_images[i-1],exapand)
            cv.imshow("lpls_down_"+str(i),lpls)


#图像长宽必须是2的倍数，即2的n次方，如果不是将会报错
src=cv.imread('testwli_pyramin.jpg')
cv.imshow("def",src)
lapalian(src)
cv.waitKey(0)
cv.destroyAllWindows()