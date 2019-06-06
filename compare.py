#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 23 00:43:32 2019

@author: parshvashah
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

BGRImage = cv2.imread('turtle.jpg')
#plt.imshow(BGRImage:
RGBImage = cv2.cvtColor(BGRImage, cv2.COLOR_BGR2RGB)
#plt.imshow(RGBImage)

hsv_frame = cv2.cvtColor(RGBImage, cv2.COLOR_BGR2HSV)

def more_color(color1, color2):
    if color1 == 'green':
        low = np.array([25, 52, 72])
        high = np.array([102, 255, 255])
    if color2 == 'blue':
        low1 = np.array([100,150,0])
        high1 = np.array([140,255,250])
    mask = cv2.inRange(hsv_frame,low, high)
    mask2 = cv2.inRange(hsv_frame,low1, high1)
    