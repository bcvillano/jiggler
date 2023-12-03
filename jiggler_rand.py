'''
Based off of jiggler.py, but incorporates randomness for mouse movements and movement intervals
'''

import pyautogui
import time
import random

def randomize_time(minimum=1,maximum=60):
    if type(minimum) == int and type(maximum) == int:
        seconds = random.randint(minimum,maximum) #Determines random amount of seconds between minimum and maximum arguments
        return seconds
    else:
        seconds = random.uniform(minimum,maximum)
        return seconds

def plus_minus():
    pm = random.randint(0,1)
    if pm == 0:
        return "PLUS"
    else:
        return "MINUS"

def jiggle():
    originalMouseX, originalMouseY = pyautogui.position() # Gets current mouse position
    sign_x = plus_minus() #Determines if mouse moves in positive or negative direction for x dimension
    sign_y = plus_minus() #Determines if mouse moves in positive or negative direction for y dimension
    x = random.randint(1,100) #Determines how far mouse moves in x dimension
    y = random.randint(1,100) #Determines how far mouse moves in y dimension
    if sign_x == "PLUS":
        if sign_y == "PLUS":
            pyautogui.moveTo(originalMouseX+x,originalMouseY+y)
        else:
            pyautogui.moveTo(originalMouseX+x,originalMouseY-y)
    else:
        if sign_y == "PLUS":
            pyautogui.moveTo(originalMouseX-x,originalMouseY+y)
        else:
            pyautogui.moveTo(originalMouseX-x,originalMouseY+y)
    secs_to_wait = randomize_time(0.1,0.5) #determines random time to wait between 0.1 and 0.5 seconds before moving back
    time.sleep(secs_to_wait)
    pyautogui.moveTo(originalMouseX,originalMouseY)   

def main():
    while True: #Program runs until manually stopped
        jiggle()
        seconds = randomize_time()
        time.sleep(seconds) #Waits for seconds amount of time before running next iteration of loop
        
if __name__ == "__main__":
    main()