import cv2
import numpy as np

img=cv2.imread('IMG_5912.jpg')

scale_percent=100
width = int(img.shape[1] * scale_percent / 1000)
height = int(img.shape[0] * scale_percent / 1000)
dim = (width, height)
#resize the original image
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

counter=0
def mouse(event,x,y,flags,param):
    global coord,counter
   
    if event==cv2.EVENT_LBUTTONDOWN:
        if counter==0:
            coord=[(x,y)]
            counter+=1
        elif counter!=0 and counter<4:
            coord.append((x,y))
            counter+=1
        if counter==4:
            P1=np.array([coord[0],coord[1],coord[2],coord[3]],np.float32)
            P2=np.array([(0, 0), (500, 0), (0, 600), (500, 600)],np.float32)
            perspective = cv2.getPerspectiveTransform(P1,P2)
            transformed = cv2.warpPerspective(resized, perspective,(500,600))
            cv2.imshow('Frame',transformed)

            

cv2.namedWindow('Frame')
cv2.setMouseCallback('Frame',mouse)

cv2.imshow('Frame',resized)
