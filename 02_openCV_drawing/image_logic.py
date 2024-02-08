import cv2 
import numpy as np 

"""" Color Picture Logic

img = np.zeros((10,10,3), dtype = np.uint8)

img[0,0] = (255,255,255)
img[0,1] = (255,255,200)
img[0,2] = (255,255,150)
img[0,3] = (255,255,15)


img = cv2.resize(img, (500,500), interpolation = cv2.INTER_AREA)

cv2.imshow("Img Blue", img)

"""

img = np.zeros((10,10), dtype = np.uint8)



img[0,0] = 255
img[0,1] = 200
img[0,2] = 100
img[0,3] = 15

img = cv2.resize(img, (500,500), interpolation = cv2.INTER_AREA)

cv2.imshow("Img Black", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

#In other words, computers see images by coloring the pixels one by one and create a picture.