#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 27 23:21:28 2019

@author: hsiehyiyong
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import time
import re
import numpy as np
import pandas as pd
import importlib,sys
importlib.reload(sys)
import urllib
#import html5lib/Users/hsiehyiyong/Documents/交大課業/四上專題/test_crawler.py

video_titles=[]
video_views=[]
video_links=[]
video_likes=[]
video_dislikes=[]

driver = webdriver.Chrome()
driver.get('https://www.youtube.com/channel/UCAKJ0tmI_RMXqTgxL_OMfIg/videos')#小舒放入欲爬頻道的「影片」頁面


times=6
for i in range(times + 1):
        height = driver.execute_script("return document.documentElement.scrollHeight")
        driver.execute_script("window.scrollTo(0, " + str(height) + ");")
        time.sleep(3)


soup = BeautifulSoup(driver.page_source,'lxml')
links = soup.select('div[id^=meta] a')

domain = 'https://www.youtube.com'
for ele in links:
    try:
        video_titles.append(ele.text)
    except:
        video_titles.append(np.nan)
    try:
        # 匹配“觀看次數:”后面的数字
        view = re.compile(r'(?<=觀看次數：)\d*\,?\d*\,?\d+')
        view.findall(ele.get('aria-label'))
        strv=''.join(view.findall(ele.get('aria-label')))
        video_views.append(strv)
    except:
        video_views.append(np.nan)
    try:
        video_links.append(domain + ele.get('href'))
        url=domain + ele.get('href')
        page = urllib.request.urlopen(url)
        vsoup = BeautifulSoup(page, 'html5lib')
        x=1
        if(vsoup.find("button",attrs={"title": "我喜歡"})!=None):
            video_likes.append(vsoup.find("button",attrs={"title": "我喜歡"}).get_text())
            print("success")
        else:
            video_likes.append(np.nan)
            """while(vsoup.find("button",attrs={"title": "我喜歡"})==None):
                page = urllib.request.urlopen(url)
                vsoup = BeautifulSoup(page, 'html5lib')
                print("fail", x ,"times")
                x = x + 1
                if(vsoup.find("button",attrs={"title": "我喜歡"})!=None):
                    print("success")
                    video_likes.append(vsoup.find("button",attrs={"title": "我喜歡"}).get_text())"""
        # dislike is similar:
        if(vsoup.find("button",attrs={"title": "我喜歡"})!=None):
            video_dislikes.append(vsoup.find("button",attrs={"title": "我不喜歡"}).get_text())
        else:
            video_dislikes.append(np.nan)
            """while(vsoup.find("button",attrs={"title": "我不喜歡"})==None):
                page = urllib.request.urlopen(url)
                vsoup = BeautifulSoup(page, 'html5lib')
                if(vsoup.find("button",attrs={"title": "我不喜歡"})!=None):
                    video_dislikes.append(vsoup.find("button",attrs={"title": "我不喜歡"}).get_text())"""
    except:
        video_links.append(np.nan)
del video_titles[len(video_titles)-1]
del video_views[len(video_views)-1]
del video_links[len(video_links)-1]
yt_test_dict = {"title":video_titles,
                  "link":video_links,
                 "views":video_views,
                 "like":video_likes,
                 "dislike":video_dislikes
                 }
yt_test_df = pd.DataFrame(yt_test_dict)
#小舒這裏放入想匯出的檔名
yt_test_df.to_csv("alisasa.csv", encoding='utf_8_sig')
