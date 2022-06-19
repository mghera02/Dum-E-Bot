import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

ledPin = 23
GPIO.setwarnings(False)
GPIO.setup(ledPin, GPIO.OUT)
while True:
    GPIO.output(ledPin,1)
    time.sleep(1)
    GPIO.output(ledPin,0)
    time.sleep(1)

