# YouTube-View-Count-Prediction-Model
1. Use project_crawler.py to get the information (view counts,title,likes, unlikes, upload date) of videos.
2. Use youtube_screenshot.py to get the screenshot of the videos.
3. Retrain Tesseract_OCR with youtuber.traineddata.
4. Use subtitle_extractor.py to get the subtitle of the videos.
5. Use Project_Comment_Model_Subtilte.py to analyze the sentimental score of the video.
6. Use sentimental score as the x-coordinate of training data and videos' information as the y-coordinate of training data to train the linear regression model.
