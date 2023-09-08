#type: ignore
import digitalio
import board
from time import sleep                          #importing libs

Rled = digitalio.DigitalInOut(board.GP0)
Rled.direction = digitalio.Direction.OUTPUT     #declaring red led as an output in pin 0

Gled = digitalio.DigitalInOut(board.GP1)
Gled.direction = digitalio.Direction.OUTPUT     #declaring green led as an output in pin 1

button = digitalio.DigitalInOut(board.GP16)
button.direction = digitalio.Direction.INPUT     #declaring button as an input in pin 16
button.pull = digitalio.Pull.UP                  #making the button a pull down

while True:
    if button.value == False:                           #if the button is pressed, do:
        for x in range (10,0,-1):                       #count down from ten to zero by -1s
            print (x)                                   #printing value
            Rled.value = True                           #turing red led on
            sleep(.5)                                   #light on for half a second
            Rled.value = False                          #turing red led off
            sleep(.5)                                   #completing the second
        print ('Liftoff!')                              #after countdown is done, print liftoff
        Gled.value = True                               #turing green led on
        sleep(3)
        Gled.value = False
