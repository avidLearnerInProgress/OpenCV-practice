import cv2
import numpy as np 
import matplotlib.pyplot as plt 

cap = cv2.VideoCapture('data/video.mp4')
while True:
	ret,frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	cv2.imshow('frame',frame)
	cv2.imshow('gray',gray)
	k = cv2.waitKey(33)
	if k == ord('a'):
		print("Exit..")
		break
cap.release()
cv2.destroyAllWindows()