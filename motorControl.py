import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

#kit.servo[15].actuation_range = 270
#kit.servo[14].actuation_range = 270
kit.servo[13].actuation_range = 90

"""kit.servo[15].angle = 0
time.sleep(2)
kit.servo[15].angle = 10
time.sleep(2)
kit.servo[15].angle = 30
time.sleep(2)
kit.servo[15].angle = 50

kit.servo[14].angle = 90
time.sleep(2)
kit.servo[14].angle = 60
time.sleep(2)
kit.servo[14].angle = 40
time.sleep(2)
kit.servo[14].angle = 60
time.sleep(2)
kit.servo[14].angle = 90
"""

# for bottom motor (port 13), 40-45 is stop, above that is ccw, below that is cw
# farther away from 45 is increasing speed (ex. 30 and 55 are equal)
kit.servo[13].angle = 40
kit.servo[13].angle = 30
time.sleep(2)
kit.servo[13].angle = 55
time.sleep(2)
kit.servo[13].angle = 40
