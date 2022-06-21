# import the necessary packages
import numpy as np
import cv2
img = "google.jpg"
image = cv2.imread(img)

# define the list of boundaries
#dark red
#red
#orange
#green
boundaries = [
	([20, 20, 80], [60, 60, 120]),
	([60, 80, 180], [100, 120, 255]),
	([120, 160, 200], [150, 200, 255]),
	([130, 180, 110], [160, 210, 140])
]

# loop over the boundaries
for (lower, upper) in boundaries:
	# create NumPy arrays from the boundaries
	lower = np.array(lower, dtype = "uint8")
	upper = np.array(upper, dtype = "uint8")
	# find the colors within the specified boundaries and apply
	# the mask
	mask = cv2.inRange(image, lower, upper)
	output = cv2.bitwise_and(image, image, mask = mask)
	# show the images
	print(np.transpose(mask.nonzero()))
	cv2.imshow("images", np.hstack([image, output]))
	cv2.waitKey(0)