#type: ignore
import board  
from time import sleep
import digitalio

led = digitalio.DigitalInOut(board.GP1)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True
    sleep(1)
    led.value = False
    sleep(1) 