#type: ignore
import board  
from time import sleep
import digitalio

countdown = 10 
for x in range (10):
    print countdown
    countdown  = countdown - 1