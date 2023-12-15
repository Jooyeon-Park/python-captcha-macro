import solveCaptcha as solveCaptcha
import pyautogui
import time
from PIL import ImageGrab

def isCaptcha():
    # Detect Captcha window
    point1 = [282,564]

    pixel_color1 = pyautogui.pixel(point1[0],point1[1])
    #pixel_color2 = pyautogui.pixel(point2[0],point2[1])

    color_hex1 = '#{:02x}{:02x}{:02x}'.format(pixel_color1[0], pixel_color1[1], pixel_color1[2])
    #color_hex2 = '#{:02x}{:02x}{:02x}'.format(pixel_color2[0], pixel_color2[1], pixel_color2[2])

    print(f"Color at ({point1[0]}, {point1[1]}): {color_hex1}")
    #print(f"Color at ({point2[0]}, {point2[1]}): {color_hex2}")

    if color_hex1 == "#183d63":
        return True
    return False

def imageCapture():
    left = 158
    top = 450
    right = 420
    bottom = 530

    screenshot = ImageGrab.grab(bbox=(left, top, right, bottom))
    screenshot.save("screenshot.png")

def main():
    while True:
        if isCaptcha:
            # Pause Macro
            pyautogui.hotkey('ctrl', 'c')
            print("Pause Macro")
            
            # Capture Captcha Image
            imageCapture
            print("Image Captured")

            # Solve Captcha
            result = solveCaptcha
            print("Solved Captcha")

            # Click Captcha input
            inputBoxCoord = ['200','200']
            pyautogui.click(inputBoxCoord[0],inputBoxCoord[1])
            print("Input Click")

            # input Captcha
            pyautogui.write(result)
            print("input Captcha")

            # Click Confirm
            confirmationCoord = ['200','200']
            pyautogui.click(confirmationCoord[0],confirmationCoord[1])
            print("Input Click")

            # Resume Macro
            pyautogui.hotkey('ctrl', 'c')
            print("Resume Macro")

        time.sleep(5)






if __name__ == "__main__":
    main()
