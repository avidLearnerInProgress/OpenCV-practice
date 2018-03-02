import numpy as np 
import cv2

img1 = cv2.imread('data/img1.jpeg')
img2 = cv2.imread('data/img3.png')

#cv2.imshow('img1', img1)
#cv2.imshow('img2', img2)

#add = img1 + img2
#weighted = cv2.addWeighted(img1, 0.8, img2, 0.2, 1)

rows, cols, channels = img.shape

cv2.imshow('add', weighted)
cv2.waitKey(0)
cv2.destroyAllWindows()