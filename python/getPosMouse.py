from pynput.mouse import Controller
import time

# Create a mouse controller object
mouse = Controller()

count = 0

x_pos = 0
y_pos = 0

try:
    print("Press Ctrl+C to stop the program.")
    while True:
        # Get the current mouse position
        position = mouse.position
        # if y_pos < position[0]:
            
        print(f"Mouse position: {position}", end="\r")  # Overwrites the same line
        time.sleep(0.1)  # Update every 100ms
except KeyboardInterrupt:
    print("\nProgram stopped by user.")


# 1227 470
# 999 423
# 1125 471