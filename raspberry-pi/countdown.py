#type: ignore
from time import sleep               #imports sleep

for x in range (10,0,-1):            #count down from ten to zero by -1s
    print (x)                        #print the value
    sleep(1)
print ('Liftoff!')                   #after countdown is done, print liftoff