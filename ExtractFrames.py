#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 18:11:37 2018

@author: vineeth
"""


### source: https://stackoverflow.com/questions/33311153/python-extracting-and-saving-video-frames
import cv2
### path to the movie file
movie = '/home/thekb/Desktop/vineeth_insight/darknet/data/objectPickUp.gif'

###  
vidcap = cv2.VideoCapture(movie)
success,image = vidcap.read()
count = 0
while success:
  vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*1000)) 
  cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file      
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1

