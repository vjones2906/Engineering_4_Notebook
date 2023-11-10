#type: ignore
import digitalio
import board
from time import sleep                      #imports required libraries 

led = digitalio.DigitalInOut(board.GP0)     #telling the pico that there is something on pin 0
led.direction = digitalio.Direction.OUTPUT  #declaring  led as an output in pin 0

print("Enter morse code message or -q to quit")                         #prompts user
message = ""    
character = 0                                                           #setting values

modifier = 0.25
dot_time = 1*modifier
dash_time = 3*modifier
between_taps = 1*modifier
between_letters = 3*modifier
between_words = 7*modifier                                              #setting timing values

MORSE_CODE = { 'A':'.-', 'B':'-...',                                    #defining letters 
    'C':'-.-.', 'D':'-..', 'E':'.',
    'F':'..-.', 'G':'--.', 'H':'....',
    'I':'..', 'J':'.---', 'K':'-.-',
    'L':'.-..', 'M':'--', 'N':'-.',
    'O':'---', 'P':'.--.', 'Q':'--.-',
    'R':'.-.', 'S':'...', 'T':'-',
    'U':'..-', 'V':'...-', 'W':'.--',
    'X':'-..-', 'Y':'-.--', 'Z':'--..',
    '1':'.----', '2':'..---', '3':'...--',
    '4':'....-', '5':'.....', '6':'-....',
    '7':'--...', '8':'---..', '9':'----.',
    '0':'-----', ', ':'--..--', '.':'.-.-.-',
    '?':'..--..', '/':'-..-.', '-':'-....-',
    '(':'-.--.', ')':'-.--.-', ' ':'/'}

while True:
    usrInput = input("Your message: ").upper()                           #Takes input from user and capitalizes it
    if "-Q" in usrInput:                                                 #Checks if user would like to exit
        exit()
    try:
        for character in range(len(usrInput)):                           #Iterates through each character of the input text
            message += MORSE_CODE[usrInput[character]] + " "             #Translates and adds a space
    except:
        message = ("Can't translate: " + str({usrInput[character]}))     #Tells you if a character you typed was invalid

    print(message)
    for character in message: 
        if character == ".":                                             #if character is a dot, do a short blink
            led.value = True
            sleep(dot_time)
            led.value = False
        if character == "-":                                             #if character is a dash, do a long blink
            led.value = True
            sleep(dash_time)
            led.value = False           
        if character == " ":                                             #if character is between letters, do a “between letters” pause
            sleep(between_letters)
        if character == "/":                                             #if it's between words, do a “between words” pause
            sleep(between_words)
        sleep(between_taps)
    message = ("")                                                       #reset message