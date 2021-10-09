#-*-coding:utf-8-*-
# https://docs.opencv.org/master/d5/daf/tutorial_py_histogram_equalization.html
import cv2
import numpy as np
from matplotlib import pyplot as plt
import numpy as np
import cv2
import os
from glob import glob


src_path = './data/train/croped_images'
dst_path = './data/train/crop_hist_images'

cnt = 0
dir_list = os.listdir(src_path)
for dir_ in dir_list:
    cur_dir_ = os.path.join(src_path, dir_)
    new_dir_ = os.path.join(dst_path, dir_)
    os.makedirs(new_dir_, exist_ok=True)

    for x in glob(cur_dir_ + '/*'):
        cur_file = os.path.join(cur_dir_, x)
        new_file = new_dir_ + '/' + x.split('/')[-1]
        cnt += 1

        ##############################################################
        bgr = cv2.imread(cur_file)
        lab = cv2.cvtColor(bgr, cv2.COLOR_BGR2LAB)

        lab_planes = cv2.split(lab)
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        lab_planes[0] = clahe.apply(lab_planes[0])
        lab = cv2.merge(lab_planes)
        bgr = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)

        cv2.imwrite(new_file, bgr)