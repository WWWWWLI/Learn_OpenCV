import cv2 as cv
capture = cv.VideoCapture(0)
while True:
    ret, frame = capture.read()
    #镜像效果
    frame = cv.flip(frame, 1)
    #展示原图
    cv.imshow('imput', frame)
    #截取部分图像
    part = frame[42:282, 184:355]
    #展示部分图形
    cv.imshow('part', part)

    #将部分图像灰灰度图，单通道
    gray = cv.cvtColor(part, cv.COLOR_BGR2GRAY)
    #原来的图像为3通道，要合并需要把单通道变回到三通道
    backpart = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)
    #改变图形
    frame[42:282, 184:355] = backpart
    #展示改变后的图形
    cv.imshow('backpart', frame)

    c = cv.waitKey(40)
    if c == 27:
        break
