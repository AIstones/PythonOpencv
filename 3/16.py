# 图像平滑

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('1.jpg')

kernel = np.ones((5,5), np.float32)/ 25

dst = cv2.filter2D(img, -1, kernel)
blur = cv2.blur(img, (5,5))
gussian = cv2.GaussianBlur(img, (5,5),0)
median = cv2.medianBlur(img, 5)
bilater = cv2.bilateralFilter(img, 9,75,75)

plt.subplot(231), plt.imshow(img), plt.title('Original')
plt.xticks([]),plt.yticks([])
plt.subplot(232), plt.imshow(dst), plt.title('Averaging')
plt.xticks([]),plt.yticks([])
plt.subplot(233), plt.imshow(blur), plt.title('Blur')
plt.xticks([]),plt.yticks([])
plt.subplot(234), plt.imshow(gussian), plt.title('Gaussian')
plt.xticks([]),plt.yticks([])
plt.subplot(235), plt.imshow(median), plt.title('Median')
plt.xticks([]),plt.yticks([])
plt.subplot(236), plt.imshow(bilater), plt.title('Bilater')
plt.xticks([]),plt.yticks([])
plt.show()

