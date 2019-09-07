import cv2
import numpy as np
import imutils

img = cv2.imread("D:/Kuliah/SEM 5/opencv-image-sharpening/images/truck.jpg")

hsv = cv2.cvtColor(img,cv2.COLOR_RGB2HSV)

lower_blue = np.array([78,158,124])
upper_blue = np.array([138,255,255])

mask = cv2.inRange(hsv,lower_blue,upper_blue)

cv2.imshow('image', img)
cv2.imshow('mask', mask)

while(True):
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()