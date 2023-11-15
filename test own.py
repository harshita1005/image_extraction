'''
import cv2
import numpy as np

img_read = cv2.imread('black_img.png', -1)
grey_image = cv2.cvtColor(img_read,cv2.COLOR_BGR2GRAY)
 
ret,thresh_img = cv2.threshold(grey_image,127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(thresh_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
 
img_contours = np.zeros(img_read.shape)
cv2.drawContours(img_contours, contours, -1, (255,0,0), 3)
cv2.imshow('black_img.png',img_contours)
cv2.imwrite("Cropped Image.jpg", img_contours)


image = cv2.imread('ss.png', cv2.IMREAD_UNCHANGED)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
gradient = cv2.morphologyEx(gray, cv2.MORPH_GRADIENT, kernel)

contours = cv2.findContours(gradient, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

for cnt in contours:
    (x,y,w,h) = cv2.boundingRect(cnt)
    cv2.rectangle(image, (x,y), (x+w,y+h), (0,0,255))

import numpy as np
import cv2

image = cv2.imread('ss.png')
y=0
x=0
h=100
w=200
crop = image[y:y+h, x:x+w]
cv2.imshow('Image', crop)
cv2.waitKey(0) 



#Import packages
import cv2, pyautogui, time

import numpy as np


img = cv2.imread("img.png", cv2.IMREAD_UNCHANGED)

#convert the image into grayscale image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (19,19))
gradient = cv2.morphologyEx(gray, cv2.MORPH_GRADIENT, kernel)

ret,thresh = cv2.threshold(gradient,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

#Contour is an area outlet that is obtained after searching for certain patterns in the image. 
contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

print("Number of contours:" + str(len(contours)))
i=0
for cnt in contours:
   
    #create an approximate rectangle along with the image. 
    #This function's primary use is to highlight the area of interest after obtaining the image's outer shape.
    (x,y,w,h) = cv2.boundingRect(cnt) 
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    roi_color = img[y:y + h, x:x + w]
    print(i," Object found. Saving locally.")
    cv2.imwrite(str(i) +'.png', roi_color)
    i+=1
    
#The function waitKey waits for a key event infinitely (when \f$\texttt{delay}\leq 0\f$ ) or for delay milliseconds, when it is positive
cv2.waitKey(0)

#The function destroyAllWindows destroys all of the opened HighGUI windows.
cv2.destroyAllWindows()



'''
'''
import cv2
import pyautogui
import time
import numpy as np

# Capture a screenshot
time.sleep(5)

#pyautogui screenshot uses pillow method which has order of colour as RGB and opencv works with BGR
#So we need to convert that RGB to BGR to work with opencv
screenshot = pyautogui.screenshot()
screenshot=np.array(screenshot)
screenshot=screenshot[:, :, ::-1].copy()

# Get the cursor position
cursor_x, cursor_y = pyautogui.position()
#convert the image into grayscale image
gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (14,14))
gradient = cv2.morphologyEx(gray, cv2.MORPH_GRADIENT, kernel)

ret,thresh = cv2.threshold(gradient,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

#Contour is an area outlet that is obtained after searching for certain patterns in the image. 
contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

print("Number of contours:", len(contours))
i = 0

for cnt in contours:
    # Get the bounding rectangle of the contour
    x, y, w, h = cv2.boundingRect(cnt)
    
    # Check if the cursor is inside the bounding rectangle
    if x <= cursor_x <= x + w and y <= cursor_y <= y + h:
        cv2.rectangle(screenshot, (x, y), (x + w, y + h), (0, 255, 0), 2)
        roi_color = screenshot[y:y + h, x:x + w]
        cv2.imwrite(f"cursor_object.png", roi_color)
        i += 1


cv2.waitKey(0)
cv2.destroyAllWindows()



import cv2
import pyautogui
import time
import numpy as np
import pygetwindow as gw

# Capture a screenshot
time.sleep(5)

# Get the cursor position
cursor_x, cursor_y = pyautogui.position()

# Find the window under the cursor
window = gw.getWindowsAt(cursor_x, cursor_y)

if window:
    # Capture the contents of the window
    screenshot = pyautogui.screenshot(region=(window[0].left, window[0].top, window[0].width, window[0].height))
    screenshot = np.array(screenshot)
    screenshot = screenshot[:, :, ::-1].copy()

    # Convert the image into grayscale
    gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (14, 14))
    gradient = cv2.morphologyEx(gray, cv2.MORPH_GRADIENT, kernel)

    ret, thresh = cv2.threshold(gradient, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Find contours
    contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

    print("Number of contours:", len(contours))
    i = 0

    for cnt in contours:
        # Get the bounding rectangle of the contour
        x, y, w, h = cv2.boundingRect(cnt)

        # Check if the cursor is inside the bounding rectangle
        if x <= cursor_x <= x + w and y <= cursor_y <= y + h:
            cv2.rectangle(screenshot, (x, y), (x + w, y + h), (0, 255, 0), 2)
            roi_color = screenshot[y:y + h, x:x + w]
            cv2.imwrite(f"cursor_object.png", roi_color)
            i += 1

    cv2.imshow("Window Screenshot", screenshot)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("No window found under the cursor.")


    

import cv2
import pyautogui
import time
import numpy as np
import pygetwindow as gw

# Capture a screenshot
time.sleep(5)

# Get the cursor position
cursor_x, cursor_y = pyautogui.position()

# Find the window under the cursor
window = gw.getWindowsAt(cursor_x, cursor_y)

if window:
    # Capture the contents of the window
    screenshot = pyautogui.screenshot(region=(window[0].left, window[0].top, window[0].width, window[0].height))
    screenshot = np.array(screenshot)
    screenshot = screenshot[:, :, ::-1].copy()

    # Convert the image into grayscale
    gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (14, 14))
    gradient = cv2.morphologyEx(gray, cv2.MORPH_GRADIENT, kernel)

    ret, thresh = cv2.threshold(gradient, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Find contours
    contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

    print("Number of contours:", len(contours))
    i = 0
    cursor_image = None  # To store the image under the cursor

    for cnt in contours:
        # Get the bounding rectangle of the contour
        x, y, w, h = cv2.boundingRect(cnt)

        # Check if the cursor is inside the bounding rectangle
        if x <= cursor_x <= x + w and y <= cursor_y <= y + h:
            cv2.rectangle(screenshot, (x, y), (x + w, y + h), (0, 255, 0), 2)
            roi_color = screenshot[y:y + h, x:x + w]
            if i == 0:
                cursor_image = roi_color  # Store the first image under the cursor
            i += 1

    cv2.imshow("Window Screenshot", screenshot)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    if cursor_image is not None:
        # Save the image under the cursor
        cv2.imwrite(f"cursor_object.png", cursor_image)
        print("Image under cursor saved as cursor_object.png")
    else:
        print("No image found under the cursor.")
else:
    print("No window found under the cursor.")

'''
import cv2
import pyautogui
import time
import numpy as np
import pygetwindow as gw

# Capture a screenshot
time.sleep(5)

# Get the cursor position
cursor_x, cursor_y = pyautogui.position()

# Get all open windows
windows = gw.getAllTitles()

# Iterate through open windows
for window_title in windows:
    # Find the window by title
    window = gw.getWindowsWithTitle(window_title)

    if window:
        window = window[0]  # Assuming there's only one window with the given title

        # Capture the contents of the window
        screenshot = pyautogui.screenshot(region=(window.left, window.top, window.width, window.height))
        screenshot = np.array(screenshot)
        screenshot = screenshot[:, :, ::-1].copy()

        # Convert the image into grayscale
        gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (14, 14))
        gradient = cv2.morphologyEx(gray, cv2.MORPH_GRADIENT, kernel)

        ret, thresh = cv2.threshold(gradient, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        # Find contours
        contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

        print("Number of contours in window", window_title, ":", len(contours))
        i = 0
        cursor_image = None  # To store the image under the cursor

        for cnt in contours:
            # Get the bounding rectangle of the contour
            x, y, w, h = cv2.boundingRect(cnt)

            # Check if the cursor is inside the bounding rectangle
            if x <= cursor_x <= x + w and y <= cursor_y <= y + h:
                cv2.rectangle(screenshot, (x, y), (x + w, y + h), (0, 255, 0), 2)
                roi_color = screenshot[y:y + h, x:x + w]
                if i == 0:
                    cursor_image = roi_color  # Store the first image under the cursor
                i += 1

        cv2.imshow("Window Screenshot", screenshot)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        if cursor_image is not None:
            # Save the image under the cursor
            cv2.imwrite(f"{window_title}_cursor_object.png", cursor_image)
            print(f"Image under cursor in {window_title} saved as {window_title}_cursor_object.png")
        else:
            print(f"No image found under the cursor in {window_title}")


'''




import cv2
import pyautogui
import time
import numpy as np
import pygetwindow as gw

# Capture a screenshot
time.sleep(5)

# Get the cursor position
cursor_x, cursor_y = pyautogui.position()

# Get all windows at the cursor position
windows = gw.getWindowsAt(cursor_x, cursor_y)

if windows:
    for window in windows:
        # Capture the contents of the window
        screenshot = pyautogui.screenshot(region=(window.left, window.top, window.width, window.height))
        screenshot = np.array(screenshot)
        screenshot = screenshot[:, :, ::-1].copy()

        # Convert the image into grayscale
        gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (14, 14))
        gradient = cv2.morphologyEx(gray, cv2.MORPH_GRADIENT, kernel)

        ret, thresh = cv2.threshold(gradient, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        # Find contours
        contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

        print("Number of contours in window:", window.title, ":", len(contours))
        i = 0
        cursor_image = None  # To store the image under the cursor

        for cnt in contours:
            # Get the bounding rectangle of the contour
            x, y, w, h = cv2.boundingRect(cnt)

            # Check if the cursor is inside the bounding rectangle
            if x <= cursor_x <= x + w and y <= cursor_y <= y + h:
                cv2.rectangle(screenshot, (x, y), (x + w, y + h), (0, 255, 0), 2)
                roi_color = screenshot[y:y + h, x:x + w]
                if i == 0:
                    cursor_image = roi_color  # Store the first image under the cursor
                i += 1

        cv2.imshow("Window Screenshot", screenshot)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        if cursor_image is not None:
            # Save the image under the cursor for this window
            cv2.imwrite(f"{window.title}_cursor_object.png", cursor_image)
            print(f"Image under cursor in {window.title} saved as {window.title}_cursor_object.png")
        else:
            print(f"No image found under the cursor in {window.title}")
else:
    print("No window found under the cursor.")






'''




























'''

import cv2

image = cv2.imread('new_black.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (17,17))
gradient = cv2.morphologyEx(gray, cv2.MORPH_GRADIENT, kernel)
#thresh = cv2.threshold(gradient, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
#ret,thresh = cv2.threshold(gradient,0,255,cv2.THRESH_OTSU+cv2.THRESH_BINARY)

#Contour is an area outlet that is obtained after searching for certain patterns in the image. 
contours= cv2.findContours(gradient, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

print("[INFO] Found objects-",(len(contours)))
i=0
for cnt in contours:
    (x,y,w,h) = cv2.boundingRect(cnt)
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    #roi_color = image[y:y + h, x:x + w]
    ##print(i," Object found. Saving locally.")
    #cv2.imwrite(str(i) +'.png', roi_color)
    #i+=1

status = cv2.imwrite('detected.jpg', image)


'''














































































'''
import cv2
image = cv2.imread('new_black.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5,5), 0)
thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7,7))
dilate = cv2.dilate(thresh, kernel, iterations=1)

# Find contours, obtain bounding box coordinates, and extract ROI
cnts = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]
image_number = 0
for c in cnts:
    x,y,w,h = cv2.boundingRect(c)
    cv2.rectangle(image, (x, y), (x + w, y + h), (36,255,12), 2)
    #ROI = original[y:y+h, x:x+w]
    #cv2.imwrite("ROI_{}.png".format(image_number), ROI)
    #image_number += 1

cv2.imshow('image', image)
cv2.imshow('thresh', thresh)
cv2.imshow('dilate', dilate)
cv2.waitKey()
'''