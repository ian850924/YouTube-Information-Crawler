# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 14:48:07 2019

@author: xxx23
"""
import math
#import jieba.analyse #把jieba資料夾放進spyder資料夾就可以成功匯入
#import jieba.posseg as pseg
import pandas as pd
import numpy as np
import os
import re
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

#DIR=r'/Users/hsiehyiyong/Desktop/mcjeng/mcjeng.csv'
#count_file=len([name for name in os.listdir(DIR)])
sentiment_dict_df=pd.read_excel(r'/Users/hsiehyiyong/Desktop/mcjeng/opinion_word.xls')
score_list=""   #score array 儲存每部影片的sentiment score

for i in range(21):
    try:
        keyword = pd.read_csv(r'/Users/hsiehyiyong/Desktop/mcjeng/關鍵字_mcjeng'+str(i+1)+'.txt', sep=" ", header=None,engine='python',encoding='utf-8')
        print(i+1,'\n')
        score_sum=0
        for index,row in sentiment_dict_df.iterrows():
            #print(row['Word'],row['Score'])
            for index1,row1 in keyword.iterrows():
                if row['Word']==row1[0]:
                    feq=row1[1]*row['Score']
                    print(row1[0],'有在詞典內')
                    score_sum+=feq
    
        score_list+=str(score_sum)+' ' 
    except:
        score_list+=str('0')+' '
        score_sum=0
    print('第',i+1,'部影片處理完畢\n')
    print('分數為: ',score_sum)

print(score_list)
f=open(r'字幕情緒_mcjeng.txt','w',encoding='utf8')
f.write(score_list)
f.close()

