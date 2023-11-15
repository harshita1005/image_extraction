
import cv2
import pyautogui
import time
import numpy as np
import win32gui
import win32con

# Function to get the desktop screenshot
def get_desktop_screenshot():
    hdesktop = win32gui.GetDesktopWindow()
    left, top, right, bottom = win32gui.GetWindowRect(hdesktop)
    screenshot = pyautogui.screenshot(region=(left, top, right - left, bottom - top))
    return np.array(screenshot)[:, :, ::-1].copy()

# Capture a screenshot
time.sleep(5)

# Get the desktop screenshot
desktop_screenshot = get_desktop_screenshot()

# Get the cursor position
cursor_x, cursor_y = pyautogui.position()

# Convert the desktop screenshot to grayscale
gray = cv2.cvtColor(desktop_screenshot, cv2.COLOR_BGR2GRAY)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (13, 13))
gradient = cv2.morphologyEx(gray, cv2.MORPH_GRADIENT, kernel)

ret, thresh = cv2.threshold(gradient, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Contours
contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

print("Number of contours:", len(contours))
i = 0

for cnt in contours:
    # Get the bounding rectangle of the contour
    x, y, w, h = cv2.boundingRect(cnt)
    
    # Check if the cursor is inside the bounding rectangle
    if x <= cursor_x <= x + w and y <= cursor_y <= y + h:
        cv2.rectangle(desktop_screenshot, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        # Extract the image within the bounding rectangle
        roi = desktop_screenshot[y:y + h, x:x + w]
        
        # Save the extracted image as "cursor_object.png"
        cv2.imwrite(f"cursor_object.png", roi)
        i += 1

cv2.imshow('Desktop with Icons', desktop_screenshot)
cv2.waitKey(0)
cv2.destroyAllWindows()

