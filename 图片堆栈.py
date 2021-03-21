# -*- coding: utf-8 -*-
# @Time    : 2021/3/21 21:49
# @Author  : VerNe
# @Email   ：1716200584@qq.com
# @FileName: 图片堆栈.py
# @Software: PyCharm

import os
import cv2
import numpy as np
from tqdm import tqdm


def read_img(path):
    img = cv2.imread(path)
    return img


def maxmiun(list):
    maxmu = max(list)
    return maxmu


def minium(lsit):
    minu = min(lsit)
    return minu


def getFileName1(path):
    input_template_All = []
    f_list = os.listdir(path)
    return f_list

def main(path):
    img_path=getFileName1(path)
    count=0
    for i in img_path:
        real_path=path+'/'+i
        img_path[count]=real_path
        count+=1
    print(img_path)
    img0=cv2.imread(img_path[0])
    height = img0.shape[0] - 1
    width = img0.shape[1] - 1
    image = np.ones_like(img0)
    image_num=[]
    for ima in img_path:
        this_image = cv2.imread(ima)
        image_num.append(this_image)
    for i in tqdm(range(height)):
        for j in (range(width)):
            red = []
            green = []
            blue = []
            for k in image_num:
                this_image = k
                red.append(this_image[i][j][0])
                green.append(this_image[i][j][1])
                blue.append(this_image[i][j][2])

            image[i][j][0] = maxmiun(red)
            image[i][j][1] = maxmiun(green)
            image[i][j][2] = maxmiun(blue)

    cv2.imwrite('test.jpg', image)

if __name__ == '__main__':
    path='align'
    main(path)
