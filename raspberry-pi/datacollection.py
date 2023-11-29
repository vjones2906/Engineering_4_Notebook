#type: ignore
import digitalio
import adafruit_mpu6050
import  busio
import board
from digitalio import DigitalInOut,Direction,Pull
from time import sleep, monotonic                      #imports required libraries 

led = digitalio.DigitalInOut(board.GP1)                #telling the pico that there is something on pin 0
led.direction = digitalio.Direction.OUTPUT             #declaring  led as an output in pin 0

ledBoard = digitalio.DigitalInOut(board.LED)        
ledBoard.direction = digitalio.Direction.OUTPUT        #declaring onboard led

sda_pin = board.GP14                                   #defining sda pin
scl_pin = board.GP15                                   #defining the scl pin
i2c = busio.I2C(scl_pin, sda_pin)                      #creating the i2c from the pins
mpu = adafruit_mpu6050.MPU6050(i2c)                    #putting them all together to make the accelerometer 

tilt = 0                                               #defining tilt

with open("/data.csv", "a") as datalog:                #write to this file
    while True: 
        ledBoard.value = True
        sleep(0.1)
        ledBoard.value = False                         #blink onboard if working
        datalog.write(f"{monotonic()},{mpu.acceleration[0]},{mpu.acceleration[2]},{mpu.acceleration[2]},{tilt}\n")  #writing acceleration data
        datalog.flush()
        sleep(.9)
        if mpu.acceleration[0] >= 9 or mpu.acceleration[1] >= 9:                                                    #if tilted turn on led
            led.value = True #led on
            tilt = 1
        elif mpu.acceleration[0] <= -9 or mpu.acceleration[1] <= -9:                                                #if tilted other way turn on led
            led.value = True
            tilt = 0
        else: led.value = False                                                                                     #else led false