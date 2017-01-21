import cv2
# import numpy as np

cam = cv2.VideoCapture(1)
rgb = cv2.VideoCapture(0)
facec = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
print facec

while True:
    ret, frame = cam.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, fr = rgb.read()
    
    gray = cv2.cvtColor(fr, cv2.COLOR_BGR2GRAY)
    # print gray.shape
    faces = facec.detectMultiScale(gray, 1.3, 5)
    
    for (x,y,w,h) in faces:
    	cv2.rectangle(fr,(x,y),(x+w,y+h),(255,0,0),2)
    
    cv2.imshow('rgb', fr)
    cv2.imshow('cam', frame)
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
