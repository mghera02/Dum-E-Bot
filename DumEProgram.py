import speechToText as STT
#import Adafruit_Python_PCA9685.simpletest as mc
#import faces

import RPi.GPIO as GPIO
import numpy
import cv2
import time

GPIO.setmode(GPIO.BOARD)
GPIOPin = 16
GPIO.setup(GPIOPin, GPIO.IN, pull_up_down = GPIO.PUD_UP)

face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt.xml')
cap = cv2.VideoCapture(0)

print("Welcome to the Dum-E Program")

#mc.moveMotor()


while True:
    if GPIO.input(GPIOPin):
        currentTime = time.time()

    if time.time() - currentTime > 1 and GPIO.input(GPIOPin):
	# Capture frame-by-frame
        coords = (0,0,0,0)
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 5)
        for (x, y, w, h) in faces:
                coords = (x, y, w, h) 
                roi_gray = gray[y:y + h, x:x + w]
                roi_color = frame[y:y + h, x:x + w]

                img_item = "my-image.png"
                cv2.imwrite(img_item, roi_gray)

                color = (0,0,255)
                stroke = 1
                width = x + w
                height = y + h
                cv2.rectangle(frame, (x, y), (width, height), color)

    	# Display the resulting frame
        cv2.imshow('frame', frame)
        x,y,w,h = coords
        print(x,y,w,h)
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
        print("not pressed")
    elif(time.time() - currentTime > 1 and not GPIO.input(GPIOPin)):
        print("speech mode")
        #STT.speechToText()
