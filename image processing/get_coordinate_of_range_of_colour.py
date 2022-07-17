# import the necessary packages
import numpy as np
import cv2
img = "google.jpg"
image = cv2.imread(img)

# define the list of boundaries
# dark red
# red
# orange
# green
boundaries = [
	# ([20, 20, 100], [60, 60, 140]),
	# ([50, 60, 215], [90, 100, 255]),
	# ([60, 140, 215], [100, 180, 255]),
	([90, 160, 90], [140, 255, 140])
]

# loop over the boundaries
# x = 1
for (lower, upper) in boundaries:
	# create NumPy arrays from the boundaries
	lower = np.array(lower, dtype = "uint8")
	upper = np.array(upper, dtype = "uint8")
	# find the colors within the specified boundaries and apply
	# the mask
	mask = cv2.inRange(image, lower, upper)
	output = cv2.bitwise_and(image, image, mask = mask)
	# show the images
	# cv2.imwrite(str(x)+".jpg", output)
	# x += 1
	a = np.transpose(mask.nonzero())
	for x in a:
		print(x)
	print("End")
	cv2.namedWindow('image', cv2.WINDOW_NORMAL)
	cv2.resizeWindow('image', 800, 400)
	# cv2.imshow("image", output)
	cv2.imshow("image", np.hstack([image, output]))
	cv2.waitKey(0)