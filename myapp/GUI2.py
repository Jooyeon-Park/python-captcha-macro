import tkinter as tk
import threading
import time
import pyautogui
import solveCaptcha
import main


def insert_text_and_scroll(text):
    """ Insert text into the output_text widget and scroll to the bottom. """
    output_text.insert(tk.END, text)
    output_text.see(tk.END)

def worker_function():
    """ Function to run in the thread. """
    while not stop_event.is_set():
        if main.isCaptcha():
            insert_text_and_scroll("캡챠떴다!!!...\n")
            # Pause Macro
            pyautogui.press('\'')
            print("Pause Macro")
            
            # Capture Captcha Image
            main.imageCapture()
            print("Image Captured")

            if stop_event.is_set():
                break

            # Solve Captcha
            result = solveCaptcha.solveCaptcha()
            print("Solved Captcha" + result)
            insert_text_and_scroll("캡차 풀었당 케케케케켘\n정답은: " + result)

            if stop_event.is_set():
                break

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
            insert_text_and_scroll("캡챠 입력완료!!!...\n")

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
    insert_text_and_scroll("Started...\n")

def stop_thread():
    """ Signal the worker thread to stop. """
    global stop_event
    stop_event.set()
    print("Thread stopping 1")
    insert_text_and_scroll("Stopped!\n")

# Create the main window
root = tk.Tk()
root.title("주연워그레이몬 메크로")

# Create an event that can be set to signal the thread to stop
stop_event = threading.Event()

l = tk.Label(root, text = "장경진 바보")
l.pack()

# Create and configure the text field
output_text = tk.Text(root, height=10, width=15)
output_text.pack()

# Create a Scrollbar and attach it to output_text
scrollbar = tk.Scrollbar(root, command=output_text.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Configure output_text to use scrollbar
output_text.config(yscrollcommand=scrollbar.set)

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
