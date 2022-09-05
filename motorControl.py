import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

kit.servo[15].actuation_range = 270
kit.servo[14].actuation_range = 270
kit.servo[12].actuation_range = 270

"""kit.servo[15].angle = 0
time.sleep(2)
kit.servo[15].angle = 10
time.sleep(2)
kit.servo[15].angle = 30
time.sleep(2)
kit.servo[15].angle = 50

kit.servo[14].angle = 80
time.sleep(1)
kit.servo[14].angle = 70
time.sleep(1)
kit.servo[14].angle = 60
time.sleep(1)
kit.servo[14].angle = 50
time.sleep(1)
kit.servo[14].angle = 40
time.sleep(1)
kit.servo[14].angle = 50
time.sleep(1)
kit.servo[14].angle = 60
time.sleep(1)
kit.servo[14].angle = 70
time.sleep(1)
kit.servo[14].angle = 80
"""
kit.servo[13].angle = 180
time.sleep(1)
kit.servo[13].angle = 150
time.sleep(1)
kit.servo[13].angle = 120
time.sleep(1)
kit.servo[13].angle = 90
time.sleep(1)
kit.servo[13].angle = 60
time.sleep(1)
kit.servo[13].angle = 30
time.sleep(1)
kit.servo[13].angle = 0
time.sleep(1)
kit.servo[13].angle = 30
time.sleep(1)
kit.servo[13].angle = 60
