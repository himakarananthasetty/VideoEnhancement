# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 16:05:12 2021

@author: vedav
"""

# import module
import cv2
import datetime

# create video capture object
data = cv2.VideoCapture('C:\\Users\\vedav\\Desktop\\INTERNSHIP\\DRDL internship\\DRDO\\imgggg\\project.avi')

# count the number of frames
frames = data.get(cv2.CAP_PROP_FRAME_COUNT)
fps = int(data.get(cv2.CAP_PROP_FPS))

# calculate dusration of the video
seconds = int(frames / fps)
video_time = str(datetime.timedelta(seconds=seconds))
print("duration in seconds:", seconds)
print("video time:", video_time)
