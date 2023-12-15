import keyboard

# Define the keys to sense
ctrl_key = 'ctrl'
key_to_sense = '5'

# Define a callback function to handle keypress events
def key_pressed(e):
    if e.event_type == keyboard.KEY_DOWN:
        if e.name == ctrl_key and keyboard.is_pressed(key_to_sense):
            print(f"Ctrl+{key_to_sense} was pressed!")

# Register the callback function for keypress events
keyboard.on_press(key_pressed)

# Keep the script running
keyboard.wait('esc')  # You can use any key to exit, here 'esc' is used

# Unregister the callback function
keyboard.unhook_all()
