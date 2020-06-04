import cv2

#For Video capture
cap = cv2.VideoCapture(0)   #Webcam input

while True:
    x,frame = cap.read()

    frame = cv2.flip(frame,0)

    cv2.imshow('Image',frame)
    
    if cv2.waitkey(1) & 0xFF == ord('q'):
        break
