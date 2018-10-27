# 7练习

import cv2
import numpy as np

# 当鼠标按下是变成True
drawing = False
# 如果mode 为 true绘制矩形，按下'm'变成绘制曲线
mode = True
ix1, iy1, ix2, iy2 = -1, -1, -1, -1

#创建回调函数
def draw_circle(event, x, y, flags, param):
    f = False
    global ix1, iy1, ix2, iy2, drawing, mode
    # 当按下左键是返回起始位置坐标
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix1, iy1 = x, y
    #当按下左键移动是绘制图像。event可以查看移动,flag查看是否按下。
    elif event == cv2.EVENT_MOUSEMOVE and flags==cv2.EVENT_FLAG_LBUTTON:  
        if drawing == True:
            if mode == True:
                cv2.rectangle(img,(ix1,iy1),(x, y), (0,255,0),3)
            else:
                # 绘制圆圈
                cv2.circle(img, (x,y), 3, (0, 255, 0),-1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing == False
        cv2.rectangle(img,(ix1,iy1),(x, y), (0,0,0),-1)
        ix2, iy2 = -1, -1


# 绘制画布
img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)
while(1):
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break

            
