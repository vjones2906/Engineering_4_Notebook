# Engineering_4_Notebook

&nbsp;

## Table of Contents
* [Launch_1-Countdown](#launch_1-countdown)
* [Launch_1-Lights](#launch_2-lights)
* [Launch_3-Button](#launch_1-button)
* [Onshape_Assignment_Template](#onshape_assignment_template)

&nbsp;

## Launch_1-Countdown

### Assignment Description

The purpose of this assingment is to create a countdown from 10 to 0 using a for loop. 

### Evidence 

![countdowngif](images/countdown.gif)

### Wiring

No wiring for this assignment

### Code

``` python
from time import sleep               #imports sleep

for x in range (10,0,-1):            #count down from ten to zero by -1s
    print (x)                        #print the value
    sleep(1)
print ('Liftoff!')                   #after countdown is done, print liftoff
```

### Reflection

This assignment was fairly basic. There are many different ways to do it, but the way I settled on was the fastest way just using a for loop but setting the bounds and the interval after declaring it. I learned that there is always a faster, more compact way to write code and try to figure it out as opposed to the long way.

&nbsp;

## Launch_2-Lights

### Assignment Description

The purpose of this assingment is to create a countdown from 10 to 0 turning on the red light for every second counting down, then turning on the green light upon completion  

### Evidence 

![countdownlightsgif](images/countdowlights.gif)

### Wiring

No wiring for this assignment

### Code

``` python
import digitalio
import board
from time import sleep                          #importing libs

Rled = digitalio.DigitalInOut(board.GP0)
Rled.direction = digitalio.Direction.OUTPUT     #declaring red led as an output in pin 0

Gled = digitalio.DigitalInOut(board.GP1)
Gled.direction = digitalio.Direction.OUTPUT     #declaring green led as an output in pin 1

for x in range (10,0,-1):                       #count down from ten to zero by -1s
    print (x)                                   #printing value
    Rled.value = True                           #turing red led on
    sleep(.5)                                   #light on for half a second
    Rled.value = False                          #turing red led off
    sleep(.5)                                   #completing the second
print ('Liftoff!')                              #after countdown is done, print liftoff
Gled.value = True                               #turing green led on
sleep(3)

```

### Reflection

For this assignment we just had to turn on lights along with the coundown. The trickiest part was figruing out how long to sleep and when to turn on the lights. I split it up .5 and .5 so it is still a full second but the red light only comes on for half a second. I also remembered that once the script ends everything turns off so the green light doesn't stay on forever. To counter this I just put a sleep at the end. 

&nbsp;

## Launch_3-Button

### Assignment Description

The purpose of this assingment is to initiate a countdown from 10 to 0 using a button with a blinking red light for each second and a static green light once the countdown is finished. 

### Evidence 

![countdownbuttongif](images/countdownbutton.gif)

### Wiring

No wiring for this assignment

### Code

``` python
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
```

### Reflection

This assingment was confusing at first becuase I forgot how button pullups and pulldowns worked. Once I fully read Mr. Miller's assignment I was able to understand why my button wasn't working. Becuase it was connected to ground and not power, it needed to be a pullup and the if loop condition should have been False with two equal signs. 

&nbsp;

## Onshape_Assignment_Template

### Assignment Description

Write your assignment description here. What is the purpose of this assignment? It should be at least a few sentences.

### Part Link 

[Create a link to your Onshape document](https://cvilleschools.onshape.com/documents/003e413cee57f7ccccaa15c2/w/ea71050bb283bf3bf088c96c/e/c85ae532263d3b551e1795d0?renderMode=0&uiState=62d9b9d7883c4f335ec42021). Don't forget to turn on link sharing in your Onshape document so that others can see it. 

### Part Image

Take a nice screenshot of your Onshape document. 

### Reflection

What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience? Your goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person. Think about your audience for this one, which may be "future you" (when you realize you need some of this code in three months), me, or your college admission committee!

&nbsp;

## Media Test

Your readme will have various images and gifs on it. Upload a test image and test gif to make sure you've got the process figured out. Pick whatever image and gif you want!

### Test Link
[Google](https://en.wikipedia.org/wiki/Minions:_The_Rise_of_Gru?scrlybrkr=e146fde2)      
### Test Image
![Minons!](images/minons.png)
### Test GIF
![More Minons!](images/minions.gif)
