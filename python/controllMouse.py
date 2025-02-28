# from pynput import keyboard
# from pynput.mouse import Controller, Button
# from pynput import mouse
# from pynput.mouse import Listener
import time
# import random

from pynput import keyboard
from pynput.mouse import Controller, Button, Listener
import random

# Define the key to listen for and the command to execute
TRIGGER_KEY = keyboard.Key.space  # Change this to any key you want
mouse = Controller()
COMMAND = "Hello, World!"

def number(n):
    offset = 50
    zeroX = 997
    zeroY = 473
    match n:
        case 0:
            mouse.position = (zeroX, zeroY)
        case 1:
            mouse.position = (zeroX, zeroY - 1*offset)
        case 2:
            mouse.position = (zeroX + 1*offset, zeroY - 1*offset)
        case 3:
            mouse.position = (zeroX + 2*offset, zeroY - 1*offset)
        case 4:
            mouse.position = (zeroX, zeroY - 2*offset)
        case 5:
            mouse.position = (zeroX + 1*offset, zeroY - 2*offset)
        case 6:
            mouse.position = (zeroX + 2*offset, zeroY - 2*offset)
        case 7:
            mouse.position = (zeroX, zeroY - 3*offset)
        case 8:
            mouse.position = (zeroX + 1*offset, zeroY - 3*offset)
        case 9:
            mouse.position = (zeroX + 2*offset, zeroY - 3*offset)
        case 10: #Enter
            mouse.position = (zeroX + 2.5*offset, zeroY)
        case 11: #Cue
            mouse.position = (zeroX + 4.5*offset, zeroY)
        case _:
            print("Outside of range")
            
def click(n):
    number(11)
    mouse.click(Button.left, 1)
    if n < 10:
        number(n)
        mouse.click(Button.left, 1)
    else:
        if n < 20:
            tioTal = 1
        elif n < 30:
            tioTal = 2
        else:
            tioTal = 3
        number(tioTal)
        mouse.click(Button.left, 1)
        number(n-tioTal*10)
        mouse.click(Button.left, 1)
    number(10)
    mouse.click(Button.left, 1)

num = random.randint(1, 32)
# def on_press(key):
#     try:          
#         if key == keyboard.Key.space:
#             global num 
#             rn = random.randint(-1,1)
#             click(num + rn)
#             num = num + rn
#             if num < 1:
#                 num = 1
#             elif num > 32:
#                 num = 32
#     except Exception as e:
#         print(f"An error occurred: {e}")
 
# def on_release(key):
#     if key == keyboard.Key.esc:
#         # Stop the listener when the Escape key is released
#         print("Exiting...")
#         return False

def on_scroll(x, y, dx, dy):
    # x, y: Current mouse position
    # dx: Horizontal scroll amount
    # dy: Vertical scroll amount
    try:          
        if dy > 0:
            click(num + 1)
            num = num + 1
            if num < 1:
                num = 1
            elif num > 32:
                num = 32
        elif dy < 0:
            click(num - 1)
            num = num - 1
            if num < 1:
                num = 1
            elif num > 32:
                num = 32
    except Exception as e:
        print(f"An error occurred: {e}")

# Start the mouse listener
# with mouse.Listener(on_scroll=on_scroll) as listener:
#     print("Listening for scroll events... Press Ctrl+C to stop.")
#     listener.join()

# Start listening for keyboard events
# with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
#     print(f"Listening for key press: {TRIGGER_KEY}. Press 'Esc' to exit.")
#     listener.join()

num = 1

x_pos = 0
y_pos = 0

while True:
    time.sleep(0.05)
    position = mouse.position
    new_x = position[1] - x_pos
    if new_x > 10:
        click(num - 1)
        num = num - 1
        num = min(num,32)
        num = max(num,1)
        x_pos = position[1]
    elif new_x < -10:
        click(num + 1)
        num = num + 1
        num = min(num,32)
        num = max(num,1)
        x_pos = position[1]

