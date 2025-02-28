from PIL import Image
import pyautogui

def find_red_pixels_in_vertical_line(x_position):
    # Capture the screen
    screenshot = pyautogui.screenshot()

    # Convert the screenshot to a PIL image
    img = Image.frombytes('RGB', screenshot.size, screenshot.tobytes())

    # Get the height of the image
    _, height = img.size

    # Load the pixel data
    pixels = img.load()

    # List to store red pixel positions
    red_pixels = []

    # Iterate through the specified vertical line
    for y in range(height):
        r, g, b = pixels[x_position, y]
        # Define "red" criteria (adjust thresholds as needed)
        if r > 100 and g < 100 and b < 100:
            red_pixels.append((x_position, y))

    return red_pixels

# Specify the line to analyze (e.g., line 500)
y_line = 340

# Find red pixels in the specified line
red_pixels = find_red_pixels_in_vertical_line(y_line)
print(f"Red pixels in line {y_line}: {red_pixels}")