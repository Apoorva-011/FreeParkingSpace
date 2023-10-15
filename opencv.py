import cv2 as cv
import numpy as np
# img1=cv.imread('img/dog.jpg')
#cv.imshow('cat',img1)
capture =cv.VideoCapture('video/sample-5s.mp4')
while True:
  isTrue ,frame =capture.read()
  cv.imshow('vieww',frame)
 
  if cv.waitKey(20):
     break

cv.destroyAllWindows
