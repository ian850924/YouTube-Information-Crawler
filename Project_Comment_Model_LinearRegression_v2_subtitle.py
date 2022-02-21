# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 18:53:59 2019

@author: xxx23
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn import cross_validation
from sklearn.metrics import mean_squared_error,mean_absolute_error
#views_df=pd.read_csv("Project\huandachien.csv",engine='python')
views_df=pd.read_csv("Project\mcjeng.csv",engine='python')
#views_df=pd.read_csv("Project\alisasa.csv",engine='python')

views_sum=0
for index,row in views_df.iterrows():
    row['views']=row['views'].replace(',','')
    views_sum+=int(row['views'])
#print(len(mean_views_df.index))
#print(views_sum)
mean_score=views_sum/len(views_df.index)
print(mean_score)
difference_array=[]
for index,row in views_df.iterrows():
    row['views']=row['views'].replace(',','')
    difference_array.append(int(row['views'])-mean_score)

difference_array=[ '%.4f' % elem for elem in difference_array ]
views_df['difference']=difference_array
views_df=views_df[:]
score = pd.read_csv(r'/Users/hsiehyiyong/Desktop/mcjeng/字幕情緒_mcjeng.txt',engine='python', sep=" ", header=None)
#score = pd.read_csv(r'C:\Users\xxx23\.spyder-py3\Project\影片情緒_恩熙俊.txt',engine='python', sep=" ", header=None)
#score = pd.read_csv(r'C:\Users\xxx23\.spyder-py3\Project\影片情緒_Alisasa.txt',engine='python', sep=" ", header=None)

score=score.T
#因為新出的影片還沒有爬點閱率，所以score先拿掉前面幾筆資料
score=score[4:-1]
views_df=views_df.round(4)
X=score
X.columns=['score']
Y=views_df['difference']
x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.2,random_state=20170816)
model=LinearRegression()
model.fit(x_train,y_train)

#計算回歸線係數
r_squared = model.score(x_train, y_train)
print('y=ax+b的 a係數:',model.coef_)
print('y=ax+b的 b截距:',model.intercept_ )
print('R平方',r_squared)

plt.figure(figsize=(20,20))
plt.scatter(x_test,y_test,color='blue',marker='.')  #marker='x' 只是圖中點的形狀
plt.plot(x_test,model.predict(x_test),color='green')
plt.xlabel('score')
plt.ylabel('views')
#plt.xlim((0,0.2))
plt.ylim((-5,30))
plt.savefig('Project/LinearRegression_subtitle_mcjeng.png',bbox_inches='tight')
plt.show()

#預測
#print('預測score=0.2 views為:',model.predict(0.2))
predict_y=[]
true_y=y_test
#print(x_test)
for index,row in x_test.iterrows():
    predict_y.append(model.predict(row['score']))
    print(model.predict(row['score']))

print('predict y',predict_y)
print('true y',y_test)
#用y_test和predict y計算MSE
predict_y=np.array(predict_y)
MAE=mean_absolute_error(true_y, predict_y)
MSE=mean_squared_error(true_y, predict_y)
RMSE=np.sqrt(MSE)
print('MAE',MAE)
print('MSE',MSE)
print('RMSE',RMSE)
    
    
    
    
    
    
    
    
    