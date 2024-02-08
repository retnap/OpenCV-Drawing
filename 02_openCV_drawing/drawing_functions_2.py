import cv2
import numpy as np

canvas = np.zeros((512,512,3), dtype = np.uint8) + 255

cv2.line(canvas, (50,50), (512,512), (255,0,0), thickness = 5)
# on canvas, starting point 50-50, finish point 512,512, color blue, thickness 5
cv2.line(canvas, (100,50), (200,250), (0,0,255), thickness = 7)


cv2.rectangle(canvas, (20,20), (50,50), (0,255,0), thickness = 7 )
# When drawing a rectangle, the coordinates of the upper left corner and lower right corner are important.
cv2.rectangle(canvas, (100,100), (200,200), (0,0,255), thickness = -1 )


cv2.circle(canvas, (250,250), 100, (255, 0, 0), thickness = 5)
# Center coordinate and radius are important when drawing a circle
cv2.circle(canvas, (500,500), 30, (255, 0, 0), thickness = -1)


# There is no special function for triangle
p1 = (100, 200)
p2 = (50,50)
p3 = (300, 100)

cv2.line(canvas, p1, p2, (0,0,0), 4)
cv2.line(canvas, p2, p3, (0,0,0), 4)
cv2.line(canvas, p1, p3, (0,0,0), 4)


# Creating a trapezoid
points = np.array([[[110, 200], [330, 200], [290, 220], [100, 100]]], np.int32)
cv2.polylines(canvas, [points], True, (0,0,100), 5)
#True is close box 


#ELLIPSE
cv2.ellipse(canvas, (300,300), (100,50), 0, 0, 360, (255,255,0), -1)

cv2.imshow("Canvas", canvas)

cv2.waitKey(0)
cv2.destroyAllWindows()