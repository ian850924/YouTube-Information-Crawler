#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 00:41:10 2019

@author: hsiehyiyong
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt


"""
#照片的前處理，捨棄雜訊

#for num in range(12):
img = cv2.imread('/Users/hsiehyiyong/Documents/交大課業/四上專題/testing_data/demo/demo1.png',0)
img = cv2.medianBlur(img,5)

ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY,11,2)
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)

titles = ['Original Image', 'Global Thresholding (v = 127)',
            'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [img, th1, th2, th3]

for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()


tesseract圖片辨識
"""
# pytesseract為在python中使用tesseract所需要的函式庫
import pytesseract
from PIL import Image
# tesseract安裝路徑
pytesseract.pytesseract.tesseract_cmd = '/usr/local/bin/tesseract'
ytbname="DaChien"
videonum="DjB3-nRiDys"
i=2401
# 打開照片
text=""
while(i<=172401):
    try:
        filename="/Users/hsiehyiyong/Documents/交大課業/四上專題/"+ytbname+"/"+videonum+"_"+str(i)+".png"
        img = Image.open(filename)
        text+=pytesseract.image_to_string(img, lang = 'chi_tra',config = '6')
        i+=5000
    except:
        text+=""
        i+=5000
f=open(ytbname+'_'+videonum+'.txt','w',encoding='utf8')
f.write(text)
f.close()

# 丟入模組內分析
"""
0 Orientation and script detection (OSD) only.
1 Automatic page segmentation with OSD.
2 Automatic page segmentation, but no OSD, or OCR.
3 Fully automatic page segmentation, but no OSD. (Default)
4 Assume a single column of text of variable sizes.
5 Assume a single uniform block of vertically aligned text.
6 Assume a single uniform block of text.
7 Treat the image as a single text line.
8 Treat the image as a single word.
9 Treat the image as a single word in a circle.
10 Treat the image as a single character.
"""


