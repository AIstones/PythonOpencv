# 基本图形操作

import cv2
import numpy as np

img = cv2.imread('1.jpg',1)
print(img.item(10,10,2))
img.itemset((10,10,2), 100)
print(img.item(10,10,2))
print(img.shape)
print(img.size)
print(img.dtype)
b,g,r = cv2.split(img)
img = cv2.merge([b,g,r])
cv2.imshow('img',img)
k = cv2.waitKey(0)
cv2.destroyAllWindows()

