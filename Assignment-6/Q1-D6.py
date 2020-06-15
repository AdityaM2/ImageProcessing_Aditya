import cv2
import numpy as np


img = cv2.imread('IMG_3879.jpg')
width = int(img.shape[1] / 10)
height = int(img.shape[0] / 10)
dim = (width, height)
#resize the original image
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

img_gray = cv2.cvtColor(resized,cv2.COLOR_BGR2GRAY)
kernel = np.ones((5,5))
dilate=cv2.dilate(img_gray,kernel)
canny = cv2.Canny(dilate,200,300)

cv2.imshow('Original',img_gray)
cv2.imshow('Dilate',dilate)
cv2.imshow('Canny',canny)
