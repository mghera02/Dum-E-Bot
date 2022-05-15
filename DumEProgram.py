import speechToText as STT

import RPi.GPIO as GPIO
import numpy
import cv2
import time

GPIO.setmode(GPIO.BOARD)
GPIOPin = 16
GPIO.setup(GPIOPin, GPIO.IN, pull_up_down = GPIO.PUD_UP)

import motorControl as motor

face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt.xml')
cap = cv2.VideoCapture(1)

print("Welcome to the Dum-E Program")

currTime = time.time()
buttonPress = 1

while True:
    currButton = GPIO.input(GPIOPin)
    if(not(currButton) and time.time() - currTime > 2):
        currTime = time.time()
        buttonPress += 1
    
    if buttonPress % 2:
        faceCenter = [0,0]
	# Capture frame-by-frame
        coords = (0,0,0,0)
        ret, frame = cap.read()
        frame = cv2.flip(frame, -1)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 5)
        for (x, y, w, h) in faces:
                coords = (x, y, w, h) 
                roi_gray = gray[y:y + h, x:x + w]
                roi_color = frame[y:y + h, x:x + w]
                
                faceCenter = [(x+w)/2, (y+h)/2]

                img_item = "my-image.png"
                cv2.imwrite(img_item, roi_gray)

                color = (0,0,255)
                stroke = 1
                width = x + w
                height = y + h
                cv2.rectangle(frame, (x, y), (width, height), color)

    	# Display the resulting frame
        cv2.imshow('frame', frame)
        print(faceCenter)
        if (faceCenter[1] < 170):
            motor.moveTopUp()
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
        print("not pressed")
    else:
        print("speech mode")
#STT.speechToText()
