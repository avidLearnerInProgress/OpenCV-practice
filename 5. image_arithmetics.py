import numpy as np 
import cv2

img1 = cv2.imread('data/img1.jpeg')
img2 = cv2.imread('data/img3.jpg')

#cv2.imshow('img1', img1)
#cv2.imshow('img2', img2)

#add = img1 + img2
#weighted = cv2.addWeighted(img1, 0.8, img2, 0.2, 1)

rows, cols, channels = img2.shape
roi = img1[0:rows, 0:cols]

img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV)

mask_inv = cv2.bitwise_not(mask)
img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
img2_fg = cv2.bitwise_and(img2, img2, mask=mask)

_add = cv2.add(img1_bg, img2)
img1[0:rows, 0:cols] = _add

cv2.imshow('result', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()