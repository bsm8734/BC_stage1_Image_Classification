import numpy as np
import cv2
import pandas as pd
import csv

# path = "/opt/ml/input/data/train/train.csv"
# files = pd.read_csv(path)
# filepath = files['filepath'].tolist()

seed = 201
img = cv2.imread('./normal.jpg')
cv2.imshow('img', img)
drag = False
default_x, default_y, w, h = -1, -1, -1, -1
blue = (255, 0, 0)

def Mouse(event, x, y, flag, param):
    global drag, default_x, default_y, img
    if event == cv2.EVENT_LBUTTONDOWN: # 마우스 왼쪽 버튼 누름
        drag = True
        default_x = x
        default_y = y
    elif event == cv2.EVENT_LBUTTONDOWN: # 마우스 이동
        if drag:
            draw = img.copy()
            cv2.rectangle(draw, (default_x, default_y), (x, y), blue, 3)
            cv2.imshow('img', draw)
    elif event == cv2.EVENT_LBUTTONUP: # 왼쪽 버튼 뗌
        if drag:
            drag = False
            w = x - default_x
            h = y - default_y
            if w > 0 and h > 0:
                draw = img.copy()
                cv2.rectangle(draw, (default_x, default_y), (x, y), blue, 3)
                cv2.imshow('img', draw)
                roi = img[default_y, default_y+h, default_x, default_x+w]
                cv2.imshow("drag", roi)
                cv2.imwrite("drag.jpg", roi)
                print(default_y, default_y+h, default_x, default_x+w)
            else:
                cv2.imshow('img', img)

cv2.setMouseCallback('img', Mouse)
cv2.waitKey()
cv2.destroyAllWindows()
