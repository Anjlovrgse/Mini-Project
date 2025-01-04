import cv2
import numpy as np

# Start the webcam
cap = cv2.VideoCapture(0)

# Define the range of the target color (red in this example)
# Adjust these values for detecting other colors
lower_red = np.array([0, 120, 70])
upper_red = np.array([10, 255, 255])

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Flip the frame for a mirror effect
    frame = cv2.flip(frame, 1)

    # Convert the frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Create a mask for detecting red color
    mask = cv2.inRange(hsv, lower_red, upper_red)

    # Perform bitwise-AND to extract the red areas
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # Display the original frame and the result
    cv2.imshow("Original Frame", frame)
    cv2.imshow("Red Color Detection", result)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()
