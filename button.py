import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

buttonPin = 18
GPIO.setwarnings(False)
GPIO.setup(buttonPin, GPIO.IN,pull_up_down=GPIO.PUD_UP)
#GPIO.setup(buttonPin, GPIO.OUT)
while True:
    buttonState = GPIO.input(buttonPin)
    print(buttonState)
    '''GPIO.output(buttonPin,1)
    time.sleep(1)
    GPIO.output(buttonPin,0)
    time.sleep(1)'''

