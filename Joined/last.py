from html2image import Html2Image
import time
import numpy as np
import cv2
from statistics import mode

def get_time():
    img = "google.jpg"
    image = cv2.imread(img)

    # define the list of boundaries
    # dark red
    # red
    # orange
    # green
    boundaries = [
        ([20, 20, 100], [60, 60, 140]),
        ([50, 60, 215], [90, 100, 255]),
        ([60, 140, 215], [100, 180, 255]),
        ([90, 160, 90], [140, 255, 140])
    ]
    coordinates = [
        ([775, 921], [780, 926]),
        ([80, 1651], [85, 1656]),
        ([236, 891], [241, 896]),
        ([683, 703], [688, 708])
    ]
    res = ["W", "S", "E", "N"]
    road = ["S", "E", "N", "W"]
    color = ["Dark Red", "Red", "Orange", "Green"]
    value = [3, 2, 1, 0]
    # loop over the boundaries
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
        temp = np.transpose(mask.nonzero())
        j = 0  # j is road and i is colour
        for (l, u) in coordinates:
            for n in temp:
                if n[0] >= l[0] and n[1] >= l[1] and n[0] <= u[0] and n[1] <= u[1]:
                    result.append((road[j], color[i], value[i]))
            j += 1
        i += 1
    coun = []
    for x in range(4):
        y = mode(result)
        coun.append(y)
        result = list(filter(lambda a: a != y, result))
    out = []
    for x in road:
        for y in coun:
            if x == y[0]:
                out.append(y)
    t = []
    l = 4
    for x in range(l):
        t.append((out[x][2] * 3) + out[(x + 2) % l][2] + out[(x + 3) % l][2])
    s = sum(t)
    if s!= 0:
        for x in range(l):
            t[x] = int((40/ s) * t[x])
            print(road[x], "--->", t[x], "sec")
    else:
        for x in range(l):
            t[x] = int(40/l)
            print(road[x], "--->", t[x], "sec")
    return t

hti = Html2Image()
while True:
    hti.screenshot(url="https://www.google.com/maps/@9.9950524,76.2921638,21z/data=!5m1!1e1", save_as="google.jpg")
    t = get_time()
    t = t[-1:] +t[:-1]
    print(t)
    time.sleep(120)
