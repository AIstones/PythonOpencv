# 用滑动条做调色板

import cv2
import numpy as np

def nothing(x):
    pass

# 当按下鼠标变成True
drawing = True
# 如果mode为True绘制矩形，再按'm'绘制曲线
mode = True
ix, iy = -1, -1

#创建回调函数
def draw_circle(event, x, y, flags, param):
    r=cv2.getTrackbarPos('R','image')
    g=cv2.getTrackbarPos('G','image')
    b=cv2.getTrackbarPos('B','image')
    color = (b, g, r)

    global ix, iy, drawing, mode
    #当按下左键返回起始位置坐标
    if event==cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    # 当按下左键移动时绘制图形.event可以查看移动,flag查看是否按下
    elif event == cv2.EVENT_MOUSEMOVE and flags==cv2.EVENT_FLAG_LBUTTON:
        if drawing == True:
            if mode == True:
                cv2.rectangle(img, (ix,iy), (x, y), color, -1)
            else:
                #绘制圆圈
                cv2.circle(img, (x, y), 3, color, -1)

    elif event == cv2.EVENT_LBUTTONUP:
                drawing = False

img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')
cv2.createTrackbar('R','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('B','image',0,255,nothing)
cv2.setMouseCallback('image', draw_circle)

while(1):
    cv2.imshow('image',img)
    
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break
    

