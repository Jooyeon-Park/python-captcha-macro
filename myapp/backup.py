import tkinter as tk
import main
import time
import threading

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
            # Pause Macro
            # pyautogui.hotkey('ctrl', 'c')
            print("Pause Macro")
            
            # Capture Captcha Image
            main.imageCapture()
            print("Image Captured")

            # # Solve Captcha
            # result = solveCaptcha
            # print("Solved Captcha")

            # # Click Captcha input
            # inputBoxCoord = ['200','200']
            # pyautogui.click(inputBoxCoord[0],inputBoxCoord[1])
            # print("Input Click")

            # # input Captcha
            # pyautogui.write(result)
            # print("input Captcha")

            # # Click Confirm
            # confirmationCoord = ['200','200']
            # pyautogui.click(confirmationCoord[0],confirmationCoord[1])
            # print("Input Click")

            # # Resume Macro
            # pyautogui.hotkey('ctrl', 'c')
            # print("Resume Macro")

        time.sleep(5)

# Function to execute when the 'Stop' button is clicked
def stop_button_click():
    global is_running
    is_running = False
    print("Stop button clicked")
    output_text.insert(tk.END, "Stopped!\n")

# Function to execute when the 'Screenshot Area' button is clicked
def screenshot_button_click():
    global is_running
    is_running = False
    output_text.insert(tk.END, "Captcha screen shot area initializing\nClick 4 corners\n")


def input_button_click():
    global is_running
    is_running = False
    output_text.insert(tk.END, "Input button...\n")
    print("Input field initialized")
    canvas = tk.Canvas(root, width=screen_width, height=screen_height)
    canvas.pack()
    canvas.bind("<Button-1>", on_mouse_click)

def on_mouse_click(event):
    global click_counter
    global clicked_coordinates
    if click_counter < 4:
        x, y = event.x, event.y
        clicked_coordinates.append((x, y))
        click_counter += 1
        output_text.insert(tk.END, f"Click {click_counter}: X={x}, Y={y}\n")

# Create the main window
root = tk.Tk()
root.title("Captcha Macro")

l = tk.Label(root, text = "Captcha Macro")
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

# Create the 'Screenshot Area' button
screenshot_button = tk.Button(root, text="Screenshot Area", command=screenshot_button_click)
screenshot_button.pack()

# Create the 'Screenshot Area' button
input_button = tk.Button(root, text="Input", command=input_button_click)
input_button.pack()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()



# Start the Tkinter event loop
root.mainloop()
