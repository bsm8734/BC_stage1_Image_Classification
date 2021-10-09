#-*-coding:utf-8-*-
# https://docs.opencv.org/master/d5/daf/tutorial_py_histogram_equalization.html
import cv2
import numpy as np
from matplotlib import pyplot as plt
import numpy as np
import cv2
import os
from glob import glob

src_path = './data/eval/croped_images'
dst_path = './data/eval/crop_hist_images'
os.makedirs(dst_path, exist_ok=True)

cnt = 0
dir_ = os.listdir(src_path)
for name_ in glob(src_path + '/*'):
    cur_file = os.path.join(src_path, name_)
    new_file = os.path.join(dst_path, name_.split('/')[-1])

    bgr = cv2.imread(cur_file)
    lab = cv2.cvtColor(bgr, cv2.COLOR_BGR2LAB)

    lab_planes = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    lab_planes[0] = clahe.apply(lab_planes[0])
    lab = cv2.merge(lab_planes)
    bgr = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)

    cv2.imwrite(new_file, bgr)