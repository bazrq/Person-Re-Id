import numpy as np

import cv2

import os



detector= cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0) #video source

while(True):

    ret, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = detector.detectMultiScale(gray, 1.3, 5)

    count = 1 
    numbs=[count]
    for (x,y,w,h) in faces:
        cropped = img[ y : y+h, x : x+w ]
        if (count==numbs):
            cv2.imwrite("crop_faces/cropped_face" + str(count+1) + ".png", cropped)
            count=count+1
            numbs.append(count)
            cv2.imshow("face"+str(count), cropped); # show an image of each face
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2) # create bounding box around face
        else:
            cv2.imwrite("crop_faces/cropped_face" + str(count) + ".png", cropped)
            count=count+1
            numbs.append(count)
            cv2.imshow("face"+str(count), cropped); # show an image of each face
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2) # create bounding box around face


    print(numbs)   
    cv2.imshow('frame',img)

    if cv2.waitKey(1) & 0xFF == ord('q'):

        break

cap.release()

cv2.destroyAllWindows()