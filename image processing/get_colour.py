from PIL import Image
# dark red = 0
# red = 1
# orange = 2
# green = 3
#rgb
boundaries = [
    ([80, 20, 20], [120, 60, 60]),
    ([180, 80, 60], [255, 120, 100]),
    ([200, 160, 120], [255, 200, 150]),
    ([110, 180, 130], [140, 210, 160])
]
# S E N W

im = Image.open('google.jpg')  # Can be many different formats.
pix = im.load()
coordinates = [
    [230, 240],
    [295, 180],
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

# for (lower, upper) in boundaries:
