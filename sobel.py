import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('D:/Kuliah/SEM 5/opencv-image-sharpening/images/rot.jpg')

laplacian = cv2.Laplacian(img,cv2.CV_64F)
sobelp = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
sobelq = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)

plt.subplot(2,2,1),plt.imshow(img,cmap='gray')
plt.title('Asli'),plt.xticks([]),plt.yticks([])
plt.subplot(2,2,2),plt.imshow(img,cmap='gray')
plt.title('Laplacian'),plt.xticks([]),plt.yticks([])
plt.subplot(2,2,3),plt.imshow(img,cmap='gray')
plt.title('Sobel P'),plt.xticks([]),plt.yticks([])
plt.subplot(2,2,4),plt.imshow(img,cmap='gray')
plt.title('Sobel Q'),plt.xticks([]),plt.yticks([])

plt.show()