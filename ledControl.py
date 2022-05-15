from board import SCL, SDA
import busio
from adafruit_pca9685 import PCA9685
import time

i2c_bus=busio.I2C(SCL, SDA)

pca = PCA9685(i2c_bus)
pca.frequency=60

while True:
    for num in range(0,32767,50): 
        pca.channels[13].duty_cycle=num
        pca.channels[14].duty_cycle=num
        pca.channels[15].duty_cycle=num
        time.sleep(.0001)
    
    for num in range(32767,1,-50): 
        pca.channels[13].duty_cycle=num
        pca.channels[14].duty_cycle=num
        pca.channels[15].duty_cycle=num
        time.sleep(.0001)
