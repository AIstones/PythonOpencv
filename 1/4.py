# 学习视频获取

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(True):
    #获取一帧图像
    ret, frame = cap.read()

    #图像类型转换
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #显示图像
    cv2.imshow('frame', gray)
    if cv2.waitKey(1)& 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
