import cv2
cap = cv2.VideoCapture(0)
counter = 0 #Initiasing the counter

while True:
    x,frame = cap.read()    
    counter +=1 #Incrementing the counter

    cv2.imwrite('IMG_'+str(counter)+'.jpg',frame) #Writing the frame into a new file
    cv2.imshow('Image',frame)

    if cv2.waitKey(1000) & 0xFF == ord('q'):
        break
