import pyautogui

while True:
    # Get the mouse coordinates
    x, y = pyautogui.position()

    # Print the x, y coordinates
    print(f"Mouse Position - X: {x}, Y: {y}")

    # Wait for a short delay (e.g., 1 second) before checking the position again
    pyautogui.sleep(1)
        