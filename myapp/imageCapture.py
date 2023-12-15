from PIL import ImageGrab

# Define the coordinates of the rectangular area you want to capture
left = 158
top = 450
right = 420
bottom = 530

# Capture the screenshot of the specified area
screenshot = ImageGrab.grab(bbox=(left, top, right, bottom))

# Save the screenshot to a file
screenshot.save("screenshot.png")

# Display the screenshot (optional)
# screenshot.show()
