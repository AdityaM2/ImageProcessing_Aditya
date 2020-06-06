import cv2
import random

img=cv2.imread('flower.jpg') #reading the image
h,w,c=img.shape #taking coordinates of the image

cv2.line(img,(0,0),(w,h),(random.randint(0,255),random.randint(0,255),random.randint(0,255)),4) #Drawing a line across the image with a random colour

cv2.imshow('Frame',img) #Displaying the edited image

