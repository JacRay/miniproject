# import the necessary packages
import numpy as np
import cv2

import statistics
from statistics import mode

img = "google.jpg"
image = cv2.imread(img)

# define the list of boundaries
# dark red
# red
# orange
# green
boundaries = [
    ([20, 20, 80], [60, 60, 120]),
    ([60, 80, 180], [100, 120, 255]),
    ([120, 160, 200], [150, 200, 255]),
    ([130, 180, 110], [160, 210, 140])
]
coordinates = [
    ([235, 225], [245, 235]),
    ([83, 396], [93, 406]),
    ([65, 224], [75, 234]),
    ([258, 115], [268, 125])
]
road = ["S", "E", "N", "W"]
color =["Dark Red", "Red", "Orange", "Green"]
# loop over the boundaries
x = 1
i = 0
result = []
for (lower, upper) in boundaries:
    # create NumPy arrays from the boundaries
    lower = np.array(lower, dtype="uint8")
    upper = np.array(upper, dtype="uint8")
    # find the colors within the specified boundaries and apply
    # the mask
    mask = cv2.inRange(image, lower, upper)
    output = cv2.bitwise_and(image, image, mask=mask)
    # show the images
    cv2.imwrite(str(x) + ".jpg", output)
    x += 1
    temp = np.transpose(mask.nonzero())
    j = 0 # j is road and i is colour
    for (l, u) in coordinates:
        for n in temp:
            if n[0] >= l[0] and n[1] >= l[1] and n[0] <= u[0] and n[1] <= u[1]:
                result.append((road[j], color[i]))
        j+= 1
    i += 1
coun = []
for x in range(4):
    y = mode(result)
    coun.append(y)
    result = list(filter(lambda a: a != y, result))
print(coun)


