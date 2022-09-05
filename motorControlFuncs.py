import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

def moveUp(currPosTop, currPosBot, extreme = False):
    moveUnit = 2
    if extreme:
        moveUnit = 8

    if currPosTop >= 4:
        kit.servo[15].angle = currPosTop - moveUnit
        currPosTop -= moveUnit
    if currPosBot <= 90:
        kit.servo[14].angle = currPosBot + moveUnit / 2
        currPosBot += moveUnit / 2
    return currPosTop, currPosBot

def moveDown(currPosTop, currPosBot, extreme = False):
    moveUnit = 2
    if extreme:
        moveUnit = 8

    if currPosTop <= 60:
        kit.servo[15].angle = currPosTop + moveUnit
        currPosTop += moveUnit
    if currPosBot >= 30:
        kit.servo[14].angle = currPosBot - moveUnit / 2
        currPosBot -= moveUnit / 2
    return currPosTop, currPosBot

def moveRight(currPos, extreme = False):
    moveUnit = 2
    if extreme:
        moveUnit = 16

    if currPos <= 178:
        kit.servo[13].angle = currPos + moveUnit
        currPos += moveUnit
    return currPos

def moveLeft(currPos, extreme = False):
    moveUnit = 2
    if extreme:
        moveUnit = 16

    if currPos >= 2:
        kit.servo[13].angle = currPos - moveUnit
        currPos -= moveUnit
    return currPos

def wakeUp():
    kit.servo[13].angle = 90
    currPosTop = 4;
    while currPosTop < 50: 
        kit.servo[15].angle = currPosTop + 2
        currPosTop += 2
        time.sleep(.1)

def sleep(currPosTop, currPosBot):
    while currPosTop > 4:
        kit.servo[15].angle = currPosTop - 2
        currPosTop -= 2
        time.sleep(.1)
    #print(currPosBot)
    if currPosBot > 65:
        while currPosBot > 65:
            kit.servo[14].angle = currPosBot - 1
            currPosBot -= 1
            time.sleep(.2)
    else: 
        while currPosBot < 65:
            kit.servo[14].angle = currPosBot + 1
            currPosBot += 1
            time.sleep(.2)
        
