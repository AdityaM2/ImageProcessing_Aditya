import cv2
import numpy as np
import random


img=cv2.imread('flower.jpg')
h,w,c=img.shape
#h=560,w=560
a1=0
a2=0
b1=int(560/7)    #b1=80
b2=int(560/7)    #b2=80

while True:     #Y axis loop
    a1=0
    b1=80

    while True: #X axis loop
        cv2.rectangle(img,(a1,a2),(b1,b2),(random.randint(0,255),random.randint(0,255),random.randint(0,255)),-1)
        a1+=80
        b1+=80
        if b1>560:
            break
       
    a2+=80
    b2+=80
    if b2>560:
        break
cv2.imshow('Frame',img)
