import numpy as np
import cv2
import os
from glob import glob

face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('./haarcascade_eye.xml')

src_path = './data/train/images'
dst_path = './data/train/croped_images'

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
        img = cv2.imread(cur_file)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        # print(type(faces))
        for (x,y,w,h) in faces:
            continue
            # img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0), 2) # blue
            # roi_gray = gray[y:y+h, x:x+w]
            # roi_color = img[y:y+h, x:x+w]
            # eyes = eye_cascade.detectMultiScale(roi_gray)
            # for (ex,ey,ew,eh) in eyes:
            #     cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2) # green
        if len(faces) != 0:
            y = int(y - h * 0.2)
            x = int(x - w * 0.2)
            if(y < 0 or x < 0 or int(y + h * (1.4)) >= 512 or int(x + w * (1.4)) >= 384) or w < 80 or h < 150:
                mid_x, mid_y = int(384 / 2), int(512 / 2)
                cw2, ch2 = int(380 / 2), int(380 / 2)
                crop_img = img[mid_y - ch2:mid_y + ch2, mid_x - cw2:mid_x + cw2]
            else:
                crop_img = img[y:int(y + h * (1.4)), x:int(x + w * (1.4))]
        else:
            mid_x, mid_y = int(384 / 2), int(512 / 2)
            cw2, ch2 = int(380 / 2), int(380 / 2)
            crop_img = img[mid_y - ch2:mid_y + ch2, mid_x - cw2:mid_x + cw2]

        dst = cv2.resize(crop_img, dsize=(380, 380), interpolation=cv2.INTER_LINEAR)

        cv2.imwrite(new_file, dst) #org_trim.jpg 라는 이름으로 저장
        #
        # cv2.imshow('img', dst)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        ##############################################################

print(cnt)



