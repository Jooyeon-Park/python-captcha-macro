import tkinter as tk
import threading
import time
import pyautogui
import solveCaptcha
import main

def worker_function():
    """ Function to run in the thread. """
    while not stop_event.is_set():
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
    print("Thread stopping 2")

def start_thread():
    """ Start the worker thread. """
    global worker_thread, stop_event
    stop_event.clear()
    worker_thread = threading.Thread(target=worker_function)
    worker_thread.start()
    output_text.insert(tk.END, "Started...\n")

def stop_thread():
    """ Signal the worker thread to stop. """
    global stop_event
    stop_event.set()
    print("Thread stopping 1")
    output_text.insert(tk.END, "Stopped!\n")

# Create the main window
root = tk.Tk()
root.title("주연워그레이몬 메크로")

# Create an event that can be set to signal the thread to stop
stop_event = threading.Event()

l = tk.Label(root, text = "장경진 바보")
l.pack()

# Create and configure the text field
output_text = tk.Text(root, height=10, width=40)
output_text.pack()

# Create the 'Start' button
start_button = tk.Button(root, text="Start", command=start_thread)
start_button.pack()

# Create the 'Stop' button
stop_button = tk.Button(root, text="Stop", command=stop_thread)
stop_button.pack()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()



# Start the Tkinter event loop
root.mainloop()
