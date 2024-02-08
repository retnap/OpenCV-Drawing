import cv2
import numpy as np 

""""
canvas = np.zeros((512,512,3), dtype = np.uint8) 
# np.zeros() the purpose of the function is to create a blank black canvas according to the given values.



print(canvas)

cv2.imshow("Canvas Black", canvas)

cv2.waitKey(0)
cv2.destroyAllWindows()
"""

canvas = np.zeros((512,512,3), dtype = np.uint8) + 255

cv2.imshow("Canvas White", canvas)

cv2.waitKey(0)
cv2.destroyAllWindows()
