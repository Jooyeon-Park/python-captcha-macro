import pyautogui

def isCaptcha():
    # Detect Captcha window
    point1 = [282,564]

    pixel_color1 = pyautogui.pixel(point1[0],point1[1])
    #pixel_color2 = pyautogui.pixel(point2[0],point2[1])

    color_hex1 = '#{:02x}{:02x}{:02x}'.format(pixel_color1[0], pixel_color1[1], pixel_color1[2])
    #color_hex2 = '#{:02x}{:02x}{:02x}'.format(pixel_color2[0], pixel_color2[1], pixel_color2[2])
    print(f"Color at ({point1[0]}, {point1[1]}): {color_hex1}")
    if color_hex1 == "#183d63":   
        print("true")
        return
    print("false")
isCaptcha()