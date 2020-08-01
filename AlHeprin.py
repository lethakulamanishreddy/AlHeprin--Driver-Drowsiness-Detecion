'''
                     AlHeprin - Drowsiness detection system

      Inspired from a person named "Al Heprin" Who never slept in his life time

      Team SAHARA developed AlHeprin which will alert driver when found sleepy
                  and can record vlogs or travel dairies.

Developed by : Team SAHARA
code contributed by: MANISH REDDY LETHAKULA

'''   



import numpy
from playsound import playsound
import time
import cv2
from tkinter import *
root=Tk()
root.geometry('500x570')
root.resizable(width=False, height=False)
root.title('Al Heprin')
root.config(background='light blue')
label = Label(root, text="Al Heprin",bg='light blue',font=('helvetica 30 bold'))
label.pack(side=TOP)
filename = PhotoImage(file="alheprin.png")
background_label = Label(root,image=filename)
background_label.pack(side=TOP)
statusbar=Label(root,width=50,text="A Project by Team SAHARA",font=("arial",13,"bold"),bg="black",fg="white",relief=SUNKEN)
statusbar.place(x=0,y=550)


def destroy():
   root.destroy()

def vlog():
   capture =cv2.VideoCapture(0)
   fourcc=cv2.VideoWriter_fourcc(*'XVID') 
   op=cv2.VideoWriter('Sample1.mp4',fourcc,11.0,(640,480))
   while True:
      ret,frame=capture.read()
      gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
      cv2.imshow('frame',frame)
      op.write(frame)
      k = cv2.waitKey(30) & 0xff
      if k==27:
          break
   op.release()
   capture.release()
   cv2.destroyAllWindows()   

      
def detec():
   capture =cv2.VideoCapture(0)
   face_cascade = cv2.CascadeClassifier('lbpcascade_frontalface.xml')
   eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
   blink_cascade = cv2.CascadeClassifier('CustomBlinkCascade.xml')
   fourcc=cv2.VideoWriter_fourcc(*'XVID') 
   op=cv2.VideoWriter('Sample2.mp4',fourcc,11.0,(640,480))
   while True:
      ret, frame = capture.read()
      gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
      faces = face_cascade.detectMultiScale(gray)

      for (x,y,w,h) in faces:
         font = cv2.FONT_HERSHEY_COMPLEX
         #cv2.putText(frame,'Face',(x+w,y+h),font,1,(250,250,250),2,cv2.LINE_AA)
         cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
         roi_gray = gray[y:y+h, x:x+w]
         roi_color = frame[y:y+h, x:x+w]

         eyes = eye_cascade.detectMultiScale(roi_gray)
         for(ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
         blink = blink_cascade.detectMultiScale(roi_gray)
         for(eyx,eyy,eyw,eyh) in blink:
            cv2.rectangle(roi_color,(eyx,eyy),(eyx+eyw,eyy+eyh),(255,255,0),2)
            playsound('alert.wav')
      cv2.imshow('AlHeprin',frame)
      op.write(frame)
      k = cv2.waitKey(30) & 0xff
      if k==27:
          break
   op.release()  
   capture.release()
   cv2.destroyAllWindows()

b1=Button(root,padx=5,pady=5,width=12,bg='white',fg='black',relief=GROOVE,command=vlog,text='Record Vlog',font=('helvetica 15 bold'),activebackground='light green')
b1.place(x=330,y=200)
b2=Button(root,padx=5,pady=5,width=12,bg='white',fg='black',relief=GROOVE,command=detec,text='Start Detection',font=('helvetica 15 bold'),activebackground='light green')
b2.place(x=330,y=325)
b3=Button(root,padx=5,pady=5,width=12,bg='white',fg='black',relief=GROOVE,text='EXIT',command=destroy,font=('helvetica 15 bold'),activebackground='red')
b3.place(x=330,y=450)


root.mainloop()

