import cv2
import numpy as np
import dlib
from math import hypot

# Load video feed and hair image
cap = cv2.VideoCapture(0)
hair_image = cv2.imread("hair1-removebg-preview.png", cv2.IMREAD_UNCHANGED)

# Load dlib detector and predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks_github.dat")

while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)

    for face in faces:
        landmarks = predictor(gray, face)

        # Get relevant landmark points
        top_head = (landmarks.part(27).x, landmarks.part(27).y)
        left_edge = (landmarks.part(19).x, landmarks.part(19).y)
        right_edge = (landmarks.part(24).x, landmarks.part(24).y)

        # Calculate hair dimensions
        width_multiplier = 2  # Increase for wider hair, decrease for narrower
        height_ratio = 0.8     # Increase for taller hair, decrease for shorter
        
        hair_width = int(hypot(left_edge[0] - right_edge[0], left_edge[1] - right_edge[1]) * width_multiplier) # Calculate the width of the hair
        hair_height = int(hair_width * height_ratio) # Calculate the height of the hair

        # Calculate position for overlay with vertical and horizontal offsets
        vertical_offset = int(hair_height * 0.5)    # Adjust this value to move hair up/down
        horizontal_offset = int(hair_width * -0.2)    # Adjust this value to move hair left/right. Positive values move right, negative move left
        
        top_left = (
            top_head[0] - hair_width // 2 + horizontal_offset,  # Add horizontal offset here
            top_head[1] - hair_height // 2 - vertical_offset
        )

        # Resize hair image
        hair_resized = cv2.resize(hair_image, (hair_width, hair_height))

        # Extract hair image alpha channel
        alpha = hair_resized[:, :, 3] / 255.0
        overlay_rgb = hair_resized[:, :, :3]

        # Place hair image on frame
        for c in range(3):  # Loop over color channels
            frame[top_left[1]:top_left[1] + hair_height, top_left[0]:top_left[0] + hair_width, c] = \
                (1 - alpha) * frame[top_left[1]:top_left[1] + hair_height, top_left[0]:top_left[0] + hair_width, c] + \
                alpha * overlay_rgb[:, :, c]

    cv2.imshow("Hair Overlay", frame)

    if cv2.waitKey(1) == 27:  # Escape key
        break

cap.release()
cv2.destroyAllWindows()