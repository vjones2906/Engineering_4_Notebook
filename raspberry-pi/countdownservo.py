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
servo1 = servo.Servo(pwm_servo, min_pulse=500, max_pulse=2500)              #setting buonds for servo


while True:
    if button.value == False:                           #if the button is pressed, do:
        for x in range (10,0,-1):                       #count down from ten to zero by -1s
            print (x)                                   #printing value
            Rled.value = True                           #this function turns an led on or off
            sleep(.5)                                   #light on for just half a second
            Rled.value = False                         
            sleep(.5)                                   #completing the second for the loop
        print ('Liftoff!')                              #after countdown is done, print liftoff
        Gled.value = True                               
        servo1.angle = 180                              #turn the servo 180 degrees
        sleep(3)
        servo1.angle = 0                                #reset servo
        Gled.value = False                      
