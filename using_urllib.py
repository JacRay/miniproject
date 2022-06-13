from matplotlib import pylab
from io import BytesIO
from PIL import Image
import urllib.request

url = "https://www.google.com/maps/@9.9763612,76.2859241,17.06z/data=!5m2!1e4!1e1"
buffer = BytesIO(urllib.request.urlopen(url).read())
image = Image.open(buffer)
pylab.imshow(image)
pylab.show()