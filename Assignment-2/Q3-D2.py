import cv2
import time
import math

cap=cv2.VideoCapture(0) #Capturing from the webcam
counter=0

st=time.time() #Taking start time

for i in range(0,5):    #Loop for five seconds
    time.sleep(1)

et=time.time()  #Taking end time
elt=et-st      #Elapsed time
elt=math.floor(elt) #Taking the integer value

while True:
    x,frame=cap.read()
    flipped=cv2.flip(frame,-1)

    time.sleep(1)
    counter += 1
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if counter % elt==0:
        cv2.imshow('Image',flipped)
    else:
        cv2.imshow('Image',frame)
    
    
    
