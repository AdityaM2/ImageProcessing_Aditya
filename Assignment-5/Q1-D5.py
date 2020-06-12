import cv2
import numpy as np

cap=cv2.VideoCapture(0)


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
            crop = frame[ty:by, tx:bx]
            cv2.imwrite('Template.jpg',crop)
            


       
cv2.namedWindow('Frame')
cv2.setMouseCallback('Frame',crop_func)

while True:
    x,frame=cap.read()
    template=cv2.imread('Template.jpg')
    if TL==True and BR==True:
        cv2.imshow('Template',template)
        template_gray=cv2.cvtColor(template,cv2.COLOR_BGR2GRAY)
        width=template.shape[1]
        height=template.shape[0]                  
        frame_gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        res=cv2.matchTemplate(frame_gray,template_gray,cv2.TM_CCOEFF_NORMED)
        loc=np.where(res>=0.7)
        for x,y in zip(*loc[::-1]):
            cv2.rectangle(frame,(x,y),(x+width,y+height),(0,255,0),1)
            cv2.putText(frame,'Object',(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),1)
    cv2.imshow('Frame',frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
