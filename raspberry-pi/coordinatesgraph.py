#credit to afton for the math and functions portion
#type: ignore

from time import sleep
import adafruit_displayio_ssd1306
import displayio
import board
import busio                                                                   #importing libs for OLED
from adafruit_display_shapes.line import Line
from adafruit_display_shapes.circle import Circle
from adafruit_display_shapes.triangle import Triangle                          #importing tools requied to make shapes on the OLED

x = 0
y = 1

displayio.release_displays()
sda_pin = board.GP14                                                           #defining sda pin
scl_pin = board.GP15                                                           #defining the scl pin
i2c = busio.I2C(scl_pin, sda_pin) 
display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=board.GP20) #declaring the OLED in this address  
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)
splash = displayio.Group()                                                     #getting OLED ready

c1 = [0,0] #creates coordinates 
c2 = [0,0]
c3 = [0,0]

def area(r1,r2,r3): #area function
    global c1
    global c2
    global c3
    try:                    # Coordinate 1
        c1 = [int(o) for o in r1.split(",")] # Splits raw string: "1,2" into a string array: "1", "2", and turns each value into an int: 1,2
    except:
        print("Coordinate 1 Invalid, please enter in 'x,y' format")
        pass
    finally:

        try:                # Coordinate 2
            c2 = [int(o) for o in r2.split(",")]
        except:
            print("Coordinate 2 Invalid, please enter in 'x,y' format")
            pass
        finally:

            try:            # Coordinate 3
                c3 = [int(o) for o in r3.split(",")]
            except:
                print("Coordinate 3 Invalid, please enter in 'x,y' format")
                pass
            finally:
                A = (1/2)*abs(c1[x]*(c2[y] - c3[y]) + c2[x]*(c3[y] - c1[y]) + c3[x]*(c1[y] - c2[y])) # Easy plug and play equation for a triangle's area
                return A



while True:
    r1 = input("Coordinate 1: ")                                                                                                                #asking for inputs
    r2 = input("Coordinate 2: ")
    r3 = input("Coordinate 3: ")
    print('The area of the triangle with vertices ('+ str(r1)+ '), ('+ str(r2)+ '), ('+ str(r3)+ ') is '+ str(area(r1,r2,r3)) +' square km')    #returning answer

    splash = displayio.Group()
    hline = Line(64,0,64,64, color=0xFFFF00)                                                               #making x, y, and the origin on the OLED graph
    vline = Line(0,32,128,32, color=0xFFFF00)
    circle = Circle(64,32,2, outline=0xFFFF00)
    triangle = Triangle(c1[x]+64,-c1[y]+32,c2[x]+64,-c2[y]+32,c3[x]+64,-c3[y]+32, outline=0xFFFF00)        #displaying the triangle based on input on the OLED graph
    splash.append(hline)
    splash.append(vline)
    splash.append(circle)
    splash.append(triangle)                                                                                #priming shapes and lines
    display.show(splash)                                                                                   #displaying everything on the OLED graph