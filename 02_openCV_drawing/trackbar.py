import cv2 
import numpy as np 


def nothing(x):  #We need a blank function about openCV
    pass 

img = np.zeros((512,512,3), dtype = np.uint8)
cv2.namedWindow("image")
#The reason why we named the window is to transfer the trackbar interface to the window whose color we will change.
#is for placing

cv2.createTrackbar("R", "image", 0,255, nothing)
cv2.createTrackbar("G", "image", 0,255, nothing)
cv2.createTrackbar("B", "image", 0,255, nothing)

switch = "0: OFF, 1: ON"
cv2.createTrackbar(switch, "image", 0,1, nothing)

while True: #for refreshing trackbar 
    cv2.imshow("image", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
      break

    r = cv2.getTrackbarPos("R", "image")   #We need to keep trackbar's positions
    g = cv2.getTrackbarPos("G", "image")
    b = cv2.getTrackbarPos("B", "image")
    s = cv2.getTrackbarPos(switch, "image")
    #We keep the variables and after that we need to send them to the window

    if s == 0:             #if switch 0 do nothing
       img[:] = [0,0,0]
    if s == 1:
       img[:] = [b,g,r]

    


cv2.destroyAllWindows()


