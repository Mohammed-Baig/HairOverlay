import numpy as np
import cv2 

# Setup camera 
cap = cv2.VideoCapture(0) 

# Read logo and resize from image path
logo = cv2.imread('chadcut.jpg') 
logo = cv2.imread('hair1-removebg-preview.png') 

# Adjust the size for a wider overlay
width, height = 200, 200  # Wider and proportional size
logo = cv2.resize(logo, (width, height)) 

# Create a mask of the logo 
img2gray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY) 
ret, mask = cv2.threshold(img2gray, 1, 255, cv2.THRESH_BINARY) 

# Offset to elevate the logo
elevation_offset = 50  # Adjust this value to raise the overlay higher

while True: 
    # Capture frame-by-frame 
    ret, frame = cap.read()
    
    # Get frame dimensions
    frame_height, frame_width, _ = frame.shape

    # Calculate the center of the frame for the overlay position
    x_center = frame_width // 2 - width // 2
    y_center = frame_height // 2 - height // 2 - elevation_offset

    # Ensure the y_center doesn't go out of bounds
    y_center = max(0, y_center)

    # Define the Region of Interest (ROI)
    roi = frame[y_center:y_center + height, x_center:x_center + width]

    # Ensure the ROI size matches the logo size
    roi[np.where(mask)] = 0  # Black-out the area of the logo
    roi += logo  # Add the logo

    # Display the resulting frame
    cv2.imshow('WebCam', frame) 
    if cv2.waitKey(1) == ord('q'): 
        break

# When everything is done, release the capture 
cap.release() 
cv2.destroyAllWindows() 
