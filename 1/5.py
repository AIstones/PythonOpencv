#保存视频文件

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

#定义视频编码类型
fourcc = cv2.VideoWriter_fourcc(*'FMP4')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        frame = cv2.flip(frame, 0)

        #写视频每帧
        out.write(frame)

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
            break

cap.release()
out.release()
cv2.destroyAllWindows()

