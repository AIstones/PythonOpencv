# 把鼠标当画笔,EVENT事件

import cv2
import numpy as np

events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)

