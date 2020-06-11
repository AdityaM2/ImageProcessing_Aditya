import cv2
import numpy as np

img=cv2.imread('flower.jpg')



TL=False
BR=False


def crop_func(event,x,y,flags,param):
    global coord,TL,BR

    if event==cv2.EVENT_LBUTTONDOWN:
        if TL==False:
            coord=[(x,y)]
            TL=True
        elif BR==False:
            coord.append((x,y))
            BR=True
        if len(coord)==2:
            ty, by, tx, bx =coord[0][1],coord[1][1],coord[0][0],coord[1][0]
            crop = img[ty:by, tx:bx]
            cv2.imshow('Frame',crop)
            

cv2.namedWindow('Frame')
cv2.setMouseCallback('Frame',crop_func)

cv2.imshow('Frame',img)
