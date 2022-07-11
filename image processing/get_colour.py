from PIL import Image
# dark red = 0  0 - 10 km/hr   0 - 3m/s    35 vehicles/50m
# red = 1       10 - 25 km/hr  3 - 7m/s    30
# orange = 2    25 - 50 km/hr  7 - 14m/s   20
# green = 3     above 50km/hr  above 14m/s 10
#rgb
vehicles = [35, 30, 20, 10]
boundaries = [
    ([80, 20, 20], [120, 60, 60]),
    ([180, 80, 60], [255, 120, 100]),
    ([200, 160, 120], [255, 200, 150]),
    ([110, 180, 130], [140, 210, 160])
]
# S E N W

im = Image.open('google1.jpg')  # Can be many different formats.
pix = im.load()
coordinates = [
    [230, 240],
    [401, 88],
    [229, 70],
    [120, 263]
]
color = []
j = 0
for c in coordinates:
    color.append(pix[c[0], c[1]])
    i = 0
    for (lower, upper) in boundaries:
        if color[j][0] >= lower[0] and color[j][0] <= upper[0] and color[j][1] >= lower[1] and color[j][1] <= upper[1] and color[j][2] >= lower[2] and color[j][2] <= upper[2] :
            print(i)
            break
        i += 1
    j+=1

