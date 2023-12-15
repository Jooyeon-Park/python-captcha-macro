import tkinter as tk
import main
import time
import threading
import pyautogui
import solveCaptcha

is_running = True
click_counter=0
clicked_coordinates=[]


# Function to execute when the 'Start' button is clicked
def start_button_click():
    global is_running,thread
    output_text.insert(tk.END, "Started...\n")
    print("Start button clicked")

    is_running = True
    thread = threading.Thread(target=run_macro)
    thread.start()  

def run_macro():
    while is_running:
        if main.isCaptcha():
            output_text.insert(tk.END, "캡챠떴다!!!...\n")
            # Pause Macro
            pyautogui.press('\'')
            print("Pause Macro")
            
            # Capture Captcha Image
            main.imageCapture()
            # print("Image Captured")

            # Solve Captcha
            result = solveCaptcha.solveCaptcha()
            print("Solved Captcha" + result)
            output_text.insert(tk.END, "캡차 풀었당 케케케케켘\n정답은: " + result)

            # Click Captcha input
            inputBoxCoord = [414,734]
            pyautogui.moveTo(inputBoxCoord[0], inputBoxCoord[1], duration=0)
            pyautogui.mouseDown()
            time.sleep(0.3)
            pyautogui.mouseUp()
            print("Input Click")

            # input Captcha
            pyautogui.write(result, interval=0.1)
            print("input Captcha")

            # # Click Confirmi
            confirmationCoord = [416,770]
            pyautogui.moveTo(confirmationCoord[0], confirmationCoord[1], duration=0)
            pyautogui.mouseDown()
            time.sleep(0.3)
            pyautogui.mouseUp()
            print("Confirmation Click")
            output_text.insert(tk.END, "캡챠 입력완료!!!...\n")

            time.sleep(1)
            # Resume Macro
            pyautogui.press(';')
            print("Resume Macro")

        time.sleep(5)

# Function to execute when the 'Stop' button is clicked
def stop_button_click():
    global is_running
    is_running = False
    print("Stop button clicked")
    output_text.insert(tk.END, "Stopped!\n")

# Create the main window
root = tk.Tk()
root.title("주연워그레이몬 메크로")

l = tk.Label(root, text = "장경진 바보")
l.pack()

# Create and configure the text field
output_text = tk.Text(root, height=10, width=40)
output_text.pack()

# Create the 'Start' button
start_button = tk.Button(root, text="Start", command=start_button_click)
start_button.pack()

# Create the 'Stop' button
stop_button = tk.Button(root, text="Stop", command=stop_button_click)
stop_button.pack()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()



# Start the Tkinter event loop
root.mainloop()
