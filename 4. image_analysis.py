import numpy as np 
import cv2

img = cv2.imread('data/index.jpg', cv2.IMREAD_COLOR)

#px = img[55,55]

img[55,55] = [255,255,255]
px = img[55,55]
print(px) 

roi = img[100:150, 100:150]
img[100:150, 100:150] = [255,255,255]
#print(roi)

watch_face = img[37:111, 107:194]
img[0:74, 0:87] = watch_face

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
