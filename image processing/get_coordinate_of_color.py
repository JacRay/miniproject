import cv2
import numpy as np

# Load image
im = cv2.imread('google.jpg')

# Define the blue colour we want to find - remember OpenCV uses BGR ordering
blue = [123,185,144]

# Get X and Y coordinates of all blue pixels
Y, X = np.where(np.all(im==blue,axis=2))

print(X,Y)