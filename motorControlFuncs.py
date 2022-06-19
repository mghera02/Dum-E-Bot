import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

kit.servo[15].actuation_range = 270
kit.servo[14].actuation_range = 270
kit.servo[13].actuation_range = 90

def moveUp(currPosTop, currPosBot):
    if currPosTop >= 4:
        kit.servo[15].angle = currPosTop - 4
        currPosTop -= 4
    if currPosBot <= 90:
        kit.servo[14].angle = currPosBot + 2
        currPosBot += 2
    return currPosTop, currPosBot

def moveDown(currPosTop, currPosBot):
    if currPosTop <= 60:
        kit.servo[15].angle = currPosTop + 4
        currPosTop += 4
    if currPosBot >= 40:
        kit.servo[14].angle = currPosBot - 2
        currPosBot -= 2
    return currPosTop, currPosBot

def moveHorizontal(direct, timeSinceCall):
    if direct != 'stop':
        if timeSinceCall - time.time() < .005:
            if direct == 'right':
                kit.servo[13].angle = 48
            else:
                kit.servo[13].angle = 36
        else:
            kit.servo[13].angle = 40
            timeSinceCall = time.time()
    else:
        kit.servo[13].angle = 40
    return timeSinceCall
        
def moveToDefaultLoc():
    kit.servo[15].angle = 50
    kit.servo[14].angle = 80
    kit.servo[13].angle = 40
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

# for bottom motor (port 13), 40-45 is stop, above that is ccw, below that is cw
# farther away from 45 is increasing speed (ex. 30 and 55 are equal)
kit.servo[13].angle = 40
kit.servo[13].angle = 30
time.sleep(2)
kit.servo[13].angle = 55
time.sleep(1.5)
kit.servo[13].angle = 40
"""
