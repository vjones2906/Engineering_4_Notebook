#type: ignore
import pwmio
from adafruit_motor import servo
import digitalio
import board
from time import sleep                                                      #importing libs

Rled = digitalio.DigitalInOut(board.GP0)
Rled.direction = digitalio.Direction.OUTPUT                                 #declaring red led as an output in pin 0

Gled = digitalio.DigitalInOut(board.GP1)
Gled.direction = digitalio.Direction.OUTPUT                                 #declaring green led as an output in pin 1

button = digitalio.DigitalInOut(board.GP16)
button.direction = digitalio.Direction.INPUT                                #declaring button as an input in pin 16
button.pull = digitalio.Pull.UP                                             #making the button a pull down

pwm_servo = pwmio.PWMOut(board.GP20, duty_cycle=2 ** 15, frequency=50)      #tells pin 20 it will control a servo
servo1 = servo.Servo(pwm_servo, min_pulse=500, max_pulse=2500)

abort = False
launch = False
servo1.angle = 0

while True:
    if button.value == False:                           #if the button is pressed, do:
        for x in range (10,0,-1):   
            if abort == False:                    #count down from ten to zero by -1s
                print (x)                                   #printing value
                Rled.value = True
                for i in range (0,30):
                    if x <= 3:
                        servo1.angle = servo1.angle + 1
                    sleep(1/60)                           #this function turns an led on or off
                Rled.value = False                         
                for i in range (0,30):
                    if x <= 3:
                        servo1.angle = servo1.angle + 1
                    sleep(1/60)                
                if button.value == False:                           #if the button is pressed, do:
                    abort = True
                if x == 1:
                    launch = True
        if launch == True:
            print ('Liftoff!')                              #after countdown is done, print liftoff
            Gled.value = True                               
            sleep(3)
            Gled.value = False
        if abort == True:    
            print('ABORT!')
            Rled.value = True
            sleep(3)
            Rled.value = False      
    abort = False
    launch = False
    servo1.angle = 0         
