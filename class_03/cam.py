import cv2
# import numpy as np

rgb = cv2.VideoCapture(0)
facec = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# print facec
font = cv2.FONT_HERSHEY_SIMPLEX

def recognize_face(im):
    im = cv2.resize(im, (100, 100))
    im = im.flatten()

    return "Shubham" #get_name(im)

while True:
    _, fr = rgb.read()
    
    gray = cv2.cvtColor(fr, cv2.COLOR_BGR2GRAY)
    # print gray.shape
    faces = facec.detectMultiScale(gray, 1.3, 5)
    
    for (x,y,w,h) in faces:
        fc = fr[x:x+w, y:y+h, :]
        out = recognize_face(fc)
        cv2.putText(fr, out, (x, y), font, 1, (255, 255, 0), 2)
    	cv2.rectangle(fr,(x,y),(x+w,y+h),(255,0,0),2)
    
    cv2.imshow('rgb', fr)
    cv2.imshow('gray', gray)
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
