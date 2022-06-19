import speechToText as STT

import RPi.GPIO as GPIO
import numpy
import cv2
import time

GPIO.setmode(GPIO.BCM)
GPIOPin = 18
GPIO.setwarnings(False)
GPIO.setup(GPIOPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
ledPin = 23
GPIO.setup(ledPin, GPIO.OUT)

import motorControlFuncs as motor

face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt.xml')
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_BUFFERSIZE,1)

print("Welcome to the Dum-E Program")

currTime = time.time()
buttonPress = 1

motor.moveToDefaultLoc()
currTopPos = 50
currMidPos = 80
timeSinceCall = time.time()
currMode = 'Camera Mode'

while True:
    currButton = GPIO.input(GPIOPin)
    if(not(currButton) and time.time() - currTime > 2):
        currTime = time.time()
        buttonPress += 1
        if(currMode == "Camera Mode"):
            currMode = "Speech Mode"
        else:
            currMode = 'Camera Mode'
        print(currMode)

    if buttonPress % 2:
        faceCenter = [-1,-1]
	# Capture frame-by-frame
        coords = (0,0,0,0)
        ret, frame = cap.read()
        frame = cv2.flip(frame, -1)
        avgColor = frame.mean(axis=0).mean(axis=0)
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
        if faceCenter != [-1,-1]:
            if (faceCenter[1] < 100):
                currTopPos, currMidPos = motor.moveUp(currTopPos, currMidPos)
                print('move up', currTopPos)
            elif (faceCenter[1] > 160):
                currTopPos, currMidPos = motor.moveDown(currTopPos, currMidPos)
                print('move down', currTopPos)
            else:
                print('dont move')

            if (faceCenter[0] > 255):
                print('move left')
                timeSinceCall = motor.moveHorizontal('left', timeSinceCall)
            elif (faceCenter[0] < 140):
                timeSinceCall = motor.moveHorizontal('right', timeSinceCall) 
            else: 
                timeSinceCall = motor.moveHorizontal('stop', timeSinceCall)

        else:
            timeSinceCall = motor.moveHorizontal('stop', timeSinceCall)
            print('no face detected')

        avgAvgColor = avgColor.mean()
        if avgAvgColor <= 70:
            GPIO.output(ledPin,1)
            print(avgAvgColor, 'on')
        else:
            GPIO.output(ledPin,0)
            print(avgAvgColor, 'off')

        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
    else:
        motor.moveHorizontal('stop', timeSinceCall)
        while(1):
            audio1 = STT.listen1() 
            text = STT.voice(audio1)
            response, action = STT.respond(text)
