import cv2
import numpy as np


img = cv2.imread('IMG_3879.jpg')
width = int(img.shape[1] / 10)
height = int(img.shape[0] / 10)
dim = (width, height)
#resize the original image
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
cv2.imshow('Original',resized)

img_gray = cv2.cvtColor(resized,cv2.COLOR_BGR2GRAY)
kernel = np.ones((5,5))
dilate=cv2.dilate(img_gray,kernel)
canny = cv2.Canny(dilate,200,300)

contours,hierarchy=cv2.findContours(canny,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
areas=[cv2.contourArea(c) for c in contours]
max_index=np.argmax(areas)
max_contour=contours[max_index]
perimeter=cv2.arcLength(max_contour,True)
coord=cv2.approxPolyDP(max_contour,0.01*perimeter,True)
cv2.drawContours(resized,[coord],-1,(0,255,0),1)
P1=np.array([coord[1],coord[0],coord[2],coord[3]],np.float32)
P2=np.array([(0, 0), (500, 0), (0, 600), (500, 600)],np.float32)
perspective = cv2.getPerspectiveTransform(P1,P2)
transformed = cv2.warpPerspective(resized, perspective,(500,600))

cv2.imshow('Contours',resized)
cv2.imshow('Transformed',transformed)
