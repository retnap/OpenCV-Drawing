import cv2
import numpy as np 

canvas = np.zeros((512,512,3), dtype = np.uint8) + 255

font1 = cv2.FONT_HERSHEY_SIMPLEX
font2 = cv2.FONT_HERSHEY_COMPLEX
font3 = cv2.FONT_HERSHEY_SCRIPT_COMPLEX


cv2.putText(canvas, "OpenCV", (30, 100), font1, 4, (0,0,0), cv2.LINE_AA )
#where to write, what to write, coordinate, font, font size, color, default font



cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()