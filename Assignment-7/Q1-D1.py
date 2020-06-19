import cv2

# Video capture
cap = cv2.VideoCapture(0)   #Capturing video from webcam
n=int(input('Enter n:')) #Taking input for n
counter = 0 #Initiasing the counter

while True:
    x,frame = cap.read()
    
    counter +=1 #Incrementing the counter

    flipped =  cv2.flip(frame,-1) #Defining a flipped frame
    
    if counter % n== 0:        #Decision making
        cv2.imshow('Image',frame) 
    else:
        cv2.imshow('Image',flipped)

    if cv2.waitKey(1000) & 0xFF == ord('q'): #Escape Sequence
        break
