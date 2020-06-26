from tkinter import *
import tkinter as tk
from tkinter import filedialog,Text
from PIL import Image,ImageTk
import cv2
import numpy as np
import pytesseract
from pytesseract import Output
import tkinter.font as tkFont

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
root = tk.Tk()
root.title('Image Processing App')
global img,counter,IMG,reserve1,reserve2,reserve3,reserve4,reserve5,reserve6
def select_image_command():
    global img,reserve1,reserve2,reserve3,reserve4,reserve5,reserve6
    filename = filedialog.askopenfilename(initialdir ='/Users/',title = 'Select an Image',filetypes = (('JPG','*.jpg'),('All files','*.*')))
    img = cv2.imread(filename)
    if img.shape[1]>1500 or img.shape[0]>1500:
        width = int(img.shape[1] / 10)
        height = int(img.shape[0] / 10)
        dim = (width, height)
        #resize the original image
        img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    cv2.imshow('Selected Image',img)
    reserve1=img.copy()
    reserve2=img.copy()
    reserve3=img.copy()
    reserve4=img.copy()
    reserve5=img.copy()
    reserve6=img.copy()
    cv2.waitKey(0)

def blur_image_command():
    global img,IMG,reserve1
    img_gray = cv2.cvtColor(reserve1,cv2.COLOR_BGR2GRAY)
    kernel = np.ones((25,25))/625
    blur = cv2.filter2D(img_gray,-1,kernel)
    cv2.imshow('Blurred Image',blur)
    IMG=blur.copy()

def auto_crop_image_command():
    global img,IMG,reserve2
    cv2.imshow('Original',reserve2)
    img_gray = cv2.cvtColor(reserve2,cv2.COLOR_BGR2GRAY)
    kernel = np.ones((5,5))
    dilate=cv2.dilate(img_gray,kernel)
    canny = cv2.Canny(dilate,200,300)

    contours,hierarchy=cv2.findContours(canny,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    areas=[cv2.contourArea(c) for c in contours]
    max_index=np.argmax(areas)
    max_contour=contours[max_index]
    perimeter=cv2.arcLength(max_contour,True)
    coords=cv2.approxPolyDP(max_contour,0.01*perimeter,True)
    if len(coords)==4:
        coord=coords.reshape(4,2)
        sumpx=[(x+y) for x,y in coord]
        diffpx=[(x-y) for x,y in coord]

        bri=np.argmax(sumpx)
        tli=np.argmin(sumpx)
        tri=np.argmax(diffpx)
        bli=np.argmin(diffpx)

        tl=coord[tli]
        tr=coord[tri]
        bl=coord[bli]
        br=coord[bri]
        P1=np.array([tl,tr,bl,br],np.float32)
        P2=np.array([(0, 0), (500, 0), (0, 600), (500, 600)],np.float32)
        perspective = cv2.getPerspectiveTransform(P1,P2)
        transformed1 = cv2.warpPerspective(reserve2, perspective,(500,600))
        cv2.imshow('Auto Cropped Image',transformed1)
        IMG=transformed1.copy()


    cv2.drawContours(reserve2,[coords],-1,(0,255,0),1)
    cv2.imshow('Image Contours',reserve2)
    
def manual_crop_image_command():
    global img,counter,IMG,reserve3
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
                transformed = cv2.warpPerspective(reserve3, perspective,(500,600))
                cv2.imshow('Manual Cropped Image',transformed)
                IMG=transformed.copy()

    cv2.namedWindow('Manual Crop')
    cv2.setMouseCallback('Manual Crop',mouse)
    cv2.imshow('Manual Crop',reserve3)
    

def ocr_command():
    global img,reserve4
    text = pytesseract.image_to_string(reserve4,lang= 'eng')
    data = pytesseract.image_to_data(reserve4,output_type= Output.DICT)
    no_word = len(data['text'])

    for i in range(no_word):
        if int(data['conf'][i]) > 50:
            x,y,w,h = data['left'][i],data['top'][i],data['width'][i],data['height'][i]
            cv2.rectangle(reserve4,(x,y),(x+w,y+h),(0,0,0),2)
            cv2.putText(reserve4,data['text'][i],(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2)
            cv2.imshow('OCR',reserve4)
            cv2.waitKey(100)


def show_txt_command():
    global img,reserve5,text
    text = pytesseract.image_to_string(reserve5,lang= 'eng')
    data = pytesseract.image_to_data(reserve5,output_type= Output.DICT)
    no_word = len(data['text'])
    text = Text(textbox,bg = '#FDFFD6')

    for i in range(no_word):
        if int(data['conf'][i]) > 50:
            text.insert('1.0',data['text'][i]+' ')
            text.pack()

def clear_txt_command():
    global img,reserve,text
    text2=text
    text2.delete('1.0',END)
    

def save_image_command():
    global img,IMG,reserve
    cv2.imwrite('Saved Image.jpg',IMG)
   

def show_original_command():
    global img,reserve6
    cv2.imshow('Original Image',reserve6)

def close_window_command():
    root.destroy()

canvas = tk.Canvas(root,height = 650,width = 600,bg='#2E3442')
canvas.pack()
fontStyle = tkFont.Font(family="Lucida Grande", size=30)
frame = tk.Frame(canvas,bg = '#141821')
frame.place(relx = 0.2,rely = 0.01,relwidth =0.6,relheight =0.75)
textbox = tk.Frame(frame,bg = '#FDFFD6')
textbox.place(relx = 0.2,rely = 0.2,relwidth =0.6,relheight =0.7)
heading=tk.Label(frame,text='OCR Output',fg='white',bg='#141821',font=fontStyle).place(x=70,y=5)
       



select_image = tk.Button(canvas,text = 'SELECT IMAGE',fg = 'white',bg='#00CE96',padx = 10,pady = 10, command = select_image_command).place(x=5,y=5)

blur_image=tk.Button(canvas,text = 'BLUR IMAGE',fg = 'white',bg='#00CE96',padx = 15,pady = 10, command = blur_image_command).place(x=340,y=505)

auto_crop_image = tk.Button(canvas,text = 'AUTO CROP',fg = 'white',bg='#00CE96',padx = 10,pady = 10, command = auto_crop_image_command).place(x=5,y=600)

manual_crop_image = tk.Button(canvas,text = 'MANUAL CROP',fg = 'white',bg='#00CE96',padx = 10,pady = 10, command = manual_crop_image_command).place(x=160,y=600)

ocr = tk.Button(canvas,text = 'OCR',fg = 'white',bg='#00CE96',padx = 35,pady = 10, command = ocr_command).place(x=490,y=505)

show_txt = tk.Button(canvas,text = 'SHOW TEXT',fg = 'white',bg='#00CE96',padx = 15,pady = 10, command = show_txt_command).place(x=160,y=505)

clear_txt=tk.Button(canvas,text= 'CLEAR TEXT',fg = 'white',bg='#00CE96',padx = 15,pady = 10, command = clear_txt_command).place(x=340,y=600)

save_image = tk.Button(canvas,text = 'SAVE IMAGE',fg = 'white',bg='#00CE96',padx = 10,pady = 10, command = save_image_command).place(x=500,y=600)

show_original = tk.Button(canvas,text = 'SHOW ORIGINAL',fg = 'white',bg='#00CE96',padx = 10,pady = 10, command = show_original_command).place(x=5,y=505)

close_window = tk.Button(canvas,text = 'CLOSE WINDOW',fg = 'white',bg='#00CE96',padx = 5,pady = 10, command = close_window_command).place(x=490,y=5)

root.mainloop()
