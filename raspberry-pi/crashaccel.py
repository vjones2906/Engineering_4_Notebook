#type: ignore
import adafruit_mpu6050
import  busio
import board
from time import sleep                #imports required libraries 

sda_pin = board.GP14                  #defining sda pin
scl_pin = board.GP15                  #defining the scl pin
i2c = busio.I2C(scl_pin, sda_pin)     #creating the i2c from the pins
mpu = adafruit_mpu6050.MPU6050(i2c)   #putting them all together to make the accelerometer 

while True:
    print("x:", mpu.acceleration[0])
    print("y:", mpu.acceleration[1])
    print("z:", mpu.acceleration[2])  #printing respective x, y, and z values
    print("")                         #printing new line
    sleep(1)                          #sleep for 1 second 