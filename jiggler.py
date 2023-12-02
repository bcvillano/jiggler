import pyautogui
import time

SECONDS = 10 #variable with how many seconds between executing the program (edit this to change how often it jiggles)

def jiggle():
    originalMouseX, originalMouseY = pyautogui.position() # Gets current mouse position
    pyautogui.moveTo(originalMouseX+10,originalMouseY)
    time.sleep(0.2) #waits
    pyautogui.moveTo(originalMouseX,originalMouseY)

    

def main():
    while True: #Program runs until manually stopped
        jiggle()
        time.sleep(SECONDS) #Waits for SECONDS constant amount of seconds before doing next iteration of loop
        
if __name__ == "__main__":
    main()