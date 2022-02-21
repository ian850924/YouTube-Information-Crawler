import pafy
import vlc
import os
import time
import io,sys,subprocess

#urls
# coding: utf-8

# In[4]:


from selenium import webdriver
driver = webdriver.Chrome()


# In[6]:

#test https://www.youtube.com/channel/UCtz0NSHlW1BBKX4YJ9gTP1A/videos
#vin https://www.youtube.com/channel/UC72ppgqXU1IOouV8iq-NlKQ/videos
#dachien https://www.youtube.com/user/fuckingtinyhippo/videos

driver.get('https://www.youtube.com/user/fuckingtinyhippo/videos')#放入欲爬頻道的「影片」頁面

times=6
for i in range(times + 1):
        height = driver.execute_script("return document.documentElement.scrollHeight")
        #print(height)
        driver.execute_script("window.scrollTo(0, " + str(height) + ");")
        #print(i,'\n')
        time.sleep(3)


# In[8]:


from bs4 import BeautifulSoup
soup = BeautifulSoup(driver.page_source,'html.parser')
links = soup.select('div[id^=meta] a')


# In[9]:


domain = 'https://www.youtube.com'
count=1
lists=[]
i=0
for ele in links:
    #print(ele.text)#title
    #print(ele.get('aria-label'))#info
    if(ele.get('href')==None):
        break
    #print(domain + ele.get('href'))#link
    lists.append(domain + ele.get('href'))
    count=count+1
    i=i+1
#print(count)
print(lists)



for vid in lists:
    url = vid 
    print(url)
    

    video = pafy.new(url)
    best = video.getbest()
    playurl = best.url

    skipTime = 1000*5 # milliseconds


    #directory = "images/"
    directory = "eric/"
    prefix = str.split(url, "=")[1] + "_" # get video ID, end of url
    harvesting = False
    waitForBuffer = False
    recordTime = 0

    def callbackBuffering(arg):
        global waitForBuffer
        global harvesting

        if(recordTime + skipTime < arg.u.new_time and harvesting):
            waitForBuffer = False

    try:
        #os.mkdir("images")
        os.mkdir("eric")
    except:
        print("directory exists")    


    Instance = vlc.Instance()
    player = Instance.media_player_new()
    eventManager = player.event_manager()
    eventManager.event_attach(vlc.EventType.MediaPlayerBuffering, callback = callbackBuffering)

    

    Media = Instance.media_new(playurl)
    Media.get_mrl()
    player.set_media(Media)

    player.play()

    time.sleep(5) # wait till the window appears
    player.pause()
    # subprocess.call(['vlc', url, '--play-and-exit', '--fullscreen'], shell=True)

    #images = 0
    Nsichun = 0
    harvesting = True
    while(player.get_time() < player.get_length()):

        waitForBuffer = True
        path = directory + prefix + str(player.get_time() ) + ".png"
        print("image will be taken at " + str(player.get_time() ) + "ms at path "+ path )   
        time.sleep(0.5)
        recordTime = player.get_time()
        player.video_take_snapshot(0, path ,i_width=player.video_get_width(), i_height=player.video_get_height())
        player.set_time(recordTime+skipTime)
        
        #os.system("TASKKILL /F /IM vlc.exe")


        while(waitForBuffer):
            print("waiting for buffering")
            time.sleep(0.1)

        print(player.get_time())
        print(player.get_position())
    player.stop()