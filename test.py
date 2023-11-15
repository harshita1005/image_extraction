


import os
import cv2
import pyautogui
import numpy as np

def capture_image_at_cursor_position(imagename):
    # Capture a screenshot
    pyautogui.screenshot(imagename)

    # Load the screenshot
    screenshot = cv2.imread(imagename)

    # Convert the screenshot to grayscale
    gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

    # Define a kernel for morphological operations
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (13, 13))
    gradient = cv2.morphologyEx(gray, cv2.MORPH_GRADIENT, kernel)

    # Apply binary thresholding
    ret, thresh = cv2.threshold(gradient, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Find contours in the thresholded image
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    print("Number of contours:", len(contours))
    i = 0
    cursor_x, cursor_y = pyautogui.position()  # Get the cursor position

    for cnt in contours:
        # Get the bounding rectangle of the contour
        x, y, w, h = cv2.boundingRect(cnt)

        # Check if the cursor is inside the bounding rectangle
        if x <= cursor_x <= x + w and y <= cursor_y <= y + h:
            cv2.rectangle(screenshot, (x, y), (x + w, y + h), (0, 255, 0), 2)
            roi_color = screenshot[y:y + h, x:x + w]
            print(f"Saving image as - {imagename}")
            cv2.imwrite(imagename, roi_color)
            i += 1

    # Save the screenshot with cursor highlighting
    cv2.imwrite("screenshot_with_cursor.png", screenshot)

def main():
    index = 0
    while True:
        imagename = os.path.join(os.path.dirname(os.path.abspath(__file__)), "References", "ImageCapture", f"{index}.png")
        print(os.path.basename(imagename))
        capture_image_at_cursor_position(imagename)
        index += 1

if __name__ == "__main__":
    main()




























































































































