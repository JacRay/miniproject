import numpy as np
import cv2

def estimate_coef(x, y):
    # number of observations/points
    n = np.size(x)

    # mean of x and y vector
    m_x, m_y = np.mean(x), np.mean(y)

    # calculating cross-deviation and deviation about x
    SS_xy = np.sum(y*x) - n*m_y*m_x
    SS_xx = np.sum(x*x) - n*m_x*m_x

    # calculating regression coefficients
    a = SS_xy / SS_xx
    b = m_y - a*m_x

    return(a, b)


# MAIN CODE
# 1. Read image
# 2. find where the pixel belonging to the line are located
# 3. perform linear regression to get coeff

images = ["1.jpg", "2.jpg", "3.jpg", "4.jpg"]      # contain the image read

# for all images to analyze
for x in range(len(images)):
  print("\n\nimage ",x, images[x])

  # read image (convert to greyscale)
  image  = cv2.imread(images[x])

  height = image.shape[0] - 1

  threshold = (np.min(image) + np.max(image)) / 2
  line = np.where(image < threshold) #get coordinate of the pixel belonging to the line

  x = line[1] # store the x position
  y = height - line[0] # store the y position. Need to invert because of image origine being on top left corner instead of bottom left

  #position = np.array([x,y])

  a, b = estimate_coef(x, y)
  print("Estimated coefficients:\n \
       a = %.6f \n \
       b = %.6f" % (a, b))