#type: ignore
print("Enter morse code message or -q to quit")
message = ""
character = 0
MORSE_CODE = { 'A':'.-', 'B':'-...',
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
    usrInput = input("Your message: ").upper() # Takes input from user and capitalizes it
    if "-Q" in usrInput: # Checks if user would like to exit
        exit()
    try:
        for character in range(len(usrInput)): # Iterates through each character of the input text
            message += MORSE_CODE[usrInput[character]] + " " # Translates and adds a space
    except:
        message = ("Can't translate: " + str({usrInput[character]})) # Tells you if a character you typed was invalid
    print(message)
    message = ("")

