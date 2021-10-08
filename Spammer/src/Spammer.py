import pyautogui
import time
# section below gives you 5 seconds after running the program
# to switch to the desired application where the message will be typed
time.sleep(5)
# change the contents of "message.txt" to send whatever message you wanna send
message = open('message.txt', 'r')
for line in message:
    for word in line.split():
        # changing the parameter below to "line" will type every line in the .txt
        # file
        pyautogui.typewrite(line)
        pyautogui.press('enter')








