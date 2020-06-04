import cv2

#For Video capture
cap = cv2.VideoCapture(0)   #Webcam input
n=int(input('Enter n:')) #Taking input for n
counter = 0 #Initiasing the counter

while True:
    x,frame = cap.read()
    
    counter +=1 
    flipped =  cv2.flip(frame,-1) #Defining a flipped frame
    
    if counter % n== 0:        #For n frames
        cv2.imshow('Image',frame) 
    else:
        cv2.imshow('Image',flipped)

    if cv2.waitKey(1) & 0xFF == ord('q'): #Escape Sequence
        break
