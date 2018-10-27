import cv2
import numpy as np

img = cv2.imread('1.jpg')
cv2.imshow('image', img)
k = cv2.waitKey(0)&0xFF
if k == 27:
    cv2.destroyAllWindows()
elif k == 's':
    cv2.imwrit('1.jpg', img)
    cv2.destroyAllWindows()
