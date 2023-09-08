#type: ignore
from time import sleep                          #importing libs

for x in range (10,0,-1):                       #count down from ten to zero by -1s
    print (x)                                   #printing value
    sleep(1)                                    #wait a second
print ('Liftoff!')                              #after countdown is done, print liftoff
