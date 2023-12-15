import pyautogui
from PIL import ImageGrab
from PIL import Image
import colorsys
import time


# Define the RGB values for the navy color
navy_color_rgb = (9, 33, 62)
navy_color_hls = colorsys.rgb_to_hls(navy_color_rgb[0] / 255, navy_color_rgb[1] / 255, navy_color_rgb[2] / 255)

def isNavy(x,y):
    global navy_color_hls
    screen_width, screen_height = pyautogui.size()
    # Capture a screenshot of the screen
    screenshot = ImageGrab.grab(bbox=(0, 0, screen_width, screen_height))

    # Get the pixel color at the specified coordinate
    pixel_color = screenshot.getpixel((x, y))
    # print("Pixel: ", pixel_color)

    # Convert the pixel color and navy color to HLS color space for comparison
    pixel_color_hls = colorsys.rgb_to_hls(pixel_color[0] / 255, pixel_color[1] / 255, pixel_color[2] / 255)

    colorsys.rgb_to_hsv 
    color_hex1 = '#{:02x}{:02x}{:02x}'.format(pixel_color[0], pixel_color[1], pixel_color[2])
    # print("HEX#####: "+ color_hex1)

    # Define a tolerance value for color comparison (adjust as needed)
    tolerance = 0.2  # Increase or decrease as needed

    # Check if the pixel color is similar to the navy color within the tolerance
    color_match = all(abs(a - b) < tolerance for a, b in zip(pixel_color_hls, navy_color_hls))

    if color_match:
        # print(f"The coordinate ({x}, {y}) has a navy shade.")
        return True
    else:
        # print(f"The coordinate ({x}, {y}) does not have a navy shade.")
        return False

def main():
    # Define the X and Y coordinates to mark
    x = 220
    y = 565

    # Move the mouse cursor to the specified coordinates
    pyautogui.moveTo(x, y, duration=0.3)

    # Simulate a mouse click to mark the location
    pyautogui.click()

    # Wait for a few seconds to keep the marker visible (you can adjust the duration)
    time.sleep(1)

    isnavy = True
    for i in range(0,5):
        if not isNavy(x+i*10,y):
            isnavy=False
            break
    
    print("REsult!!" + str(isnavy))

# main()

