# 旋转

import cv2
import numpy as np

img = cv2.imread('1.jpg')

rows, cols = img.shape[:2]

M = cv2.getRotationMatrix2D((cols/2, rows/2), 45, 0.6)

dst = cv2.warpAffine(img, M, (2*cols, 2*rows))

while(1):
    cv2.imshow('img', dst)
    if cv2.waitKey(1) & 0xFF ==27:
        break

cv2.destroyAllWindows()

