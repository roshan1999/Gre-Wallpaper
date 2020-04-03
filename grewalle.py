#!/usr/bin/env python
# coding: utf-8

# In[1]:


import argparse
import imutils
import cv2
import pandas as pd
def create(i,thresh,image): #i denotes the dataframe's index
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    for c in cnts:
        M = cv2.moments(c)
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
    return [cX,cY]
def main(i):
    image = cv2.imread('wallpaper.jpg',cv2.IMREAD_UNCHANGED)
    image2 = cv2.imread('wallpaper.jpg',cv2.IMREAD_UNCHANGED)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]
    lst = []
    lst = create(i,thresh,image)
    cX = lst[0]
    cY = lst[1]
    wordtext_shape = cv2.getTextSize("word: "+df.values[i][0],cv2.FONT_HERSHEY_DUPLEX,4,3)
    meantext_shape = cv2.getTextSize("Meaning: "+df.values[i][1],cv2.FONT_HERSHEY_SCRIPT_COMPLEX,3,3)
    cv2.putText(image2, "word: "+df.values[i][0], (cX - (int)(wordtext_shape[0][0]/2), cY - 200-wordtext_shape[0][1]),cv2.FONT_HERSHEY_DUPLEX, 4, (255, 255, 255), 4)
    cv2.putText(image2, "Meaning: "+df.values[i][1], (cX - (int)(meantext_shape[0][0]/2), cY - 100-meantext_shape[0][1]),cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 3, (255, 255, 255), 3)
    cv2.imwrite('img'+str(i)+".png",image2)

if __name__ == '__main__':
    df = pd.read_csv("randword.csv",sep = ",", names = ["word","meaning"])
    for i in range(100):
        main(i)

