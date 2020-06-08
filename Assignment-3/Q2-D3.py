import cv2
import numpy as np
import random
import time

img=cv2.imread('flower.jpg')
h,w,c=img.shape
#h=560,w=560
a1=0
a2=0
b1=int(560/7)   #b1=80
b2=int(560/7)   #b2=80

row=0
while True: #Y axis loop
    
    if row % 2==0: #Even row
        a1=0
        b1=80
        
        while True:
            cv2.rectangle(img,(a1,a2),(b1,b2),(random.randint(0,255),random.randint(0,255),random.randint(0,255)),-1)
            cv2.imshow('Frame',img)
            cv2.waitKey(500)
            a1+=80
            b1+=80
            if b1>560:
                break

    else: #Odd row
        a1=480
        b1=560
        
        while True:
            cv2.rectangle(img,(a1,a2),(b1,b2),(random.randint(0,255),random.randint(0,255),random.randint(0,255)),-1)
            cv2.imshow('Frame',img)
            cv2.waitKey(500)
            a1-=80
            b1-=80
            if a1<0:
                break

    a2+=80
    b2+=80
    row+=1
    if b2>560:
        break
