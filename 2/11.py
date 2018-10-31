# 使用Opencv检测程序效率

import cv2
import numpy as np

img1 = cv2.imread('1.jpg')

e1 = cv2.getTickCount()
for i in range(5, 49, 2):
    img1 = cv2.medianBlur(img1, i)
e2 = cv2.getTickCount()

time = (e2-e1)/ cv2.getTickFrequency()

print(time)

